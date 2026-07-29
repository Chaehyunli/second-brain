---
title: "[STUDYING] 11 - 2. 스마트 데이터 이해 및 활용_Day3_실습"
created: 2026-07-30
updated: 2026-07-30
type: blog-post
tags: ["blog", "technical-writing"]
category: "STUDYING"
published: 2026-07-29
source_url: https://ch010104.tistory.com/325
---
# [STUDYING] 11 - 2. 스마트 데이터 이해 및 활용_Day3_실습

## 원문

https://ch010104.tistory.com/325

## 노트 유형

`tutorial`

## 학습 목표 및 맥락

측정 명령: EXPLAIN (ANALYZE, BUFFERS, TIMING OFF) (문제 1은 VERBOSE 추가)

측정 기준: Execution Time · Buffers · actual/estimated rows · loops

## 원문 기반 학습 정리

### 공통 실행 환경

측정 명령: EXPLAIN (ANALYZE, BUFFERS, TIMING OFF) (문제 1은 VERBOSE 추가)

측정 기준: Execution Time · Buffers · actual/estimated rows · loops

목표: 특정 밀리초가 아니라 실행 계획과 읽은 블록 수의 변화 해석

### 문제 1. 기본 키 검색의 실행 계획 읽기 (튜닝 불필요 증명)

### 문제 / 개선 목표

사원번호 100 검색. 이미 빠른 쿼리도 튜닝 대상인지 판단. 목표는 빠르게 만드는 것이 아니라 튜닝 불필요를 증명하기.

```sql
EXPLAIN (ANALYZE, BUFFERS, VERBOSE, TIMING OFF)
SELECT *
FROM employees
WHERE employee_id = 100;
```

### 개선 전 QUERY PLAN

```text
Index Scan using employees_pkey on day03_tuning.employees  (cost=0.29..8.31 rows=1 width=111) (actual rows=1 loops=1)
  Index Cond: (employees.employee_id = 100)
  Buffers: shared hit=6
Planning:
  Buffers: shared hit=53
Planning Time: 0.868 ms
Execution Time: 0.056 ms
```

### 개선안

튜닝하지 않음. employee_id는 PRIMARY KEY라 이미 B-tree 인덱스가 존재하므로 중복 인덱스 추가는 쓰기 비용과 저장 공간만 늘림.

### 개선 후 QUERY PLAN

개선 전과 동일 (변화 없음).

### 개선 결과 해석

변경된 Plan Node: 없음

Buffers 변화: 없음

Execution Time 변화: 미미함

employee_id는 PK라 자동으로 B-tree 인덱스가 생성되어 Index Scan이 선택됨

단건 조회를 위한 중복 인덱스 추가는 이득이 없음. 정답은 계획을 확인하되 별도 튜닝하지 않는 것

Seq Scan이 보인다면 테이블 크기·통계·설정을 먼저 확인하고 무조건 인덱스를 추가하지 않음

### 인덱스 정의 확인

```text
CREATE UNIQUE INDEX employees_pkey ON day03_tuning.employees USING btree (employee_id)
```

### 문제 2. 함수가 적용된 이메일 검색 — 표현식 인덱스

### 문제 / 개선 목표

대소문자 무시 lower(email) = 'user1234@corp.com' 검색. WHERE절 표현식과 동일한 lower(email) 표현식 인덱스를 설계.

```sql
EXPLAIN (ANALYZE, BUFFERS, TIMING OFF)
SELECT employee_id, employee_no, full_name, email
FROM employees
WHERE lower(email) = 'user1234@corp.com';
```

### 개선 전 QUERY PLAN

```text
Seq Scan on employees  (cost=0.00..1658.00 rows=250 width=46) (actual rows=1 loops=1)
  Filter: (lower((email)::text) = 'user1234@corp.com'::text)
  Rows Removed by Filter: 49999
  Buffers: shared hit=908
Planning Time: 0.363 ms
Execution Time: 20.343 ms
```

### 개선안

```text
DROP INDEX IF EXISTS idx_employees_lower_email;
CREATE INDEX idx_employees_lower_email
    ON employees (lower(email));
ANALYZE employees;
```

### 개선 후 QUERY PLAN

```text
Index Scan using idx_employees_lower_email on employees  (cost=0.41..8.43 rows=1 width=46) (actual rows=1 loops=1)
  Index Cond: (lower((email)::text) = 'user1234@corp.com'::text)
  Buffers: shared hit=1 read=3
Planning Time: 0.569 ms
Execution Time: 0.056 ms
```

### 개선 결과 해석

변경된 Plan Node: Seq Scan → Index Scan

Buffers 변화: shared hit=908 → shared hit=1 read=3

Execution Time 변화: 20.343 ms → 0.056 ms

일반 인덱스 ON employees(email)는 lower(email) 검색식과 구조가 달라 사용 불가

ON employees(lower(email))은 WHERE절 표현식과 일치하므로 인덱스 조건으로 사용됨

