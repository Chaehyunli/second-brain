---
title: "[데이터베이스 설계] 쿼리 최적화 (Query Optimization)"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "Database", "Design"]
category: "DATABASE DESIGN"
published: 2025-10-20
source_url: https://ch010104.tistory.com/165
---

# [데이터베이스 설계] 쿼리 최적화 (Query Optimization)

## 원문

https://ch010104.tistory.com/165

## 노트 유형

`guide`

## 적용 목적과 전제조건

- 주어진 쿼리를 처리하는 데 가장 효율적인 **쿼리-평가 계획(query-evaluation plan)**을 선택하는 프로세스

목표: 동일한 결과를 생성하는 여러 전략 중 비용(cost)이 가장 적은 계획을 찾는 것

## 구현 절차·검증·주의점

### 쿼리 최적화 (Query Optimization) 개요

- 주어진 쿼리를 처리하는 데 가장 효율적인 **쿼리-평가 계획(query-evaluation plan)**을 선택하는 프로세스

목표: 동일한 결과를 생성하는 여러 전략 중 비용(cost)이 가장 적은 계획을 찾는 것

중요성: 최적화 여부에 따라 쿼리 수행 시간이 며칠에서 몇 초로 단축될 수 있음

두 가지 최적화 측면:

관계 대수 수준: 더 효율적인 동등한(equivalent) 표현식 찾기

전략적 수준: 연산(operation) 수행을 위한 구체적인 알고리즘 (예: Hash Join, Merge Join) 및 인덱스(index) 사용 여부 결정

### 비용 기반 최적화 (Cost-Based Optimization) 단계

- 옵티마이저는 비용 추정(cost estimation)을 기반으로 최적의 계획을 선택

동등한 표현식 생성: 동등 규칙(equivalence rules)을 사용하여 논리적으로 동일한 여러 표현식을 생성

대안적 계획 생성: 생성된 표현식에 구체적인 알고리즘 및 인덱스 사용법을 주석(annotate)으로 달아 여러 실행 계획을 도출

최저 비용 계획 선택: 추정된 비용을 기반으로 가장 저렴한 계획을 선택

- 비용 추정은 릴레이션의 튜플 수, 속성별 고유값 수 등 **통계 정보(statistical information)**를 기반으로 이루어짐

### 관계 표현식 변환 (Transformation of Relational Expressions)

효율적인 계획을 찾기 위해 **동등 규칙(Equivalence Rules)**을 사용하여 쿼리 표현식을 변환

동등한 표현식: 모든 합법적인 데이터베이스 인스턴스에 대해 동일한 튜플 집합을 생성하는 두 표현식13.

주요 동등 규칙:

### 핵심 최적화 전략 및 쿼리 예시

1. Selection 일찍 수행하기 (Pushing Selections)

가장 기본적이고 중요한 최적화로, 조인(Join) 전에 선택(Selection)을 먼저 수행하여 처리할 튜플 수를 줄임

쿼리 예시: 'Music' 학과 강사의 이름과 그들이 가르치는 과목명 검색.

초기 표현식 (Initial Expression):

$\Pi_{name, title}(\sigma_{dept\_name = \text{"Music"}}(\text{instructor} \bowtie (\text{teaches} \bowtie \Pi_{course\_id, title}(\text{course}))))$

문제점: instructor와 teaches $\bowtie$ course의 전체 조인을 수행한 후, 'Music' 학과를 필터링.

최적화 (Rule 7a 적용):

$\sigma_{dept\_name = \text{"Music"}}$ 조건은 instructor 테이블의 속성만 사용하므로 23, 조인 전에 instructor 테이블로 이동

변환된 표현식 (Transformed Expression):

$\Pi_{name, title}((\sigma_{dept\_name = \text{"Music"}}(\text{instructor})) \bowtie (\text{teaches} \bowtie \Pi_{course\_id, title}(\text{course})))$

이점: 'Music' 학과 강사(소수)만 먼저 추출하여 조인 비용을 크게 줄임

다중 변환 예시

2009년에 강의한 'Music' 학과 강사 쿼리 27: $\sigma_{dept\_name = \text{"Music"} \land year=2009}$

