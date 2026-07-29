---
title: "[STUDYING] 11 - 1. 스마트 데이터 이해 및 활용_Day3_핵심 정리"
created: 2026-07-30
updated: 2026-07-30
type: blog-post
tags: ["blog", "technical-writing"]
category: "STUDYING"
published: 2026-07-29
source_url: https://ch010104.tistory.com/324
---
# [STUDYING] 11 - 1. 스마트 데이터 이해 및 활용_Day3_핵심 정리

## 원문

https://ch010104.tistory.com/324

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

인덱스는 특정 컬럼 값을 기준으로 데이터 위치를 빠르게 찾도록 돕는 보조 구조임. 인덱스 유무에 따라 조회 방식과 성능이 크게 달라짐.

인덱스가 없을 때는 Table Full Scan 방식으로 전체 행을 순차 검사하므로 시간 복잡도가 O(N)임.

## 원문 기반 개념 정리

### 인덱스 개념 및 트레이드오프

인덱스는 특정 컬럼 값을 기준으로 데이터 위치를 빠르게 찾도록 돕는 보조 구조임. 인덱스 유무에 따라 조회 방식과 성능이 크게 달라짐.

인덱스가 없을 때는 Table Full Scan 방식으로 전체 행을 순차 검사하므로 시간 복잡도가 O(N)임.

인덱스를 생성하면 B-Tree 탐색을 통해 O(log N)으로 조회 가능함. 수백만 행 규모에서는 수십 ms 수준의 차이로 이어짐.

### 핵심 트레이드오프

읽기 성능 향상: 자주 쓰는 필드(WHERE / JOIN / ORDER BY)에 대한 조회가 빨라짐

쓰기 비용 증가: INSERT / UPDATE / DELETE 시 인덱스 재정렬 비용이 발생함

저장 공간 증가: 인덱스 자체가 디스크 공간을 추가로 소모함

### 인덱스 설계 원칙

WHERE 조건에 자주 등장하는 컬럼을 우선 대상으로 함

선택도(Selectivity)가 높은 컬럼일수록 좋은 인덱스임. 고유값이 많을수록 필터링 효율이 높음

주민번호, 학번, 이메일 등 UNIQUE한 것

FK 컬럼에는 반드시 인덱스를 검. JOIN 성능과 FOREIGN KEY 제약 체크 성능에 영향을 줌

주민번호, 학번, 이메일 등은 FK로 사용 x

위 항목들을 FK로 쓰려면, 보안상 암호화를 해야하는데 암호화 비용이 너무 큼

쓰기 중심(OLTP)과 읽기 중심(OLAP)은 인덱스 전략이 서로 다름

OLTP는 주문·결제·회원가입처럼 짧은 삽입·수정·삭제가 초당 대량으로 발생하는 실시간 트랜잭션 처리 시스템임. 인덱스가 많으면 매 쓰기마다 갱신 부담이 커지므로, 꼭 필요한 인덱스만 최소한으로 유지함

OLAP는 누적된 데이터를 집계·분석하는 시스템(데이터 웨어하우스, 리포트, 대시보드)임. 쓰기는 드물고 복잡한 조회가 대부분이므로, 조회 속도를 위해 인덱스를 상대적으로 적극적으로 사용함

미사용 인덱스는 제거해야 함. 쓰기 비용만 늘고 조회 이점은 없기 때문임

### 인덱스 종류 비교

### B-Tree 인덱스 — 생성 및 성능 비교

AI 연계 서비스의 사용자 쿼리 로그 테이블(query_logs)을 예시로, 인덱스 유무에 따른 실제 성능 차이를 측정한 실습임.

```sql
-- 테이블 생성
CREATE TABLE query_logs (
  id SERIAL PRIMARY KEY,
  user_id TEXT,        -- 실습용 편의 타입, 실무에선 INTEGER/UUID 권장
  user_input TEXT,
  similarity FLOAT,
  response_quality TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);
```

user_input처럼 자유형식 문자열은 TEXT가 적합하지만, user_id를 TEXT로 선언하는 것은 실무에서는 적절하지 않음. TEXT는 가변 길이 문자열을 힙(heap) 영역에 별도 저장하므로 버퍼 캐시 공간을 불필요하게 많이 소모하고, 인덱스 비교 시에도 문자열 비교가 발생해 정수 비교보다 느림. 실무에서 식별자 컬럼은 INTEGER나 BIGINT, 또는 분산 환경이라면 UUID를 사용하는 것이 일반적임. 이 실습에서는 데이터 생성 편의상 TEXT를 쓴 것임.

```sql
-- 100만 건 데이터 삽입
INSERT INTO query_logs (user_id, user_input, similarity, response_quality)
SELECT 'u' || (i % 1000),
       'query_' || i,
       RANDOM(),
       CASE (i%4) WHEN 0 THEN 'excellent' WHEN 1 THEN 'good'
                  WHEN 2 THEN 'fair' ELSE 'poor' END
FROM GENERATE_SERIES(1, 1000000) i;
```

```text
-- 인덱스 생성
CREATE INDEX idx_query_logs_user ON query_logs(user_id);
CREATE INDEX idx_query_logs_created ON query_logs(created_at DESC);
```

created_at DESC처럼 정렬 방향을 명시하면, 최신순 조회 쿼리에서 별도 정렬 없이 인덱스를 그대로 활용할 수 있음.

### 인덱스 생성 명령어

기본 CREATE INDEX 외에도 용도에 따라 다양한 변형이 존재함.

### 복합 인덱스 (Composite Index)

```text
CREATE INDEX idx_orders_cust_date ON orders (customer_id, order_date DESC);
```

선두 컬럼 원칙(leftmost prefix rule)이 적용됨. 인덱스는 앞 컬럼부터 순서대로 조건이 있어야 탐색에 사용됨.

사용 가능: WHERE customer_id = 5, WHERE customer_id = 5 AND order_date > '...', ORDER BY order_date DESC (customer_id 조건 포함 시)

사용 불가: WHERE order_date > '2024-01-01' (customer_id 없음) — 선두 컬럼이 빠지면 인덱스를 탈 수 없음

복합 인덱스 설계 시 등호(=) 조건 컬럼을 앞에, 범위(<, >) 조건 컬럼을 뒤에 배치하고, 선택도가 높은 컬럼을 우선함.

### 커버링 인덱스 (Covering Index)

```sql
CREATE INDEX idx_customer_cover ON customers (customer_id) INCLUDE (name, email);
SELECT customer_id, name, email FROM customers WHERE customer_id = 42;
```

INCLUDE로 추가된 컬럼은 인덱스에 함께 저장되므로, 위 쿼리는 테이블을 전혀 읽지 않고 인덱스만으로 결과를 반환함(Index Only Scan). 테이블 접근 자체가 없어 가장 빠른 조회 방식임.

→ EXPLAIN ANALYZE 했을 경우, Index Only로 출력됨

### 부분 인덱스 (Partial Index)

```text
CREATE INDEX idx_orders_pending ON orders (created_at)
WHERE status = 'PENDING';
```

특정 조건에 해당하는 행만 인덱싱함. PENDING 상태가 전체의 5%라면 인덱스 크기가 95% 줄어들고 속도는 올라감. 특정 값만 집중적으로 조회되는 패턴에 유리함.

→ 조건(status = 'PENDING')을 만족하는 데이터만 B-Tree에 미리 등록(인덱스)을 해둠

### 함수 기반 인덱스

```text
CREATE INDEX idx_users_email_lower ON users (LOWER(email));
```

컬럼 값에 함수를 적용한 결과를 인덱싱함. WHERE LOWER(email) = 'user@example.com'처럼 함수가 포함된 조건에서 인덱스를 탈 수 있음. 대소문자 무관 검색에 자주 씀.

### CONCURRENTLY

```text
CREATE INDEX CONCURRENTLY idx_products_category ON products (category_id);
```

