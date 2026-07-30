---
title: "[STUDYING] 12 - 2. 스마트 데이터 이해 및 활용_Day4_실습"
created: 2026-07-31
updated: 2026-07-31
type: blog-post
tags: ["blog", "technical-writing"]
category: "STUDYING"
published: 2026-07-30
source_url: https://ch010104.tistory.com/328
---
# [STUDYING] 12 - 2. 스마트 데이터 이해 및 활용_Day4_실습

## 원문

https://ch010104.tistory.com/328

## 노트 유형

`tutorial`

## 학습 목표 및 맥락

원문에서 추출한 학습·구현 내용을 구조화했습니다.

## 원문 기반 학습 정리

### 문제 1. 고객 등급별 할인율 계산

### 함수 정의:

```sql
CREATE OR REPLACE FUNCTION proc_lab.fn_grade_discount_rate(p_grade text)
RETURNS numeric
LANGUAGE sql
IMMUTABLE
STRICT
PARALLEL SAFE
AS $function$
    SELECT CASE upper(trim(p_grade))
               WHEN 'VIP'    THEN 0.15
               WHEN 'GOLD'   THEN 0.10
               WHEN 'SILVER' THEN 0.05
               ELSE 0
           END;
$function$;
```

### 단독 검증:

```sql
SELECT proc_lab.fn_grade_discount_rate(' gold ');
```

```text
fn_grade_discount_rate
----------------------
                  0.10
```

### customers 테이블과 함께:

```text
SELECT
    customer_id,
    customer_name,
    customer_grade,
    proc_lab.fn_grade_discount_rate(customer_grade) AS "고객 등급별 할인율"
FROM proc_lab.customers
ORDER BY customer_id;
```

```text
customer_id|customer_name|customer_grade|고객 등급별 할인율
-----------+-------------+--------------+----------
          1|김민준         |GOLD          |      0.10
          2|이서연         |VIP           |      0.15
          3|박지훈         |SILVER        |      0.05
          4|최유리         |BASIC         |         0
          5|정도윤         |GOLD          |      0.10
```

### 문제 2. 기준 재고 미만 상품 목록 반환

### 함수 정의:

```text
DROP FUNCTION IF EXISTS proc_lab.fn_products_below_stock(integer);

CREATE OR REPLACE FUNCTION proc_lab.fn_products_below_stock(p_threshold integer)
RETURNS TABLE (
    product_id   bigint,
    product_name varchar,
    stock_qty    integer,
    shortage_qty integer,
    unit_price   numeric
)
LANGUAGE sql
STABLE
STRICT
AS $function$
    SELECT
        p.product_id,
        p.product_name,
        p.stock_qty,
        p_threshold - p.stock_qty AS shortage_qty,
        p.unit_price
    FROM proc_lab.products AS p
    WHERE p.active = true
      AND p.stock_qty < p_threshold
    ORDER BY p.stock_qty, p.product_id;
$function$;
```

### 검증:

```sql
SELECT * FROM proc_lab.fn_products_below_stock(70);
```

```text
product_id|product_name|stock_qty|shortage_qty|unit_price
----------+------------+---------+------------+----------
         3|27인치 모니터  |       40|          30| 329000.00
         5|웹캠         |       60|          10|  79000.00
```

### 문제 3. 고객 주문 요약 JSONB 반환

### 함수 정의:

```sql
CREATE OR REPLACE FUNCTION proc_lab.fn_customer_order_summary_json(p_customer_id bigint)
RETURNS jsonb
LANGUAGE plpgsql
STABLE
STRICT
AS $function$
DECLARE
    v_customer     proc_lab.customers%ROWTYPE;
    v_order_count  integer;
    v_total_amount numeric;
BEGIN
-- 고객 조회 (없으면 P0002)
    SELECT *
      INTO STRICT v_customer
      FROM proc_lab.customers
     WHERE customer_id = p_customer_id;

-- 주문 집계 (CANCELLED 제외)
    SELECT
        count(*),
        coalesce(sum(total_amount), 0)
      INTO v_order_count, v_total_amount
      FROM proc_lab.orders
     WHERE customer_id = p_customer_id
       AND order_status <> 'CANCELLED';

    RETURN jsonb_build_object(
        'customer', jsonb_build_object(
            'customer_id', v_customer.customer_id,
            'name',        v_customer.customer_name,
            'email',       v_customer.email,
            'grade',       v_customer.customer_grade
        ),
        'order_count',  v_order_count,
        'total_amount', v_total_amount
    );

EXCEPTION
    WHEN NO_DATA_FOUND THEN
        RAISE EXCEPTION '고객번호 %를 찾을 수 없습니다.', p_customer_id
            USING ERRCODE = 'P0002';
END;
$function$;
```

