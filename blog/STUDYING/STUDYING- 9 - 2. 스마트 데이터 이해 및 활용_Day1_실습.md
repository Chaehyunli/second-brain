---
title: "[STUDYING] 9 - 2. 스마트 데이터 이해 및 활용_Day1_실습"
created: 2026-07-27
updated: 2026-07-27
type: blog-post
tags: ["blog", "technical-writing"]
category: "STUDYING"
published: 2026-07-27
source_url: https://ch010104.tistory.com/322
---
# [STUDYING] 9 - 2. 스마트 데이터 이해 및 활용_Day1_실습

## 원문

https://ch010104.tistory.com/322

## 노트 유형

`tutorial`

## 학습 목표 및 맥락

학사관리시스템을 주제로 데이터베이스 환경 구성부터 ERD 설계, 제약조건을 포함한 테이블 생성(DDL), 샘플 데이터 입력(DML), 기초 조회 및 함수 활용까지의 전 과정을 직접 수행한다.

ERD 설계 3.1 학사관리시스템 요구사항 (설계 방향) 3.2 ERD 그림 3.3 범례 (설명문) 3.4 테이블 설계도 3.5 관계 설명

## 원문 기반 학습 정리

### 실습 개요

### 실습 목적

학사관리시스템을 주제로 데이터베이스 환경 구성부터 ERD 설계, 제약조건을 포함한 테이블 생성(DDL), 샘플 데이터 입력(DML), 기초 조회 및 함수 활용까지의 전 과정을 직접 수행한다.

### 실습 범위

PostgreSQL 접속 확인

DATABASE / SCHEMA 생성

ERD 설계

CREATE

PostgreSQL 접속 확인 (DBeaver)

CREATE DATABASE / CREATE SCHEMA 실행

ERD 설계 3.1 학사관리시스템 요구사항 (설계 방향) 3.2 ERD 그림 3.3 범례 (설명문) 3.4 테이블 설계도 3.5 관계 설명

CREATE TABLE — 제약조건을 포함한 DDL 작성

INSERT INTO (테이블 데이터 최소 10건 이상) 5.1 course 초기 데이터 5.2 department 초기 데이터 5.3 enrollment 초기 데이터 5.4 professor 초기 데이터 5.5 student 초기 데이터

SELECT + WHERE + ORDER BY 기초 조회

COALESCE / CASE WHEN / 날짜 함수 활용 7.1 COALESCE 7.2 CASE WHEN 7.3 날짜 함수

### 1. PostgreSQL 접속 확인 (DBeaver)

### 2. CREATE DATABASE / CREATE SCHEMA 실행

### 3. ERD 설계

### 3.1 학사관리시스템 요구사항 (설계 방향)

본 시스템은 대학의 학사 정보를 관리하기 위한 데이터베이스로, 학과·교수·학생·과목·수강신청 정보를 다룬다. 설계 시 반영한 주요 요구사항은 다음과 같다.

모든 학생과 교수는 반드시 하나의 학과에 소속된다.

하나의 학과에는 여러 명의 학생과 교수가 속할 수 있다.

하나의 과목은 하나의 학과에서 개설하며, 한 명의 교수가 담당한다. (담당 교수는 미정일 수 있다.)

한 명의 학생은 여러 과목을 수강할 수 있고, 하나의 과목은 여러 학생이 수강할 수 있다. (학생-과목은 다대다 관계이며, 수강신청 테이블로 해소한다.)

동일 학생이 동일 과목을 중복 신청할 수 없다.

성적은 수강신청 시점에 미입력 상태(NULL)일 수 있으며, 이후 부여된다.

### 3.2 ERD 그림

### 3.3 범례 (설명문)

### 3.4 테이블 설계도

department (학과)

professor (교수)

student (학생)

course (과목)

enrollment (수강신청 — 교차 테이블)

### 3.5 관계 설명

student와 course는 직접적으로 다대다(N:M) 관계이며, 이를 enrollment 교차 테이블이 두 개의 일대다(1:N) 관계로 분해하여 해소한다. 즉 "한 학생이 여러 과목을, 한 과목을 여러 학생이" 수강하는 관계를 enrollment가 중간에서 연결한다.

### 4. CREATE TABLE — 제약 조건 을 포함한 DDL 작성