운영 중 테이블 잠금 없이 인덱스를 생성함. 일반 CREATE INDEX는 생성 중 테이블을 잠그므로, 서비스 중단 없이 인덱스를 추가할 때 사용함. 단, 생성 시간이 더 오래 걸림.

→ 테이블을 잠그면, 해당 테이블에 CRUD가 막힘

### 인덱스 DBMS별 상세 차이

### 인덱스 설계 전략 — 선택도와 컬럼 순서

### 선택도 (Selectivity)

고유값 수 / 전체 행 수로 계산하며, 1에 가까울수록 인덱스 효과가 큼. gender(M/F)는 선택도 0.5로 인덱스 효율이 낮고, email은 ≈1로 높음.

### 복합 인덱스 컬럼 순서

등호(=) 조건 컬럼을 앞에, 범위(<, >, BETWEEN) 조건 컬럼을 뒤에 배치함.

WHERE status='A' AND created_at > '2024-01-01' → INDEX(status, created_at) 효율적

INDEX(created_at, status) 순서면 범위로 먼저 넓게 잡고 status 필터 → 비효율

### 미사용 인덱스 감지 및 제거

pg_stat_user_indexes의 idx_scan = 0인 인덱스는 한 번도 사용되지 않은 것으로 삭제 검토 대상임. PK 인덱스는 제외하고 조회해야 함.

### 인덱스 관리 — 사용률 모니터링 및 제거

```sql
-- PostgreSQL: 사용 횟수 낮은 인덱스 조회 (제거 후보)
SELECT indexrelname AS index_name, relname AS table_name,
       idx_scan AS scan_count,
       pg_size_pretty(pg_relation_size(indexrelid)) AS index_size
FROM pg_stat_user_indexes
ORDER BY idx_scan ASC
LIMIT 20;

-- 미사용 인덱스만 추출 (PK 제외)
SELECT indexrelname, relname, pg_size_pretty(pg_relation_size(indexrelid))
FROM pg_stat_user_indexes
WHERE idx_scan = 0 AND indexrelname NOT LIKE 'pk_%'
ORDER BY pg_relation_size(indexrelid) DESC;

-- 인덱스 재구성 (블로트 제거, 운영 중 잠금 없이)
REINDEX INDEX CONCURRENTLY idx_orders_cust_date;
REINDEX TABLE CONCURRENTLY orders; -- 테이블 전체

-- MySQL: 선택도(Cardinality) 낮은 인덱스 조회
SELECT TABLE_NAME, INDEX_NAME, CARDINALITY
FROM information_schema.STATISTICS
WHERE TABLE_SCHEMA = 'mydb'
ORDER BY CARDINALITY ASC;
```

인덱스도 시간이 지나면 삽입·삭제로 인해 내부가 단편화됨(블로트). REINDEX CONCURRENTLY로 운영 중단 없이 재구성할 수 있음. MySQL에서는 CARDINALITY가 선택도에 해당하며, 낮은 것부터 검토하면 제거 후보를 찾기 쉬움.

### 인덱스 심화 — B-Tree 내부 구조

B-Tree(Balanced Tree)는 모든 리프 노드가 같은 깊이를 유지하도록 자동으로 균형을 맞추는 트리 구조임. 어떤 값을 탐색하든 루트에서 리프까지 거치는 단계 수가 동일하므로 O(log N) 탐색이 보장됨.

### 구성 요소

Root Node: 탐색의 시작점

Branch Node: 탐색 경로를 안내하는 중간 노드. 키 값의 범위를 기준으로 하위 노드로 분기함

Leaf Node: 실제 인덱스 키 값과 해당 행의 물리 위치(ctid / ROWID)를 함께 저장함. 리프 노드끼리는 이중 연결 리스트로 연결되어 있어 범위 탐색 시 순차적으로 이동할 수 있음

### 인덱스 키 크기 영향

키가 작을수록 노드 하나에 더 많은 항목이 들어가므로 트리 깊이가 줄고 탐색이 빨라짐. UUID(16바이트)는 BIGINT(8바이트)보다 키가 두 배 커서 트리가 더 깊고 인덱스 크기도 커짐. 성능이 중요한 경우 식별자 타입 선택이 인덱스 효율에 영향을 줌.

### Fill Factor (페이지 채움 비율)

기본값 90%로, 페이지를 90%만 채우고 10%를 여유 공간으로 남겨둠. UPDATE가 잦은 테이블에서 Fill Factor를 낮추면(예: 70%) 페이지에 여유 공간이 많아져 행 갱신 시 같은 페이지 내에서 처리 가능해 페이지 분할(Split)이 줄어듦.

```text
CREATE INDEX idx_name ON table_name (column) WITH (fillfactor = 70);
```

### 커버링 인덱스 심화 — Index Only Scan 달성

SELECT에 필요한 모든 컬럼이 인덱스에 포함되면 테이블 힙(Heap)을 전혀 읽지 않고 인덱스만으로 결과를 반환할 수 있음. 이를 Index Only Scan이라 하며, 추가 I/O가 없어 가장 빠른 조회 방식임.

```sql
-- 일반 인덱스: email로 찾은 뒤 id, name을 가져오려면 테이블 접근 필요
CREATE INDEX idx_email ON users (email);
SELECT id, name FROM users WHERE email = 'a@b.com';
-- → Index Scan + Heap Fetch (추가 I/O 발생)

-- 커버링 인덱스: id, name을 INCLUDE에 포함 → 테이블 접근 없음
CREATE INDEX idx_email_cover ON users (email) INCLUDE (id, name);
SELECT id, name FROM users WHERE email = 'a@b.com';
-- → Index Only Scan (I/O 최소화)
```

EXPLAIN (ANALYZE, BUFFERS)로 실행계획을 확인하면 Heap Fetches: 0이 나와야 완전한 Index Only Scan임. Heap Fetches가 0이 되려면 Visibility Map이 최신 상태여야 하며, VACUUM으로 유지함. 갱신이 잦아 Visibility Map이 오래됐으면 Heap Fetch가 발생할 수 있음.

DBMS별 구현 차이: PostgreSQL과 SQL Server는 INCLUDE 절로 반환 전용 컬럼을 추가하고, MySQL은 WHERE + SELECT 컬럼을 모두 인덱스 키에 포함시키는 방식으로 커버링 인덱스를 구현함.

### 실행계획이란?

DB 옵티마이저가 SQL을 실행하기 전에 결정하는 실행 방법임. "어떤 순서로 테이블을 읽고, 어떤 인덱스를 쓰며, 어떤 조인 방식을 택했는가"를 보여주는 창임. 쿼리가 느린 이유를 진단할 때 가장 먼저 확인해야 할 도구임.

### EXPLAIN vs EXPLAIN ANALYZE

→ EXPLAIN ANALYZE를 사용할 경우, 쿼리가 실제로 실행되기 때문에, DML처럼 데이터를 수정하는 쿼리의 경우 ROLLBACK 권장

### 실행계획을 읽어야 하는 상황

쿼리가 갑자기 느려졌을 때

인덱스를 만들었는데 안 쓰이는 것 같을 때

JOIN 방식이 이상하게 보일 때 (Hash vs Nested Loop)

rows 예측값과 actual rows가 크게 다를 때 → 통계 갱신(ANALYZE) 필요

시각화 도구: explain.dalibo.com — PostgreSQL EXPLAIN (FORMAT JSON) 결과를 붙여넣으면 트리 구조로 시각화해줌

### PostgreSQL EXPLAIN ANALYZE — 플랜 읽기

```sql
BEGIN;
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT s.name, c.title, e.score
FROM students s
JOIN enrollments e ON e.student_id = s.id
JOIN courses c ON c.id = e.course_id
WHERE s.major_id = 1;
ROLLBACK;
```

결과 예시에서 읽어야 할 핵심 항목들임.

cost=12.5..45.8: 옵티마이저 추정 비용 (시작..종료)

actual time=0.5..2.3 rows=185: 실제 실행 시간과 반환 행 수