저장 시 이메일을 항상 소문자로 정규화한다면 email = '...' + 일반 인덱스도 대안

### 인덱스 정의 확인

```text
CREATE INDEX idx_employees_lower_email ON day03_tuning.employees USING btree (lower((email)::text))
```

### 문제 3. 접미사 LIKE 검색 — pg_trgm GIN 인덱스

### 문제 / 개선 목표

email LIKE '%@gmail.com' 검색. 선두 와일드카드라 B-tree 정렬 순서 활용 불가. pg_trgm과 GIN 인덱스로 포함/접미사 검색 개선. (gmail 계정은 전체의 약 1%)

```sql
EXPLAIN (ANALYZE, BUFFERS, TIMING OFF)
SELECT employee_id, employee_no, full_name, email
FROM employees
WHERE email LIKE '%@gmail.com';
```

### 개선 전 QUERY PLAN

```text
Seq Scan on employees  (cost=0.00..1533.00 rows=505 width=46) (actual rows=500 loops=1)
  Filter: ((email)::text ~~ '%@gmail.com'::text)
  Rows Removed by Filter: 49500
  Buffers: shared hit=908
Planning Time: 0.093 ms
Execution Time: 8.052 ms
```

### 개선안

```text
DROP INDEX IF EXISTS idx_employees_email_trgm;
CREATE INDEX idx_employees_email_trgm
    ON employees USING gin (email gin_trgm_ops);
ANALYZE employees;
```

### 개선 후 QUERY PLAN

```text
Bitmap Heap Scan on employees  (cost=96.25..1059.01 rows=1010 width=46) (actual rows=500 loops=1)
  Recheck Cond: ((email)::text ~~ '%@gmail.com'::text)
  Heap Blocks: exact=500
  Buffers: shared hit=577
  ->  Bitmap Index Scan on idx_employees_email_trgm  (cost=0.00..96.00 rows=1010 width=0) (actual rows=500 loops=1)
        Index Cond: ((email)::text ~~ '%@gmail.com'::text)
        Buffers: shared hit=77
Planning Time: 0.100 ms
Execution Time: 1.635 ms
```

### 개선 결과 해석

변경된 Plan Node: Seq Scan → Bitmap Heap Scan

Buffers 변화: shared hit=908 → shared hit=577

Execution Time 변화: 8.052 ms → 1.635 ms

선두 와일드카드라 B-tree 정렬 순서를 못 써 Seq Scan이 선택됨

pg_trgm은 문자열을 3글자 단위(trigram)로 쪼개 인덱싱해 접미사/포함 검색에서도 후보를 좁힘

Buffers 감소폭이 작은 이유: gmail 사원이 테이블 전체에 흩어져(Heap Blocks exact=500) Heap 접근 블록이 크게 줄지 않음

반면 Execution Time은 필터 대상이 5만 건에서 500건 후보로 좁혀져 약 5배 개선

매칭 비율이 높으면 옵티마이저가 Seq Scan을 다시 택할 수 있음

### 인덱스 정의 확인

```text
CREATE INDEX idx_employees_email_trgm ON day03_tuning.employees USING gin (email gin_trgm_ops)
```

### 문제 4. 필터 + ORDER BY + LIMIT — 부분 정렬 인덱스

### 문제 / 개선 목표

재직 중이며 최근 365일 입사자를 연봉순 상위 100명 조회. 재직자만 담는 부분 인덱스 + ORDER BY salary DESC와 LIMIT 100의 조기 종료 유도.

```text
EXPLAIN (ANALYZE, BUFFERS, TIMING OFF)
SELECT
    employee_id,
    employee_no,
    full_name,
    hire_date,
    salary
FROM employees
WHERE employment_status = 'ACTIVE'
  AND hire_date >= current_date - 365
ORDER BY salary DESC
LIMIT 100;
```

### 개선 전 QUERY PLAN

```text
Limit  (cost=2081.06..2081.31 rows=100 width=39) (actual rows=100 loops=1)
  Buffers: shared hit=908
  ->  Sort  (cost=2081.06..2092.38 rows=4528 width=39) (actual rows=100 loops=1)
        Sort Key: salary DESC
        Sort Method: top-N heapsort  Memory: 39kB
        Buffers: shared hit=908
        ->  Seq Scan on employees  (cost=0.00..1908.00 rows=4528 width=39) (actual rows=4411 loops=1)
              Filter: (((employment_status)::text = 'ACTIVE'::text) AND (hire_date >= (CURRENT_DATE - 365)))
              Rows Removed by Filter: 45589
              Buffers: shared hit=908
Planning Time: 0.092 ms
Execution Time: 7.703 ms
```

### 개선안

```text
DROP INDEX IF EXISTS idx_employees_active_salary_hire;
CREATE INDEX idx_employees_active_salary_hire
    ON employees (salary DESC, hire_date)
    INCLUDE (employee_id, employee_no, full_name)
    WHERE employment_status = 'ACTIVE';
```

### 개선 후 QUERY PLAN