```sql
-- ============================================
-- 학사 관리 시스템 DDL
-- ============================================

BEGIN;  -- 트랜잭션 시작

-- 1. 학과
CREATE TABLE IF NOT EXISTS department (
    dept_id      SERIAL PRIMARY KEY,
    dept_name    VARCHAR(50) NOT NULL UNIQUE,
    office_phone VARCHAR(20),
    created_at   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

SAVEPOINT sp_department;

-- 2. 교수
CREATE TABLE IF NOT EXISTS professor (
    prof_id    SERIAL PRIMARY KEY,
    prof_name  VARCHAR(30) NOT NULL,
    dept_id    INT NOT NULL,
    hire_date  DATE NOT NULL DEFAULT CURRENT_DATE,
    email      VARCHAR(100) UNIQUE,
    CONSTRAINT fk_prof_dept FOREIGN KEY (dept_id)
        REFERENCES department (dept_id) ON DELETE RESTRICT
);

SAVEPOINT sp_professor;

-- 3. 학생
CREATE TABLE IF NOT EXISTS student (
    student_id   SERIAL PRIMARY KEY,
    student_name VARCHAR(30) NOT NULL,
    dept_id      INT NOT NULL,
    grade        SMALLINT NOT NULL DEFAULT 1,
    gender       CHAR(1),
    birth_date   DATE,
    enroll_date  DATE NOT NULL DEFAULT CURRENT_DATE,
    email        VARCHAR(100) UNIQUE,
    CONSTRAINT fk_stu_dept FOREIGN KEY (dept_id)
        REFERENCES department (dept_id) ON DELETE RESTRICT,
    CONSTRAINT chk_grade  CHECK (grade BETWEEN 1 AND 4),
    CONSTRAINT chk_gender CHECK (gender IN ('M', 'F'))
);

SAVEPOINT sp_student;

-- 4. 과목
CREATE TABLE IF NOT EXISTS course (
    course_id   SERIAL PRIMARY KEY,
    course_name VARCHAR(50) NOT NULL,
    dept_id     INT NOT NULL,
    prof_id     INT,
    credit      SMALLINT NOT NULL DEFAULT 3,
    semester    VARCHAR(10) NOT NULL,
    capacity    INT NOT NULL DEFAULT 40,
    CONSTRAINT fk_course_dept FOREIGN KEY (dept_id)
        REFERENCES department (dept_id) ON DELETE RESTRICT,
    CONSTRAINT fk_course_prof FOREIGN KEY (prof_id)
        REFERENCES professor (prof_id) ON DELETE SET NULL,
    CONSTRAINT chk_credit   CHECK (credit BETWEEN 1 AND 6),
    CONSTRAINT chk_capacity CHECK (capacity > 0)
);

SAVEPOINT sp_course;

-- 5. 수강신청 (교차 테이블)
CREATE TABLE IF NOT EXISTS enrollment (
    enroll_id    SERIAL PRIMARY KEY,
    student_id   INT NOT NULL,
    course_id    INT NOT NULL,
    enroll_date  DATE NOT NULL DEFAULT CURRENT_DATE,
    grade_score  NUMERIC(4,1),
    grade_letter VARCHAR(2),
    CONSTRAINT fk_enroll_student FOREIGN KEY (student_id)
        REFERENCES student (student_id) ON DELETE CASCADE,
    CONSTRAINT fk_enroll_course FOREIGN KEY (course_id)
        REFERENCES course (course_id) ON DELETE CASCADE,
    CONSTRAINT uq_enroll UNIQUE (student_id, course_id),
    CONSTRAINT chk_score CHECK (grade_score BETWEEN 0 AND 100)
);

SAVEPOINT sp_enrollment;

COMMIT;
```

### 5. INSERT INTO (테이블 데이터는 에서 최소 10건 이상)