Buffers: shared hit=12 read=5: hit은 메모리에서 읽은 것(빠름), read는 디스크에서 읽은 것(느림). read가 많으면 캐시 히트율이 낮다는 신호임

Seq Scan on enrollments: 인덱스 없이 전체 스캔 중 → 인덱스 추가 검토

Planning Time / Execution Time: 계획 수립 시간과 실제 실행 시간

체크포인트:

Hash Batches > 1 → 해시 조인 중 메모리 부족으로 디스크로 Spill 발생. work_mem 증가 검토

예측 rows와 실제 rows 차이가 크면 → ANALYZE 실행으로 통계 갱신 필요

DML 포함 시에는 반드시 BEGIN ~ ROLLBACK으로 감싸야 실제 데이터 변경을 막을 수 있음.

### MySQL / SQL Server / Oracle 실행계획

```sql
-- MySQL: JSON 포맷 (dalibo 등 시각화 도구에 활용)
EXPLAIN FORMAT=JSON
SELECT * FROM orders o
JOIN customers c ON o.customer_id = c.id
WHERE o.order_date >= '2024-01-01';

-- MySQL EXPLAIN ANALYZE (8.0.18+): 실제 측정값 포함
EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 1;
-- → Index lookup on orders using idx_cust (actual time=0.1..0.5 rows=10)

-- SQL Server: 텍스트 실행계획
SET SHOWPLAN_ALL ON;
SELECT * FROM Orders o JOIN Customers c ON o.CustomerID = c.CustomerID
WHERE o.OrderDate >= '2024-01-01';
SET SHOWPLAN_ALL OFF;

-- Oracle: AUTOTRACE
SET AUTOTRACE ON;
SELECT * FROM orders WHERE order_date >= DATE '2024-01-01';
-- → NESTED LOOPS, INDEX RANGE SCAN 등
```

MySQL 결과에서 주요 확인 항목: access_type이 ALL이면 Full Scan(나쁨), range면 범위 인덱스 스캔(좋음). key 필드로 어떤 인덱스가 사용됐는지 확인 가능.

### 실행계획 주요 노드 타입 해석

### SQL 튜닝 안티패턴 vs 해결책

### 인덱스 관련 안티패턴 (1~4)

안티패턴 1 — 인덱스 컬럼에 함수 적용

WHERE 절에서 인덱스가 걸린 컬럼에 함수를 씌우면 옵티마이저가 인덱스를 탈 수 없음. 함수를 적용한 결과는 인덱스에 저장된 원본 값과 달라지기 때문임.

```text
-- X: 인덱스 무력화
WHERE YEAR(order_date) = 2024
WHERE UPPER(email) = 'A@B.COM'

-- O: 범위 조건으로 풀기
WHERE order_date >= '2024-01-01' AND order_date < '2025-01-01'

-- O: 함수 기반 인덱스 생성 (함수를 꼭 써야 하는 경우)
CREATE INDEX idx_email_lower ON users (LOWER(email));
```

안티패턴 2 — SELECT *

불필요한 컬럼을 모두 가져오면 네트워크 트래픽이 늘고, 커버링 인덱스(Index Only Scan)를 활용할 수 없게 됨.

```sql
-- X
SELECT * FROM orders WHERE customer_id = 1;
-- O
SELECT id, order_date, amount FROM orders WHERE customer_id = 1;
```

안티패턴 3 — 암묵적 타입 변환

컬럼 타입이 INT인데 문자열로 비교하면 DB가 전체 행을 변환하면서 Full Scan이 발생함.

```text
-- X: user_id가 INT인데 문자열로 비교 → 전체 타입 변환
WHERE user_id = '12345'
-- O
WHERE user_id = 12345
```

안티패턴 4 — LIKE '%keyword%' (앞 와일드카드)

앞에 %가 붙으면 B-Tree 인덱스로 탐색 시작점을 찾을 수 없어 Full Scan이 발생함. prefix% 형태는 인덱스 사용 가능. 중간/뒤 검색이 필요하면 pg_trgm 확장을 통해 GIN 인덱스로 해결함.

```sql
-- X
WHERE name LIKE '%길동%'
-- O (prefix는 인덱스 사용 가능)
WHERE name LIKE '홍%'
-- O (중간 검색이 필요한 경우)
CREATE EXTENSION pg_trgm;
CREATE INDEX idx_name_trgm ON users USING GIN (name gin_trgm_ops);
SELECT * FROM users WHERE name LIKE '%길동%'; -- 인덱스 사용
```

### 쿼리 구조 관련 안티패턴 (5~8)

안티패턴 5 — N+1 문제

루프 안에서 건별 쿼리를 반복 실행하면 N개 행에 대해 N번 쿼리가 발생함. 한 번의 JOIN으로 대체해야 함.

```sql
-- X: 학생 수만큼 쿼리 반복
for student in students:
    score = db.query("SELECT score FROM e WHERE student_id=%s", student.id)

-- O: 한 번의 JOIN으로 처리
SELECT s.id, s.name, e.score
FROM students s LEFT JOIN enrollments e ON e.student_id = s.id
WHERE s.id = ANY($1); -- 배열로 한 번에
```

안티패턴 6 — NOT IN + NULL 포함

서브쿼리 결과에 NULL이 하나라도 있으면 NOT IN은 항상 빈 집합을 반환함. NULL과의 비교는 항상 UNKNOWN이어서 전체 조건이 거짓이 되기 때문임. NOT EXISTS로 대체해야 함.

```sql
-- X: enrollments에 NULL이 있으면 결과 없음
WHERE id NOT IN (SELECT student_id FROM enrollments)

-- O
WHERE NOT EXISTS (SELECT 1 FROM enrollments e WHERE e.student_id = s.id)
```

안티패턴 7 — DISTINCT 남용

중복이 왜 발생하는지 원인을 파악하지 않고 DISTINCT로 덮어버리는 패턴임. 보통 JOIN 조건이 잘못되어 중복이 생기는 경우가 많으며, 존재 여부만 확인하면 되는 경우 EXISTS가 적합함.

```sql
-- X: 중복 원인 파악 없이 제거
SELECT DISTINCT s.name FROM students s JOIN enrollments e ON e.student_id = s.id

-- O: 존재 여부 확인 (중복 없음)
SELECT name FROM students s
WHERE EXISTS (SELECT 1 FROM enrollments e WHERE e.student_id = s.id)
```

안티패턴 8 — 대용량 OFFSET 페이지네이션

OFFSET 100000이면 DB가 앞의 10만 행을 스캔한 뒤 버림. 페이지가 뒤로 갈수록 선형으로 느려짐(O(N)). 마지막으로 조회한 id를 커서로 삼는 Cursor 방식으로 대체하면 O(log N)으로 일정하게 빠름.

```sql
-- X: 10만 행 스캔 후 버림
SELECT * FROM orders ORDER BY id LIMIT 10 OFFSET 100000;

-- O: Cursor 방식 (마지막 id를 다음 요청에 넘김)
SELECT * FROM orders WHERE id > :last_id ORDER BY id LIMIT 10;
```

### 안티패턴 요약

### 느린 쿼리 식별 — MySQL & PostgreSQL

### MySQL: Slow Query Log

기준 시간을 초과한 쿼리를 파일에 자동으로 기록함. 운영 중 문제 쿼리를 수집하는 첫 번째 도구임.

```text
SET GLOBAL slow_query_log = 'ON';
SET GLOBAL long_query_time = 1;  -- 1초 이상 쿼리 기록
SET GLOBAL slow_query_log_file = '/var/log/mysql/slow.log';

-- 로그 분석: 실행 시간 기준 상위 10개 추출
mysqldumpslow -s t -n 10 /var/log/mysql/slow.log
```

MySQL 8.0에서는 performance_schema를 통해 쿼리별 누적 통계를 조회할 수 있음.

```sql
SELECT DIGEST_TEXT, COUNT_STAR, AVG_TIMER_WAIT/1e12 AS avg_sec
FROM performance_schema.events_statements_summary_by_digest
ORDER BY AVG_TIMER_WAIT DESC LIMIT 10;
```