```text
Limit  (cost=0.42..40.94 rows=100 width=39) (actual rows=100 loops=1)
  Buffers: shared hit=11
  ->  Index Only Scan using idx_employees_active_salary_hire on employees  (cost=0.42..1835.21 rows=4528 width=39) (actual rows=100 loops=1)
        Index Cond: (hire_date >= (CURRENT_DATE - 365))
        Heap Fetches: 0
        Buffers: shared hit=11
Planning Time: 0.147 ms
Execution Time: 0.104 ms
```

### 개선 결과 해석

변경된 Plan Node: Seq Scan + Sort(top-N heapsort) → Index Only Scan (Sort 제거)

Buffers 변화: shared hit=908 → shared hit=11

Execution Time 변화: 7.703 ms → 0.104 ms (약 74배)

WHERE employment_status='ACTIVE' 부분 인덱스라 재직자만 담겨 스캔 대상이 작음

선두 컬럼을 salary DESC로 둬 인덱스가 이미 연봉 내림차순 정렬이라 Sort 노드가 사라지고 LIMIT 100 앞부분만 읽고 조기 종료

INCLUDE로 출력 컬럼과 hire_date를 담아 Heap Fetches=0인 Index Only Scan이 되어 테이블 접근 제거

### 인덱스 정의 확인

```text
CREATE INDEX idx_employees_active_salary_hire ON day03_tuning.employees USING btree (salary DESC, hire_date) INCLUDE (employee_id, employee_no, full_name) WHERE ((employment_status)::text = 'ACTIVE'::text)
```

### 문제 5. OR 조건과 IN 조건 비교

### 문제 / 개선 목표

지점 코드 B003, B004, B005 검색. branch_code 인덱스를 추가하고 OR/IN 두 쿼리의 계획을 비교.

```sql
EXPLAIN (ANALYZE, BUFFERS, TIMING OFF)
SELECT employee_id, employee_no, full_name, branch_code
FROM employees
WHERE branch_code = 'B003'
   OR branch_code = 'B004'
   OR branch_code = 'B005';
```

### 개선 전 QUERY PLAN

```text
Seq Scan on employees  (cost=0.00..1783.00 rows=1549 width=33) (actual rows=1500 loops=1)
  Filter: (((branch_code)::text = 'B003'::text) OR ((branch_code)::text = 'B004'::text) OR ((branch_code)::text = 'B005'::text))
  Rows Removed by Filter: 48500
  Buffers: shared hit=908
Planning Time: 0.284 ms
Execution Time: 12.682 ms
```

### 개선안

```text
DROP INDEX IF EXISTS idx_employees_branch_code;
CREATE INDEX idx_employees_branch_code
    ON employees (branch_code);
ANALYZE employees;
```

### 개선 후 QUERY PLAN (A: OR)

```text
Bitmap Heap Scan on employees  (cost=24.88..995.50 rows=1443 width=33) (actual rows=1500 loops=1)
  Recheck Cond: (((branch_code)::text = 'B003'::text) OR ((branch_code)::text = 'B004'::text) OR ((branch_code)::text = 'B005'::text))
  Heap Blocks: exact=506
  Buffers: shared hit=510 read=4
  ->  BitmapOr  (cost=24.88..24.88 rows=1457 width=0) (actual rows=0 loops=1)
        ->  Bitmap Index Scan on idx_employees_branch_code (actual rows=500 loops=1)
              Index Cond: ((branch_code)::text = 'B003'::text)
        ->  Bitmap Index Scan on idx_employees_branch_code (actual rows=500 loops=1)
              Index Cond: ((branch_code)::text = 'B004'::text)
        ->  Bitmap Index Scan on idx_employees_branch_code (actual rows=500 loops=1)
              Index Cond: ((branch_code)::text = 'B005'::text)
Execution Time: 0.860 ms
```

### 개선 후 QUERY PLAN (B: IN)

```text
Bitmap Heap Scan on employees  (cost=24.17..989.33 rows=1457 width=33) (actual rows=1500 loops=1)
  Recheck Cond: ((branch_code)::text = ANY ('{B003,B004,B005}'::text[]))
  Heap Blocks: exact=506
  Buffers: shared hit=510
  ->  Bitmap Index Scan on idx_employees_branch_code  (cost=0.00..23.80 rows=1457 width=0) (actual rows=1500 loops=1)
        Index Cond: ((branch_code)::text = ANY ('{B003,B004,B005}'::text[]))
        Buffers: shared hit=4
Execution Time: 0.832 ms
```

### 개선 결과 해석

변경된 Plan Node: Seq Scan → Bitmap Heap Scan (OR은 BitmapOr + Bitmap Index Scan 3개, IN은 = ANY로 Bitmap Index Scan 1개)

Buffers 변화: shared hit=908 → OR 510 read=4 / IN 510 (둘 다 Heap Blocks exact=506)

Execution Time 변화: 12.682 ms → OR 0.860 ms / IN 0.832 ms (약 15배)