$\sigma$ 조건을 분리(Rule 1, 7b)하여 $\sigma_{dept_name = \text{"Music"}}$는 instructor로, $\sigma_{year = 2009}$는 teaches로 이동시켜 각각 조인 전에 수행

2. Projection 일찍 수행하기 (Pushing Projections)

조인 과정에서 불필요한 속성(attribute)을 미리 제거하여 중간 결과(intermediate results)의 크기(width)를 줄임

쿼리 예시: (위의 쿼리 계속)

문제 상황: $(\sigma_{...}(\text{instructor}) \bowtie \text{teaches})$ 연산의 중간 결과는 ID, salary, sec_id, semester 등 최종 결과($\Pi_{name, title}$)에 필요 없는 많은 속성을 포함

최적화 (Rule 8b 적용):

최종 결과 $\Pi_{name, title}$에 필요한 속성은 name과 title

중간 조인에 필요한 속성은 course_id (조인 키)

따라서 instructor에서는 name, course_id만, course에서는 title, course_id만 미리 프로젝션함.

변환된 표현식:

$\Pi_{name, title}( (\Pi_{name, course\_id}(\sigma_{...}(\text{instructor})) \bowtie \Pi_{course\_id}(\text{teaches})) \bowtie \Pi_{course\_id, title}(\text{course}) )$

3. 조인 순서 최적화 (Join Ordering)

조인은 결합 법칙(Rule 6a)이 성립하므로, 중간 결과의 크기가 가장 작게 생성되는 순서로 조인 순서를 결정

쿼리 예시: $r_1 \bowtie r_2 \bowtie r_3$

휴리스틱: 만약 $r_1$이 매우 작고 $(r_2 \bowtie r_3)$이 매우 크다면, $(r_1 \bowtie r_2) \bowtie r_3$ 순서로 계산하여 임시 릴레이션의 크기를 작게 유지

적용 예시:

$(\sigma_{dept\_name= \text{“Music”}}(\text{instructor}))$ $\bowtie$ $\text{teaches}$ $\bowtie$ $\Pi_{course\_id, title}(\text{course})$

나쁜 계획: $(\text{teaches} \bowtie \Pi_{...}(\text{course}))$를 먼저 수행. (결과가 매우 큼)

좋은 계획: $\sigma_{...}(\text{instructor})$의 결과가 매우 작을 것이므로 , $(\sigma_{...}(\text{instructor}) \bowtie \text{teaches})$를 먼저 수행

### 평가 계획 생성 및 선택

평가 계획 (Evaluation Plan): 쿼리 트리의 각 연산에 사용할 정확한 알고리즘 (예: merge join , hash join, index 1 사용)과 실행 방법을 명시한 상세 계획

계획 생성의 복잡성:

옵티마이저는 동등 규칙을 적용해 가능한 모든 표현식을 체계적으로 생성

이 과정은 시간과 공간 복잡도가 매우 높음 (NP-hard)

최적화 기법:

Dynamic Programming: 하위 쿼리(subset)의 최적 계획을 한 번만 계산하고 그 비용과 계획을 저장(memorization)한 뒤, 더 큰 쿼리 계획 시 재사용하여 시간 단축

공통 하위 표현식 공유: 동일한 하위 표현식(subtree)을 포인터로 공유하여 메모리 공간 절약

## 관련 글

- [[blog/DATABASE DESIGN/index|DATABASE DESIGN]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 비용 추정을 위한 통계 1 (STATISTICS FOR COST ESTIMATION)|[데이터베이스 설계] 비용 추정을 위한 통계 1 (STATISTICS FOR COST ESTIMATION)]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 비용 추정을 위한 통계 2 (MATERIALIZED VIEWS)|[데이터베이스 설계] 비용 추정을 위한 통계 2 (MATERIALIZED VIEWS)]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 쿼리 처리(Query Processiong) - 정렬(Sorting)과 조인(Join)|[데이터베이스 설계] 쿼리 처리(Query Processiong) - 정렬(Sorting)과 조인(Join)]]