### PostgreSQL: pg_stat_statements

postgresql.conf에 shared_preload_libraries = 'pg_stat_statements'를 설정하고 재시작한 뒤 활성화함. 이후 실행된 모든 쿼리의 누적 호출 수, 총 시간, 평균 시간, 캐시 히트율을 조회할 수 있음.

```sql
CREATE EXTENSION IF NOT EXISTS pg_stat_statements; -- 실행된 '모든 쿼리의 누적 통계'를 합산해서 보여줌

-- 느린 쿼리 TOP-10 (평균 실행 시간 기준)
SELECT
  ROUND(mean_exec_time::NUMERIC, 2) AS avg_ms,
  calls,
  ROUND(total_exec_time::NUMERIC, 0) AS total_ms,
  ROUND(shared_blks_hit::NUMERIC /
    NULLIF(shared_blks_hit+shared_blks_read,0)*100,1) AS cache_hit_pct,
  LEFT(query, 100) AS query_snippet
FROM pg_stat_statements
ORDER BY mean_exec_time DESC
LIMIT 10;

-- 튜닝 전후 비교를 위한 통계 초기화
SELECT pg_stat_statements_reset();
```

cache_hit_pct가 낮은 쿼리는 디스크 I/O가 많이 발생하고 있다는 신호임. PostgreSQL의 log_min_duration_statement = 1000(ms) 설정으로도 Slow Query를 로그에 남길 수 있음.

### Slow Query 수집 및 분석 방법론

느린 쿼리를 발견했을 때 단순히 인덱스를 추가하는 것에 그치지 않고, 4단계 프로세스로 체계적으로 접근함.

### 1단계 — Slow Query 수집

PostgreSQL: log_min_duration_statement = 1000 (1초 이상 로깅)

MySQL: slow_query_log = ON, long_query_time = 1

두 DBMS 모두 pg_stat_statements / performance_schema로 누적 통계 분석 가능

### 2단계 — 병목 쿼리 특정 및 EXPLAIN 분석

수집된 쿼리에 EXPLAIN ANALYZE를 실행해 원인을 진단함.

Seq Scan on 대형 테이블 → 인덱스 추가 검토

actual rows와 rows 예측값 차이가 크면 → ANALYZE 실행으로 통계 갱신

Hash Batches > 1 → 메모리 Spill 발생 중. SET work_mem = '256MB' 등 per-session 증가 검토 (전역 설정은 모든 세션에 영향을 주므로 주의)

### 3단계 — 개선 적용 및 검증

인덱스 추가 시 CONCURRENTLY 옵션으로 운영 중단 없이 적용

적용 후 EXPLAIN ANALYZE로 실행계획 재확인

쿼리 구조 변경: 서브쿼리 → CTE/JOIN, DISTINCT 제거 등

Before/After 실행 시간을 측정해 개선 효과를 수치로 기록함

### 4단계 — 지속 모니터링

pg_stat_statements_reset() 후 일정 기간 재수집해 튜닝 효과 검증

pg_stat_statements에 누적되어 있는 데이터는 서버가 켜진 이후(또는 마지막 리셋 이후)부터의 '누적 평균값과 총합’이기 때문에, 초기화하지 않으면 쿼리 최적화 이전의 결과값으로 인해 개선을 확인하기 어려움

클라우드 환경에서는 AWS Performance Insights, GCP Query Insights 등 관리형 모니터링 도구를 활용할 수 있음

### 파티셔닝 전략 — Range / Hash / List

파티셔닝은 하나의 큰 테이블을 기준 컬럼에 따라 여러 물리적 조각으로 나누는 기법임. 인덱스만으로 해결이 어려운 수억 건 이상의 대용량 테이블에서 조회 성능, 유지보수, 아카이빙을 동시에 개선할 수 있음.

### Range 파티셔닝

날짜·숫자 범위로 분할함. 시계열 데이터에 가장 자주 쓰임.

```sql
-- PostgreSQL: 날짜 기준 연도별 분할
CREATE TABLE sales (
  id BIGSERIAL,
  sale_date DATE NOT NULL,
  amount NUMERIC
) PARTITION BY RANGE (sale_date);

-- sales를 파티션으로 나눈다고 위에서 선언 후, 자식 파티션 테이블에 범위 지정해서 생성해야함
CREATE TABLE sales_2023 PARTITION OF sales
  FOR VALUES FROM ('2023-01-01') TO ('2024-01-01');
CREATE TABLE sales_2024 PARTITION OF sales
  FOR VALUES FROM ('2024-01-01') TO ('2025-01-01');
CREATE TABLE sales_2025 PARTITION OF sales
  FOR VALUES FROM ('2025-01-01') TO ('2026-01-01');
```

### Hash 파티셔닝

특정 컬럼 값을 해시해서 N개 파티션에 균등 분산함. 범위 기준이 없고 고르게 분산해야 할 때 사용함.

```sql
-- MySQL: customer_id 해시로 4개 파티션에 균등 분산
CREATE TABLE orders (order_id INT NOT NULL, customer_id INT NOT NULL, ...)
PARTITION BY HASH(customer_id) PARTITIONS 4;
```

### List 파티셔닝

특정 값 목록으로 분할함. 국가·지역·카테고리처럼 값의 종류가 정해진 경우에 적합함.

```sql
-- PostgreSQL: 지역별 분할
CREATE TABLE orders PARTITION BY LIST (region);
CREATE TABLE orders_kr PARTITION OF orders FOR VALUES IN ('KR', 'KO');
CREATE TABLE orders_us PARTITION OF orders FOR VALUES IN ('US', 'CA');
```

### 파티션 프루닝 (Partition Pruning)

WHERE 절에 파티션 키가 포함되면 옵티마이저가 해당 파티션만 스캔하고 나머지를 자동으로 제외함(Pruning).

EXPLAIN으로 확인하면 Seq Scan on sales_2024처럼 특정 파티션만 나타남. 반대로 파티션 키가 WHERE에 없으면 모든 파티션을 스캔하므로 파티셔닝 효과가 없음.

### 파티셔닝 전략 DB별 지원 현황

SQL Server의 파티셔닝은 Enterprise Edition 이상에서만 지원됨.

### 파티셔닝 심화 — 운영 관리 및 성능

### 파티션 인덱스

부모 테이블에 인덱스를 생성하면 모든 파티션에 자동으로 적용됨.

```text
CREATE INDEX ON orders (customer_id);
-- → orders_kr, orders_us 등 모든 파티션에 자동 생성
```

### 파티션 유지관리

신규 파티션은 미리 생성해둬야 함. Range 파티션에 범위를 벗어난 데이터가 들어오면 에러 발생

오래된 파티션 삭제: DROP TABLE orders_2022q1 — 파티션은 독립 파일이므로 DELETE보다 훨씬 빠름

pg_partman 확장을 사용하면 PostgreSQL 파티션의 생성·삭제·유지보수를 자동화할 수 있음

### 파티셔닝 vs 샤딩

파티셔닝은 단일 서버에서 대용량을 처리하는 데 적합하고, 샤딩은 단일 서버의 한계를 넘어야 할 때 선택함.

### SQL 튜닝 실전 체크리스트

느린 쿼리를 마주했을 때 순서대로 따라가는 4단계 접근법임.

1단계 — 실행계획 확인: EXPLAIN ANALYZE로 Seq Scan 여부, actual rows vs rows 예측 차이, Hash Batches > 1(Spill) 확인

2단계 — 인덱스 최적화: WHERE/JOIN/ORDER BY 컬럼 인덱스 추가. 복합 인덱스는 등호 먼저, 범위 나중. 커버링 인덱스로 Index Only Scan 유도

3단계 — 쿼리 개선: 함수 적용 컬럼 → 범위 조건 또는 함수 기반 인덱스로 변경. 서브쿼리 → JOIN/CTE. N+1 → 한 번의 JOIN으로 해결

