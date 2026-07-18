---
title: "[데이터베이스 설계] 비용 추정을 위한 통계 2 (MATERIALIZED VIEWS)"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "Database", "Design"]
category: "DATABASE DESIGN"
published: 2025-10-29
source_url: https://ch010104.tistory.com/174
---

# [데이터베이스 설계] 비용 추정을 위한 통계 2 (MATERIALIZED VIEWS)

## 원문

https://ch010104.tistory.com/174

## 노트 유형

`guide`

## 적용 목적과 전제조건

비용 추정 예시를 위한 student 및 takes 테이블의 카탈로그 정보:

f_{student} (student 블로킹 팩터): 50 (블록 당 50개 튜플)

## 구현 절차·검증·주의점

### 조인 연산 예시

비용 추정 예시를 위한 student 및 takes 테이블의 카탈로그 정보:

n_{student} (student 튜플 수): 5,000

f_{student} (student 블로킹 팩터): 50 (블록 당 50개 튜플)

b_{student} (student 블록 수): 100 (5000 / 50)

n_{takes} (takes 튜플 수): 10,000

f_{takes} (takes 블로킹 팩터): 25

b_{takes} (takes 블록 수): 400 (10000 / 25)

V(ID, student) (student의 ID(PK) 고유값 수): 5,000

V(ID, takes) (takes의 ID(FK) 고유값 수): 2,500

takes의 ID는 student를 참조하는 외래 키(Foreign Key)

V(ID, takes) 수치를 통해 평균적으로 학생 1명이 4개의 강좌를 수강함을 추정 (10000 / 2500)

### 조인 크기 추정

Cartesian Product (r x s): n_r * n_s 개의 튜플을 포함

키(Key)를 이용한 추정:

만약 조인 속성이 S에서는 외래 키이고 R을 참조하는 경우 (R ∩ S가 S의 FK), 조인 결과(r \bowtie s)는 정확히 n_s 개의 튜플을 가짐

예시: student \bowtie takes에서 takes.ID는 student를 참조하는 FK 13, 따라서 결과 튜플 수는 n_{takes}인 10,000개

만약 조인 속성이 R의 키(Key)인 경우, 조인 결과는 최대 $n_s$ 개의 튜플을 가짐

키가 아닌 경우의 추정: (R ∩ S = {A}가 키가 아닐 때)

추정 1 (r \bowtie s): \frac{n_r * n_s}{V(A, s)} (s의 A 속성 고유값 수로 나눔)

추정 2 (s \bowtie r): \frac{n_r * n_s}{V(A, r)} (r의 A 속성 고유값 수로 나눔)

두 추정치는 다를 수 있으며, 이 중 더 낮은 추정치를 선택하는 것이 일반적으로 더 정확

예시 (외래 키 정보 없이 추정):

V(ID, takes) = 2500$, $V(ID, student) = 5000

추정 1 (T join S 관점): (5000 * 10000) / 2500 = 20,000

추정 2 (S join T 관점): (10000 * 5000) / 5000 = 10,000

더 낮은 추정치인 10,000을 선택

### 기타 연산 크기 추정

Projection \prod_A(r): 추정 크기 = V(A, r) (A의 고유값 수)

Aggregation _{A}g_{F}(r): 추정 크기 = V(A, r)

Set Operations (다른 릴레이션 간):

r \cup s: size(r) + size(s)

r \cap s: min(size(r), size(s))

r - s: size(r)

(이 추정치들은 부정확할 수 있으나 결과의 상한선을 제공)

Outer Join Operations:

Left Outer (r \text{ ⟕ } s): size(r \bowtie s) + size(r)

Full Outer (r \text{ ⟗ } s): size(r \bowtie s) + size(r) + size(s)

### 📈 실행 계획 선택

비용 기반 최적화

실행 계획(Evaluation Plan): 각 연산에 사용할 알고리즘과 연산 실행 순서를 정의

비용 기반 최적화기(Cost-based Optimizer): 동일한 결과를 내는 실행 계획 공간을 탐색하여 추정 비용이 가장 낮은 계획을 선택

복잡한 쿼리의 경우 모든 계획을 탐색하는 비용이 매우 클 수 있음

대부분의 최적화기는 최적의 계획을 찾지 못할 위험을 감수하고, 최적화 비용을 줄이기 위해 휴리스틱(Heuristics)을 사용

조인 순서 선택의 복잡성:

n개의 릴레이션 조인(r_1 \bowtie ... \bowtie r_n) 시, 가능한 조인 순서의 수는 \frac{(2(n-1))!}{(n-1)!}

n=7일 때 약 66만 개, n=10일 때 1760억 개 이상

