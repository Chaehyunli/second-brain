---
title: "[STUDYING] 12 - 1. 스마트 데이터 이해 및 활용_Day4_핵심 정리"
created: 2026-07-31
updated: 2026-07-31
type: blog-post
tags: ["blog", "technical-writing"]
category: "STUDYING"
published: 2026-07-30
source_url: https://ch010104.tistory.com/327
---
# [STUDYING] 12 - 1. 스마트 데이터 이해 및 활용_Day4_핵심 정리

## 원문

https://ch010104.tistory.com/327

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

두 객체는 모두 DB에 저장된 로직이지만, 목적과 사용 맥락이 다름.

핵심 구분 기준: "결과값 하나를 돌려주는가, 아니면 여러 SQL을 묶어 처리하는가"로 쉽게 나뉨. 함수는 SELECT 안에서 행마다 호출되므로 DML이 일어나면 쿼리 실행 중 데이터가 바뀌어 일관성이 깨짐. 그래서 구조적으로 DML을 막아둔 것임.

## 원문 기반 개념 정리

### Stored Procedure vs 함수 (Function / UDF) 비교

두 객체는 모두 DB에 저장된 로직이지만, 목적과 사용 맥락이 다름.

핵심 구분 기준: "결과값 하나를 돌려주는가, 아니면 여러 SQL을 묶어 처리하는가"로 쉽게 나뉨. 함수는 SELECT 안에서 행마다 호출되므로 DML이 일어나면 쿼리 실행 중 데이터가 바뀌어 일관성이 깨짐. 그래서 구조적으로 DML을 막아둔 것임.

### 함수 예시 — 4개 DBMS (부가세 10% 계산)

fn_vat(amount) 함수를 DBMS별로 구현. amount * 0.1이라는 동일한 연산을 각 DBMS 문법에 맞게 선언하는 것이 핵심이고, DBMS마다 함수의 순수성(같은 입력 → 같은 출력 보장 여부)을 선언하는 키워드가 다름.

```sql
-- MySQL / MariaDB
CREATE FUNCTION fn_vat(amount DECIMAL(10,2))
RETURNS DECIMAL(10,2) DETERMINISTIC
-- DETERMINISTIC: 같은 입력이면 항상 같은 결과를 보장한다고 선언
-- 옵티마이저가 불필요한 재계산을 줄일 수 있음
BEGIN RETURN amount * 0.1; END;

-- 호출: orders 테이블의 각 행에서 total_amount에 fn_vat를 적용해 vat 컬럼으로 출력
SELECT order_id, fn_vat(total_amount) AS vat FROM orders;
```

```sql
-- PostgreSQL
CREATE OR REPLACE FUNCTION fn_vat(amount NUMERIC)
RETURNS NUMERIC LANGUAGE sql IMMUTABLE
-- IMMUTABLE: 입력값만으로 결과가 확정됨 → DB 상태와 무관
-- 이 덕분에 함수를 인덱스 표현식에도 사용할 수 있음
AS $$ SELECT amount * 0.1 $$;

-- 함수 기반 인덱스: fn_vat(total_amount) 결과값에 인덱스를 걸어
-- WHERE fn_vat(total_amount) > 1000 같은 조건도 인덱스 스캔 가능
CREATE INDEX idx_tax ON orders ((fn_vat(total_amount)));
```

```sql
-- SQL Server (인라인 테이블 함수 — 가장 빠름)
-- 스칼라 함수 대신 테이블을 반환하는 형태로 만들면
-- 옵티마이저가 인라인으로 펼쳐서 실행하므로 성능이 더 좋음
CREATE FUNCTION dbo.fn_vat(@amount DECIMAL(10,2))
RETURNS TABLE AS RETURN (SELECT @amount * 0.1 AS tax);
```

```text
-- Oracle
CREATE OR REPLACE FUNCTION fn_vat(p_amount NUMBER)
RETURN NUMBER RESULT_CACHE DETERMINISTIC
-- RESULT_CACHE: 한 번 계산한 결과를 메모리에 캐싱해두고 같은 입력이 오면 재사용
-- 자주 호출되는 함수에서 성능 이점이 큼
IS BEGIN RETURN p_amount * 0.1; END;
/
```

PostgreSQL의 함수 순수성 키워드 정리:

### Stored Procedure 예시 — 4개 DBMS (연도별 매출 상위 5명)

sp_top_customers(p_year) 프로시저. 연도를 파라미터로 받아 해당 연도의 고객별 총 매출을 집계하고 상위 5명을 반환함. orders와 customers를 JOIN한 뒤 GROUP BY로 고객별 합산, ORDER BY ... DESC로 내림차순 정렬하는 구조는 세 DBMS 모두 동일하고, 문법 선언 방식만 다름.

→ 하나의 SQL 저장 프로시저 안에는 여러개의 SELECT 문, DML 등을 원하는 만큼 추가 가능

```sql
-- MySQL
DELIMITER $$
-- MySQL은 기본 구문 종결자가 ;이므로, 프로시저 본문 안의 ;와 충돌하지 않도록
-- DELIMITER로 구분자를 $$로 임시 변경한 뒤 정의하고 다시 복원함
CREATE PROCEDURE sp_top_customers(IN p_year INT)
-- IN: 입력 전용 파라미터 (OUT이면 출력, INOUT이면 양방향)
BEGIN
  SELECT c.customer_id, SUM(o.total_amount) AS total_sales
  FROM orders o JOIN customers c ON o.customer_id = c.customer_id
  WHERE YEAR(o.order_date) = p_year
  GROUP BY c.customer_id ORDER BY total_sales DESC LIMIT 5;
END$$
DELIMITER ;
CALL sp_top_customers(2024);
```

```sql
-- PostgreSQL
CREATE OR REPLACE PROCEDURE sp_top_customers(p_year INT) LANGUAGE plpgsql AS $$
-- LANGUAGE plpgsql: PostgreSQL의 절차적 언어(PL/pgSQL)를 사용한다고 명시
-- 연도 추출은 EXTRACT(YEAR FROM 날짜컬럼) 사용 (MySQL의 YEAR()와 동일한 역할)
BEGIN
  SELECT c.customer_id, SUM(o.total_amount)
  FROM orders o JOIN customers c ON c.customer_id = o.customer_id
  WHERE EXTRACT(YEAR FROM o.order_date) = p_year
  GROUP BY c.customer_id ORDER BY 2 DESC LIMIT 5;
-- ORDER BY 2: SELECT 절의 두 번째 컬럼(SUM)을 기준으로 정렬
END; $$;
CALL sp_top_customers(2024);
```

```sql
-- SQL Server
CREATE PROCEDURE sp_top_customers @year INT
-- 파라미터명 앞에 @ 붙임. IN/OUT 키워드 없이 기본이 입력 파라미터
AS
BEGIN
  SELECT TOP 5 c.customer_id, SUM(o.total_amount) AS total_sales
-- TOP 5: LIMIT 대신 SELECT 바로 뒤에 위치
  FROM orders o
  JOIN customers c ON c.customer_id = o.customer_id
  WHERE YEAR(o.order_date) = @year
  GROUP BY c.customer_id
  ORDER BY total_sales DESC;
END;
GO
-- GO: SQL Server에서 배치(batch) 구분자. 앞의 구문을 하나의 실행 단위로 서버에 전송
```

### 보안 모델 — DEFINER vs INVOKER

Stored Procedure·함수를 실행할 때 "누구의 권한으로 내부 SQL을 실행할 것인가"를 결정하는 설정임.

DEFINER: 프로시저/함수를 만든 사람(작성자)의 권한으로 실행. 호출자가 해당 테이블에 직접 접근 권한이 없어도 실행 가능.

INVOKER: 실제로 호출한 사람의 권한으로 실행. 호출자 권한이 부족하면 실행 중 에러 발생.

대부분의 DBMS에서 기본값은 DEFINER임. 호출자에게 테이블 직접 권한을 주지 않고 프로시저를 통해서만 접근하게 통제할 수 있어 보안 설계에 자주 쓰임. 단, 잘못 설정하면 권한 상승 경로가 되므로 주의가 필요함.

search_path 하이재킹이란, DEFINER 함수 실행 중 악의적인 사용자가 스키마 탐색 순서를 조작해 의도한 것과 다른 테이블·함수가 호출되도록 만드는 공격임. 이를 막으려면 함수 정의 시 SET search_path = public 처럼 경로를 명시적으로 고정해야 함.

Oracle에서 ROLE 권한이 유효하지 않은 이유는, PL/SQL 실행 컨텍스트에서는 세션에 부여된 ROLE이 비활성화되고 직접 GRANT된 권한만 인정되기 때문임. 프로시저 안에서 테이블에 접근하려면 ROLE이 아닌 직접 권한 부여가 필요함.

### 함수 성능 키워드 — DB별 최적화 힌트

함수를 선언할 때 "이 함수의 결과가 얼마나 안정적인가"를 DB에 알려주는 키워드가 있음. 이를 통해 옵티마이저가 불필요한 재계산을 줄이거나, 인덱스에 함수를 사용하거나, 캐싱을 적용할 수 있음. 자주 바뀌는 비즈니스 로직은 앱 코드에 두고, 여러 쿼리에서 공통으로 쓰이는 계산은 DB 함수로 두는 것이 기본 원칙임. Cloud 환경에서는 함수 실행 시간 제한이 있을 수 있으므로 주의.

### MySQL / MariaDB — DETERMINISTIC

같은 입력이면 항상 같은 결과를 보장한다고 선언하는 키워드. DB가 복제(replication)나 캐싱을 할 때 이 함수 결과를 믿고 재사용할 수 있어 안전해짐.

반대인 NOT DETERMINISTIC이 기본값이며, random(), NOW() 같이 호출 시점마다 결과가 달라지는 함수가 포함된 경우 해당됨.

### PostgreSQL — 함수 안정성 3단계

IMMUTABLE로 선언하면 옵티마이저가 인덱스 표현식이나 상수 폴딩(constant folding)에 해당 함수를 활용할 수 있어 성능상 이점이 큼. 단, 실제로 IMMUTABLE하지 않은 함수에 잘못 선언하면 결과 불일치가 발생하므로 정확히 파악한 뒤 사용해야 함.

### SQL Server — 인라인 함수 vs 스칼라 함수

인라인 테이블 함수(iTVF): 내부 SQL을 그대로 쿼리 안에 펼쳐서(인라이닝) 실행함. 옵티마이저가 전체 쿼리와 함께 최적화할 수 있어 빠름.

스칼라 함수: 행마다 별도로 호출되어 느림. SQL Server 2019부터 일부 스칼라 함수에 자동 인라이닝이 지원되기 시작했지만, 성능이 중요한 경우 인라인 테이블 함수를 우선 고려하는 것이 권장됨.

### Oracle — RESULT_CACHE

같은 입력값이 여러 번 들어올 때 최초 계산 결과를 SGA(공유 메모리 영역)에 캐싱해두고 재사용함. 계산 비용이 높고 동일 입력이 반복되는 함수에서 효과가 큼.

### Stored Procedure 심화 — 에러 처리 패턴

### 예외 처리 (Exception Handling)

프로시저 실행 중 에러가 발생했을 때 이를 잡아서 처리하는 구문. DBMS마다 문법이 다르지만 역할은 동일함 — 에러 발생 시 롤백하거나 로그를 남기거나 대체 로직을 실행함.

### 트랜잭션 롤백 패턴 (주문 생성 SP 예시)

여러 DML이 순서대로 실행되어야 하는 작업에서 중간에 실패하면 전체를 되돌리는 패턴임. 주문 생성의 경우 아래 순서로 실행되며, 하나라도 실패하면 앞서 성공한 작업까지 전부 롤백해야 데이터 불일치가 생기지 않음.