4단계 — 아키텍처 개선: 대용량 집계 → Materialized View 또는 집계 테이블. 전체 스캔 불가피 → 파티셔닝. 읽기 부하 → Replica(읽기 전용 복제본) 분산

### SQL 튜닝 Before/After 성능 비교

### MVCC (Multi-Version Concurrency Control) 심화

MVCC는 데이터 수정 시 기존 레코드를 덮어쓰지 않고 새 버전을 생성하는 방식으로 동시성을 처리함. 각 트랜잭션은 시작 시점의 스냅샷을 기준으로 읽기 때문에, 읽기 작업이 쓰기 작업을 차단하지 않음(Reader-Writer Lock 경합 감소).

MVCC의 비용: 버전 저장 공간 증가, 장수 트랜잭션 실행 시 가비지(Dead tuple) 증가, 인덱스 유지 복잡성 증가.

### PostgreSQL MVCC 구현

각 행에 xmin(해당 행을 생성한 TX ID)과 xmax(삭제/수정한 TX ID)를 시스템 컬럼으로 저장함. UPDATE는 내부적으로 새 버전 INSERT + 구버전 xmax 업데이트로 처리됨(In-place 수정 없음). 더 이상 어떤 트랜잭션도 참조하지 않는 구버전 행은 Dead tuple이 되고, VACUUM이 주기적으로 회수함. 장수 트랜잭션이 있으면 VACUUM이 차단되어 Dead tuple이 쌓이는 Table Bloat가 발생할 수 있으므로 주의해야 함.

### MySQL InnoDB MVCC

변경 전 데이터를 별도의 Undo Log 공간에 저장하고, 트랜잭션 시작 시 Read View(스냅샷)를 생성함. 더 이상 필요 없는 Undo Log는 Purge Thread가 자동으로 정리함.

### Isolation Level 실습 — PostgreSQL

### Read Committed (PostgreSQL/Oracle 기본값)

같은 트랜잭션 안에서도 SELECT를 실행할 때마다 그 시점에 커밋된 최신 값을 읽음. 이로 인해 Non-Repeatable Read(같은 쿼리가 다른 값을 반환)가 발생할 수 있음.

```sql
-- Session 1
BEGIN ISOLATION LEVEL READ COMMITTED;
SELECT balance FROM bank WHERE name='Alice'; -- 1000

-- Session 2 (동시 실행 후 커밋)
BEGIN; UPDATE bank SET balance=800 WHERE name='Alice'; COMMIT;

-- Session 1 재조회 → 800 (바뀐 값 반영됨 = Non-Repeatable Read)
SELECT balance FROM bank WHERE name='Alice';
COMMIT;
```

### Repeatable Read

트랜잭션 시작 시점의 스냅샷을 끝까지 유지함. Session 2가 값을 바꾸고 커밋해도 Session 1에서는 처음 읽은 값이 그대로 보임.

```sql
BEGIN ISOLATION LEVEL REPEATABLE READ;
SELECT balance FROM bank WHERE name='Alice'; -- 1000
-- Session 2에서 700으로 변경 후 커밋
SELECT balance FROM bank WHERE name='Alice'; -- 여전히 1000 (스냅샷 유지)
COMMIT;
```

### Serializable — 가장 엄격한 격리

모든 트랜잭션이 순서대로 실행된 것처럼 보장함. PostgreSQL은 SSI(Serializable Snapshot Isolation)로 순환 충돌을 감지해 충돌 시 강제 에러를 발생시킴. 에러 코드 40001(Serialization Failure)이 반환되므로 애플리케이션에서 재시도 로직이 필요함.

sql

```sql
-- Session 1
BEGIN ISOLATION LEVEL SERIALIZABLE;
SELECT SUM(balance) FROM bank; -- 2000

-- Session 2 (동시에 커밋 성공)
BEGIN ISOLATION LEVEL SERIALIZABLE;
UPDATE bank SET balance = balance - 100 WHERE name = 'Alice'; COMMIT;

-- Session 1 계속
UPDATE bank SET balance = balance + 100 WHERE name = 'Bob';
COMMIT;
-- ERROR: could not serialize access due to concurrent update
```

### 격리 수준 설정

```text
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;         -- 현재 트랜잭션
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED; -- MySQL 세션
ALTER SYSTEM SET default_transaction_isolation = 'read committed'; -- PG 전역
```

### Isolation Level — 이상현상 방지 범위 및 DBMS별 지원

### 격리 수준별 실무 적용 가이드

### Lock 종류 및 PostgreSQL Lock 구조

Lock은 여러 트랜잭션이 동일 데이터를 동시에 변경할 때 무결성 위반을 막기 위해 필요함.

### PostgreSQL Lock 계층

Row-Level Lock (Tuple Lock): UPDATE, DELETE 시 행 단위로 자동 획득. 다른 트랜잭션의 동일 행 수정을 차단함

Table-Level Lock: ACCESS SHARE(읽기), ROW EXCLUSIVE(쓰기), ACCESS EXCLUSIVE(DDL) 등 다양한 레벨 존재

Advisory Lock: DB 테이블이 아닌 사용자 정의 숫자 키로 논리적 잠금을 구현함. pg_advisory_xact_lock()으로 트랜잭션 범위 락 획득 가능

### Row-Level Lock 옵션

FOR UPDATE: 해당 행에 배타적 Lock 획득. 다른 UPDATE / DELETE는 COMMIT/ROLLBACK 때까지 대기

FOR UPDATE NOWAIT: 이미 잠겨 있으면 대기하지 않고 즉시 ERROR 반환

FOR UPDATE SKIP LOCKED: 잠긴 행은 건너뛰고 잠금 가능한 행만 처리. 분산 작업 큐, 이메일 발송 Queue, 배치 처리에서 여러 Worker가 중복 없이 작업을 나눌 때 유용함

Lock은 COMMIT 또는 ROLLBACK 시점에 자동 해제됨. 트랜잭션이 길수록 Lock 유지 시간이 늘고 충돌 확률이 커지므로, 트랜잭션을 짧게 유지하는 것이 핵심임.

### 낙관적 Lock vs 비관적 Lock

### Row Lock 시나리오 및 SKIP LOCKED

UPDATE는 해당 행에 자동으로 Row Lock을 걸고, COMMIT 전까지 다른 세션의 동일 행 수정을 블로킹함.

```sql
-- NOWAIT: 잠겨있으면 즉시 에러
SELECT * FROM items WHERE id = 1 FOR UPDATE NOWAIT;
-- ERROR: could not obtain lock on row in relation "items"

-- SKIP LOCKED: 여러 Worker가 중복 없이 작업 분배
WITH picked AS (
  SELECT id FROM job_queue
  WHERE status = 'READY'
  ORDER BY id
  FOR UPDATE SKIP LOCKED  -- 다른 Worker가 처리 중인 행은 건너뜀
  LIMIT 10
)
UPDATE job_queue SET status = 'RUNNING', started_at = now()
FROM picked WHERE job_queue.id = picked.id
RETURNING job_queue.*;
```

### Deadlock 발생 구조 및 자동 감지

Deadlock은 두 트랜잭션이 서로 상대방이 보유한 Lock을 기다리는 순환 대기 상태임.

```text
Session 1: row 1 Lock 획득 → row 2 요청 (Session 2 대기 중)
Session 2: row 2 Lock 획득 → row 1 요청 (Session 1 대기 중)
→ 서로를 무한 대기
```

PostgreSQL은 deadlock_timeout(기본 1s) 이후 순환 대기를 감지하고, 한 쪽 트랜잭션을 자동 ROLLBACK 처리함. 나머지 트랜잭션은 계속 진행됨.

```text
ERROR: deadlock detected
DETAIL: Process 123 waits for ShareLock on transaction 456; blocked by process 456.
        Process 456 waits for ShareLock on transaction 123; blocked by process 123.
```

### Deadlock 해소 — 순서 통일 + Advisory Lock