### 검증:

```sql
SELECT jsonb_pretty(proc_lab.fn_customer_order_summary_json(1));
```

```text
{
    "customer": {
        "name": "김민준",
        "email": "minjun@example.com",
        "grade": "GOLD",
        "customer_id": 1
    },
    "order_count": 2,
    "total_amount": 305000.00
}
```

### 예외 확인:

```sql
SELECT proc_lab.fn_customer_order_summary_json(999);
```

```text
ERROR:  고객번호 999를 찾을 수 없습니다.
SQLSTATE: P0002
```

### 문제 4. 상품 한 종류 주문 생성

### 프로시저 정의:

```sql
CREATE OR REPLACE PROCEDURE proc_lab.pr_create_order(
    IN    p_customer_id bigint,
    IN    p_product_id  bigint,
    IN    p_quantity    integer,
    INOUT p_order_id    bigint DEFAULT NULL
)
LANGUAGE plpgsql
AS $procedure$
DECLARE
    v_unit_price numeric;
    v_stock_qty  integer;
BEGIN
    IF p_quantity <= 0 THEN
        RAISE EXCEPTION '주문 수량은 1 이상이어야 합니다.'
            USING ERRCODE = '22003';
    END IF;

    IF NOT EXISTS (
        SELECT 1 FROM proc_lab.customers
         WHERE customer_id = p_customer_id
           AND active = true
    ) THEN
        RAISE EXCEPTION '존재하지 않거나 비활성 고객입니다: %', p_customer_id
            USING ERRCODE = 'P0002';
    END IF;

    SELECT unit_price, stock_qty
      INTO STRICT v_unit_price, v_stock_qty
      FROM proc_lab.products
     WHERE product_id = p_product_id
       AND active = true
     FOR UPDATE;

    IF v_stock_qty < p_quantity THEN
        RAISE EXCEPTION '재고가 부족합니다. 현재 재고: %', v_stock_qty
            USING ERRCODE = 'P0001';
    END IF;

    UPDATE proc_lab.products
       SET stock_qty = stock_qty - p_quantity
     WHERE product_id = p_product_id;

    INSERT INTO proc_lab.orders (customer_id, order_status, total_amount)
    VALUES (p_customer_id, 'PENDING', v_unit_price * p_quantity)
    RETURNING order_id INTO p_order_id;

    INSERT INTO proc_lab.order_items
        (order_id, product_id, quantity, unit_price)
    VALUES
        (p_order_id, p_product_id, p_quantity, v_unit_price);

    RAISE NOTICE '새 주문번호: %', p_order_id;
END;
$procedure$;
```

### 검증:

```text
BEGIN;
CALL proc_lab.pr_create_order(1, 2, 3, NULL);
```

```text
NOTICE: 새 주문번호: 6
```

```sql
SELECT * FROM proc_lab.orders ORDER BY order_id DESC LIMIT 1;
```

```text
order_id|customer_id|order_status|total_amount|note|ordered_at|updated_at
--------+-----------+------------+------------+----+----------+----------
       6|          1|PENDING     |   147000.00|    |   (현재시각)|  (현재시각)
```

```sql
SELECT * FROM proc_lab.order_items ORDER BY order_item_id DESC LIMIT 1;
```

```text
order_item_id|order_id|product_id|quantity|unit_price|line_amount
-------------+--------+----------+--------+----------+-----------
            7|       6|         2|       3|  49000.00|  147000.00
```

```sql
SELECT product_id, product_name, stock_qty FROM proc_lab.products WHERE product_id = 2;
```

```text
product_id|product_name|stock_qty
----------+------------+---------
         2|무선 마우스    |      147
```

```text
ROLLBACK;
```

### 문제 5. 주문 상태 전환 및 이력 저장

### 프로시저 정의:

```sql
CREATE OR REPLACE PROCEDURE proc_lab.pr_change_order_status(
    IN  p_order_id   bigint,
    IN  p_new_status text,
    OUT p_message    text
)
LANGUAGE plpgsql
AS $procedure$
DECLARE
    v_old_status text;
BEGIN
    IF p_new_status NOT IN
       ('PENDING', 'PAID', 'SHIPPING', 'COMPLETED', 'CANCELLED') THEN
        RAISE EXCEPTION '허용되지 않은 주문 상태입니다: %', p_new_status
            USING ERRCODE = '22023';
    END IF;

    SELECT order_status
      INTO STRICT v_old_status
      FROM proc_lab.orders
     WHERE order_id = p_order_id
     FOR UPDATE;

    IF v_old_status = p_new_status THEN
        p_message := format('주문 %s는 이미 %s 상태입니다.',
                            p_order_id, p_new_status);
        RETURN;
    END IF;

    IF NOT (
        (v_old_status = 'PENDING'  AND p_new_status IN ('PAID', 'CANCELLED')) OR
        (v_old_status = 'PAID'     AND p_new_status IN ('SHIPPING', 'CANCELLED')) OR
        (v_old_status = 'SHIPPING' AND p_new_status = 'COMPLETED')
    ) THEN
        RAISE EXCEPTION '허용되지 않은 상태 전환입니다: % → %',
                        v_old_status, p_new_status
            USING ERRCODE = 'P0001';
    END IF;

    UPDATE proc_lab.orders
       SET order_status = p_new_status,
           updated_at   = clock_timestamp()
     WHERE order_id = p_order_id;

    INSERT INTO proc_lab.order_status_history
        (order_id, old_status, new_status)
    VALUES
        (p_order_id, v_old_status, p_new_status);

    p_message := format('주문 %s: %s → %s 변경 완료',
                        p_order_id, v_old_status, p_new_status);

EXCEPTION
    WHEN NO_DATA_FOUND THEN
        RAISE EXCEPTION '주문번호 %를 찾을 수 없습니다.', p_order_id
            USING ERRCODE = 'P0002';
END;
$procedure$;
```

### 검증:

```text
BEGIN;
CALL proc_lab.pr_change_order_status(2, 'COMPLETED', NULL);
```

```text
p_message
---------------------------------
주문 2: SHIPPING → COMPLETED 변경 완료
```

```sql
SELECT order_id, order_status, updated_at FROM proc_lab.orders WHERE order_id = 2;
```

```text
order_id|order_status|updated_at
--------+------------+----------
       2|COMPLETED   | (현재시각)
```

```sql
SELECT * FROM proc_lab.order_status_history ORDER BY history_id DESC;
```

```text
history_id|order_id|old_status|new_status|changed_by|changed_at
----------+--------+----------+----------+----------+----------
         1|       2|SHIPPING  |COMPLETED |postgres  | (현재시각)
```

```text
ROLLBACK;
```

### 문제 6. 멱등성이 보장되는 일괄 할인

### 프로시저 정의:

```sql
CREATE OR REPLACE PROCEDURE proc_lab.pr_bulk_discount_once(
    IN  p_batch_key        text,
    IN  p_discount_percent numeric,
    IN  p_min_price        numeric,
    OUT p_affected         integer
)
LANGUAGE plpgsql
AS $procedure$
DECLARE
    v_batch_key       text;
    v_claimed         integer;
    v_saved_discount  numeric;
    v_saved_min_price numeric;
    v_saved_affected  integer;
    v_saved_status    text;
BEGIN
    v_batch_key := btrim(p_batch_key);

    IF v_batch_key IS NULL OR v_batch_key = '' THEN
        RAISE EXCEPTION 'batch_key는 필수입니다.'
            USING ERRCODE = '23502';
    END IF;

    IF p_discount_percent IS NULL
       OR p_discount_percent <= 0
       OR p_discount_percent > 50 THEN
        RAISE EXCEPTION '할인율은 0 초과 50 이하이어야 합니다.'
            USING ERRCODE = '22023';
    END IF;

    IF p_min_price IS NULL OR p_min_price < 0 THEN
        RAISE EXCEPTION '최소가격은 0 이상이어야 합니다.'
            USING ERRCODE = '22023';
    END IF;

    INSERT INTO proc_lab.bulk_discount_runs (
        batch_key, discount_percent, min_price, affected_count, run_status
    )
    VALUES (v_batch_key, p_discount_percent, p_min_price, 0, 'PROCESSING')
    ON CONFLICT (batch_key) DO NOTHING;

    GET DIAGNOSTICS v_claimed = ROW_COUNT;

    IF v_claimed = 0 THEN
        SELECT discount_percent, min_price, affected_count, run_status
          INTO STRICT v_saved_discount, v_saved_min_price, v_saved_affected, v_saved_status
          FROM proc_lab.bulk_discount_runs
         WHERE batch_key = v_batch_key
         FOR UPDATE;

        IF v_saved_discount IS DISTINCT FROM p_discount_percent
           OR v_saved_min_price IS DISTINCT FROM p_min_price THEN
            RAISE EXCEPTION
                'batch_key %는 이미 다른 조건으로 사용되었습니다. 기존 할인율=%, 기존 최소가격=%',
                v_batch_key, v_saved_discount, v_saved_min_price
                USING ERRCODE = '22023';
        END IF;

        p_affected := v_saved_affected;
        RAISE NOTICE 'batch_key %는 이미 완료되었습니다. 기존 처리 건수=%',
                     v_batch_key, p_affected;
        RETURN;
    END IF;

    UPDATE proc_lab.products
       SET unit_price = round(unit_price * (1 - p_discount_percent / 100.0), 2)
     WHERE active = true
       AND unit_price >= p_min_price;

    GET DIAGNOSTICS p_affected = ROW_COUNT;

    UPDATE proc_lab.bulk_discount_runs
       SET affected_count = p_affected,
           run_status     = 'COMPLETED',
           completed_at   = clock_timestamp()
     WHERE batch_key = v_batch_key;

    RAISE NOTICE 'batch % 완료: 할인율=%, 최소가격=%, 처리건수=%',
                 v_batch_key, p_discount_percent, p_min_price, p_affected;
END;
$procedure$;
```