```text
재고 확인
→ 주문 헤더 INSERT
→ 주문 아이템 INSERT
→ 재고 UPDATE
→ 모든 단계 성공 시 COMMIT
→ 재고 부족 등 실패 시 전체 ROLLBACK + 에러 발생
```

이처럼 "전부 성공하거나 전부 실패하거나"를 보장하는 것이 트랜잭션의 핵심이며, Stored Procedure가 이 패턴에 적합한 이유임.

### 커서 (Cursor) 활용

결과 집합을 행 단위로 순회하며 처리할 때 사용하는 객체임. 예를 들어 각 행마다 조건에 따라 다른 로직을 적용해야 할 때 씀.

단, 커서는 행마다 개별 처리하므로 대용량 데이터에서는 매우 느림. 가능하면 UPDATE ... WHERE, INSERT ... SELECT 같은 집합 기반(Set-based) 처리로 대체하는 것이 권장됨.

### SP(Stored Procedure) vs 앱 코드 선택 기준

DB에 두면 네트워크 왕복 없이 데이터 가까이서 처리 가능하지만, 배포·버전 관리가 어려움. 앱 코드에 두면 테스트·변경이 쉽지만 DB 왕복이 늘어남. 변경 빈도와 데이터 접근 패턴을 기준으로 판단함.

### PostgreSQL SP 예시 — 주문 생성 (재고 부족 시 ROLLBACK)

앞서 설명한 트랜잭션 롤백 패턴을 실제 코드로 구현한 예시임. p_items로 주문할 상품 목록을 JSONB 배열로 받아, 각 아이템을 순회하며 재고 확인 → 삽입 → 차감을 순서대로 처리함. 중간에 재고가 부족하면 RAISE EXCEPTION으로 에러를 발생시키고, PostgreSQL이 자동으로 전체를 롤백함.

```sql
CREATE OR REPLACE PROCEDURE sp_create_order(
  p_customer_id BIGINT,
  p_items JSONB  -- 주문 상품 목록을 JSON 배열로 받음. 예: [{"product_id":1,"qty":2}, ...]
) LANGUAGE plpgsql AS $$
DECLARE
-- 프로시저 안에서 사용할 지역 변수 선언
  v_order_id BIGINT;   -- INSERT 후 생성된 주문 ID를 담을 변수
  v_item     JSONB;    -- 루프에서 현재 처리 중인 아이템
  v_stock    INT;      -- 조회한 재고 수량
  v_price    NUMERIC;  -- 조회한 상품 단가
BEGIN

-- 1. 주문 헤더 생성
  INSERT INTO orders (customer_id, status)
  VALUES (p_customer_id, 'created')
  RETURNING id INTO v_order_id;
-- RETURNING ... INTO: INSERT 직후 생성된 PK를 바로 변수에 저장하는 PostgreSQL 문법

-- 2. 각 아이템 처리 (JSONB 배열을 행으로 풀어서 순회)
  FOR v_item IN SELECT * FROM jsonb_array_elements(p_items) LOOP
-- jsonb_array_elements(): JSONB 배열을 행 단위로 분해하는 함수

-- 재고 확인 (FOR UPDATE로 동시성 처리)
    SELECT stock_qty, price INTO v_stock, v_price
    FROM products
    WHERE id = (v_item->>'product_id')::INT FOR UPDATE;
-- FOR UPDATE: 이 행을 조회하는 동시에 잠금(lock)을 걸어
-- 다른 트랜잭션이 동시에 같은 재고를 차감하지 못하도록 막음

-- 재고 부족 시 예외 발생 → 자동 ROLLBACK
    IF v_stock < (v_item->>'qty')::INT THEN
      RAISE EXCEPTION '재고 부족: product_id=%', (v_item->>'product_id');
-- RAISE EXCEPTION: 에러를 발생시켜 이후 코드 실행을 중단함
-- PostgreSQL은 EXCEPTION 발생 시 해당 트랜잭션을 자동으로 전체 롤백함
    END IF;

-- 주문 아이템 삽입 + 재고 차감
    INSERT INTO order_items (order_id, product_id, qty, unit_price)
    VALUES (v_order_id, (v_item->>'product_id')::INT, (v_item->>'qty')::INT, v_price);
-- v_item->>'product_id': JSONB에서 product_id 값을 텍스트로 추출 후 ::INT로 캐스팅

    UPDATE products
    SET stock_qty = stock_qty - (v_item->>'qty')::INT
    WHERE id = (v_item->>'product_id')::INT;

  END LOOP;

-- 모든 아이템 처리 성공 시 주문 상태를 'paid'로 변경
  UPDATE orders SET status = 'paid' WHERE id = v_order_id;

-- EXCEPTION이 없으면 트랜잭션은 CALL 이후 자동 COMMIT됨
END; $$;

-- 호출 예시: 고객 42번이 상품 1번 2개, 상품 3번 1개 주문
CALL sp_create_order(42, '[{"product_id":1,"qty":2},{"product_id":3,"qty":1}]');
```

실행 흐름 요약:

```text
주문 헤더 INSERT (orders)
  → 아이템 1 재고 확인 (FOR UPDATE 잠금)
    → 재고 충분하면 order_items INSERT + products 재고 차감
  → 아이템 2 재고 확인 ...
    → 재고 부족이면 RAISE EXCEPTION → 전체 ROLLBACK
  → 모든 아이템 성공 → status = 'paid' UPDATE → COMMIT
```

FOR UPDATE 없이 재고를 조회하면, 동시에 두 요청이 같은 재고를 읽고 둘 다 차감을 시도해 재고가 음수가 되는 문제가 생길 수 있음. 잠금을 걸면 먼저 온 요청이 끝날 때까지 나머지는 대기하게 되어 이를 방지함.

### Trigger 기본 개념 및 사용 시점

Trigger는 특정 DML(INSERT, UPDATE, DELETE) 또는 DDL 이벤트가 발생할 때 DB가 자동으로 실행하는 코드임. 사람이 직접 호출하는 SP와 달리, 이벤트에 반응해 자동으로 실행된다는 점이 핵심 차이임.

### 트리거의 구성 요소

타이밍 — 이벤트 기준으로 언제 실행할지 결정함:

BEFORE: DML 실행 전. 값을 검증하거나 변경할 때 씀.

AFTER: DML 실행 후. 로그 기록, 파생 컬럼 업데이트 등에 씀.

INSTEAD OF: 뷰 전용. DML을 실제로 실행하지 않고 트리거 로직으로 대체함.

→ 보통 AFTER 를 많이 사용함

범위 — 몇 번 실행할지 결정함:

행 단위(FOR EACH ROW): 영향받은 행 하나마다 트리거가 한 번씩 실행됨. 행별로 다른 처리가 필요할 때 씀.

문장 단위(statement-level): DML 전체에 대해 한 번만 실행됨. 행 수에 무관하게 실행 횟수가 고정됨.

가상 테이블 — 트리거 안에서 변경 전/후 값에 접근하는 방법:

MySQL / PostgreSQL / Oracle: OLD(변경 전 행), NEW(변경 후 행)

SQL Server: deleted(변경 전), inserted(변경 후)

예를 들어 UPDATE 트리거에서 OLD.price는 수정 전 가격, NEW.price는 수정 후 가격을 가리킴.

### 트리거가 잘 맞는 경우

감사 로그(Audit): 누가 언제 무엇을 바꿨는지 자동으로 기록. 앱 코드와 무관하게 DB 레벨에서 강제할 수 있어 누락 위험이 없음.

기본값/유효성 보강: created_at 자동 세팅, 다른 컬럼 값으로부터 계산되는 파생 컬럼 자동 갱신.

비즈니스 규칙 보강: 재고 수량이 음수가 되는 것을 DB 레벨에서 차단.

소프트 삭제/버전 관리: 삭제 이벤트 발생 시 행을 실제로 지우지 않고 아카이브 테이블로 이동.

### 피해야 할 경우

외부 연동 (API 호출, 장시간 작업): 트리거는 DML 트랜잭션 안에서 실행되므로, 외부 호출이 느리거나 실패하면 트랜잭션 전체가 지연되거나 롤백됨.

순서 의존/상호참조 트리거: 트리거가 다른 트리거를 유발하는 연쇄 구조는 실행 흐름을 추적하기 어려워 유지보수가 매우 힘들어짐.

대량 DML에 행 단위 트리거: UPDATE 100만 행에 FOR EACH ROW 트리거가 걸려 있으면 트리거가 100만 번 실행됨. 이 경우 문장 단위(statement-level) 트리거로 전환하거나 배치 처리로 분리하는 것이 권장됨.

### Trigger 예시 — PostgreSQL 감사 로그 (row-level vs statement-level)

PostgreSQL에서 트리거는 함수와 트리거 선언 두 단계로 나뉨. 먼저 트리거가 실행할 로직을 함수로 만들고, 그 함수를 언제 어떤 테이블에 붙일지를 CREATE TRIGGER로 선언하는 구조임.

### 공통 — 감사 로그 테이블

```sql
CREATE TABLE audit_log(
  id         BIGSERIAL PRIMARY KEY,  -- 자동 증가 PK
  table_name TEXT,                   -- 어느 테이블에서 발생한 이벤트인지
  op         TEXT,                   -- 어떤 DML인지 (INSERT/UPDATE/DELETE)
  row_json   JSONB,                  -- 변경된 행의 전체 데이터를 JSON으로 저장
  at         TIMESTAMPTZ DEFAULT now() -- 발생 시각 자동 기록
);
```

### Row-level 트리거 — 행마다 실행

```sql
-- 트리거 함수 정의
CREATE OR REPLACE FUNCTION trg_sales_ai() RETURNS trigger AS $$
BEGIN
  INSERT INTO audit_log(table_name, op, row_json)
  VALUES ('sales', TG_OP, to_jsonb(NEW));
-- TG_OP: 트리거를 유발한 DML 종류를 담은 내장 변수 ('INSERT'/'UPDATE'/'DELETE')
-- NEW: 방금 삽입된 행 전체를 가리키는 가상 레코드
-- to_jsonb(NEW): 해당 행을 JSONB로 변환해 로그에 저장

  RETURN NEW;
-- BEFORE 트리거면 RETURN NEW가 실제 INSERT에 반영될 값을 결정함
-- AFTER 트리거에서는 이미 INSERT가 끝났으므로 형식적인 반환값임
END$$ LANGUAGE plpgsql;

-- 트리거 선언
CREATE TRIGGER sales_ai
AFTER INSERT ON sales          -- sales 테이블에 INSERT가 발생한 후
FOR EACH ROW                   -- 삽입된 행 하나마다
EXECUTE FUNCTION trg_sales_ai(); -- 위 함수를 실행
```

INSERT 10건이면 트리거 함수가 10번 호출되고, audit_log에도 10개의 행이 생김.

### Statement-level 트리거 + Transition table — 대량 DML에 효율적

```sql
-- 트리거 함수 정의
CREATE OR REPLACE FUNCTION trg_sales_stmt_ai() RETURNS trigger AS $$
BEGIN
  INSERT INTO audit_log(table_name, op, row_json)
  SELECT 'sales', TG_OP, to_jsonb(n)
  FROM new_table AS n;
-- new_table: REFERENCING NEW TABLE로 선언한 Transition table
-- INSERT로 영향받은 모든 행이 new_table에 한꺼번에 담겨 있음
-- 행마다 함수를 호출하는 대신, 한 번 호출에 전체 행을 SET 기반으로 처리

  RETURN NULL;
-- statement-level 트리거는 특정 행을 반환하지 않으므로 NULL 반환
END$$ LANGUAGE plpgsql;

-- 트리거 선언
CREATE TRIGGER sales_stmt_ai
AFTER INSERT ON sales
REFERENCING NEW TABLE AS new_table  -- 이번 INSERT로 삽입된 전체 행을 new_table이라는 이름으로 참조
FOR EACH STATEMENT                  -- DML 전체에 대해 딱 한 번만 실행
EXECUTE FUNCTION trg_sales_stmt_ai();
```