```sql
-- ============================================
-- 학사 관리 시스템 샘플 데이터 (테이블별 10건 이상)
-- ============================================

BEGIN;

-- 1. 학과 (10건)
INSERT INTO department (dept_name, office_phone) VALUES
    ('컴퓨터공학과', '02-300-1001'),
    ('전자공학과',   '02-300-1002'),
    ('기계공학과',   '02-300-1003'),
    ('경영학과',     '02-300-1004'),
    ('경제학과',     '02-300-1005'),
    ('영어영문학과', '02-300-1006'),
    ('국어국문학과', '02-300-1007'),
    ('수학과',       '02-300-1008'),
    ('물리학과',     '02-300-1009'),
    ('화학과',       '02-300-1010')
ON CONFLICT (dept_name) DO NOTHING;

SAVEPOINT sp_department;

-- 2. 교수 (10건)
INSERT INTO professor (prof_name, dept_id, hire_date, email) VALUES
    ('김교수', 1, '2010-03-01', 'kim@univ.ac.kr'),
    ('이교수', 1, '2012-09-01', 'lee@univ.ac.kr'),
    ('박교수', 2, '2008-03-01', 'park@univ.ac.kr'),
    ('최교수', 3, '2015-03-01', 'choi@univ.ac.kr'),
    ('정교수', 4, '2011-09-01', 'jung@univ.ac.kr'),
    ('강교수', 5, '2013-03-01', 'kang@univ.ac.kr'),
    ('조교수', 6, '2009-03-01', 'cho@univ.ac.kr'),
    ('윤교수', 7, '2016-09-01', 'yoon@univ.ac.kr'),
    ('장교수', 8, '2014-03-01', 'jang@univ.ac.kr'),
    ('임교수', 9, '2017-03-01', 'lim@univ.ac.kr')
ON CONFLICT (email) DO NOTHING;

SAVEPOINT sp_professor;

-- 3. 학생 (12건)
INSERT INTO student (student_name, dept_id, grade, gender, birth_date, enroll_date, email) VALUES
    ('홍길동', 1, 3, 'M', '2002-05-14', '2021-03-02', 'hong@univ.ac.kr'),
    ('김영희', 1, 2, 'F', '2003-08-21', '2022-03-02', 'younghee@univ.ac.kr'),
    ('이철수', 2, 4, 'M', '2001-01-30', '2020-03-02', 'chulsoo@univ.ac.kr'),
    ('박민지', 3, 1, 'F', '2004-11-11', '2024-03-02', 'minji@univ.ac.kr'),
    ('최준호', 4, 3, 'M', '2002-07-07', '2021-03-02', 'junho@univ.ac.kr'),
    ('정수빈', 5, 2, 'F', '2003-03-25', '2022-03-02', 'subin@univ.ac.kr'),
    ('강민석', 6, 4, 'M', '2001-09-09', '2020-03-02', 'minseok@univ.ac.kr'),
    ('조은지', 7, 1, 'F', '2004-02-18', '2024-03-02', 'eunji@univ.ac.kr'),
    ('윤재현', 8, 3, 'M', '2002-12-01', '2021-03-02', 'jaehyun@univ.ac.kr'),
    ('장서연', 9, 2, 'F', '2003-06-06', '2022-03-02', 'seoyeon@univ.ac.kr'),
    ('임도현', 1, 1, 'M', '2004-04-19', '2024-03-02', 'dohyun@univ.ac.kr'),
    ('한지우', 2, 3, 'F', '2002-10-23', '2021-03-02', 'jiwoo@univ.ac.kr')
ON CONFLICT (email) DO NOTHING;

SAVEPOINT sp_student;

-- 4. 과목 (10건)
INSERT INTO course (course_name, dept_id, prof_id, credit, semester, capacity) VALUES
    ('자료구조',       1, 1, 3, '2024-1', 40),
    ('운영체제',       1, 2, 3, '2024-1', 35),
    ('디지털논리회로', 2, 3, 3, '2024-1', 30),
    ('열역학',         3, 4, 3, '2024-1', 40),
    ('경영학원론',     4, 5, 2, '2024-1', 50),
    ('미시경제학',     5, 6, 3, '2024-1', 45),
    ('영미소설',       6, 7, 2, '2024-1', 30),
    ('현대국문학',     7, 8, 2, '2024-1', 25),
    ('선형대수',       8, 9, 3, '2024-1', 40),
    ('일반물리학',     9, 10, 3, '2024-1', 40)
ON CONFLICT DO NOTHING;

SAVEPOINT sp_course;

-- 5. 수강신청 (12건)
INSERT INTO enrollment (student_id, course_id, enroll_date, grade_score, grade_letter) VALUES
    (1, 1, '2024-03-05', 92.5, 'A'),
    (1, 2, '2024-03-05', 85.0, 'B'),
    (2, 1, '2024-03-06', 78.0, 'C'),
    (3, 3, '2024-03-05', 88.5, 'B'),
    (4, 4, '2024-03-07', 95.0, 'A'),
    (5, 5, '2024-03-05', 70.0, 'C'),
    (6, 6, '2024-03-06', 81.5, 'B'),
    (7, 7, '2024-03-05', 90.0, 'A'),
    (8, 8, '2024-03-08', 65.0, 'D'),
    (9, 9, '2024-03-05', 77.5, 'C'),
    (10, 10, '2024-03-06', 83.0, 'B'),
    (11, 1, '2024-03-07', NULL, NULL)  -- 성적 미입력 (COALESCE 실습용)
ON CONFLICT (student_id, course_id) DO NOTHING;

SAVEPOINT sp_enrollment;

COMMIT;
```

### 5.1 course 초기 데이터