### 할인 전 가격 확인:

```sql
SELECT product_id, product_name, unit_price FROM proc_lab.products;
```

```text
product_id|product_name |unit_price
----------+-------------+----------
         1|기계식 키보드   |  89000.00
         2|무선 마우스    |  49000.00
         3|27인치 모니터  | 329000.00
         4|USB-C 허브   |  59000.00
         5|웹캠          |  79000.00
```

### 첫 번째 호출:

```text
CALL proc_lab.pr_bulk_discount_once('DAY04-SALE-001', 10, 70000, NULL);
```

```text
NOTICE: batch DAY04-SALE-001 완료: 할인율=10%, 최소가격=70000, 처리건수=3
```

### 할인 후 가격 확인:

```sql
SELECT product_id, product_name, unit_price FROM proc_lab.products;
```

```text
product_id|product_name |unit_price
----------+-------------+----------
         1|기계식 키보드   |  80100.00
         2|무선 마우스    |  49000.00
         3|27인치 모니터  | 296100.00
         4|USB-C 허브   |  59000.00
         5|웹캠          |  71100.00
```

### 두 번째 호출 (멱등성 확인):

```text
CALL proc_lab.pr_bulk_discount_once('DAY04-SALE-001', 10, 70000, NULL);
```

```text
NOTICE: batch_key DAY04-SALE-001는 이미 완료되었습니다. 기존 처리 건수=3
```

### 가격 변화 없음 확인:

```sql
SELECT product_id, product_name, unit_price FROM proc_lab.products;
```

```text
product_id|product_name |unit_price
----------+-------------+----------
         1|기계식 키보드   |  80100.00
         2|무선 마우스    |  49000.00
         3|27인치 모니터  | 296100.00
         4|USB-C 허브   |  59000.00
         5|웹캠          |  71100.00
```

### 이력 확인:

```sql
SELECT * FROM proc_lab.bulk_discount_runs;
```

```text
batch_key      |discount_percent|min_price|affected_count|run_status|started_at|completed_at
---------------+----------------+---------+--------------+----------+----------+------------
DAY04-SALE-001 |              10|    70000|             3|COMPLETED | (현재시각)| (현재시각)
```

### 문제 7. orders 변경 자동 감사

### 트리거 함수 정의:

```sql
CREATE OR REPLACE FUNCTION proc_lab.fn_audit_orders()
RETURNS trigger
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = pg_catalog, proc_lab, pg_temp
AS $function$
BEGIN
    INSERT INTO proc_lab.audit_log
        (table_name, operation, row_id, old_data, new_data, changed_by)
    VALUES (
        TG_TABLE_NAME,
        TG_OP,
        CASE
            WHEN TG_OP = 'DELETE' THEN OLD.order_id
            ELSE NEW.order_id
        END,
        CASE WHEN TG_OP IN ('UPDATE', 'DELETE') THEN to_jsonb(OLD) END,
        CASE WHEN TG_OP IN ('INSERT', 'UPDATE') THEN to_jsonb(NEW) END,
        session_user
    );

    IF TG_OP = 'DELETE' THEN
        RETURN OLD;
    END IF;

    RETURN NEW;
END;
$function$;
```