INSERT 10만 건이어도 트리거 함수는 딱 한 번만 호출되고, 내부에서 new_table을 SELECT해 한꺼번에 audit_log에 삽입함. row-level 대비 함수 호출 오버헤드가 없어 대량 DML에서 성능 차이가 큼.

두 방식 비교:

### Trigger 예시 — MySQL / SQL Server / Oracle 비교

### MySQL — row-level only, BEFORE/AFTER

MySQL은 row-level 트리거만 지원함. 같은 이벤트에 BEFORE와 AFTER 트리거를 각각 따로 만들 수 있음.

```sql
DELIMITER //

-- BEFORE INSERT 트리거: 삽입 전에 created_at 기본값 보정
CREATE TRIGGER sales_bi BEFORE INSERT ON sales FOR EACH ROW
BEGIN
  SET NEW.created_at = COALESCE(NEW.created_at, NOW());
-- COALESCE: 첫 번째 인자가 NULL이면 두 번째 값을 사용
-- 즉, 앱에서 created_at을 넘기면 그대로 쓰고, 안 넘기면 현재 시각으로 채움
END//

-- AFTER INSERT 트리거: 삽입 후 audit_log에 기록
CREATE TRIGGER sales_ai AFTER INSERT ON sales FOR EACH ROW
BEGIN
  INSERT INTO audit_log(table_name, op, row_json)
  VALUES ('sales', 'INSERT', JSON_OBJECT('id', NEW.id, 'amount', NEW.amount));
-- JSON_OBJECT(): 키-값 쌍으로 JSON을 만드는 MySQL 함수
-- PostgreSQL의 to_jsonb(NEW)처럼 행 전체를 한 번에 변환하는 방법은 없어
-- 필요한 컬럼을 직접 나열해야 함
END//

DELIMITER ;

-- 주의: MySQL은 트리거 안에서 트리거가 걸린 같은 테이블(sales)을 수정하면 오류 1442 발생
```

### SQL Server — statement-level 중심, inserted/deleted 가상 테이블

```sql
CREATE TRIGGER dbo.trg_sales_ai ON dbo.Sales AFTER INSERT AS
BEGIN
  SET NOCOUNT ON;
-- NOCOUNT ON: 트리거 내부 DML이 "몇 행 영향받음" 메시지를 클라이언트에 보내지 않도록 억제
-- 없으면 앱에서 영향받은 행 수를 잘못 읽는 문제가 생길 수 있음

  INSERT INTO dbo.AuditLog(table_name, op, row_json, at)
  SELECT 'Sales', 'INSERT', (SELECT * FROM inserted FOR JSON PATH), SYSUTCDATETIME();
-- inserted: SQL Server의 가상 테이블. 이번 INSERT로 삽입된 모든 행이 담겨 있음
-- FOR JSON PATH: inserted 결과를 JSON 문자열로 변환
-- SYSUTCDATETIME(): UTC 기준 현재 시각
END;
-- SQL Server 트리거는 기본적으로 statement-level처럼 동작하며
-- inserted/deleted에 이번 DML로 영향받은 전체 행이 들어옴
```

### Oracle — BEFORE row + Compound Trigger로 Mutating Table 회피

```text
-- BEFORE row 트리거: 삽입 전 created_at 기본값 세팅
CREATE OR REPLACE TRIGGER sales_bi BEFORE INSERT ON sales FOR EACH ROW
BEGIN
  :NEW.created_at := NVL(:NEW.created_at, SYSTIMESTAMP);
-- Oracle에서 NEW/OLD 앞에 콜론(:)을 붙임 (:NEW, :OLD)
-- NVL(): NULL이면 두 번째 값으로 대체. MySQL COALESCE, PostgreSQL COALESCE와 동일한 역할
-- SYSTIMESTAMP: 현재 타임스탬프 (시간대 포함)
END;
/
-- /: Oracle SQL*Plus에서 PL/SQL 블록 실행 종결자

-- Mutating Table 문제:
-- Oracle에서 row 트리거 안에서 트리거가 걸린 테이블을 SELECT/UPDATE하면 오류 발생
-- 이를 해결하려면 Compound Trigger를 사용함
-- (BEFORE STATEMENT / BEFORE EACH ROW / AFTER EACH ROW / AFTER STATEMENT 4개 시점을
--  하나의 트리거 블록 안에 묶어, AFTER STATEMENT 시점에 집계 처리하는 방식)
```

### DBMS별 Trigger 기능 비교

설계 관점 핵심: MySQL은 row 트리거만 지원하므로, 대량 DML에서 트리거가 걸리면 행 수만큼 반복 실행되어 성능 부담이 큼. SQL Server는 statement 트리거 중심으로 설계되어 inserted/deleted에 전체 변경 행이 한꺼번에 담기므로, 트리거 안에서 집합 기반 처리를 해야 정확한 결과를 얻을 수 있음. 이 차이가 트리거 설계 방식에 큰 영향을 줌.

### 이벤트 처리 아키텍처 — 배치·알림·CDC

트리거에서 외부 API를 직접 호출하면 트랜잭션이 외부 응답을 기다리며 지연되거나, 외부 장애가 DB 트랜잭션 실패로 전파됨. 그래서 원칙은 트리거는 로그 테이블이나 메시지 토픽에 이벤트를 쌓는 것까지만 하고, 실제 처리는 비동기 소비자가 담당하도록 분리하는 것임.

### 스케줄 작업 (배치)

주기적으로 SQL을 자동 실행하는 내장 스케줄러. DBMS마다 제공 방식이 다름.

MySQL / MariaDB: EVENT Scheduler 사용. 기본적으로 꺼져 있어 SET GLOBAL event_scheduler = ON;으로 활성화 필요.

PostgreSQL: 내장 스케줄러가 없음. pg_cron 확장을 설치하거나 OS 레벨 cron, 외부 스케줄러(Airflow 등)를 사용함.

SQL Server: SQL Server Agent로 작업과 스케줄을 GUI 또는 T-SQL로 관리함.

Oracle: DBMS_SCHEDULER(현재 권장)와 구버전 방식인 DBMS_JOB 두 가지가 있음. DBMS_SCHEDULER가 더 세밀한 제어와 모니터링을 지원함.

### 알림 / 메시지

DB 이벤트를 앱에 실시간으로 전달하는 메커니즘. 트리거가 이벤트를 감지하고, 채널에 메시지를 보내면 앱이 구독해서 받는 구조임.

PostgreSQL: LISTEN / NOTIFY 메커니즘. 트리거 안에서 PERFORM pg_notify('channel', payload)로 메시지를 발행하면, 해당 채널을 LISTEN하고 있는 앱이 실시간으로 수신함. 폴링 없이 push 방식으로 동작해 가볍고 빠름.

SQL Server: Service Broker(DB 내부 큐 기반 비동기 메시징)와 Event Notifications를 사용함.

Oracle: Advanced Queuing (AQ). DB 안에 메시지 큐를 내장해 발행-구독 패턴을 구현함.

### CDC (Change Data Capture)

DB의 변경 내역(INSERT/UPDATE/DELETE)을 실시간 이벤트 스트림으로 외부에 흘려보내는 아키텍처. 트리거 기반 감사 로그와 달리, DB 내부 로그(바이너리 로그, WAL)를 직접 읽으므로 DB 부하가 거의 없음.

MySQL / MariaDB: Binlog(바이너리 로그)를 Debezium이 읽어 Kafka로 전달하는 구조가 표준 패턴임. Debezium은 Kafka Connect 기반 CDC 오픈소스.

PostgreSQL: Logical Decoding 기능으로 WAL(Write-Ahead Log)을 논리적 변경 스트림으로 변환함. wal2json, pgoutput 등의 플러그인을 사용하고, 마찬가지로 Debezium → Kafka로 연결함.

SQL Server: CDC와 Change Tracking 기능이 내장되어 있어 별도 도구 없이도 변경 추적이 가능함.

Oracle: GoldenGate가 표준 솔루션임. 엔터프라이즈급 상용 제품으로 다양한 이기종 DB 간 실시간 복제도 지원함.

### Trigger 심화 — CDC 패턴과 pg_notify

### CDC with Trigger (Outbox 패턴)

Debezium 같은 외부 도구 없이 트리거만으로 간단한 CDC를 구현할 수 있음. 트리거가 변경 내용을 outbox 테이블에 기록하면, 별도 프로세스(앱 워커, 배치 등)가 이를 읽어 처리하는 구조임. 트리거는 기록까지만 담당하고 외부 처리는 분리함.

### PostgreSQL NOTIFY/LISTEN 패턴

트리거 안에서 pg_notify()를 호출하면 해당 채널을 구독(LISTEN)하고 있는 앱에 실시간으로 메시지가 push됨. 폴링 없이 이벤트 기반으로 동작해 실시간 대시보드 갱신, 웹소켓 푸시 알림 등에 활용됨.

### DDL Trigger — PostgreSQL Event Trigger

일반 트리거는 DML 이벤트에 반응하지만, PostgreSQL의 Event Trigger는 CREATE TABLE, ALTER TABLE 같은 DDL 이벤트에 반응함. 스키마 변경 감시·차단, 네이밍 규칙 자동 검사, DDL 변경 이력 자동 기록 등에 사용함.

### Trigger vs Application 선택 기준

트리거: 어떤 경로로 데이터가 변경되어도 반드시 실행되어야 하는 로직 (감사, 무결성 보강). 짧고 결정적으로, 외부 의존성 없이 작성하는 것이 원칙.

앱: 자주 바뀌는 비즈니스 로직, 외부 시스템 호출, 복잡한 흐름 제어.

### PostgreSQL Event Trigger & NOTIFY 예시

### 1. DDL 변경 이력 자동 기록

```sql
-- DDL 이력을 쌓을 테이블
CREATE TABLE ddl_history (
  id          BIGSERIAL PRIMARY KEY,
  event_tag   TEXT,                          -- 어떤 DDL인지 (CREATE TABLE 등)
  object      TEXT,                          -- 대상 객체명
  executed_by TEXT DEFAULT current_user,     -- 누가 실행했는지 자동 기록
  at          TIMESTAMPTZ DEFAULT now()
);

-- Event Trigger 함수: RETURNS event_trigger (일반 트리거와 반환 타입이 다름)
CREATE OR REPLACE FUNCTION fn_ddl_logger() RETURNS event_trigger AS $$
DECLARE r RECORD;
BEGIN
  FOR r IN SELECT * FROM pg_event_trigger_ddl_commands() LOOP
-- pg_event_trigger_ddl_commands(): 방금 실행된 DDL 명령의 상세 정보를 반환하는 내장 함수
-- command_tag(DDL 종류), object_identity(대상 객체) 등의 컬럼을 제공함
    INSERT INTO ddl_history(event_tag, object)
    VALUES (r.command_tag, r.object_identity);
  END LOOP;
END$$ LANGUAGE plpgsql;

-- Event Trigger 선언: ON ddl_command_end = DDL 실행이 끝난 직후 발동
CREATE EVENT TRIGGER ddl_logger ON ddl_command_end
EXECUTE FUNCTION fn_ddl_logger();
```

### 2. 실시간 알림 (NOTIFY/LISTEN)