해결 1: 항상 동일 순서로 Lock 획득

여러 행을 잠글 때 ORDER BY id로 순서를 고정하면 교차 대기가 발생하지 않음.

```sql
WITH targets AS (
  SELECT id FROM items
  WHERE id = ANY(ARRAY[1, 2])
  ORDER BY id  -- 항상 id 오름차순으로 잠금
  FOR UPDATE
)
UPDATE items SET stock = stock - 1
FROM targets WHERE items.id = targets.id;
COMMIT;
```

해결 2: 트랜잭션 짧게 유지

비즈니스 로직, HTTP 호출, 파일 I/O는 트랜잭션 밖에서 수행

꼭 필요한 테이블/행만 접근

격리 수준 READ COMMITTED 유지

해결 3: Advisory Lock (업무 단위 직렬화)

테이블 구조와 무관하게 특정 숫자 키로 논리적 직렬화가 필요할 때 사용함. 트랜잭션 종료 시 자동 해제됨.

```sql
BEGIN;
SELECT pg_advisory_xact_lock(42); -- user_id=42에 대한 논리 락
UPDATE users SET balance = balance - 1000 WHERE id = 42;
INSERT INTO payments (user_id, amount) VALUES (42, 1000);
COMMIT;
```

해결 4: 애플리케이션 레벨 재시도

Deadlock 에러 코드 40P01을 받으면 짧은 Jitter(무작위 대기)를 두고 재시도함. 동시에 재시도하면 또 충돌할 수 있으므로 랜덤 대기가 중요함.

### Deadlock 모니터링

```sql
-- Lock 대기 중인 세션 확인
SELECT bl.pid AS waiting_pid, wl.pid AS blocking_pid,
       bl.query AS waiting_query, wl.query AS blocking_query,
       now() - bl.query_start AS waiting_for
FROM pg_catalog.pg_locks l1
JOIN pg_catalog.pg_stat_activity bl ON bl.pid = l1.pid
JOIN pg_catalog.pg_locks l2
  ON l1.locktype = l2.locktype AND l1.relation IS NOT DISTINCT FROM l2.relation
  AND l1.pid <> l2.pid
JOIN pg_catalog.pg_stat_activity wl ON wl.pid = l2.pid
WHERE NOT l1.granted AND l2.granted
ORDER BY waiting_for DESC;

-- 30초 이상 대기 중인 세션
SELECT pid, state, wait_event, now()-query_start AS duration, query
FROM pg_stat_activity
WHERE state != 'idle' AND now()-query_start > INTERVAL '30 seconds';

-- 세션 강제 종료
SELECT pg_cancel_backend(pid);    -- 현재 쿼리만 취소
SELECT pg_terminate_backend(pid); -- 연결 완전 종료
```

postgresql.conf 권장 설정: log_lock_waits = on(락 대기 로그 기록), deadlock_timeout = 500ms(감지 주기 단축)

### Deadlock 제어 — DBMS별 방법 비교

### BCNF (Boyce-Codd Normal Form) 상세

BCNF는 3NF보다 엄격한 정규형으로, 함수 종속성 분석 → 후보키 파악 → 결정자 검사 순서로 적용함.

조건: 어떤 함수 종속 X → Y가 있을 때, X가 후보키(Candidate Key)가 아니면 BCNF 위반임.

학습지원(교수, 과목, 강의실) 테이블을 예로 들면, 교수는 항상 같은 강의실을 사용하므로 교수 → 강의실 종속이 존재함. 그런데 교수는 후보키가 아님(과목도 함께 있어야 행을 식별) → BCNF 위반. 이를 교수강의실(교수, 강의실) + 강의배정(교수, 과목) 두 테이블로 분리해 해결함.

### 3NF vs BCNF

3NF: 함수 종속 보존 우선. 비후보 결정자도 일부 허용 가능

BCNF: 정합성 우선. 모든 결정자가 반드시 후보키여야 함

실무에서는 3NF까지 적용하는 경우가 많음. BCNF까지 분해하면 JOIN 비용과 관리 복잡도가 증가하기 때문임

### 정규화 심화 — 4NF / 5NF

### 정규화 vs 반정규화 선택

정규화 유지 (OLTP) 반정규화 허용 (OLAP)

### SCD (Slowly Changing Dimension) — 이력 데이터 관리

천천히 변하는 차원 데이터(고객 주소, 부서명 등)를 어떻게 저장하고 이력을 관리할지에 관한 설계 패턴임.

SCD Type 1: 덮어쓰기. UPDATE로 값을 바꾸면 이전 값이 사라짐. 이력 추적 불가

SCD Type 2: 이력 보존. 변경 시 기존 행을 종료(valid_to 업데이트, is_current = FALSE)하고 새 행을 삽입함. valid_from / valid_to / is_current로 시점별 조회 가능

```sql
-- 변경 발생 시: 기존 행 종료
UPDATE customer_history
SET valid_to = CURRENT_DATE - 1, is_current = FALSE
WHERE customer_id = 42 AND is_current = TRUE;

-- 새 행 삽입
INSERT INTO customer_history (customer_id, name, city, valid_from)
VALUES (42, '홍길동', '부산', CURRENT_DATE);

-- 특정 시점 조회 (2023-06-01 기준)
SELECT * FROM customer_history
WHERE customer_id = 42
AND valid_from <= '2023-06-01'
AND (valid_to IS NULL OR valid_to >= '2023-06-01');
```

SCD Type 3: 현재값 + 이전값을 별도 컬럼으로 보존. 직전 1회만 추적 가능

SCD Type 6: Type 1+2+3을 혼합한 방식

### 샤딩(Sharding) — 수평 분할 전략

샤딩은 단일 DB 인스턴스의 한계를 넘어 데이터를 여러 DB 인스턴스에 수평으로 분산 저장하는 방식임. 파티셔닝이 단일 DB 내 논리/물리 분할이라면, 샤딩은 그것의 물리적 확장(Scale-out)임.

### 주요 샤딩 전략

Range 샤딩: ID 범위 기준으로 분산. 구현이 단순하지만 특정 범위에 트래픽이 몰리는 hot spot이 발생할 수 있음

Hash 샤딩: user_id % N으로 균등 분산. 고르지만 샤드 수가 바뀌면 Re-sharding이 어려움

Directory 샤딩: 샤드 맵 테이블로 어떤 데이터가 어느 샤드에 있는지 관리. 유연하지만 디렉토리 테이블이 단일 장애점이 될 수 있음

### 구현 도구

Citus (PostgreSQL): 분산 쿼리, 자동 샤딩, SQL 그대로 사용 가능

Vitess (MySQL): YouTube 출신 오픈소스 MySQL 샤딩 솔루션

TiDB: MySQL 호환 분산 NewSQL. Google Spanner 영향을 받은 설계

### 주의사항

Cross-shard JOIN 불가 → 앱 레벨에서 처리 필요

분산 트랜잭션 복잡 (2PC 필요)

샤딩 전에 파티셔닝, Read Replica로 충분한지 먼저 검토할 것

### 샤딩 & CDC & MSA DB 패턴

### CDC (Change Data Capture)

DB 변경을 실시간 이벤트로 스트리밍하는 기법임. 애플리케이션 코드를 건드리지 않고 DB 로그 레벨에서 변경을 감지해 전파함.

PostgreSQL: Logical Decoding + wal2json → Kafka

MySQL: Binlog → Debezium → Kafka

활용: 실시간 동기화, DW 적재, 마이크로서비스 이벤트 전파

### MSA Database per Service 패턴

각 마이크로서비스가 독립적인 DB를 소유함. 서비스별 독립 배포, 기술 선택 자유, 장애 격리가 장점이지만, 분산 트랜잭션이 복잡하고 데이터 일관성 유지가 어려움.

이를 해결하기 위한 세 가지 패턴:

Saga 패턴: 분산 트랜잭션을 로컬 TX 체인으로 처리함. 주문→결제→재고→배송 각 서비스가 로컬 트랜잭션 + 이벤트 발행으로 연결되고, 실패 시 보상 트랜잭션(Compensating TX)을 실행함. Choreography(이벤트 기반 자율 조정)와 Orchestration(중앙 조정자) 두 방식이 있음

CQRS (Command Query Responsibility Segregation): 읽기(Query)와 쓰기(Command) 모델을 분리함. 쓰기는 정규화된 RDBMS, 읽기는 비정규화 캐시나 Read Replica를 사용함

Outbox 패턴: 트랜잭션 내 이벤트 발행을 보장함. 메인 로직과 아웃박스 테이블 INSERT를 같은 트랜잭션으로 묶고, CDC(Debezium) → Kafka → 소비자 서비스로 이벤트를 전달해 최소 1회 전달을 보장함

### [참고] PostgreSQL 백업 및 복구

### 논리 백업 (SQL 형태)

데이터베이스의 물리적 파일 디스크를 복사하는 대신, 데이터의 '구조(스키마)'와 '내용(데이터)'을 추출해 SQL 문장이나 텍스트 파일 형태로 변환해 만드는 백업

스키마 뿐 아니라, 사용자의 데이터도 같이 백업이 됨(어떤 방식으로 입력된 데이터인지는 상관 x)

```text
pg_dump -U postgres -d mydb -f backup.sql          # 단순 SQL
pg_dump -U postgres -d mydb -Fc -f backup.dump     # 압축 바이너리 (권장)
pg_dump -U postgres -d mydb -Fd -j 4 -f backup_dir/ # 병렬 (4 코어)

# 전체 클러스터 백업 (전역 객체 포함)
pg_dumpall -U postgres > full_cluster_backup.sql
```

→ 백업뿐 아니라, 백업에 대한 복구에 대한 연습 및 테스트로 해봐야함.

### 물리 백업 (PITR용)

실제 디스크 파일(바이너리 파일)을 물리적으로 그대로 복사해서 보관하는 백업 방식

```text
pg_basebackup -U replicator -D /backup/base -Ft -z -P --wal-method=stream
```

PITR(Point-In-Time Recovery) 설정은 postgresql.conf에서 WAL 아카이빙을 활성화하고, 복구 시 목표 시점을 지정함.

```text
# postgresql.conf
wal_level = replica
archive_mode = on
archive_command = 'cp %p /backup/wal/%f'

# 복구 목표 시점 지정
restore_command = 'cp /backup/wal/%f %p'
recovery_target_time = '2024-12-15 14:30:00'

# 자동 백업 스크립트 (매일 새벽 3시, crontab)
0 3 * * * pg_dump -U postgres -Fc -d mydb > /backup/daily-$(date +%F).dump
```

### 복구

```text
psql -U postgres -d mydb < backup.sql
pg_restore -U postgres -d mydb -j 4 backup.dump    # 병렬 복구
```

백업 원칙: 3-2-1 규칙 (3개 복사본 / 2가지 미디어 / 1개 오프사이트 보관 / 정기 복원 테스트). 백업은 만들었다고 끝이 아니라 실제로 복원이 되는지 테스트하는 것이 필수임.

### [참고] VACUUM & Table Bloat 관리

### Table Bloat란?

PostgreSQL에서 UPDATE는 기존 행을 수정하는 것이 아니라 새 버전을 삽입하고 구버전을 Dead tuple로 표시하는 방식으로 동작함(MVCC). Dead tuple이 쌓여 테이블이 실제 데이터보다 물리적으로 훨씬 커지는 현상을 Table Bloat라고 함. Dead tuple은 공간을 차지하고 순차 스캔 속도도 떨어뜨림.

→ MVCC 로 인해서 발생:

→ 여러 트랜잭션이 읽고 쓸 때 서로 기다리지 않게(Lock 없이) 만들기 위해 UPDATE나 DELETE를 할 때 기존 데이터를 덮어쓰거나 즉시 삭제하지 않음

### VACUUM 종류

### autovacuum 설정 최적화

기본값은 대용량 테이블에서 너무 늦게 실행되는 경우가 있으므로 테이블별로 조정 가능함.

```text
-- 전역 기본값
autovacuum_vacuum_scale_factor = 0.05   -- 5% dead tuple 시 VACUUM 실행
autovacuum_analyze_scale_factor = 0.02  -- 2% 변경 시 ANALYZE 실행

-- 특정 테이블 오버라이드 (갱신이 잦은 테이블에 적용)
ALTER TABLE orders SET (
  autovacuum_vacuum_scale_factor = 0.01,   -- 1% dead tuple 시 실행
  autovacuum_analyze_scale_factor = 0.005  -- 0.5% 변경 시 통계 갱신
);
```

### Bloat 확인 및 수동 VACUUM

```sql
-- Dead tuple 비율이 높은 테이블 상위 10개 확인
SELECT relname AS table_name,
       pg_size_pretty(pg_total_relation_size(relname::regclass)) AS total_size,
       n_dead_tup AS dead_tuples,
       n_live_tup AS live_tuples,
       ROUND(n_dead_tup::NUMERIC / NULLIF(n_live_tup + n_dead_tup, 0) * 100, 1) AS dead_pct,
       last_autovacuum, last_autoanalyze
FROM pg_stat_user_tables
ORDER BY n_dead_tup DESC LIMIT 10;

-- 수동 실행
VACUUM orders;               -- Dead tuple 회수 (잠금 없음, 공간 미반환)
VACUUM ANALYZE orders;       -- Dead tuple + 통계 갱신
VACUUM FULL orders;          -- 완전 재작성 (배타적 잠금, 공간 반환)
VACUUM FREEZE orders;        -- TX ID Wraparound 방지

-- 인덱스 공간만 회수 (Dead tuple 없이)
REINDEX INDEX CONCURRENTLY idx_orders_customer;

-- Transaction ID Wraparound 모니터링
SELECT relname, age(relfrozenxid) AS xid_age,
       pg_size_pretty(pg_total_relation_size(oid)) AS size
FROM pg_class
WHERE relkind = 'r' AND age(relfrozenxid) > 100000000
ORDER BY age(relfrozenxid) DESC;
```

장수 트랜잭션(Long-running TX)이 있으면 VACUUM이 차단되어 Bloat가 빠르게 쌓임. pg_stat_activity로 장수 트랜잭션을 주기적으로 모니터링해야 함.

### [참고] Connection Pool — pgBouncer 설정

### Connection Pool이 필요한 이유

PostgreSQL은 연결당 약 5MB 메모리와 핸드셰이크 비용이 발생함. 1000개 연결 = 5GB 메모리 소모, max_connections 초과 시 연결 거부가 발생함. pgBouncer는 앱과 DB 사이에서 연결을 재사용해 이 문제를 해결하는 커넥션 풀러임. MySQL은 ProxySQL, AWS는 RDS Proxy, GCP는 Cloud SQL Proxy가 같은 역할을 함.

### pgBouncer 모드

Session Mode: 클라이언트 연결 동안 DB 연결 유지. 안전하지만 효율 낮음

Transaction Mode: 트랜잭션 단위로 DB 연결을 할당/반환. 권장, 가장 효율적

Statement Mode: 문장 단위. PREPARE 사용 불가로 거의 미사용

Transaction Mode의 핵심: 20개 DB 연결로 2000개 앱 연결을 처리 가능 → 연결 오버헤드 대폭 감소

### 주요 설정 (pgbouncer.ini)

```text
[databases]
skala_db = host=127.0.0.1 port=5432 dbname=skala_db

[pgbouncer]
pool_mode = transaction          -- 트랜잭션 단위 연결 할당 (권장)
max_client_conn = 2000           -- 앱 측 최대 연결 수
default_pool_size = 20           -- DB에 실제 연결되는 수
min_pool_size = 5
reserve_pool_size = 5
server_idle_timeout = 600        -- 유휴 DB 연결 유지 시간(초)
```

### 모니터링