n=3일 때 12가지 순서 존재

동적 프로그래밍(Dynamic Programming)을 사용하여 모든 순서를 생성하지 않고 최적의 조인 순서를 찾음

동적 프로그래밍

개념 (피보나치 예시):

단순 재귀(O(2^n))는 fibonacci(3) 등 동일한 계산을 반복

메모이제이션(Memoization): 계산된 값을 저장(memo[n])하고 재사용하여 중복 계산을 제거

조인 순서 최적화 적용:

n개 릴레이션 집합 S의 최적 계획을 찾기 위해, S의 모든 부분집합 S_1에 대해 S_1 \bowtie (S - S_1) 형태의 계획을 고려

기저 사례(Base case): 단일 릴레이션 접근 계획 (예: 인덱스를 사용한 selection)

어떤 부분집합 S의 최적 계획이 계산되면, 이를 저장(memoization)하고 향후 재사용하여 재계산을 방지

알고리즘 (FindBestPlan(S)):

bestplan[S]가 이미 계산되었으면 즉시 반환 (메모이제이션)

S가 단일 릴레이션이면, 최적의 접근 계획(인덱스 사용 등)을 계산하여 저장

S의 모든 부분집합 S1에 대해 P1 = FindBestPlan(S1)과 P2 = FindBestPlan(S - S1)을 재귀적으로 호출

P1과 P2의 결과를 조인하는 최적의 알고리즘 A를 선택

총 비용 (P1.cost + P2.cost + cost(A))을 계산

이 비용이 bestplan[S].cost보다 작으면, bestplan[S]를 갱신

휴리스틱 최적화

비용 기반 최적화는 DP를 사용해도 여전히 비쌈

시스템은 휴리스틱(규칙)을 사용하여 비용 기반으로 탐색할 선택지를 줄임

주요 휴리스틱 규칙:

Selection을 가능한 한 빨리 수행 (튜플 수 감소)

Projection을 가능한 한 빨리 수행 (속성 수 감소)

가장 제한적인(결과 크기가 가장 작은) Selection 및 Join을 먼저 수행

일부 시스템은 휴리스틱만 사용하거나, 휴리스틱과 비용 기반 최적화를 결합하여 사용

최적화기 구조

Left-Deep Join Trees:

많은 최적화기는 Left-Deep Join Tree 형태의 조인 순서만을 고려

Left-Deep Tree는 조인 시 오른쪽 입력이 항상 기본 릴레이션인 트리

이 방식은 최적화 복잡도를 줄이고, 파이프라인 처리에 유리한 계획을 생성

중첩 부질의 (Nested Subqueries):

복잡한 중첩 부질의의 최적화는 매우 어려움

Decorrelation: 중첩 쿼리를 조인(Join)과 임시 릴레이션을 사용하는 쿼리로 대체하는 과정

예: EXISTS를 사용한 중첩 쿼리를 CREATE TABLE (임시 테이블)과 조인을 사용한 쿼리로 변경

최적화기가 효율적으로 변환하지 못할 수 있으므로 가능하면 복잡한 중첩 쿼리는 피하는 것이 좋음

최적화 오버헤드:

비용 기반 최적화는 오버헤드가 크지만, 비싼 쿼리(expensive queries)에 대해서는 그만한 가치가 있음

쿼리는 한 번 최적화된 후, 생성된 실행 계획은 매번 재사용될 수 있음

최적화기는 간단한 쿼리에는 단순 휴리스틱을, 비싼 쿼리에는 비용 기반의 탐색을 수행

물리적 동등성 규칙(Physical Equivalence Rules):

논리적 계획을 물리적 계획(실제 알고리즘 명시)으로 변환

예: Join -> Hash Join, Nested-Loop Join 등

효율적인 최적화는 부분 표현식 공유, 메모이제이션 기반 DP, 비용 기반 가지치기(pruning)등에 의존

### 🗃️ 구체화된 뷰 (MATERIALIZED VIEWS)

정의: 뷰의 내용을 미리 계산하여 저장해 놓은 뷰

예시: 부서별 급여 총합(department_total_salary) 뷰

장점: 자주 요청되는 쿼리(예: 부서별 총급여)의 성능을 향상 (매번 집계할 필요 없음)

단점: 원본 데이터가 변경되면 저장된 뷰도 업데이트해야 함

뷰 유지보수(View Maintenance):

뷰를 기본 데이터와 일치시키는 작업

방법 1: 매 업데이트마다 뷰 전체를 재계산(Recomputation)

방법 2: 증분 뷰 유지보수(Incremental View Maintenance)

데이터베이스 관계의 변경분(changes)만을 사용하여 뷰의 변경분을 계산하고 업데이트