```text
-- 트리거 함수: orders에 INSERT가 발생하면 order_channel로 메시지 발행
CREATE OR REPLACE FUNCTION fn_notify_order() RETURNS trigger AS $$
BEGIN
  PERFORM pg_notify('order_channel', row_to_json(NEW)::TEXT);
-- pg_notify(채널명, 페이로드): 해당 채널을 LISTEN 중인 모든 연결에 메시지 전송
-- row_to_json(NEW)::TEXT: 삽입된 행 전체를 JSON 문자열로 변환해 페이로드로 전달
  RETURN NEW;
END$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_order_notify AFTER INSERT ON orders
FOR EACH ROW EXECUTE FUNCTION fn_notify_order();
```

앱(Python psycopg2) 수신 측:

```text
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
# AUTOCOMMIT 필수: LISTEN은 트랜잭션 밖에서 동작해야 함
cur.execute("LISTEN order_channel")
while True:
    select.select([conn], ...)  # 소켓에 데이터가 올 때까지 블로킹 대기
    conn.poll()                 # 수신된 알림을 내부 큐로 가져옴
    print(conn.notifies.pop())  # 알림 꺼내서 처리
```

전체 흐름: orders INSERT → 트리거 발동 → pg_notify() → DB가 order_channel 구독자에게 push → 앱이 conn.poll()로 수신 → 처리.

### On-Prem vs DBaaS vs Cloud-Native DB 비교

DB를 어디서 어떻게 운영하느냐에 따라 세 가지 모델로 나뉨. 오른쪽으로 갈수록 클라우드 의존도가 높아지고, 운영 부담은 줄지만 커스터마이징 자유도도 함께 줄어드는 트레이드오프가 있음.

On-Prem: 서버를 직접 구매해 사내 데이터센터에 설치·운영하는 전통적인 방식. 모든 것을 직접 통제할 수 있지만 그만큼 책임도 전부 조직 안에 있음.

DBaaS (Database as a Service): AWS RDS, Google Cloud SQL처럼 클라우드 사업자가 DB 인스턴스를 제공하는 서비스. 기존 DBMS(MySQL, PostgreSQL 등)를 그대로 쓰되 운영 부담을 클라우드에 위임함.

Cloud-Native DB: Aurora(AWS), Spanner(GCP)처럼 클라우드 환경에 맞게 처음부터 새로 설계된 DB. 스토리지·복제·확장 구조 자체가 클라우드 전용으로 만들어져 있음.

→ CAPEX(자본지출) : 미래 가치를 위해 초기에 크게 투자하는 비용 → OPEX (운영비용) : 시스템을 유지·운영하기 위해 매달/매년 나가는 비용

### DBaaS 할 일 vs 우리가 할 일

DBaaS를 쓴다고 DB 관련 모든 책임이 사라지는 것이 아님. 인프라 레벨은 맡기지만, 데이터 설계·성능·보안의 책임은 여전히 사용자 몫임.

### DBaaS가 해주는 것

인프라와 운영 레벨의 반복 작업을 대신 처리해줌:

하드웨어/스토리지 관리, 장애 디스크 교체

백업/스냅샷 스케줄링 및 보관·복구 기능 제공

모니터링 지표·알림 제공

엔진 소규모 패치(마이너 버전 업데이트) 자동 적용

고가용성 토폴로지(Multi-AZ, 자동 장애조치) 제공

### 우리(고객)가 해야 하는 것

DBaaS가 대신해주지 않는 영역. 여전히 직접 판단하고 설계해야 함:

스키마/인덱스/쿼리 최적화: DBaaS라도 느린 쿼리, 잘못된 인덱스는 클라우드가 고쳐주지 않음. 성능 책임은 사용자에게 있음.

DB 파라미터 전략: 초기 설정과 운영 중 튜닝 프로파일을 직접 결정해야 함.

보안정책 설계: 권한 관리, 암호화 설정, 네트워크 경계(VPC, 보안 그룹 등) 설계는 직접 해야 함.

비용/성능 SLO 설계와 관측: 가용성 목표를 세우고, 실제로 지켜지는지 옵저버빌리티 체계를 갖추는 것은 사용자 몫임.

메이저 버전 Upgrade: 마이너 패치는 자동이지만, PostgreSQL 15 → 16 같은 메이저 업그레이드는 호환성을 직접 검증하고 타이밍을 결정해야 함.

호환성 검증: 버전 변경 시 기존 쿼리·드라이버·ORM이 정상 동작하는지 직접 확인해야 함.

### 어떤 모델을 선택할지 — 의사결정 기준

### AWS RDS vs Aurora 선택 가이드

RDS와 Aurora 모두 AWS의 관리형 DB 서비스지만, Aurora는 클라우드 전용으로 내부 구조를 새로 설계한 Cloud-Native DB임.

용어 정리:

EBS(Elastic Block Store): AWS의 블록 스토리지. RDS는 인스턴스마다 EBS 볼륨이 붙는 구조라 스토리지와 컴퓨팅이 묶여 있음.

Blue/Green 배포: 현재 운영 환경(Blue)과 동일한 새 환경(Green)을 만들어 트래픽을 전환하는 무중단 배포 방식. RDS에서 메이저 버전 업그레이드 시 활용함.

RDS Proxy: 앱과 DB 사이에 커넥션 풀링 레이어를 추가해, Lambda처럼 커넥션을 많이 여닫는 환경에서 DB 부하를 줄여주는 서비스.

Backtrack: Aurora 전용 기능. 실제 백업 없이도 특정 시점으로 DB를 되감을 수 있음. 실수로 데이터를 날렸을 때 빠르게 복구 가능.

Serverless v2: 트래픽에 따라 Aurora 컴퓨팅 용량을 자동으로 늘리고 줄이는 기능. 간헐적 트래픽 환경에서 비용 효율적임.

### GCP Cloud SQL & Azure Database 핵심

### GCP Cloud SQL

GCP의 표준 DBaaS. MySQL·PostgreSQL·SQL Server를 지원하며 RDS와 유사한 포지션임.

Enterprise / Enterprise Plus 에디션으로 성능 티어가 나뉨.

Regional HA: 기본/대기 인스턴스 구성으로 자동 페일오버. Read Replica로 읽기 확장 가능.

IAM DB Auth: GCP 서비스 계정이나 IAM 사용자 토큰으로 DB에 로그인할 수 있음. 비밀번호 없이 IAM 권한만으로 접근 제어가 가능해 보안 관리가 단순해짐. PostgreSQL 중심으로 지원.

최대 64TB 스토리지, 오토그로스(용량 자동 확장) 설정 가능.

### Azure Database (MySQL/PostgreSQL)

Azure의 표준 DBaaS. Flexible Server 모델로 제공되며 HA 구성을 선택할 수 있음.

Zone-redundant HA: SLA 99.99% 보장. 단, Burstable(저사양 버스트) 티어에서는 HA 미지원.

Microsoft Entra ID(구 Azure AD) 인증 연동 가능. Microsoft 생태계(Office 365, Azure 서비스)와 통합된 환경에서 편리함.

### Azure SQL Database (SQL Server 호환 PaaS)

On-Prem SQL Server를 클라우드로 올리거나, SQL Server 호환 DB가 필요할 때의 선택지.

Serverless: 사용하지 않을 때 자동 일시중지, 요청이 오면 재개. 간헐적 트래픽에서 비용 효율적.

Hyperscale: 수TB급 대용량 DB를 위한 티어. 신속한 백업·복구와 수평 확장 지원.

Managed Instance: On-Prem SQL Server와 가장 높은 호환성을 목표로 한 옵션. 기존 SQL Server 앱을 마이그레이션할 때 코드 변경을 최소화할 수 있음.

### GCP AlloyDB

GCP의 Cloud-Native DB. Aurora와 유사한 포지션으로, PostgreSQL 호환 인터페이스를 갖추면서 내부 아키텍처를 새로 설계함.

로그-분리형 아키텍처: 스토리지와 컴퓨팅을 분리하고, WAL 처리를 별도 레이어로 분리해 쓰기 성능을 높임.

분석(OLAP)과 트랜잭션(OLTP) 혼합 워크로드 성능에 특화되어 있음. 일반 PostgreSQL 대비 분석 쿼리에서 특히 차이가 나도록 설계됨.

### Cloud DB 선택 의사결정 프레임워크

Cloud DB를 선택할 때 순서대로 검토해야 할 4단계 프레임워크임.

### 1단계 — 규제/컴플라이언스 확인

가장 먼저 확인해야 하는 제약 조건. 기술 선호보다 법적 의무가 우선함.

데이터 주권(Data Residency): 특정 국가/리전에 데이터를 반드시 저장해야 하는 의무가 있는지 확인. 금융·의료·공공 분야에서 자주 등장함.

GDPR·개인정보보호법·금융 규제 등으로 외부 클라우드 반출이 금지된다면 → On-Prem 또는 특정 리전 Cloud로 제한됨.

### 2단계 — 팀 역량 확인

운영을 감당할 수 있는 인력이 있는지 현실적으로 판단함.

DBA 전문가가 있다 → On-Prem 운영 가능.

DevOps 팀이 작거나 DB 운영 인력이 부족하다 → DBaaS 권장. 운영 부담을 클라우드에 위임.

### 3단계 — 워크로드 특성

트래픽 패턴과 지리적 요구사항에 따라 적합한 DB 유형이 달라짐.

트래픽 예측 가능·안정적 → 고정 인스턴스 (RDS/Cloud SQL)

트래픽 급변·간헐적 → 서버리스 (Aurora Serverless v2, Neon)

글로벌 사용자·멀티리전 일관성 필요 → Spanner/CockroachDB

### 4단계 — 비용 총합 계산 (TCO)

단순 인스턴스 비용만 보지 않고 전체 비용 구조를 따져야 함.

On-Prem: CAPEX(서버 구매) + OPEX(인건비·전기·유지보수)

DBaaS: OPEX(사용량) + Data Egress + IOPS + 백업 스토리지

Cloud에서 간과하기 쉬운 항목: Egress(외부 전송), IOPS(디스크 입출력 횟수 과금), API 호출 비용

### 쿼리 및 아키텍처 개선 포인트

성능 문제를 마주쳤을 때 접근하는 두 가지 레벨의 개선 방법임.

쿼리 레벨 개선:

함수가 적용된 컬럼을 WHERE 조건으로 쓰면 인덱스를 못 탐 → 범위 조건으로 바꾸거나 함수 기반 인덱스로 전환

반복 서브쿼리 → JOIN 또는 CTE로 변경해 중복 실행 제거

N+1 문제(루프마다 쿼리 1번씩 실행) → 한 번의 JOIN으로 한꺼번에 가져오도록 수정

아키텍처 레벨 개선:

대용량 집계가 느린 경우 → Materialized View 또는 별도 집계 테이블로 미리 계산해두기

전체 테이블 스캔이 불가피한 경우 → 파티셔닝으로 스캔 범위를 줄여 I/O 감소

읽기 부하가 집중되는 경우 → Replica(읽기 전용 복제본)로 분산

### 서버리스·분산 DB 주요 서비스 4종

### Aurora Serverless v2 (MySQL/PG 호환)

트래픽에 따라 컴퓨팅 용량을 자동으로 늘리고 줄이는 Aurora. 간헐적이거나 변동성이 큰 OLTP 워크로드에 적합함.

ACU(Aurora Capacity Unit) 단위로 자동 스케일. 수동 개입 불필요.

Global DB·Backtrack 옵션 사용 가능.

스케일 이벤트 시 잠깐의 지연이 발생할 수 있으므로, 커넥션 풀·읽기/쓰기 분리 설계를 함께 고려해야 함.

### Google Cloud Spanner (True Distributed SQL)

전 세계에 분산된 노드에서 SQL과 강한 일관성을 동시에 제공하는 Cloud-Native DB. 멀티리전에서 단일 DB처럼 동작하는 것이 핵심임.