### 5.2 department 초기 데이터

### 5.3 enrollment 초기 데이터

### 5.4 professor 초기 데이터

### 5.5 student 초기 데이터

### 6. SELECT + WHERE + ORDER BY 기초 조회

```sql
-- ============================================
-- SELECT + WHERE + ORDER BY 기초 조회
-- ============================================

-- (1) 전체 조회 : 학과 전체를 이름순으로
SELECT dept_id, dept_name, office_phone
FROM department
ORDER BY dept_name ASC;
```

```sql
-- ============================================
-- SELECT + WHERE + ORDER BY 기초 조회
-- ============================================

-- (2) 특정 조건 : 3학년 학생만 조회 (학번 오름차순)
SELECT student_id, student_name, grade, gender
FROM student
WHERE grade = 3
ORDER BY student_id ASC;
```

```sql
-- ============================================
-- SELECT + WHERE + ORDER BY 기초 조회
-- ============================================

-- (3) 비교 연산 : 정원이 40명 이상인 과목 (정원 많은 순)
SELECT course_name, credit, capacity
FROM course
WHERE capacity >= 40
ORDER BY capacity DESC;
```

```sql
-- ============================================
-- SELECT + WHERE + ORDER BY 기초 조회
-- ============================================

-- (4) 문자열 검색 : 이름에 '김'이 들어가는 학생
SELECT student_id, student_name, dept_id
FROM student
WHERE student_name LIKE '김%'
ORDER BY student_name ASC;
```

```sql
-- ============================================
-- SELECT + WHERE + ORDER BY 기초 조회
-- ============================================

-- (5) 범위 조건 (BETWEEN) : 성적 80~100점 수강 기록 (높은 점수 순)
SELECT enroll_id, student_id, course_id, grade_score
FROM enrollment
WHERE grade_score BETWEEN 80 AND 100
ORDER BY grade_score DESC;
```

```sql
-- ============================================
-- SELECT + WHERE + ORDER BY 기초 조회
-- ============================================

-- (6) 목록 조건 (IN) : 특정 학과(1,2,3번) 소속 학생
SELECT student_id, student_name, dept_id, grade
FROM student
WHERE dept_id IN (1, 2, 3)
ORDER BY dept_id ASC, grade DESC;
```

```sql
-- ============================================
-- SELECT + WHERE + ORDER BY 기초 조회
-- ============================================

-- (7) 복합 조건 (AND) : 컴퓨터공학과(1번) 3학년 남학생
SELECT student_id, student_name, grade, gender
FROM student
WHERE dept_id = 1 AND grade = 3 AND gender = 'M'
ORDER BY student_id ASC;
```

```sql
-- ============================================
-- SELECT + WHERE + ORDER BY 기초 조회
-- ============================================

-- (8) OR 조건 : 1학년이거나 4학년인 학생
SELECT student_id, student_name, grade
FROM student
WHERE grade = 1 OR grade = 4
ORDER BY grade ASC, student_name ASC;
```

```sql
-- ============================================
-- SELECT + WHERE + ORDER BY 기초 조회
-- ============================================

-- (9) NULL 조회 : 성적이 아직 입력되지 않은 수강 기록
SELECT enroll_id, student_id, course_id, grade_score
FROM enrollment
WHERE grade_score IS NULL
ORDER BY enroll_id ASC;
```

```sql
-- ============================================
-- SELECT + WHERE + ORDER BY 기초 조회
-- ============================================

-- (10) 다중 정렬 : 학생을 학년 내림차순, 같은 학년은 이름 오름차순
SELECT student_id, student_name, grade, dept_id
FROM student
ORDER BY grade DESC, student_name ASC;
```

```sql
-- ============================================
-- SELECT + WHERE + ORDER BY 기초 조회
-- ============================================
-- (11) 상위 N건 (LIMIT) : 성적 상위 5건
SELECT enroll_id, student_id, course_id, grade_score
FROM enrollment
WHERE grade_score IS NOT NULL
ORDER BY grade_score DESC
LIMIT 5;
```

### 7. COALESCE / CASE WHEN / 날짜 함수 활용

### 7.1 COALESCE

```sql
-- ============================================
-- COALESCE / CASE WHEN / 날짜 함수 활용
-- ============================================

-- --------------------------------------------
-- [A] COALESCE : NULL 대체
-- --------------------------------------------

-- (A-1) 미입력 성적을 0점으로 표시
SELECT enroll_id, student_id, course_id,
       COALESCE(grade_score, 0) AS score_view
FROM enrollment
ORDER BY enroll_id ASC;
```