인덱스가 없을 땐 3개 OR 조건을 5만 건 전체에 Filter로 적용하는 Seq Scan

인덱스 추가 후 각 값을 Bitmap으로 합쳐 약 1,500건(3%)으로 좁혀짐

OR과 IN은 최종 Heap Blocks(506)와 실행 시간이 사실상 동일. 다만 IN은 = ANY로 정규화되어 인덱스 스캔 노드가 1개라 계획이 더 단순하고 가독성도 좋음

값 개수가 늘어날수록 OR은 BitmapOr 가지가 늘어 IN 표기가 유지보수에 유리

### 인덱스 정의 확인

```text
CREATE INDEX idx_employees_branch_code ON day03_tuning.employees USING btree (branch_code)
```

### 문제 6. 비-SARGable 날짜 조건 — 함수 대신 범위 검색

### 문제 / 개선 목표

2025년 입사자 검색. EXTRACT 함수 조건과 원본 컬럼 범위 조건을 비교. 반개구간 [2025-01-01, 2026-01-01)으로 재작성.

```sql
-- 비교 A: 컬럼에 함수 적용
EXPLAIN (ANALYZE, BUFFERS, TIMING OFF)
SELECT employee_id, employee_no, full_name, hire_date
FROM employees
WHERE extract(year FROM hire_date) = 2025;

-- 비교 B: SARGable 범위 조건 <<< 이부분은 직접 작성합니다.
EXPLAIN (ANALYZE, BUFFERS, TIMING OFF)
SELECT employee_id, employee_no, full_name, hire_date
FROM employees
WHERE hire_date >= date '2025-01-01'
  AND hire_date <  date '2026-01-01';
```

### 개선 전 QUERY PLAN (A: 함수 적용)

```text
Seq Scan on employees  (cost=0.00..1658.00 rows=250 width=32) (actual rows=5003 loops=1)
  Filter: (EXTRACT(year FROM hire_date) = '2025'::numeric)
  Rows Removed by Filter: 44997
  Buffers: shared hit=908
Execution Time: 11.804 ms
```

### 개선 전 QUERY PLAN (B: SARGable 범위)

```text
Seq Scan on employees  (cost=0.00..1658.00 rows=4926 width=32) (actual rows=5003 loops=1)
  Filter: ((hire_date >= '2025-01-01'::date) AND (hire_date < '2026-01-01'::date))
  Rows Removed by Filter: 44997
  Buffers: shared hit=908
Execution Time: 4.931 ms
```

### 개선안

```text
DROP INDEX IF EXISTS idx_employees_hire_date;
CREATE INDEX idx_employees_hire_date
    ON employees (hire_date);
ANALYZE employees;
```

### 개선 후 QUERY PLAN (A: 함수 적용 — 여전히 Seq Scan)

```text
Seq Scan on employees  (cost=0.00..1658.00 rows=250 width=32) (actual rows=5003 loops=1)
  Filter: (EXTRACT(year FROM hire_date) = '2025'::numeric)
  Rows Removed by Filter: 44997
  Buffers: shared hit=908
Execution Time: 7.922 ms
```

### 개선 후 QUERY PLAN (B: SARGable 범위 — 인덱스 사용)

```text
Bitmap Heap Scan on employees  (cost=75.88..1059.37 rows=5033 width=32) (actual rows=5003 loops=1)
  Recheck Cond: ((hire_date >= '2025-01-01'::date) AND (hire_date < '2026-01-01'::date))
  Heap Blocks: exact=586
  Buffers: shared hit=594
  ->  Bitmap Index Scan on idx_employees_hire_date  (cost=0.00..74.62 rows=5033 width=0) (actual rows=5003 loops=1)
        Index Cond: ((hire_date >= '2025-01-01'::date) AND (hire_date < '2026-01-01'::date))
        Buffers: shared hit=8
Execution Time: 1.439 ms
```

### 개선 결과 해석

변경된 Plan Node: A(함수 조건)는 인덱스 생성 후에도 Seq Scan 유지 / B(범위 조건)는 Seq Scan → Bitmap Heap Scan

Buffers 변화: A는 908 그대로 / B는 908 → 594 (Heap Blocks exact=586)

Execution Time 변화: A는 11.804 → 7.922 ms(캐시 효과일 뿐 여전히 전체 스캔) / B는 4.931 → 1.439 ms

컬럼에 함수를 씨우면(extract) 인덱스에 저장된 원본 값과 매칭 불가(비-SARGable)해 Seq Scan 강제

hire_date >= '2025-01-01' AND hire_date < '2026-01-01' 반개구간은 컬럼이 가공되지 않아(SARGable) B-tree로 바로 탐색

부가 이점: A는 함수 때문에 추정 행 수가 250건으로 실제(5003)와 크게 빗나가 계획 정확도 저하, B는 5033으로 거의 일치

상한을 < '2026-01-01'로 둔 것은 경계값 누락을 피하는 반개구간 관례

### 인덱스 정의 확인