Paxos 합의 알고리즘 + TrueTime(원자시계 기반 타임스탬프)으로 글로벌 트랜잭션과 외부 일관성을 보장함.

Strict Serializability: 분산 환경에서 가장 강한 수준의 일관성 보장. 어느 리전에서 읽어도 항상 최신 커밋 상태를 봄.

스키마 설계와 핫스팟(특정 키에 트래픽 집중) 회피 설계가 성능에 결정적 영향을 미침.

### Azure Cosmos DB (다중 모델·일관성 선택)

단일 서비스에서 문서·키값·Cassandra·MongoDB 등 다양한 API를 지원하는 NoSQL DB. 일관성 레벨을 5단계로 선택할 수 있어 성능과 일관성을 트레이드오프할 수 있음. IoT·이벤트·세션 데이터처럼 전 지구적으로 분산된 쓰기가 많은 워크로드에 적합함. 일관성을 낮게 설정하면 그만큼 앱 로직에서 보완해야 함.

### PlanetScale / Neon / Supabase (차세대 개발자 DB)

개발자 경험을 중심으로 설계된 차세대 서비스들.

PlanetScale: MySQL 호환. Vitess(YouTube가 만든 MySQL 샤딩 레이어) 기반. DB 브랜칭(Git처럼 스키마를 브랜치로 관리)과 무중단 스키마 변경(Online DDL)이 강점.

Neon: PostgreSQL 호환. scale-to-zero(사용 안 하면 컴퓨팅이 꺼짐)와 스토리지-컴퓨팅 분리 구조. 개발·스테이징 환경 비용 절감에 유리.

Supabase: PostgreSQL에 인증(Auth)·실시간 구독(Realtime)·엣지 함수(Edge Functions)를 통합 제공. 백엔드 전체를 빠르게 구성할 수 있어 스타트업·해커톤에서 자주 씀.

### 서버리스/분산 vs 전통 RDBMS 비교

### MSA 환경 DB 패턴 선택 가이드

마이크로서비스 아키텍처(MSA)에서는 서비스 간 DB를 어떻게 나누고 데이터를 어떻게 일관성 있게 다룰지가 핵심 설계 과제임.

Saga Choreography vs Orchestration 차이: Choreography는 각 서비스가 이벤트를 듣고 알아서 반응하는 구조(분산), Orchestration은 한 곳에서 "A 해, 다음에 B 해"라고 지시하는 구조(중앙 집중)임. 전자는 결합도가 낮지만 흐름 파악이 어렵고, 후자는 흐름이 명확하지만 코디네이터 의존도가 높아짐.

### OLTP vs OLAP 비교

DB를 어떤 목적으로 쓰느냐에 따라 설계 방향이 완전히 달라짐. OLTP는 실시간 트랜잭션 처리, OLAP은 대량 데이터 분석에 최적화됨.

→ 스타/스노우플레이크 스키마: OLAP에서 쓰는 비정규화 스키마 설계 방식. 중앙에 팩트 테이블(매출 등 측정값), 주변에 차원 테이블(날짜·상품·지역 등)을 배치함. 스노우플레이크는 차원 테이블을 추가로 정규화한 형태.

### 분석 DB 핵심 기술 3가지

### 파티션 프루닝 (Partition Pruning)

테이블을 날짜·범위 등 기준으로 물리적으로 나눠두고, 쿼리 조건에 해당하는 파티션만 읽고 나머지는 완전히 건너뛰는 기술임. I/O를 수십~수백 배 줄일 수 있고, BigQuery·Snowflake처럼 스캔 바이트로 과금하는 서비스에서는 비용 직접 절감으로 이어짐.

DBMS별 구현 방식:

BigQuery: PARTITION BY DATE(event_time)으로 날짜 파티션 생성. WHERE event_time BETWEEN ... 조건이 있으면 해당 파티션만 스캔.

Snowflake: 마이크로파티션 통계(각 파티션의 min/max 값)를 자동 관리. 범위 밖 파티션은 자동으로 스킵.

ClickHouse: PARTITION BY toDate(ts) + ORDER BY로 범위별 병렬 처리. 파티션 키와 정렬 키를 함께 설계하는 것이 중요함.

### 컬럼 프루닝 (Column Pruning)

컬럼 지향 저장 방식의 핵심 이점. SELECT에 명시한 컬럼만 디스크에서 읽고, 나머지 컬럼은 I/O 자체가 발생하지 않음.

BigQuery에서는 스캔 바이트가 곧 비용이므로, SELECT *는 모든 컬럼을 읽어 불필요한 비용이 발생함. 분석 DB에서 SELECT *는 절대 금지로 취급하고, 필요한 컬럼만 명시하는 것이 원칙임.

### 벡터화 실행 (Vectorized Execution)

행 단위가 아닌 컬럼 단위로 값을 1000개씩 묶어(벡터) CPU SIMD 명령어로 한 번에 처리하는 방식임.

SIMD(Single Instruction Multiple Data): CPU가 하나의 명령으로 여러 데이터를 동시에 처리하는 명령어 집합. 예를 들어 SUM(amount)를 계산할 때 값 하나씩 더하는 대신, 1000개를 한 묶음으로 처리함.

BigQuery·Snowflake·DuckDB·ClickHouse 모두 벡터화 실행 엔진을 채택함.

효과: CPU 효율↑ (SIMD 활용), 캐시 효율↑ (연속 메모리 접근), 병렬 처리 용이.

세 기술의 관계: 파티션 프루닝으로 읽을 파일 수를 줄이고 → 컬럼 프루닝으로 읽을 컬럼을 줄이고 → 벡터화로 남은 데이터를 빠르게 처리하는 구조임. 분석 DB 성능 최적화의 핵심 3단계로 이해하면 됨.

### 분석 DB 제품별 특징 비교

### 스타 스키마 & 데이터 웨어하우스 설계 원칙

### 스타 스키마 (Star Schema)

DW의 기본 설계 형태. 중앙에 팩트 테이블을 두고 여러 디멘전 테이블이 별처럼 둘러싸는 구조임.

팩트 테이블: 매출액·수량·클릭수 같은 측정값(measure)과 FK만 담음. 행이 매우 많고 계속 추가(append-only)되며, 시간 기준으로 파티션을 나눔.

디멘전 테이블: 사용자·상품·시간·지역 등 분석 기준. 비교적 작고, SCD Type2로 이력을 관리함(값이 바뀌면 새 행을 추가해 과거 상태를 보존).

### 스타 스키마 설계 규칙

Surrogate Key: 디멘전에 정수형 대체키(자동 증가 ID)를 사용. 자연키(실제 속성값)는 변경될 수 있어 FK로 쓰기 위험함.

팩트는 얇게 길게: 많은 행, 측정값과 FK만. 설명성 컬럼은 디멘전에 둠.

Role-Playing Dimension: 날짜 디멘전 하나를 만들고 order_date, ship_date처럼 별칭을 붙여 여러 역할로 재사용.

Junk Dimension: Y/N, 소수 플래그 등 단독으로 디멘전 만들기 애매한 값들을 하나의 작은 디멘전으로 묶음.

Conformed Dimension: 여러 데이터 마트에서 같은 정의로 공유하는 디멘전(카테고리·지역 등). 일관된 분석 기준을 보장함.

### 스노우플레이크 vs 3NF DW

스노우플레이크 스키마: 스타 스키마에서 디멘전을 추가로 정규화한 형태. 카테고리·지역처럼 계층이 자주 바뀌는 경우에 선별 사용.

3NF DW: 원천/코어 레이어는 3NF로 정규화해 무결성을 유지하고, 소비 레이어(데이터 마트)는 스타 스키마로 비정규화해 쿼리 성능을 높이는 혼합 방식.

Cloud DW(BigQuery·Snowflake): 조인 비용이 낮으므로 굳이 정규화하지 않고 넓은(wide) 테이블을 선호하는 경향이 있음.

### BigQuery 파티션·클러스터 설계 + ClickHouse MergeTree

### BigQuery — 파티션 + 클러스터

```sql
-- 팩트 테이블 생성: 파티션 + 클러스터 동시 적용
CREATE TABLE mart.fact_sales
PARTITION BY DATE(event_ts)
-- 날짜별로 물리적으로 파티션을 나눔. 날짜 조건 쿼리 시 해당 파티션만 스캔 → 비용 절감
CLUSTER BY user_id, item_id AS
-- 파티션 안에서 user_id → item_id 순으로 정렬해 저장
-- user_id나 item_id로 필터링하면 관련 블록만 읽어 추가 I/O 절감
SELECT
  event_ts, user_id, item_id,
  qty, amount, channel
FROM stg.sales_cleaned;

-- 파티션 프루닝 적용 예시: Q1 기간만 집계
SELECT SUM(amount) FROM mart.fact_sales
WHERE event_ts >= '2024-01-01' AND event_ts < '2024-04-01';
-- → 2024년 1~3월 파티션만 스캔, 나머지 완전 스킵 → 비용 대폭 절감
```

파티션과 클러스터의 차이: 파티션은 파일 단위로 스킵하고, 클러스터는 파티션 안에서 블록 단위로 추가 스킵함. 함께 쓰면 두 단계로 I/O를 줄일 수 있음.

### ClickHouse — MergeTree 엔진 (초고속 실시간 OLAP)

```sql
CREATE TABLE fact_events (
  event_time DateTime,
  user_id    UInt64,
  action     LowCardinality(String),
-- LowCardinality: 값의 종류가 적은 컬럼(예: 'click','purchase' 등)에 적용
-- 내부적으로 딕셔너리 인코딩해 저장 공간과 연산 비용을 줄임
  amount     Decimal(12,2)
) ENGINE = MergeTree
PARTITION BY toDate(event_time)  -- 날짜별 파티션
ORDER BY (user_id, event_time)
-- 정렬 키 = 스킵 인덱스 역할. user_id로 필터링 시 관련 블록만 읽음
-- ORDER BY 설계가 ClickHouse 성능의 핵심
TTL event_time + INTERVAL 90 DAY;
-- TTL: 90일이 지난 데이터를 자동으로 삭제. 로그·이벤트 데이터 보관 정책에 유용

-- 실시간 집계 (ms 단위 응답 가능)
SELECT user_id, COUNT(), SUM(amount)
FROM fact_events
WHERE action = 'purchase'
  AND event_time >= today() - 7  -- 최근 7일
GROUP BY user_id
ORDER BY SUM(amount) DESC LIMIT 10;
```

ORDER BY가 ClickHouse에서 중요한 이유: 데이터가 정렬 키 순서로 저장되므로, WHERE user_id = 123 조건이 있으면 해당 user_id가 모인 블록만 읽으면 됨. OLTP의 B-Tree 인덱스와 비슷한 역할을 하지만 컬럼형 저장에 맞게 동작함.

### Cloud DW 제품 선택 가이드

요구사항 중심으로 어떤 제품을 고를지 정리한 의사결정 표임.

클라우드 벤더가 정해져 있으면 해당 벤더의 제품을 우선 검토하고, 멀티 클라우드이거나 운영을 단순하게 가져가고 싶으면 Snowflake, ms 단위 실시간 집계가 필요하면 ClickHouse를 고려하는 것이 기본 흐름임.

### Cloud DW 제품 선택 가이드

요구사항 중심으로 어떤 제품을 고를지 정리한 의사결정 표임.

선택 기준을 한 줄로 요약하면: 클라우드 벤더가 정해져 있으면 해당 벤더의 제품을 우선 검토하고, 멀티 클라우드이거나 운영을 단순하게 가져가고 싶으면 Snowflake, ms 단위 실시간 집계가 필요하면 ClickHouse를 고려하는 것이 기본 흐름임.

### NewSQL — SQL + 트랜잭션 + 수평 확장