```text
psql -p 6432 pgbouncer -c "SHOW POOLS;"    -- 풀 현황
psql -p 6432 pgbouncer -c "SHOW CLIENTS;"  -- 연결된 클라이언트
psql -p 6432 pgbouncer -c "SHOW SERVERS;"  -- DB 연결 현황
psql -p 6432 pgbouncer -c "SHOW STATS;"    -- 통계
```

### [참고] DB 모니터링 핵심 쿼리 모음

```sql
-- 현재 실행 중인 쿼리 (30초 이상)
SELECT pid, now() - query_start AS duration,
       state, wait_event, LEFT(query, 100) AS query_snippet
FROM pg_stat_activity
WHERE state != 'idle'
AND now() - query_start > INTERVAL '30 seconds'
ORDER BY duration DESC;

-- 연결 수 현황 (상태별)
SELECT state, COUNT(*) AS cnt
FROM pg_stat_activity
GROUP BY state;

-- 캐시 히트율 (권장: 99% 이상)
SELECT SUM(blks_hit)::FLOAT / NULLIF(SUM(blks_hit) + SUM(blks_read), 0) * 100
AS cache_hit_pct
FROM pg_stat_database WHERE datname = current_database();

-- 테이블 크기 순위
SELECT relname, pg_size_pretty(pg_total_relation_size(relname::regclass)) AS size
FROM pg_stat_user_tables
ORDER BY pg_total_relation_size(relname::regclass) DESC
LIMIT 10;

-- 미사용 인덱스 (idx_scan = 0)
SELECT indexrelname, relname, pg_size_pretty(pg_relation_size(indexrelid))
FROM pg_stat_user_indexes
WHERE idx_scan = 0 AND relname NOT LIKE 'pg_%'
ORDER BY pg_relation_size(indexrelid) DESC;
```

### [참고] DB 성능 최적화 4단계 접근법

성능 문제가 생겼을 때 무작정 인덱스부터 추가하는 것이 아니라, 영향력이 큰 순서대로 단계적으로 접근하는 것이 핵심임.

1단계 — 설계 단계 최적화 (영향력 가장 큼): 이미 잘못 설계된 테이블 구조 위에서는 인덱스와 쿼리 튜닝의 효과가 제한적임. 적절한 정규화 수준 결정(OLTP: 3NF / OLAP: 반정규화), PK 선택(자연키 vs 대체키. UUID는 16바이트로 인덱스 효율 저하), FK 컬럼에 반드시 인덱스 생성, 데이터 타입 최적화(NUMERIC은 금액, TIMESTAMPTZ는 시각)를 설계 시점에 결정해야 함

2단계 — 쿼리 최적화: SELECT * 제거, 서브쿼리 → CTE/JOIN 변환, N+1 문제 해결, EXPLAIN ANALYZE로 병목 파악

3단계 — 인덱스 최적화: 선택도 높은 컬럼 우선, 복합 인덱스 컬럼 순서 설계, 커버링/부분/함수 기반 인덱스 활용, 미사용 인덱스(idx_scan = 0) 제거

4단계 — DB 설정 최적화: 메모리(shared_buffers는 DB 캐시, work_mem은 정렬/해시 per-query), Connection Pool(pgBouncer), VACUUM/ANALYZE 스케줄 설정

### Q&A 보충

옵티마이저란?

DB 내부의 '네비게이션'임. 데이터(목적지)를 찾아달라고 명령하면, 여러 길(인덱스 이용, 전체 스캔 등) 중 가장 빠르고 저렴한 길을 찾아줌.

비용 계산 방식을 직접 바꿀 수 있나?

가능함. 네비게이션 옵션에서 최단 거리 우선, 고속도로 우선을 고르듯, DB 파라미터 설정으로 "디스크 읽는 비용을 높게 측정해줘" 혹은 "CPU 계산 비용을 낮춰줘"처럼 가중치를 조절할 수 있음.

모든 DB가 똑같이 계산하나?

아님. 네이버 지도, 카카오내비, Tmap이 빠른 길을 찾는 알고리즘과 예상 시간이 조금씩 다른 것처럼, MySQL, Oracle, PostgreSQL 등 DBMS마다 비용을 계산하는 공식과 가중치가 모두 다름.

통계 정보란?

옵티마이저(네비게이션)가 길을 잘 찾으려면 "어느 도로가 막히는지", "어느 구역에 책이 많은지" 알아야 함. 이 정보를 통계 정보라고 함.

데이터가 1건 추가될 때마다 통계를 즉시 갱신하나?

아님. 도서관에 책이 새로 한 권 들어올 때마다 전체 도서 수, 장르별 비율을 매번 계산하면 일하는 직원(DB)이 업무 과로로 쓰러짐(쓰기 성능 급격히 하락). 실제로는 세 가지 방식으로 운영함.

주기적 자동 갱신: 책이 어느 정도(전체의 10~20%) 쌓이면 밤이나 한가한 시간에 백그라운드 작업자가 비동기로 갱신함

샘플링: 책 전체를 다 세지 않고 몇몇 책장만 훑어보고 전체 양을 추측함

수동 갱신: 대량의 데이터를 한꺼번에 넣은 직후에는 사람이 직접 "지금 통계표 다시 작성해!"라고 명령(ANALYZE)을 내림. EXPLAIN ANALYZE에서 rows 예측값과 actual rows가 크게 다를 때가 이 경우에 해당함

파티셔닝이란?

테이블에 데이터가 수천만 건 쌓이면 조회하기 너무 무거워짐. 서류철을 "2024년용 서류함", "2025년용 서류함"처럼 물리적으로 서랍을 나누어 보관하는 기술임.

부모 테이블에 데이터가 모여있고 인덱스(색인)만 따로 있는 건가?

아님. 데이터 자체가 서로 다른 서랍(물리적 파일)에 나누어져 들어감.

인덱스는 어떻게 동작하나?

두 가지 방식이 있음.

로컬 인덱스: 서랍마다 자기 서랍 안에 무엇이 들어있는지 적힌 작은 색인표를 가짐. "2025년 데이터 보여줘" 하면 2025년 서랍으로 바로 달려가서 그 안의 색인표만 확인하므로 아주 빠름

글로벌 인덱스: 모든 서랍의 내용을 합쳐놓은 하나의 큰 색인표. 관리하기 까다로워 보통은 서랍별 색인표를 따로 둠

실무에서는 두 방식을 함께 쓰기도 함. 부모 테이블에 설정한 인덱스를 자식 파티션 전체에 그대로 적용하는 방식으로 성능을 개선한 사례가 있음.

인덱스란?

책 맨 뒤에 있는 '찾아보기(색인)'임. 색인이 있으면 특정 단어를 찾을 때 첫 장부터 다 읽을 필요 없이 한 번에 찾아갈 수 있음(SELECT 속도 향상). 단, 새로운 내용을 책에 추가할 때는 본문도 쓰고 뒤의 '찾아보기' 페이지에도 단어와 쪽수를 일일이 적어야 함(INSERT/UPDATE 속도 하락).

실무에서 EXPLAIN만 보고 인덱스를 결정하나?

아님. EXPLAIN은 "이 색인표를 사용해서 찾을 예정이다"라는 '계획'만 보여주는 도구임. 실제 검증은 두 단계로 함.

조회 검증: EXPLAIN (ANALYZE, BUFFERS)로 인덱스를 실제로 타는지, Seq Scan 여부와 실행 시간을 확인함

쓰기 부하 검증: EXPLAIN으로는 데이터가 들어갈 때 얼마나 버벅거리는지 알 수 없음. 테스트 환경에서 실제로 초당 수천 건의 데이터를 막 넣어보면서(부하 테스트) 삽입이 늦어지지 않는지 직접 시계로 측정함

최종 결정 기준은?

"찾는 건 엄청 빨라지는데, 데이터를 넣을 때 느려지는 손해가 크지 않은가?"를 종합적으로 따져본 뒤 인덱스를 최종 적용함.

## 관련 글

- [[blog/STUDYING/index|STUDYING]]