수동 트리거(Triggers)나 코드를 통해서도 유지보수 가능

유지보수 시점:

즉시(Immediate): 업데이트 트랜잭션의 일부로 즉시 수행

지연(Deferred): 나중으로 유지보수를 연기

증분 유지보수 기법

Differential (차등): 릴레이션에 대한 변경(삽입/삭제)

i_r: r에 삽입된 튜플 집합

d_r: r에서 삭제된 튜플 집합

Update는 Delete 후 Insert로 처리

Join (v = r \bowtie s):

r에 삽입(i_r) 발생 시: v^{new} = v^{old} \cup (i_r \bowtie s)(새로 삽입된 튜플과 s의 조인 결과만 기존 뷰에 추가)

r에서 삭제(d_r) 발생 시: v^{new} = v^{old} - (d_r \bowtie s)

Selection (v = \sigma_{\theta}(r)):

삽입 시: v^{new} = v^{old} \cup \sigma_{\theta}(i_r)

삭제 시: v^{new} = v^{old} - \sigma_{\theta}(d_r)

Projection (v = \prod_A(r)):

Projection은 더 복잡

문제점: r = {(a, 2), (a, 3)}일 때 \prod_A(r) = \{(a)\}97. 여기서 (a, 2)가 삭제되어도 (a)는 뷰에서 삭제되면 안 됨

해결책: Count 유지

뷰의 각 튜플마다 파생 횟수(count)를 유지

삽입 시: Count 1 증가 (새 튜플이면 Count=1로 추가)

삭제 시: Count 1 감소

Count가 0이 되면 뷰에서 해당 튜플 삭제

Aggregation (Count, Sum):

COUNT: 삽입/삭제 시 해당 그룹의 Count를 1씩 증감. Count가 0이 되면 그룹 삭제

SUM: Count와 유사하게 B 값을 더하거나 뺌

SUM의 경우, 튜플이 0개인 그룹(count=0)과 튜플의 합이 0인 그룹(sum=0)을 구별하기 위해 별도의 Count를 함께 유지해야 함

Aggregation (Avg, Min/Max):

AVG: Sum과 Count를 별도로 유지하고 마지막에 나눔

MIN, MAX: 삽입은 간단

MIN/MAX 값 삭제 시: 해당 그룹의 다른 모든 튜플을 다시 확인하여 새로운 MIN/MAX를 찾아야 하므로 비용이 비쌈

Set Operations ($v = r \cap s$):

r에 삽입 시: 삽입된 튜플이 s에도 존재하면 v에 추가

r에서 삭제 시: 삭제된 튜플이 v에 존재하면 v에서 제거

최적화와 뷰 선택

쿼리 재작성 (Query Rewriting):

옵티마이저는 쿼리를 실행할 때 구체화된 뷰를 사용할 수 있음

예: 뷰 v = r \bowtie s가 있을 때, r \bowtie s \bowtie t 쿼리는 v \bowtie t로 재작성 가능

뷰 대체 (Replacing View):

반대로, 구체화된 뷰를 사용하는 것이 항상 최선은 아님

예: 뷰 v = r \bowtie s (인덱스 없음)에 대해 \sigma_{A=10}(v) 쿼리 실행 시

만약 r 테이블이 A 속성에 인덱스를 가지고 있다면, 뷰 v를 사용하지 않고 v의 정의(definition)로 대체하여 \sigma_{A=10}(r) \bowtie s (인덱스 사용)로 실행하는 것이 더 빠를 수 있음

최적화기는 이러한 모든 대안을 고려하여 최적의 계획을 선택해야 함

뷰 선택 (View Selection):

"어떤 뷰를 구체화하는 것이 최적인가?"

이는 "어떤 인덱스를 생성하는 것이 최적인가?"(인덱스 선택) 문제와 유사

데이터베이스 튜닝(Tuning)의 일부

시스템의 일반적인 워크로드(queries and updates)를 기반으로 결정

목표: 공간 및 시간 제약 하에 워크로드 실행 시간을 최소화

상용 시스템은 DBA를 돕는 "튜닝 어시스턴트(Tuning Assistants)" 도구를 제공

## 관련 글

- [[blog/DATABASE DESIGN/index|DATABASE DESIGN]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 비용 추정을 위한 통계 1 (STATISTICS FOR COST ESTIMATION)|[데이터베이스 설계] 비용 추정을 위한 통계 1 (STATISTICS FOR COST ESTIMATION)]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 트랜젝션과 Serializability|[데이터베이스 설계] 트랜젝션과 Serializability]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 쿼리 최적화 (Query Optimization)|[데이터베이스 설계] 쿼리 최적화 (Query Optimization)]]