### 트리거 생성:

```text
DROP TRIGGER IF EXISTS trg_orders_audit ON proc_lab.orders;

CREATE TRIGGER trg_orders_audit
AFTER INSERT OR UPDATE OR DELETE
ON proc_lab.orders
FOR EACH ROW
EXECUTE FUNCTION proc_lab.fn_audit_orders();
```

### 검증:

```text
BEGIN;

UPDATE proc_lab.orders
   SET note = '문제 7 감사 테스트'
 WHERE order_id = 1;
```

### 감사 로그 확인:

```sql
SELECT audit_id, table_name, operation, row_id, changed_by, changed_at,
       old_data, new_data
  FROM proc_lab.audit_log
 ORDER BY audit_id DESC;
```

```text
audit_id|table_name|operation|row_id|changed_by|old_data           |new_data
--------+----------+---------+------+----------+-------------------+--------
       1|orders    |UPDATE   |     1|postgres  |{"note": "오전 배송 희망", ...}|{"note": "문제 7 감사 테스트", ...}
```

```text
ROLLBACK;
```

### 문제 8. 주문 상세 변경 시 주문 총액 자동 재계산

### 트리거 함수 정의:

```sql
CREATE OR REPLACE FUNCTION proc_lab.fn_sync_order_total()
RETURNS trigger
LANGUAGE plpgsql
AS $function$
BEGIN
    IF TG_OP = 'UPDATE' AND OLD.order_id <> NEW.order_id THEN
        UPDATE proc_lab.orders
           SET total_amount = (
               SELECT coalesce(sum(line_amount), 0)
                 FROM proc_lab.order_items
                WHERE order_id = OLD.order_id
           ),
           updated_at = clock_timestamp()
         WHERE order_id = OLD.order_id;
    END IF;

    UPDATE proc_lab.orders
       SET total_amount = (
               SELECT coalesce(sum(line_amount), 0)
                 FROM proc_lab.order_items
                WHERE order_id = CASE WHEN TG_OP = 'DELETE'
                                      THEN OLD.order_id
                                      ELSE NEW.order_id
                                 END
           ),
           updated_at = clock_timestamp()
     WHERE order_id = CASE WHEN TG_OP = 'DELETE'
                           THEN OLD.order_id
                           ELSE NEW.order_id
                      END;

    IF TG_OP = 'DELETE' THEN
        RETURN OLD;
    END IF;

    RETURN NEW;
END;
$function$;
```

### 트리거 생성:

```text
DROP TRIGGER IF EXISTS trg_order_items_sync_total ON proc_lab.order_items;

CREATE TRIGGER trg_order_items_sync_total
AFTER INSERT OR UPDATE OR DELETE
ON proc_lab.order_items
FOR EACH ROW
EXECUTE FUNCTION proc_lab.fn_sync_order_total();
```

### 기존 총액 확인:

```sql
SELECT order_id, total_amount FROM proc_lab.orders WHERE order_id = 3;
```

```text
order_id|total_amount
--------+------------
       3|   118000.00
```

### 검증:

```sql
BEGIN;

INSERT INTO proc_lab.order_items (order_id, product_id, quantity, unit_price)
VALUES (3, 1, 2, 89000);

SELECT order_id, total_amount FROM proc_lab.orders WHERE order_id = 3;
```

```text
order_id|total_amount
--------+------------
       3|   296000.00
```

```sql
UPDATE proc_lab.order_items
   SET quantity = 3
 WHERE order_id = 3 AND product_id = 1;

SELECT order_id, total_amount FROM proc_lab.orders WHERE order_id = 3;
```

```text
order_id|total_amount
--------+------------
       3|   385000.00
```

```sql
DELETE FROM proc_lab.order_items
 WHERE order_id = 3 AND product_id = 1;

SELECT order_id, total_amount FROM proc_lab.orders WHERE order_id = 3;
```

```text
order_id|total_amount
--------+------------
       3|   118000.00
```

```text
ROLLBACK;
```

## 관련 글

- [[blog/STUDYING/index|STUDYING]]