```text
CREATE INDEX idx_employees_hire_date ON day03_tuning.employees USING btree (hire_date)
```

### 문제 7. 복합 인덱스와 왼쪽 우선 규칙

### 문제 / 개선 목표

부서 5의 DEV 직무 사원을 연봉순 상위 20명 조회. 등호 조건을 앞에, 정렬 컬럼을 뒤에 배치. 왼쪽 선두 컬럼이 빠진 검색도 비교.

```sql
EXPLAIN (ANALYZE, BUFFERS, TIMING OFF)
SELECT employee_id, employee_no, full_name, salary
FROM employees
WHERE department_id = 5
  AND job_code = 'DEV'
ORDER BY salary DESC
LIMIT 20;
```

### 개선 전 QUERY PLAN

```text
Limit  (cost=1664.76..1664.81 rows=20 width=35) (actual rows=20 loops=1)
  Buffers: shared hit=908
  ->  Sort  (cost=1664.76..1665.39 rows=254 width=35) (actual rows=20 loops=1)
        Sort Key: salary DESC
        Sort Method: top-N heapsort  Memory: 27kB
        ->  Seq Scan on employees  (actual rows=250 loops=1)
              Filter: ((department_id = 5) AND ((job_code)::text = 'DEV'::text))
              Rows Removed by Filter: 49750
              Buffers: shared hit=908
Execution Time: 7.470 ms
```

### 개선안

```text
DROP INDEX IF EXISTS idx_employees_dept_job_salary;
CREATE INDEX idx_employees_dept_job_salary
    ON employees (department_id, job_code, salary DESC);
ANALYZE employees;
```

### 개선 후 QUERY PLAN (본 쿼리, ORDER BY 있음 — Sort 제거)

```text
Limit  (cost=0.41..71.68 rows=20 width=35) (actual rows=20 loops=1)
  Buffers: shared hit=23
  ->  Index Scan using idx_employees_dept_job_salary on employees  (cost=0.41..912.58 rows=256 width=35) (actual rows=20 loops=1)
        Index Cond: ((department_id = 5) AND ((job_code)::text = 'DEV'::text))
        Buffers: shared hit=23
Execution Time: 0.071 ms
```

### 개선 후 QUERY PLAN (참고: ORDER BY 생략 시 — Bitmap, 순서 미보장)

```text
Limit  (cost=11.04..55.40 rows=20 width=35) (actual rows=20 loops=1)
  Buffers: shared hit=24
  ->  Bitmap Heap Scan on employees (actual rows=20 loops=1)
        Recheck Cond: ((department_id = 5) AND ((job_code)::text = 'DEV'::text))
        Heap Blocks: exact=20
        ->  Bitmap Index Scan on idx_employees_dept_job_salary (actual rows=250 loops=1)
Execution Time: 0.118 ms
```

### 개선 후 QUERY PLAN (선두 생략 — job_code만, 인덱스 미사용)

```text
Limit  (actual rows=20 loops=1)
  Buffers: shared hit=908
  ->  Sort  (Sort Key: salary DESC, top-N heapsort)
        ->  Seq Scan on employees (actual rows=5000 loops=1)
              Filter: ((job_code)::text = 'DEV'::text)
              Rows Removed by Filter: 45000
              Buffers: shared hit=908
Execution Time: 5.761 ms
```

### 개선 결과 해석

변경된 Plan Node: 본 쿼리(ORDER BY 있음) Seq Scan + Sort → Index Scan (Sort 제거) / 선두 생략(job만)은 Seq Scan + Sort 유지

Buffers 변화: 본 쿼리 908 → 23 / 선두 생략은 908 그대로

Execution Time 변화: 본 쿼리 7.470 → 0.071 ms / 선두 생략 5.761 ms (개선 없음)

(department_id, job_code, salary DESC) 복합 인덱스는 등호 조건 둘을 선두에 두어 부서 5·DEV 250건으로 바로 좁힘

salary DESC를 마지막에 두어 이미 연봉 내림차순 정렬되어 ORDER BY가 있어도 Sort 없이 Index Scan으로 앞 20건만 읽고 조기 종료

ORDER BY를 생략하면 옵티마이저가 Bitmap Heap Scan을 택하는데, 이는 정렬 순서를 보장하지 않음. 연봉순 상위 20명 요구를 정확히 만족하려면 ORDER BY 유지 필요

job_code만으로 검색하면 선두 컬럼 department_id가 빠져 왼쪽 우선 규칙(leftmost prefix rule) 미충족 → 인덱스 활용 불가, Seq Scan + Sort로 되돌아감

### 인덱스 정의 확인

```text
CREATE INDEX idx_employees_dept_job_salary ON day03_tuning.employees USING btree (department_id, job_code, salary DESC)
```

### 문제 8. 커버링 인덱스와 Index Only Scan

### 문제 / 개선 목표

특정 사번 구간의 이름과 이메일 조회. 검색 컬럼과 출력 컬럼을 구분해 INCLUDE 커버링 인덱스 설계. Heap Fetches가 적은 Index Only Scan 가능성을 높임.

