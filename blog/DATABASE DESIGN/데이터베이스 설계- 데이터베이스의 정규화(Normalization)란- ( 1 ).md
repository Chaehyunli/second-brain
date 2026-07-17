---
title: "[데이터베이스 설계] 데이터베이스의 정규화(Normalization)란? ( 1 )"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "Database", "Design"]
category: "DATABASE DESIGN"
published: 2025-09-15
source_url: https://ch010104.tistory.com/126
---

# [데이터베이스 설계] 데이터베이스의 정규화(Normalization)란? ( 1 )

## 원문

https://ch010104.tistory.com/126

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

목표: 불필요한 중복(redundancy) 없이 필요한 정보를 모두 표현(저장)할 수 있는 Schema

핵심 질문: 어떤 attribute들을 갖는 어떤 table을 둘 것인가?

## 원문 기반 개념 정리

### 1. 기본 개념 (Basic Concepts)

데이터베이스 설계의 목표

목표: 불필요한 중복(redundancy) 없이 필요한 정보를 모두 표현(저장)할 수 있는 Schema

핵심 질문: 어떤 attribute들을 갖는 어떤 table을 둘 것인가?

스키마 정의

R = (A B C D E) ← single relation schema 정의

DB1 = {R1, ..., Rn} ← DB schema 정의 (set of relation schemas)

설계 문제점

동일한 문제에 대해서 여러 가지 디자인이 가능함

어떤 것이 더 좋은 디자인인가? 왜 더 좋은 디자인인가?

### 2. 스키마 결합의 문제점

예시: instructor와 department 결합

instructor와 department를 inst_dept로 결합할 경우:

문제점:

정보의 반복 (Repetition of information)

예산 업데이트 문제 (updating budget)

새 부서 생성 문제 (creating new departments)

### 3. 분해(Decomposition)와 함수 종속성

분해가 필요한 이유

부서별 정보가 중복되어 저장되므로 다음과 같은 문제 발생:

dept_name이 후보키가 아니므로 building과 budget이 반복됨

함수 종속성: dept_name → building, budget

함수 종속성 (Functional Dependencies)

정의: α → β는 "α가 정해지면 반드시 β가 정해진다"

α 값이 같은데 β 값이 다를 수는 없다

실제 application의 규칙에 의하여 정해짐

예시:

학번 → 이름 (가능)

이름 → 학번 (불가능)

주민등록번호 → 학번 (가능)

### 4. 잘못된 분해의 예

Lossy Decomposition

employee(ID, name, street, city, salary)를 다음과 같이 분해:

employee1(ID, name)

employee2(name, street, city, salary)

문제점: 동명이인이 있을 경우 정확한 정보 복원 불가능

예시

분해 후 natural join하면 원래 없던 조합이 생성됨 → "lossy decomposition"

### 5. 이상 현상 (Anomaly)

Codd가 정의한 이상 현상들

삽입 이상 (Insertion anomaly): loan-number 없이 branch-name 등 insert 불가

삭제 이상 (Deletion anomaly): 어떤 branch의 마지막 loan을 delete하면 branch 자체가 사라짐

갱신 이상 (Update anomaly): 하나의 정보(예: assets)를 update했으면 다른 것들도 함께 업데이트해야만 함

이상 현상의 원인

정보의 중복(Redundancy)

여러 entity가 하나의 table에 합쳐짐

해결책

Decomposition! - 테이블을 적절히 분해하여 중복을 제거

### 6. 정규화 (Normalization)

정규화의 정의

관계형 데이터베이스의 설계에서 중복을 최소화하게 데이터를 구조화하는 프로세스

정규화의 목표

generate a set of relation schemas that allows us to store information without unnecessary redundancy

yet also allows us to retrieve information easily

design schemas that are in an appropriate normal form

정규형의 계층 구조

1NF ⊃ 2NF ⊃ 3NF ⊃ BCNF ⊃ 4NF

### 7. 제1정규형 (First Normal Form, 1NF)

원자성 (Atomic) 조건

Domain이 atomic하려면 그 원소들이 분할 불가능한 단위여야 함

비원자적 도메인의 예

이름들의 집합

복합 속성 (예: 주소 = 거리, 도시, 주, 우편번호)

분해 가능한 식별번호 (예: "CS101", "EE1127")

1NF 정의

관계 스키마가 제1정규형에 있다 ⟺ 모든 속성의 도메인이 원자적

1NF 위반 예시

곡명 속성이 여러 값을 가지므로 1NF 위반

### 8. 분해 (Decomposition) 기본 개념

분해의 정의

R을 관계 스키마라고 하자

{R1, ..., Rn}이 R의 분해라는 것은 R = R1 ∪ ... ∪ Rn

주로 이진 분해를 다룸: R을 {R1, R2}로 분해 (R = R1 ∪ R2)

무손실 조인 분해 (Lossless-Join Decomposition)

정의: 분해 {R1, R2}가 무손실 조인 분해 ⟺ r = ΠR1(r) ⋈ ΠR2(r)

원본 관계를 완전히 복원할 수 있는 분해

무손실 조인 분해 예시

R = (A, B, C)를 R1 = (A, B), R2 = (B, C)로 분해:

원본:

분해 후 조인하면 원본과 동일하게 복원됨 → 무손실 조인 분해

### 9. 함수 종속성 상세

함수 종속성의 정의

R을 관계 스키마, α ⊆ R, β ⊆ R이라 하자.

함수 종속성 α → β가 R에서 성립 ⟺ 모든 합법적 관계 r(R)에서 두 튜플 t1, t2가 α에서 일치하면 β에서도 일치

수식: t1[α] = t2[α] ⇒ t1[β] = t2[β]

함수 종속성과 키의 관계

K가 superkey ⟺ K → R

K가 candidate key ⟺ K → R이고, K의 진부분집합 α에 대해 α → R이 성립하지 않음

함수 종속성 예시

inst_dept(ID, name, salary, dept_name, building, budget)에서:

dept_name → building, budget (기대되는 종속성)

ID → name, salary, dept_name (기대되는 종속성)

dept_name → salary (기대되지 않는 종속성)

## 관련 글

- [[blog/DATABASE DESIGN/index|DATABASE DESIGN]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- E-R 모델(관계 표현과 스키마 변환)|[데이터베이스 설계] E-R 모델(관계 표현과 스키마 변환)]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 데이터베이스의 정규화(Normalization)란- ( 2 ) - BCNF 와 3NF|[데이터베이스 설계] 데이터베이스의 정규화(Normalization)란? ( 2 ) - BCNF 와 3NF]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- ER 다이어그램이란|[데이터베이스 설계] ER 다이어그램이란?]]