전통 RDBMS는 ACID와 SQL이 강하지만 수평 확장이 어렵고, NoSQL은 확장은 쉽지만 트랜잭션·조인이 약함. NewSQL은 이 둘의 장점을 모두 취하는 방향으로 설계됨. Shared-nothing 분산 아키텍처 위에 Raft/Paxos(분산 합의) + MVCC(다중 버전 동시성 제어)를 얹어 강한 일관성과 수평 확장을 동시에 달성함.

### CockroachDB

키-값 스토어 위에 SQL 레이어, Range 단위 자동 샤딩, Raft 그룹 복제.

모든 노드가 동등(리더 없음), 자동 분산·리밸런싱, 기본 격리 수준이 SERIALIZABLE.

약점: 멀티리전 쓰기 시 합의 왕복으로 지연 증가, 스키마 설계 최적화 필요.

### TiDB (PingCAP)

MySQL 호환 SQL(TiDB) + TiKV(분산 KV, Raft) + PD(Placement Driver, 메타데이터 관리) + TiFlash(컬럼형 OLAP) 로 구성.

HTAP(OLTP+OLAP 동시 지원)이 강점. MySQL 생태계 완전 호환.

약점: 클러스터 구성요소가 많아 이해와 운영 복잡도가 높음.

선택 기준: 강한 일관성 + 기본 SERIALIZABLE → CockroachDB. MySQL 호환 유지 + 수평 확장 + HTAP → TiDB.

### 시계열 DB & Vector DB

### TimescaleDB (PostgreSQL 확장)

PostgreSQL 확장으로 설치하므로 표준 SQL·트랜잭션·GIS·확장 생태계를 그대로 유지하면서 시계열 최적화를 추가함.

```sql
CREATE EXTENSION IF NOT EXISTS timescaledb;

-- 일반 테이블 생성 후 Hypertable로 변환
CREATE TABLE metrics (
  ts       TIMESTAMPTZ NOT NULL,
  host     TEXT NOT NULL,
  cpu_pct  DOUBLE PRECISION,
  mem_mb   INT
);
SELECT create_hypertable('metrics', 'ts');
-- time + space 기준으로 파티션을 자동 관리하는 Hypertable로 변환
-- 이후부터는 일반 테이블처럼 INSERT/SELECT 가능

-- 테스트 데이터 10만 건 삽입
INSERT INTO metrics
SELECT now() - (random() * INTERVAL '30 days'),
  'host_' || (random()*10)::INT,
  random() * 100,
  (random() * 8192)::INT
FROM generate_series(1, 100000);

-- Continuous Aggregate: 5분 단위 평균 자동 집계
CREATE MATERIALIZED VIEW metrics_5m WITH (timescaledb.continuous) AS
SELECT time_bucket('5 minutes', ts) AS bucket,
  host, AVG(cpu_pct) AS cpu_avg, AVG(mem_mb) AS mem_avg
FROM metrics GROUP BY bucket, host;
-- time_bucket(): 시간을 지정 단위로 반올림하는 TimescaleDB 함수
-- WITH (timescaledb.continuous): 새 데이터가 들어오면 집계를 자동 갱신

-- 보존 정책: 30일 초과 데이터 자동 삭제
SELECT add_retention_policy('metrics', INTERVAL '30 days');

-- 조회: 자동으로 Continuous Aggregate 뷰를 활용
SELECT * FROM metrics_5m WHERE host = 'host_3' ORDER BY bucket DESC LIMIT 10;
```

### InfluxDB

시계열 전용으로 고속 쓰기·압축·보존 최적화. Retention·Downsampling 파이프라인이 내장되어 있어 오래된 데이터를 자동으로 낮은 해상도로 변환함. 단, SQL이 아닌 Flux/InfluxQL을 사용하고 표준 조인·트랜잭션 개념이 제한됨. SQL 생태계를 유지하고 싶으면 TimescaleDB, 고속 ingest에 특화하려면 InfluxDB.

### Vector DB — AI 시대의 유사도 검색

텍스트·이미지를 임베딩(고차원 벡터)으로 변환해 저장하고, 질문 임베딩과 유사한 벡터를 찾는 DB. RAG(Retrieval-Augmented Generation) 파이프라인의 핵심 컴포넌트임.

pgvector: PostgreSQL 확장. vector 타입 + HNSW/IVF 인덱스 + SQL + 트랜잭션 + JOIN 그대로 사용 가능.

Pinecone: 완전 관리형. 초대규모 클러스터 운영, 필터링, 멀티 테넌시 지원.

Weaviate: 오픈소스+매니지드. BM25(키워드)+벡터 하이브리드 검색, GraphQL/REST API.

선택 기준: DB 내 SQL+조인 → pgvector. 초대규모+운영 단순 → Pinecone. 오픈소스+API 유연 → Weaviate.

### pgvector — RAG 하이브리드 검색 패턴

RAG란 문서를 임베딩으로 DB에 저장해두고, 질문의 임베딩으로 유사 문서를 검색해 LLM의 컨텍스트로 주입하는 패턴임.

```sql
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS pg_trgm; -- 전문검색(Full-Text Search)용

CREATE TABLE knowledge_base (
  id         BIGSERIAL PRIMARY KEY,
  title      TEXT NOT NULL,
  content    TEXT,
  chunk_idx  INT DEFAULT 0,         -- 긴 문서를 청크 단위로 나눈 순서
  embedding  VECTOR(1536),          -- OpenAI text-embedding-3-small 차원 수
  search_ts  TSVECTOR,              -- 한국어 FTS용 전처리 컬럼
  created_at TIMESTAMPTZ DEFAULT now()
);

-- HNSW 인덱스: 코사인 유사도 기준 근사 최근접 이웃 탐색
CREATE INDEX ON knowledge_base USING HNSW (embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);
-- m: 각 노드의 연결 수. 높을수록 정확하지만 메모리↑
-- ef_construction: 인덱스 구축 시 탐색 범위. 높을수록 정확하지만 느림
CREATE INDEX ON knowledge_base USING GIN (search_ts); -- 키워드 검색용

-- 하이브리드 검색: 벡터 70% + 키워드 30% 가중 합산
WITH vector_search AS (
  SELECT id, 1 - (embedding <=> $1::VECTOR) AS vec_score
-- <=>: 코사인 거리 연산자. 1 - 거리 = 유사도 (1에 가까울수록 유사)
  FROM knowledge_base ORDER BY embedding <=> $1::VECTOR LIMIT 20
),
keyword_search AS (
  SELECT id, ts_rank(search_ts, plainto_tsquery('korean', $2)) AS kw_score
  FROM knowledge_base WHERE search_ts @@ plainto_tsquery('korean', $2)
)
SELECT kb.title, kb.content,
  COALESCE(vs.vec_score,0)*0.7 + COALESCE(ks.kw_score,0)*0.3 AS hybrid_score
FROM knowledge_base kb
LEFT JOIN vector_search vs ON vs.id = kb.id
LEFT JOIN keyword_search ks ON ks.id = kb.id
WHERE vs.id IS NOT NULL OR ks.id IS NOT NULL
ORDER BY hybrid_score DESC LIMIT 5;
```

하이브리드 검색을 쓰는 이유: 벡터 검색은 의미적으로 유사한 문서를 잘 찾지만 정확한 키워드(고유명사, 코드 등)를 놓칠 수 있음. 키워드 검색은 반대. 두 결과를 가중 합산해 정확도를 높임.

### AI/ML + DB 통합 패턴 3가지

### 패턴 1 — in-DB ML

BigQuery ML, Snowflake Snowpark, SQL Server ML Services, PostgreSQL MADlib 등을 이용해 SQL로 회귀·분류·시계열·클러스터링 모델을 DB 안에서 직접 실행함. 데이터를 외부로 꺼내지 않아 보안·규정 준수에 유리하고, 재현성·권한 통합이 쉬움. 단, 모델 다양성·최신성은 PyTorch/TensorFlow 전용 프레임워크 대비 제한됨.

### 패턴 2 — RAG

원문 → 임베딩 → Vector DB 저장 → 질문 유사 문서 검색 → LLM 컨텍스트 주입. 품질 핵심은 청크 분할 방식, 필터링, 재순위(re-ranking), 최신성 갱신, 출처 보강임. pgvector + PostgreSQL로 SQL+트랜잭션+조인을 활용한 완전한 RAG 파이프라인 구현 가능.

### 패턴 3 — 피처 스토어 + 실시간 예측

Feast 같은 피처 스토어로 훈련과 서빙 시 동일한 피처 스키마를 유지해 학습-서빙 불일치를 방지함. DB/DWH는 오프라인 피처 소스, Redis는 온라인(실시간) 피처 캐시 역할. BigQuery·Snowflake·Redshift 같은 Cloud DW에 내장 ML/UDTF/외부 함수로 예측을 통합할 수 있음.

### GraphQL + DB & Edge DB — 최신 트렌드

### GraphQL + DB 패턴

REST는 Over-fetch(필요 이상 데이터 전송)와 Under-fetch(필요한 데이터가 부족해 추가 요청 필요) 문제가 있음. GraphQL은 클라이언트가 필요한 필드만 질의해 불필요한 데이터 전송을 없앰.

Hasura: PostgreSQL 위에서 즉시 GraphQL API 생성 + 권한·RLS 연동 + 실시간 구독.

PostGraphile: PostgreSQL 스키마로 GraphQL 자동 생성. PostgreSQL 기능(함수, 뷰 등)을 깊게 활용 가능.

Prisma: 타입 세이프 ORM. GraphQL 서버와 궁합이 좋고 Next.js 등 현대 풀스택 환경에서 자주 씀.

주의: N+1 쿼리(DataLoader로 방지), 권한·멀티테넌시, CDN 캐싱 전략 설계 필요.

### Edge DB 패턴

사용자와 가까운 엣지 노드에 DB를 두어 ms 단위 응답을 가능하게 하는 패턴임. 읽기는 로컬 엣지 캐시에서, 쓰기는 중앙 합의를 거쳐 최종 일관성을 유지하는 구조.

Turso: libSQL/SQLite를 분산해 엣지 노드에서 SQLite를 실행.

Cloudflare D1: SQLite 기반, Cloudflare Workers와 통합.

Neon/PlanetScale: 서버리스 PG/MySQL, 분리형 스토리지·브랜치·자동 스케일.

주의: GDPR·데이터 거주성 규제, 일관성 선택·충돌 해결(CRDT) 전략이 필요함.AI 시대 DB 엔지니어의 역할 변화

### AI 시대 DB 엔지니어의 역할 변화

### 목적별 DB 선택

데이터 성격에 따라 적합한 DB가 다름. 하나의 RDBMS로 모든 것을 해결하려 하지 말고, 데이터 유형에 맞는 DB를 선택하는 것이 현대적인 설계 원칙임.

### DB 보안 전체 구조

DB 보안은 다섯 레이어로 나뉨. 각 레이어가 독립적으로 동작하므로 하나가 뚫려도 나머지가 방어선 역할을 함.

### 사용자·역할·권한

핵심 원칙은 최소 권한(Least Privilege) — 업무에 필요한 권한만 부여하고 나머지는 주지 않음. 역할(ROLE)을 먼저 만들어 권한을 묶고, 사용자에게 역할을 부여하는 방식이 표준 패턴임.

```sql
-- PostgreSQL (가장 직관적)
-- 1. 역할 생성 (로그인 불가 — 권한 묶음 역할)
CREATE ROLE app_reader NOLOGIN;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO app_reader;

-- 2. 실제 로그인 사용자 생성 후 역할 부여
CREATE ROLE app_user LOGIN PASSWORD 'secret';
GRANT app_reader TO app_user;
-- app_user로 로그인하면 app_reader 권한을 상속받음
```