```sql
EXPLAIN (ANALYZE, BUFFERS, TIMING OFF)
SELECT employee_no, full_name, email
FROM employees
WHERE employee_no >= 'EMP040000'
  AND employee_no <  'EMP040051'
ORDER BY employee_no;
```

### 개선 전 QUERY PLAN

```text
Sort  (cost=1658.01..1658.02 rows=1 width=38) (actual rows=51 loops=1)
  Sort Key: employee_no
  Sort Method: quicksort  Memory: 27kB
  Buffers: shared hit=908
  ->  Seq Scan on employees  (actual rows=51 loops=1)
        Filter: (((employee_no)::text >= 'EMP040000'::text) AND ((employee_no)::text < 'EMP040051'::text))
        Rows Removed by Filter: 49949
        Buffers: shared hit=908
Execution Time: 21.839 ms
```

### 개선안

```text
DROP INDEX IF EXISTS idx_employees_no_covering;
CREATE INDEX idx_employees_no_covering
    ON employees (employee_no)
    INCLUDE (full_name, email);
VACUUM ANALYZE employees;  -- 따로 실행 (visibility map 갱신 → Heap Fetches 0)
```

### 개선 후 QUERY PLAN

```text
Index Only Scan using idx_employees_no_covering on employees  (cost=0.41..4.43 rows=1 width=38) (actual rows=51 loops=1)
  Index Cond: ((employee_no >= 'EMP040000'::text) AND (employee_no < 'EMP040051'::text))
  Heap Fetches: 0
  Buffers: shared hit=1 read=4
Execution Time: 0.126 ms
```

### 개선 결과 해석

변경된 Plan Node: Seq Scan + Sort(quicksort) → Index Only Scan (Sort 노드 제거)

Buffers 변화: shared hit=908 → shared hit=1 read=4 (Heap 접근 제거)

Execution Time 변화: 21.839 ms → 0.126 ms (약 173배)

employee_no 인덱스가 범위 조건을 정렬 순서로 바로 탐색하고, 이미 employee_no 오름차순이라 ORDER BY용 Sort 노드가 사라짐

INCLUDE로 출력 컬럼(full_name, email)을 인덱스 리프에 담아 테이블 접근 없이 Index Only Scan

VACUUM ANALYZE로 visibility map을 갱신했기에 Heap Fetches=0. 이 과정을 생략하면 Index Only Scan이라도 가시성 확인을 위해 Heap을 다시 읽어 Heap Fetches가 크게 남음

계획 이름이 Index Only Scan이라도 Heap Fetches 값을 함께 확인해야 실제 커버링 효과를 판단할 수 있음

### 인덱스 정의 확인

```text
CREATE INDEX idx_employees_no_covering ON day03_tuning.employees USING btree (employee_no) INCLUDE (full_name, email)
```

### 문제 9. 조인, loops, 근무 기록 복합 인덱스

### 문제 / 개선 목표

부서 5 재직자 중 최근 30일 초과근무 합계가 큰 사원 20명 조회. 5만 사원 × 50만 근무기록 조인. 외부 사원 행마다 반복되는 work_logs 탐색 비용과 loops를 줄임.

```text
EXPLAIN (ANALYZE, BUFFERS, TIMING OFF)
SELECT
    e.employee_id,
    e.employee_no,
    e.full_name,
    sum(w.overtime_minutes) AS total_overtime_minutes
FROM employees AS e
JOIN employee_work_logs AS w
  ON w.employee_id = e.employee_id
WHERE e.department_id = 5
  AND e.employment_status = 'ACTIVE'
  AND w.work_date >= current_date - 30
GROUP BY
    e.employee_id,
    e.employee_no,
    e.full_name
ORDER BY total_overtime_minutes DESC
LIMIT 20;
```

### 개선 전 QUERY PLAN

```text
Limit  (cost=10027.53..10027.58 rows=20 width=36) (actual rows=20 loops=1)
  Buffers: shared hit=6965 read=10
  ->  Sort (Sort Key: sum(w.overtime_minutes) DESC, top-N heapsort)
        ->  Finalize GroupAggregate (actual rows=616 loops=1)
              ->  Gather Merge (Workers Launched: 2)
                    ->  Partial GroupAggregate (actual rows=289 loops=3)
                          ->  Hash Join  (actual rows=342 loops=3)
                                Hash Cond: (w.employee_id = e.employee_id)
                                ->  Parallel Seq Scan on employee_work_logs w (actual rows=7077 loops=3)
                                      Filter: (work_date >= (CURRENT_DATE - 30))
                                      Rows Removed by Filter: 159589
                                      Buffers: shared hit=4167
                                ->  Hash (actual rows=2500 loops=3)
                                      ->  Bitmap Heap Scan on employees e (actual rows=2500 loops=3)
                                            Recheck Cond: (department_id = 5)
                                            Filter: ((employment_status)::text = 'ACTIVE'::text)
Execution Time: 25.814 ms
```