```sql
-- ============================================
-- COALESCE / CASE WHEN / 날짜 함수 활용
-- ============================================

-- --------------------------------------------
-- [A] COALESCE : NULL 대체
-- --------------------------------------------

-- (A-2) 미입력 등급을 '미평가' 문자열로 대체
SELECT enroll_id, student_id, course_id,
       COALESCE(grade_letter, '미평가') AS letter_view
FROM enrollment
ORDER BY enroll_id ASC;
```

```sql
-- ============================================
-- COALESCE / CASE WHEN / 날짜 함수 활용
-- ============================================

-- --------------------------------------------
-- [A] COALESCE : NULL 대체
-- --------------------------------------------

-- (A-3) 연락처 없는 학과는 '연락처 없음'으로
SELECT dept_name,
       COALESCE(office_phone, '연락처 없음') AS phone_view
FROM department
ORDER BY dept_name ASC;
```

### 7.2 CASE WHEN

```sql
-- ============================================
-- COALESCE / CASE WHEN / 날짜 함수 활용
-- ============================================

-- --------------------------------------------
-- [B] CASE WHEN : 조건 분기
-- --------------------------------------------

-- (B-1) 점수 → 학점 등급 변환
SELECT enroll_id, student_id, grade_score,
       CASE
           WHEN grade_score IS NULL THEN '미평가'
           WHEN grade_score >= 90 THEN 'A'
           WHEN grade_score >= 80 THEN 'B'
           WHEN grade_score >= 70 THEN 'C'
           WHEN grade_score >= 60 THEN 'D'
           ELSE 'F'
       END AS calc_grade
FROM enrollment
ORDER BY grade_score DESC NULLS LAST;
```

```sql
-- ============================================
-- COALESCE / CASE WHEN / 날짜 함수 활용
-- ============================================

-- --------------------------------------------
-- [B] CASE WHEN : 조건 분기
-- --------------------------------------------

-- (B-2) 합격/불합격 판정 (60점 기준)
SELECT enroll_id, student_id, grade_score,
       CASE
           WHEN grade_score IS NULL THEN '미응시'
           WHEN grade_score >= 60 THEN '합격'
           ELSE '불합격'
       END AS pass_status
FROM enrollment
ORDER BY enroll_id ASC;
```

```sql
-- ============================================
-- COALESCE / CASE WHEN / 날짜 함수 활용
-- ============================================

-- --------------------------------------------
-- [B] CASE WHEN : 조건 분기
-- --------------------------------------------

-- (B-3) 학년 → 재학 구분 문자열
SELECT student_id, student_name, grade,
       CASE grade
           WHEN 1 THEN '1학년 (신입)'
           WHEN 2 THEN '2학년'
           WHEN 3 THEN '3학년'
           WHEN 4 THEN '4학년 (졸업예정)'
           ELSE '기타'
       END AS grade_label
FROM student
ORDER BY grade ASC;
```

### 7.3 날짜 함수

```sql
-- ============================================
-- COALESCE / CASE WHEN / 날짜 함수 활용
-- ============================================

-- --------------------------------------------
-- [C] 날짜 함수
-- --------------------------------------------

-- (C-1) 학생 나이 계산 (AGE + EXTRACT)
SELECT student_id, student_name, birth_date,
       EXTRACT(YEAR FROM AGE(birth_date)) AS age
FROM student
ORDER BY age DESC;
```

```sql
-- ============================================
-- COALESCE / CASE WHEN / 날짜 함수 활용
-- ============================================

-- --------------------------------------------
-- [C] 날짜 함수
-- --------------------------------------------

-- (C-2) 입학 후 경과 일수
SELECT student_id, student_name, enroll_date,
       CURRENT_DATE - enroll_date AS days_enrolled
FROM student
ORDER BY days_enrolled DESC;
```

```sql
-- ============================================
-- COALESCE / CASE WHEN / 날짜 함수 활용
-- ============================================

-- --------------------------------------------
-- [C] 날짜 함수
-- --------------------------------------------

-- (C-3) 입학일 포맷 변환 (TO_CHAR)
SELECT student_id, student_name,
       TO_CHAR(enroll_date, 'YYYY년 MM월 DD일') AS enroll_fmt
FROM student
ORDER BY student_id ASC;
```

```sql
-- (C-4) 현재 시각 및 조회 시점 표시 (NOW)
SELECT student_id, student_name,
       enroll_date,
       NOW() AS query_time,
       NOW() - enroll_date AS elapsed
FROM student
ORDER BY student_id ASC;
```

## 관련 글

- [[blog/STUDYING/index|STUDYING]]