```sql
-- MySQL 8.0 이상 (권장 방식)
CREATE ROLE 'app_reader';
GRANT SELECT ON mydb.* TO 'app_reader';
CREATE USER 'app_user'@'%' IDENTIFIED BY 'secret';
-- @'%': 어느 호스트에서든 접속 허용. 실무에선 특정 IP로 제한 권장
GRANT 'app_reader' TO 'app_user'@'%';
```

```sql
-- SQL Server (Windows/AD 연동 가능)
CREATE ROLE app_reader;
GRANT SELECT ON SCHEMA::dbo TO app_reader;
CREATE LOGIN app_user WITH PASSWORD='secret'; -- 서버 레벨 로그인
CREATE USER app_user FOR LOGIN app_user;       -- DB 레벨 사용자
EXEC sp_addrolemember 'app_reader','app_user'; -- 역할 부여
```

```sql
-- Oracle (권한이 매우 세세함)
CREATE ROLE APP_READER;
GRANT CREATE SESSION TO APP_READER; -- 로그인 자체도 별도 권한
GRANT SELECT ON HR.EMPLOYEES TO APP_READER;
CREATE USER APP_USER IDENTIFIED BY secret;
GRANT APP_READER TO APP_USER;
```

Oracle은 CREATE SESSION 같은 시스템 권한도 명시적으로 부여해야 하는 등 권한 단위가 가장 세밀함.

### Row-Level Security (RLS) — 행 단위 보안

같은 테이블을 조회하더라도 사용자별로 볼 수 있는 행을 제한하는 기능. 멀티테넌시(하나의 테이블에 여러 고객 데이터가 섞여 있는 구조)에서 특히 유용함.

```sql
-- PostgreSQL RLS
ALTER TABLE orders ENABLE ROW LEVEL SECURITY;

CREATE POLICY customer_policy ON orders
  FOR SELECT USING (customer_id = current_setting('app.customer_id')::int);
-- current_setting(): 현재 세션의 설정값을 읽는 함수
-- 앱이 세션에 고객 ID를 설정하면, 해당 고객 ID의 행만 SELECT 가능

-- 앱에서 세션에 고객 ID 설정
SELECT set_config('app.customer_id', '42', true);
-- 이후 SELECT * FROM orders 를 실행하면 customer_id = 42인 행만 반환됨
```

SQL Server는 SESSION_CONTEXT를 이용해 동일한 패턴을 구현함.

### SQL Injection — 원인과 방어법

원인: 사용자 입력을 SQL 문자열에 직접 이어붙이면, 공격자가 입력값에 SQL 구문을 섞어 쿼리 구조를 바꿀 수 있음.

```sql
# 절대 금지 — 문자열 포맷으로 쿼리 조립
sql = f"SELECT * FROM users WHERE name = '{user_input}'"
cur.execute(sql)
# user_input에 "' OR '1'='1" 같은 값이 들어오면 모든 행이 반환됨

# 올바른 방법 — 파라미터 바인딩 (Prepared Statement)
cur.execute("SELECT * FROM users WHERE name =%s", (user_input,))
# 입력값이 항상 데이터로만 처리되고 SQL 구조에 영향을 주지 못함
```

ORDER BY처럼 파라미터 바인딩이 불가능한 컬럼명/정렬 방향은 화이트리스트로 검증 후 사용:

```sql
if order not in ('name', 'created_at'):
    order = 'created_at'  # 허용 목록에 없으면 기본값으로 고정
sql = f"SELECT * FROM items ORDER BY{order}"
```

ORM(SQLAlchemy 등)은 대부분 파라미터 바인딩을 자동으로 처리해 기본적으로 안전함. 단, raw SQL이나 .execute(text(...))에 입력을 직접 포맷팅하면 동일하게 취약해짐. ORM을 써도 ORM의 파라미터 바인딩 API만 사용하는 것이 원칙임.

### 암호화 — TLS, TDE, 컬럼 암호화

### 전송 암호화 (TLS)

클라이언트 ↔ DB 사이의 네트워크 통신을 암호화함. 항상 켜두어야 하며, 끄면 네트워크 도청으로 쿼리와 데이터가 평문으로 노출될 수 있음.

### 디스크 암호화 / TDE (Transparent Data Encryption)

DB 파일(데이터파일·백업)을 자동으로 암호화함. 앱은 암호화 여부를 모르고 평소처럼 사용하면 됨. 백업 파일까지 암호화되는 장점이 있지만, 컬럼 단위 제어는 불가능함. Oracle·SQL Server·대부분의 클라우드 DB가 TDE 또는 스토리지 암호화를 제공함.

### 컬럼 암호화 (민감 컬럼만 암호화)

주민번호·카드번호처럼 특정 민감 컬럼만 선택적으로 암호화. TDE보다 세밀하지만 암호화된 컬럼은 인덱스/검색이 제한되고 성능이 저하됨.

```sql
-- PostgreSQL pgcrypto 예시
CREATE EXTENSION IF NOT EXISTS pgcrypto;

INSERT INTO customers (name, ssn_enc)
VALUES ('Alice', pgp_sym_encrypt('111-22-3333', 'mypassword'));
-- pgp_sym_encrypt(): 대칭키로 암호화. bytea 타입으로 저장됨

-- 복호화
SELECT pgp_sym_decrypt(ssn_enc, 'mypassword') FROM customers;
```

SQL Server는 Always Encrypted 방식으로 암호화 키를 클라이언트 측에서 관리해 DB 서버 자체도 평문을 볼 수 없음.

### 클라우드 DB에서 달라지는 점

On-Prem과 달리 클라우드에서는 DB 권한과 클라우드 IAM 권한을 함께 설계해야 함.

키 관리: 클라우드는 KMS(Key Management Service)를 제공. KMS 키 권한을 잃으면 암호화된 백업도 복구 불가 → 키 권한 정책 문서화와 백업 키 관리가 필수.

IAM/AD 연동: DB 계정 대신 클라우드 IAM 계정으로 DB 접근을 관리할 수 있어 중앙 관리가 편해짐. AWS RDS는 IAM 인증·KMS 키, GCP Cloud SQL은 Cloud KMS·IAM, Azure SQL은 Azure AD·Key Vault를 사용.

감사 & 로깅: 클라우드 감사 로그를 DB 로그와 연결해 자동 보관·알림 구성이 가능함.

### 흔히 하는 실수 & 해결방법 / 핵심 체크리스트

보안 핵심 체크리스트:

TLS 강제 적용

DB 사용자·역할 설계 → 최소권한 적용

클라우드 키 관리는 팀 문서화 + 백업키 보관

앱은 Prepared Statement/ORM 안전 API만 사용

민감데이터는 컬럼 암호화 또는 TDE 적용 결정

감사 로그(누가 언제) 설정 및 모니터링

### PostgreSQL 사용자(Role) 개념

PostgreSQL은 User와 Role을 구분하지 않고 "Role"로 통합함. LOGIN 속성이 있으면 실제 로그인 가능한 사용자, 없으면 권한 묶음 역할로 사용함.

### 사용자 및 역할 생성/삭제

```sql
-- 단순 로그인 가능한 사용자
CREATE ROLE analyst LOGIN PASSWORD 'analyst_pw';

-- 개발자: DB 생성 권한 추가
CREATE ROLE dev_user LOGIN PASSWORD 'dev_pw' CREATEDB;

-- 읽기 전용 사용자
CREATE ROLE readonly_user LOGIN PASSWORD 'readonly_pw' NOSUPERUSER;

-- 삭제
DROP ROLE readonly_user;

-- 존재 여부 확인 (psql 명령)
\du
-- 또는
SELECT rolname, rolsuper, rolcreatedb, rolcanlogin FROM pg_roles;
```

### GRANT / REVOKE — 권한 부여·회수

대상 레벨에 따라 부여 가능한 권한이 다름. PostgreSQL에서는 Database → Schema → Table 순으로 권한을 쌓아 올려야 함. Schema USAGE 없이 Table SELECT만 줘도 접근 불가.

### 실무 예시 — 역할 기반 권한 분리 설계

### RBAC 역할 설계표

api_user, analyst_user는 직접 테이블에 접근시키지 않고 VIEW를 통해 간접적으로 제한된 데이터만 제공하는 것이 일반적임.

```sql
-- etl_user 설정 예시
CREATE ROLE etl_user LOGIN PASSWORD 'etl_pw';
GRANT CONNECT ON DATABASE your_database TO etl_user;
GRANT USAGE ON SCHEMA public TO etl_user;
GRANT INSERT, TRUNCATE ON TABLE sales TO etl_user;

-- 권한 확인
SELECT grantee, privilege_type, table_name
FROM information_schema.role_table_grants
WHERE grantee = 'analyst';

SELECT current_user; -- 현재 로그인 사용자 확인
```

### 실무 예시 — 권한 모니터링 SQL

```sql
-- 전체 역할 목록 및 속성
SELECT rolname, rolsuper, rolcreatedb, rolcreaterole, rolcanlogin
FROM pg_roles ORDER BY rolname;

-- 사용자별 테이블 권한 확인
SELECT grantee, table_schema, table_name, privilege_type
FROM information_schema.role_table_grants
WHERE grantee IN ('data_engineer', 'data_analyst', 'api_user')
ORDER BY grantee, table_name;

-- 특정 사용자의 함수 권한 확인
SELECT grantee, routine_schema, routine_name, privilege_type
FROM information_schema.role_routine_grants
WHERE grantee = 'data_analyst';

-- 특정 테이블에 부여된 권한 전체 조회
SELECT * FROM information_schema.role_table_grants
WHERE table_name = 'sales';

-- 현재 세션 사용자 확인
SELECT current_user, session_user;
-- current_user: 현재 권한 컨텍스트 사용자 (SET ROLE로 바뀔 수 있음)
-- session_user: 실제 로그인한 사용자 (바뀌지 않음)
```

### 실무 예시 — VIEW 기반 보안

민감 데이터가 있는 테이블은 직접 접근을 막고 VIEW를 통해 필요한 컬럼·행만 노출하는 방식이 표준 패턴임.

```sql
-- 분석가용: 민감 컬럼(급여, 주민번호 등) 제외
CREATE VIEW v_employee_basic AS
SELECT emp_id, emp_name, department FROM employee;

-- API용: 더 제한적으로 emp_id, department만
CREATE VIEW v_employee_api AS
SELECT emp_id, department FROM employee;

-- 각 역할에 VIEW 권한만 부여
GRANT SELECT ON v_employee_basic TO data_analyst;
GRANT SELECT ON v_employee_api TO api_user;

-- 원본 테이블 직접 접근은 차단
REVOKE ALL ON employee FROM data_analyst, api_user;
```

VIEW 기반 보안의 장점: 테이블 구조가 바뀌어도 VIEW 정의만 수정하면 되고, 접근 제어 로직이 DB 레벨에서 일관되게 적용됨. 앱 코드에서 WHERE 절로 필터링하는 것보다 훨씬 안전함.

### RDB 별 User/Privilege 제어 핵심 구조

### MySQL

사용자 계정이 user@host 형태임. 호스트를 명시해 접속 위치를 제한할 수 있어 보안 설계에 유용함. 예를 들어 app@'192.168.1.%'는 해당 IP 대역에서만 접속 허용.

권한 범위는 글로벌 → 데이터베이스 → 테이블 → 컬럼 → 객체(뷰/프로시저/함수) 순으로 세분화됨. SHOW GRANTS FOR 'user'@'host'로 현재 부여된 권한을 확인할 수 있음.

MySQL 8.0부터 CREATE ROLE로 권한 묶음 역할을 만들고 사용자에게 할당하는 방식이 가능해짐. BACKUP_ADMIN, FIREWALL_ADMIN 같은 동적 권한도 플러그인·기능별로 추가됨.