### 개선안

```text
-- (1) 조인 대상 work_logs 인덱스
DROP INDEX IF EXISTS idx_work_logs_emp_date;
CREATE INDEX idx_work_logs_emp_date
    ON employee_work_logs (employee_id, work_date)
    INCLUDE (overtime_minutes);

-- (2) 부서 5 재직자 필터용 인덱스 (다른 문제 인덱스에 의존하지 않도록)
DROP INDEX IF EXISTS idx_employees_dept_active;
CREATE INDEX idx_employees_dept_active
    ON employees (department_id)
    WHERE employment_status = 'ACTIVE';

ANALYZE employee_work_logs;
ANALYZE employees;
```

### 개선 후 QUERY PLAN

```text
Limit  (cost=7548.78..7548.83 rows=20 width=36) (actual rows=20 loops=1)
  Buffers: shared hit=8417
  ->  Sort (Sort Key: sum(w.overtime_minutes) DESC, top-N heapsort)
        ->  GroupAggregate (actual rows=616 loops=1)
              ->  Sort (Sort Key: e.employee_id, actual rows=1026 loops=1)
                    ->  Nested Loop  (cost=25.35..7462.91 rows=920 width=32) (actual rows=1026 loops=1)
                          Buffers: shared hit=8417
                          ->  Bitmap Heap Scan on employees e (actual rows=2500 loops=1)
                                Recheck Cond: ((department_id = 5) AND ((employment_status)::text = 'ACTIVE'::text))
                                ->  Bitmap Index Scan on idx_employees_dept_active (actual rows=2500 loops=1)
                          ->  Index Only Scan using idx_work_logs_emp_date on employee_work_logs w (actual rows=0 loops=2500)
                                Index Cond: ((employee_id = e.employee_id) AND (work_date >= (CURRENT_DATE - 30)))
                                Heap Fetches: 0
                                Buffers: shared hit=7505
Execution Time: 8.015 ms
```

### 개선 결과 해석

변경된 Plan Node: Hash Join(Parallel Seq Scan on work_logs) → Nested Loop + Index Only Scan on idx_work_logs_emp_date. employees 측은 idx_employees_dept_active로 처리

Buffers 변화: shared hit=6965 read=10 → shared hit=8417 (총 블록 수는 오히려 증가)

Execution Time 변화: 25.814 ms → 8.015 ms (약 3배 단축)

개선 전엔 work_logs에 인덱스가 없어 50만 건을 Parallel Seq Scan으로 읽고 Filter로 최근 30일만 남김. 이후 Hash Join으로 결합

(employee_id, work_date) INCLUDE(overtime_minutes) 복합 인덱스로 옵티마이저가 Nested Loop로 전환. 부서 5 재직자 2,500명을 외부(driving)로 두고 각 사원의 최근 30일 근무기록을 인덱스로 직접 탐색(loops=2500, Heap Fetches=0)

주목: 총 Buffers가 6965 → 8417로 오히려 늘었음. Nested Loop이 2,500명마다 인덱스를 반복 탐색해 인덱스 블록 접근이 누적될. 그럼에도 시간이 빨라진 이유는 늘어난 블록이 대부분 캐시된 인덱스 블록(shared hit)이고 Heap Fetches=0이라 블록당 비용이 낮으며, 병렬 Hash 구성·해시 빌드 같은 무거운 작업이 사라졌기 때문

결론: Plan 이름이나 Buffers 총량만으로 우열을 판단하지 말고, loops·블록 성격(hit/read, Heap Fetches)·실제 실행 시간을 함께 봐야 함

### 인덱스 정의 확인

```text
CREATE INDEX idx_work_logs_emp_date ON day03_tuning.employee_work_logs USING btree (employee_id, work_date) INCLUDE (overtime_minutes)
CREATE INDEX idx_employees_dept_active ON day03_tuning.employees USING btree (department_id) WHERE ((employment_status)::text = 'ACTIVE'::text)
```

### 문제 10. NOT IN의 NULL 함정과 NOT EXISTS 안티 조인

### 문제 / 개선 목표

완료된 교육 이력이 없는 사원을 찾음. 서브쿼리에 NULL이 포함된 NOT IN의 결과를 확인하고 정확한 쿼리로 수정. 성능보다 결과 정확성 회복이 먼저.

```sql
-- 잘못된 쿼리: 서브쿼리 결과에 NULL이 있어 전체 결과가 0건이 될 수 있다. -> NOT IN 사용
EXPLAIN (ANALYZE, BUFFERS, TIMING OFF)
SELECT e.employee_id, e.employee_no, e.full_name
FROM employees AS e
WHERE e.employee_id NOT IN (
    SELECT t.employee_id
    FROM employee_training AS t
    WHERE t.completion_status = 'COMPLETED'
);
```

### 개선 전 QUERY PLAN (잘못된 NOT IN)

