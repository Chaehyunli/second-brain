---
title: "[데이터베이스 설계] 쿼리 처리(Query Processing) - A4 ~ A10"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "Database", "Design"]
category: "DATABASE DESIGN"
published: 2025-09-29
source_url: https://ch010104.tistory.com/147
---

# [데이터베이스 설계] 쿼리 처리(Query Processing) - A4 ~ A10

## 원문

https://ch010104.tistory.com/147

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

- Secondary Index는 Primary Index와 달리 데이터가 물리적으로 정렬되어 있지 않은 경우에 사용

후보 키(Candidate Key)에 대한 검색: - 검색하려는 키가 고유한 값(unique)이라면, Primary Index와 유사하게 인덱스 트리의 높이(hi​)만큼 탐색하고, 실제 데이터 블록에 한 번 더 접근

## 원문 기반 개념 정리

### 1. Secondary Index를 이용한 동등(Equality) 조건 선택 (A4)

- Secondary Index는 Primary Index와 달리 데이터가 물리적으로 정렬되어 있지 않은 경우에 사용

A4 (Secondary B+-Tree, 동등 조건)

후보 키(Candidate Key)에 대한 검색: - 검색하려는 키가 고유한 값(unique)이라면, Primary Index와 유사하게 인덱스 트리의 높이(hi​)만큼 탐색하고, 실제 데이터 블록에 한 번 더 접근

후보 키가 아닌 컬럼에 대한 검색: - 검색 결과로 여러 개의 레코드가 반환될 수 있으며, 이 레코드들은 물리적으로 서로 다른 데이터 블록에 흩어져 있을 수 있음 - 따라서 인덱스 탐색 후, 조건을 만족하는 n개의 레코드를 가져오기 위해 각각 I/O 작업이 발생할 수 있어 비용이 크게 증가할 수 있음

용어 정리

hi​: 인덱스 트리의 높이 (Height of index)

tT​: 데이터 블록 하나를 전송(transfer)하는 데 걸리는 시간

tS​: 디스크 헤드를 특정 트랙으로 이동(seek)시키는 데 걸리는 시간

n: 조건을 만족하는 레코드의 수

### 2. 인덱스를 이용한 비교(Comparison) 조건 선택 (A5, A6)

- > 또는 <와 같은 비교 연산자를 사용하는 선택 연산은 데이터의 정렬 여부에 따라 효율이 크게 달라짐

A5 (Primary B+-Tree, 비교 조건)

A >= V 형태의 검색: - 데이터가 검색 키(A)를 기준으로 물리적으로 정렬되어 있으므로, 인덱스를 통해 조건을 만족하는 첫 번째 데이터(V)의 위치를 찾은 후, 그 지점부터 순차적으로 디스크를 읽으면 됨 - A <= V 형태의 검색: - 이 경우, 인덱스를 사용하는 것보다 테이블의 처음부터 조건을 만족하지 않는 데이터가 나올 때까지 순차적으로 스캔(Sequential Scan)하는 것이 더 효율적일 수 있음

A6 (Secondary B+-Tree, 비교 조건)

A >= V 또는 A <= V 조건 모두, 먼저 인덱스의 리프 노드를 스캔하여 조건을 만족하는 데이터 레코드의 포인터 목록을 찾음 - 그 후, 이 포인터들을 이용해 실제 데이터 블록에 접근

각 레코드를 가져올 때마다 I/O가 발생할 수 있어, 경우에 따라서는 전체 파일을 스캔하는 것이 더 저렴할 수도 있음

### 3. 복합(Complex) 조건 선택 처리

- 여러 조건이 AND나 OR로 결합된 복합 선택 연산은 다음과 같은 전략을 사용

Conjunctive Selection (AND 연산)

- 여러 조건을 동시에 만족하는 데이터를 찾는 AND 연산

A7 (단일 인덱스 사용): - 여러 조건 중 가장 비용이 적게 드는(가장 선택도(Selectivity)가 좋은) 조건 하나를 골라 인덱스를 통해 데이터를 필터링 - 그리고 메모리로 가져온 결과에 나머지 조건들을 적용하여 최종 결과를 찾음

A8 (복합 인덱스 사용): - 만약 여러 컬럼을 묶어서 만든 복합 인덱스가 존재한다면, 이를 활용하는 것이 가장 빠를 수 있음

A9 (Identifier의 교집합 활용): - 각 조건에 해당하는 인덱스를 모두 사용하여 각각의 결과(레코드 포인터 목록)를 얻어냄 - 이 목록들의 교집합을 구해 최종적으로 가져올 레코드를 식별한 후, 디스크에서 데이터를 가져옴

Disjunctive Selection (OR 연산)

여러 조건 중 하나라도 만족하면 되는 OR 연산

A10 (Identifier의 합집합 활용): - 각 조건에 대해 인덱스를 사용하여 레코드 포인터 목록을 얻은 후, 이 목록들을 모두 합집합(Union)하여 결과를 생성 - 이 방법은 모든 조건에 인덱스가 존재할 때 유용하며, 그렇지 않다면 전체 테이블 스캔이 더 나을 수 있음

Negation (부정 연산): - NOT과 같은 부정 조건은 일반적으로 인덱스를 활용하기 어려워 전체 파일을 스캔(Linear Scan)해야 함 - 이 때문에 성능 저하의 원인이 될 수 있음

## 관련 글

- [[blog/DATABASE DESIGN/index|DATABASE DESIGN]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 쿼리 처리(Query Processing) - 비용 측정부터 선택 연산(A1-A3)|[데이터베이스 설계] 쿼리 처리(Query Processing) -  비용 측정부터 선택 연산(A1-A3)]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 쿼리 처리(Query Processiong) - 정렬(Sorting)과 조인(Join)|[데이터베이스 설계] 쿼리 처리(Query Processiong) - 정렬(Sorting)과 조인(Join)]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 함수 종속성 이론과 스키마 분해|[데이터베이스 설계]  함수 종속성 이론과 스키마 분해]]