보안 관리 핵심: 최소권한 원칙, 서비스 계정과 관리 계정 분리, audit_log 활성화, 비밀번호 정책·만료 관리.

### PostgreSQL

User와 Role을 구분하지 않고 Role로 통합. LOGIN 속성 여부로 로그인 가능 사용자와 권한 묶음 역할을 구분함.

권한 부여는 GRANT privilege ON object TO role 구조. 테이블/시퀀스/함수/스키마/데이터베이스 단위로 세분화해 지정 가능하고, 역할 간 계층적 상속(INHERIT)을 지원함.

관리/보안 방법:

pg_hba.conf: 접속 인증 방식을 파일 단위로 제어 (IP 대역, 인증 방법 — md5, scram, cert 등)

pg_roles, pg_catalog: 역할·권한 정보 조회 및 감사 쿼리에 활용

### Oracle

User와 Role을 분리해 관리함. 권한은 두 종류로 나뉨:

시스템 권한(System Privilege): DB 수준 작업 허용. 예: CREATE SESSION(로그인), CREATE TABLE.

객체 권한(Object Privilege): 특정 테이블·뷰 등에 대한 접근. 예: SELECT ON HR.EMPLOYEES.

내장 역할로 CONNECT(로그인), RESOURCE(객체 생성), DBA(전체 권한)가 있음. ORA_AUDIT(감사 기능) 활성화로 역할 변동·사용 추적 가능.

보안 관리 핵심:

세밀한 역할 분할 및 각 역할에 대한 목적·권한 문서화

Active Directory 연동, role 관리 자동화, 주기적 감사

WITH ADMIN OPTION(권한을 다른 사용자에게 재부여할 수 있는 옵션) 최소화 권장 — 남발하면 권한이 통제 없이 퍼질 수 있음

변경 및 권한 동향에 대한 감사·모니터링 필수

### SQL Server

로그인(서버 레벨 인증) → DB 사용자(DB 레벨) → Role(권한 묶음)의 3단계 구조임. 하나의 로그인을 여러 DB의 사용자 계정에 매핑할 수 있음.

내장 role로 db_owner(DB 소유자), db_datareader(읽기 전용), AuditViewer 등이 있고, 커스텀 role도 생성 가능. GRANT/REVOKE 외에 DENY가 있어 상위 role에서 부여된 권한을 명시적으로 차단할 수 있음. Active Directory 연동으로 Windows 계정 기반 인증도 지원.

보안 관리 핵심:

최소권한 할당 + RBAC + SOD(Segregation of Duties, 역할 분리로 한 사람이 전체 프로세스를 통제하지 못하게 함)

강한 패스워드·MFA, 사용자/권한 주기적 감사 및 audit/monitoring 활성

불필요 계정 정리, 권한 변경 이력 기록

DBMS별 핵심 차이 한 줄 요약:

### Google Cloud Spanner 권한 관리

Cloud Native DB인 Spanner는 전통 RDBMS와 달리 SQL 명령이 아닌 Cloud IAM을 중심으로 권한을 관리함.

### IAM 기반 Role/Permission

Cloud IAM에서 Spanner Admin, Database Admin, Database User 등 역할을 지정함

역할의 종류: 소유자 / 편집자 / 읽기전용 / 백업권한 / 세분화된 FGAC 등

단순한 DB 접근 수준이 아니라 세부 작업 단위(읽기, 쓰기, 스키마 변경 등)까지 구분 가능함

### 세분화 (Fine-grained Access Control, FGAC)

DB 내부 개체(테이블/열) 단위까지 접근을 세밀하게 제어할 수 있음

IAM 역할과 DB 역할을 연계해 유연한 권한 구성이 가능함

### 권한 관리 단위

프로젝트 → 인스턴스 → DB → 테이블 계층 전체에 걸쳐 리소스별로 Role을 할당함

### Amazon Aurora / RDS 권한 관리

AWS 관리형 RDB인 Aurora와 RDS는 IAM과 SQL 기반 권한 관리를 혼합해서 사용함.

### IAM과 연동

RDS 액세스 관리에 Option Group / Security Group을 활용함

인스턴스 접근 및 DB 수준 접근 제어가 가능함

### SQL 기반 권한 관리

MySQL, PostgreSQL 등 RDB 엔진별 자체 권한 관리(GRANT/REVOKE)와 IAM 접근관리를 동시에 활용할 수 있음

엔진 종류에 따라 권한 체계가 다르므로 엔진별 권한 구조를 함께 파악해야 함

### 기타 Cloud / NoSQL (RBAC 대표)

ScyllaDB, Cassandra 등 다수의 NoSQL 및 분산 DB가 채택하는 방식임.

### Role 기반 제어 (RBAC)

RBAC(Role Based Access Control): 역할에 권한을 묶어두고 사용자에게 역할을 부여하는 구조

계층적 역할/권한 부여가 가능하며, 조직/직책별 역할 간 상속 구조를 설계할 수 있음

### 클라우드 관리 콘솔

리소스/서비스별 사용자 구분을 콘솔에서 시각적으로 관리함

REST API / SDK를 통해 권한을 자동으로 배포하거나 회수할 수 있음

### 대표 명령어/관점 비교

DBMS별 사용자 계정 생성, 권한 부여, 역할 관리, 세분화 단위, 관리 구조를 정리한 표임.

PostgreSQL은 사용자 계정 자체도 CREATE ROLE로 만들며, 사용자와 역할의 구분이 없음

SQL Server만 DENY(명시적 거부) 명령이 별도로 존재함 — GRANT/REVOKE와 달리 상속된 권한도 차단함

### 백업 유형 비교 — Multi-AZ 구조

AWS의 Multi-AZ(Availability Zone) 구조는 동일 리전 내 두 개의 AZ에 DB를 복제해 운영하는 고가용성 아키텍처임.

### 구성 요소

Primary DB (AZ-A): 애플리케이션이 실제로 접속해 읽기/쓰기를 수행하는 주 DB

Standby DB (AZ-B): 복제만 받으며 평소에는 읽기 불가 — 장애 시 승격용으로 대기

### 동기 복제 방식

쓰기 요청이 완료되려면 Primary와 Standby 양쪽 모두 쓰기가 끝나야 "성공"으로 응답함

따라서 RPO(데이터 손실 허용 시간) ≈ 0 — 장애 시 유실 데이터가 거의 없음

### Failover

Primary에 장애가 발생하면 AWS가 자동으로 Standby를 Primary로 승격함

RTO(서비스 복구 허용 시간)는 수 분 이내

### 백업 유형 비교 — 유형별 정리

Incremental과 Differential의 차이: Incremental은 직전 백업 이후 변경분만 쌓고, Differential은 마지막 Full 이후의 모든 변경분을 유지함 → Differential이 파일 크기는 더 크지만 복구 단계가 단순함

### PITR & Streaming Replication — PostgreSQL

### PITR (Point-In-Time Recovery)

오염된 데이터가 발생하기 전 시점으로 DB를 되돌리는 복구 기법임.

Base backup + WAL 아카이브를 보관해두고, recovery_target_time을 설정해 원하는 시점으로 복구함

실수로 DELETE를 실행한 직전 시점으로도 복구 가능함

postgresql.conf에서 아래 설정이 필요함:

archive_mode=on

archive_command='cp %p /backup/wal/%f'

### Streaming Replication

Primary에서 Standby로 WAL을 실시간으로 스트리밍해 복제하는 방식임.

Standby가 Primary와 거의 동일한 데이터를 실시간으로 유지함

Hot Standby: Standby에서 SELECT 쿼리 허용 → 읽기 부하 분산에 활용 가능

### Failover 전략 & DR 목표

### Failover 전략 (PostgreSQL 기준)

Patroni: Python 기반 HA 클러스터 매니저. Primary 장애 시 자동으로 Standby를 승격함

pg_auto_failover / Repmgr: 대안 HA 도구

Cloud (RDS Multi-AZ / Aurora): CNAME 전환 방식으로 수십 초 내 장애 조치 자동 처리

### DR (재해 복구) 목표 지표

RPO (Recovery Point Objective): 장애 발생 시 최대 허용 데이터 손실 시간

RTO (Recovery Time Objective): 장애 발생 시 최대 허용 서비스 다운 시간

두 지표 모두 낮을수록 이상적이며, 동기 복제는 RPO를 0에 가깝게, Multi-AZ/클라우드 Failover는 RTO를 수십 초~수 분 수준으로 줄임.

### DBMS별 백업·복구·HA 비교

### 고가용성 솔루션 심화

### Oracle RAC (Real Application Clusters)

여러 인스턴스가 **공유 스토리지(ASM)**를 동시에 접근하는 구조

Cache Fusion: 노드 간 데이터 블록 캐시 일관성을 유지하는 메커니즘

읽기/쓰기 모두 확장이 필요한 대형 엔터프라이즈, 무정지 요구 환경에 적합

AWS RDS for Oracle은 RAC를 지원하지 않음 (Exadata on AWS는 가능)

### SQL Server Always On AG (Availability Groups)

DB 집합 단위로 HA/DR을 구성하며 읽기 스케일아웃도 지원함

동기식(HA): RPO=0, 성능 약간 저하

비동기식(DR): 지연 허용, 원거리 DR용

보조 복제본에서 읽기 전용 리포팅 쿼리 실행 가능

RDS Multi-AZ는 내부적으로 Always On AG를 활용함

### PostgreSQL FDW (Foreign Data Wrapper)

postgres_fdw: 원격 PostgreSQL 서버의 테이블을 로컬 테이블처럼 참조할 수 있음

이기종 DB 조인, 데이터 가상화, 점진적 마이그레이션에 활용함

Logical Replication: 테이블 단위 Pub/Sub 복제 방식으로 다음 용도에 사용함

테이블 단위 증분 복제

무중단 마이그레이션

읽기 분산

### "모니터링"이란?

DB 모니터링은 DB의 건강 상태를 지속적으로 확인하고 이상 징후를 미리 발견하는 일임. 사람의 건강검진에 비유하면 아래와 같음.

### 기본 지표 — TPS, QPS, Latency

용어 뜻 표현 예시

세 지표의 역할을 카페에 비유하면:

QPS → 초당 주문 수 (얼마나 많은 일을 처리하는지)

TPS → 초당 결제 완료 수 (얼마나 많은 거래가 완료되는지)

Latency → 한 잔 나오기까지 시간 (얼마나 빠른지)

### 모니터링 툴

### Prometheus + Grafana 연동 예시

Prometheus와 Grafana는 가장 널리 쓰이는 오픈소스 모니터링 조합임.

Prometheus가 DB에서 "현재 CPU 몇 %, TPS 몇?" 같은 지표 데이터를 주기적으로 수집

Grafana가 그 데이터를 그래프로 대시보드화

대시보드에서 확인하는 주요 항목:

초당 쿼리 수(QPS) 그래프

p95 지연시간 그래프 — 상위 95%ile 기준의 응답 지연

복제 지연(replica lag) 그래프

Active connection 수

→ 전체적으로 DB용 심전도 모니터와 같은 역할을 함

### Cloud DB 모니터링 서비스

Cloud에서는 직접 설정 없이도 기본 지표가 자동 수집되지만, 세세한 로그를 보려면 "Logs Export" 기능을 별도로 활성화해야 함.

### 이상 징후 확인

### 이상 징후 확인 — RDBMS vs Cloud DB 차이

### 알람(Alert) 설정 예시

실무에서 자주 설정하는 알람 기준과 대응 행동임.

### On-Prem DB vs 클라우드 DB 차이

한 줄 요약: 내가 다 하는 것 vs. 대부분 자동, 하지만 세밀 제어는 제한

## 관련 글

- [[blog/STUDYING/index|STUDYING]]