```text
Seq Scan on employees e  (cost=1028.41..2561.41 rows=25000 width=28) (actual rows=0 loops=1)
  Filter: (NOT (ANY (employee_id = (hashed SubPlan 1).col1)))
  Rows Removed by Filter: 50000
  Buffers: shared hit=1284
  SubPlan 1
    ->  Seq Scan on employee_training t (actual rows=36001 loops=1)
          Filter: ((completion_status)::text = 'COMPLETED'::text)
          Rows Removed by Filter: 9000
Execution Time: 20.430 ms
```

```text
wrong_result_count = 0   -- NULL 함정으로 0건 반환
```

### 개선안

```sql
DROP INDEX IF EXISTS idx_training_completed_emp;
CREATE INDEX idx_training_completed_emp
    ON employee_training (employee_id)
    WHERE completion_status = 'COMPLETED';
ANALYZE employee_training;

-- 정확한 쿼리 -> NOT EXISTS 사용
EXPLAIN (ANALYZE, BUFFERS, TIMING OFF)
SELECT e.employee_id, e.employee_no, e.full_name
FROM employees AS e
WHERE NOT EXISTS (
    SELECT 1
    FROM employee_training AS t
    WHERE t.employee_id = e.employee_id
      AND t.completion_status = 'COMPLETED'
);
```

### 개선 후 QUERY PLAN (정확한 NOT EXISTS)

```text
Hash Anti Join  (cost=1388.49..3108.26 rows=14002 width=28) (actual rows=14000 loops=1)
  Hash Cond: (e.employee_id = t.employee_id)
  Buffers: shared hit=1284
  ->  Seq Scan on employees e (actual rows=50000 loops=1)
  ->  Hash (actual rows=36000 loops=1)
        ->  Seq Scan on employee_training t (actual rows=36001 loops=1)
              Filter: ((completion_status)::text = 'COMPLETED'::text)
              Rows Removed by Filter: 9000
Execution Time: 19.539 ms
```

```text
correct_result_count = 14000   -- 정확한 미이수자 수
```

### 개선 결과 해석

변경된 Plan Node: (NOT IN) Seq Scan + hashed SubPlan → (NOT EXISTS) Hash Anti Join

Buffers 변화: shared hit=1284 → shared hit=1284 (동일)

Execution Time 변화: 20.430 ms → 19.539 ms (사실상 동일)

이 문제의 핵심은 성능이 아니라 결과 정확성 회복. employee_training에 employee_id가 NULL인 COMPLETED 행이 있어 NOT IN 서브쿼리 결과에 NULL이 섞임

3값 논리에서 x NOT IN (..., NULL)은 어떤 x에대해서도 참이 될 수 없어(UNKNOWN) 전체 결과가 0건(wrong_result_count = 0)

NOT EXISTS는 각 사원마다 완료 이력 존재 여부만 판단하므로 NULL 영향 없음. 옵티마이저는 Hash Anti Join으로 처리해 정확한 14,000명 반환

성능(시간·Buffers)은 거의 변하지 않음. 두 쿼리 모두 employees 5만 건과 완료 이력 3.6만 건을 대부분 읽어야 하는 구조라 읽는 데이터 양이 비슷함

### 부분 인덱스가 사용되지 않은 이유

COMPLETED 부분 인덱스를 만들었지만 실행 계획엔 쓰이지 않고 Seq Scan이 선택됨. 완료 이력이 전체 45,000건 중 36,001건으로 대다수(약 80%)라 선택도가 낮기 때문

안티 조인은 완료 이력 대부분을 읽어 해시 테이블을 만들어야 하므로, 인덱스 임의 접근보다 순차 스캔 후 해시 조인이 더 저렴하다고 옵티마이저가 판단

부분 인덱스는 대상 행이 소수일 때(예: PLANNED 등 희소 상태) 효과적이며, 이 경우처럼 대상이 다수면 순차 스캔이 합리적 선택

### 인덱스 정의 확인

```text
CREATE INDEX idx_training_completed_emp ON day03_tuning.employee_training USING btree (employee_id) WHERE ((completion_status)::text = 'COMPLETED'::text)
```

### 전체 요약

### 배운 핵심 포인트

인덱스 이름만으로 판단 금지: Index Only Scan이어도 Heap Fetches, Nested Loop에서도 Buffers 총량과 실행 시간을 함께 해석

비-SARGable(컬럼에 함수)은 인덱스를 만들어도 무력화 → 범위 조건으로 재작성

복합 인덱스는 등호 앞·정렬 뒤, 왼쪽 우선 규칙 준수 시에만 효과

부분 인덱스는 선택도가 높을(대상이 소수) 때 효과적; 대상이 다수면 Seq Scan이 합리적(문제 10)

NOT IN + NULL은 결과 0건 함정 → NOT EXISTS로 정확성 먼저 회복

day3_쿼리_임채현.sql 0.05MB PostgreSQL_day03_tuning_샘플_스키마_DDL_DML.sql 0.01MB

## 관련 글

- [[blog/STUDYING/index|STUDYING]]
