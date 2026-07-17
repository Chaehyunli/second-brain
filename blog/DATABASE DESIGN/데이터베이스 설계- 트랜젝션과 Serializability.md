---
title: "[데이터베이스 설계] 트랜젝션과 Serializability"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "Database", "Design"]
category: "DATABASE DESIGN"
published: 2025-11-05
source_url: https://ch010104.tistory.com/181
---

# [데이터베이스 설계] 트랜젝션과 Serializability

## 원문

https://ch010104.tistory.com/181

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

기본 가정: 각 트랜잭션은 데이터베이스의 일관성(consistency)을 보존함

따라서, 트랜잭션 집합을 직렬적으로(순차적으로) 실행하면 데이터베이스 일관성이 보존됨

## 원문 기반 개념 정리

### 1. Serializability (직렬 가능성)

기본 가정: 각 트랜잭션은 데이터베이스의 일관성(consistency)을 보존함

따라서, 트랜잭션 집합을 직렬적으로(순차적으로) 실행하면 데이터베이스 일관성이 보존됨

직렬 가능 스케줄(Serializable Schedule): (동시 실행될 수 있는) 어떤 스케줄이 직렬 스케줄(serial schedule)과 동일한 결과를 가질 때

스케줄 동등성(equivalence)의 형태에 따라 다음 개념들이 발생함:

충돌 직렬 가능성 (Conflict Serializability)

뷰 직렬 가능성 (View Serializability)

### 2. Conflicting Instructions (충돌 명령어)

트랜잭션 T_i의 명령어 I_i와 T_j의 명령어 I_j가 충돌하는 경우는 다음과 같음:

두 명령어가 동일한 데이터 항목 Q에 접근하고

적어도 하나의 명령어가 Q에 쓰는(write) 연산을 할 때.

충돌하지 않는 경우: I_i = \text{read}(Q)와 I_j = \text{read}(Q)

충돌하는 경우:

I_i = \text{read}(Q), I_j = \text{write}(Q)

I_i = \text{write}(Q), $I_j = \text{read}(Q)

I_i = \text{write}(Q)$, $I_j = \text{write}(Q)

충돌은 명령어들 사이에 논리적인 시간 순서를 강제함

충돌하지 않는 명령어들은 스케줄에서 순서를 바꾸어도 결과가 같음

### 3. Conflict Serializability (충돌 직렬 가능성)

충돌 동등(Conflict Equivalent): 스케줄 S가 충돌하지 않는 명령어들의 일련의 교환(swaps)을 통해 스케줄 S'로 변환될 수 있을 때

충돌 직렬 가능(Conflict Serializable): 스케줄 S가 직렬 스케줄과 충돌 동등할 때

예시: Schedule 3은 충돌하지 않는 명령어들의 교환을 통해 T_1 다음에 $T_2$가 오는 직렬 스케줄인 Schedule 6으로 변환 가능하므로 충돌 직렬 가능함

충돌 직렬 가능하지 않은 예시: T_3의 \text{read}(Q)와 T_4의 \text{write}(Q)가 충돌하고, 이어서 T_3의 \text{write}(Q)와 T_4의 \text{write}(Q)가 충돌 관계이므로, T_3 \to T_4 또는 T_4 \to T_3 직렬 스케줄로 명령어 순서를 바꿀 수 없음

### 4. View Serializability (뷰 직렬 가능성)

뷰 동등(View Equivalent): 두 스케줄 S와 S'가 다음 세 가지 조건을 만족할 때:

T_i가 Q의 초기 값을 읽으면, S'에서도 T_i는 Q의 초기 값을 읽어야 함.

T_i의 \text{read}(Q) 값이 T_j의 \text{write}(Q)에 의해 생성된 것이라면, S'에서도 동일한 T_j$의 \text{write}(Q)로부터 읽어야 함

S에서 Q에 대한 최종 \text{write}(Q) 연산을 수행한 트랜잭션이 S'에서도 최종 \text{write}(Q)를 수행해야 함.

뷰 직렬 가능(View Serializable): 스케줄 S가 직렬 스케줄과 뷰 동등할 때

관계: 모든 충돌 직렬 가능 스케줄은 뷰 직렬 가능함

특징: 충돌 직렬 가능하지 않으면서 뷰 직렬 가능한 모든 스케줄은 블라인드 쓰기(blind writes)를 포함함.

### 5. Testing for Serializability (직렬 가능성 테스트)

선행 그래프(Precedence Graph):

꼭짓점(vertices)은 트랜잭션 이름들임 (T_1, T_2, \dots, T_n)

두 트랜잭션 T_i와 T_j가 충돌하고 T_i가 충돌을 발생시킨 데이터 항목에 먼저 접근했을 경우, T_i에서 T_j로 호(arc)를 그림

충돌 직렬 가능성 테스트:

스케줄은 선행 그래프가 비순환적(acyclic)일 때만 충돌 직렬 가능함.

그래프가 비순환적이면, 직렬화 순서(serializability order)는 그래프의 위상 정렬(topological sorting)을 통해 얻을 수 있음.

뷰 직렬 가능성 테스트:

선행 그래프 테스트를 직접 사용할 수 없음

뷰 직렬 가능성을 확인하는 문제는 NP-완전(NP-complete) 문제에 속함

실제로는 충분 조건만 확인하는 실용적인 알고리즘을 사용함

### 6. Recoverable Schedules (회복 가능한 스케줄)

회복 가능 스케줄(Recoverable Schedule): 트랜잭션 T_j가 T_i가 이전에 쓴 데이터 항목을 읽을 경우, T_i의 커밋 연산이 T_j의 커밋 연산보다 먼저 나타나야 함

파란 글씨 필기: 트랜잭션이 실행 중 오류가 나면 롤백(rollback)해야 하므로, 회복 가능한 스케줄인지 판단하는 것이 중요함

T_9가 T_8이 쓴 A를 \text{read}하고 T_8보다 먼저 \text{commit}하는 경우, T_8이 \text{abort}하면 T_9는 일관되지 않은 상태를 읽게 되므로 회복 가능하지 않음

### 7. Cascadeless Schedules (연쇄 없는 스케줄)

연쇄적인 롤백(Cascading Rollbacks): 하나의 트랜잭션 실패가 일련의 트랜잭션 롤백을 유발하는 현상.

예시: T_{10}이 \text{write}(A)하고, T_{11}이 \text{read}(A)하고 \text{write}(A), T_{12}가 \text{read}(A)한 상황에서 T_{10}이 \text{abort}하면 T_{11}과 T_{12}도 모두 롤백되어야 함

연쇄적인 롤백은 많은 작업을 되돌려야 하므로 피하는 것이 좋음.

연쇄 없는 스케줄(Cascadeless Schedules): 연쇄적인 롤백이 발생할 수 없는 스케줄.

T_j가 T_i가 이전에 쓴 데이터 항목을 읽을 경우, T_i의 커밋 연산이 T_j의 읽기(read) 연산보다 먼저 나타나야 함

파란 글씨 필기: 다른 트랜잭션에서 아직 커밋되지 않은 데이터를 \text{READ}하는 것을 명시적으로 금지하는 규칙

모든 연쇄 없는 스케줄은 회복 가능함 (Every Cascadeless schedule is also recoverable)

### 8. Concurrency Control (동시성 제어)

목표: 데이터베이스 시스템은 모든 가능한 스케줄이 충돌 또는 뷰 직렬 가능해야 하며, 회복 가능하고 가급적 연쇄 없는(cascadeless) 스케줄임을 보장해야 함

동시성 제어 프로토콜: 직렬 가능하지 않은 스케줄을 방지하는 규율을 부과하여 직렬 가능성을 보장하는 메커니즘

성능과의 상충 관계(Tradeoff): 허용하는 동시성 정도와 발생하는 오버헤드 사이의 균형을 맞춤.

직렬 가능성 테스트는 동시성 제어 프로토콜이 올바른 이유를 이해하는 데 도움을 줌

### 9. Weak Levels of Consistency (낮은 수준의 일관성)

- 일부 응용 프로그램은 성능을 위해 직렬 가능하지 않은 낮은 수준의 일관성을 허용할 수 있음.

예시: 모든 계좌의 대략적인 총 잔액을 알고 싶어 하는 읽기 전용 트랜잭션.

예시: 쿼리 최적화를 위해 계산되는 대략적인 데이터베이스 통계.

SQL-92의 일관성 수준 (Isolation Levels)(높은 수준$\to$ 낮은 수준):

Serializable (직렬 가능):

필수(default).

항상 직렬 가능한 결과 보장

Dirty Read, Nonrepeatable Read, Phantom Read 모두 불가능

Repeatable Read (반복 가능 읽기):

Commit된 레코드만 읽음

동일한 레코드를 반복적으로 읽어도 같은 값을 반환하도록 보장

직렬 가능하지 않은 스케줄 발생 가능

Dirty Read, Nonrepeatable Read 불가능

Phantom Read 문제 발생 가능 (새로운 레코드(tuple)가 추가될 수 있음).

Read Committed (커밋된 읽기):

Commit된 레코드만 읽을 수 있음

Dirty Read 불가능

Nonrepeatable Read 가능 (연속적인 $\text{read}$가 다른 (커밋된) 값을 반환할 수 있음)

Phantom Read 가능

Read Uncommitted (커밋되지 않은 읽기):

Commit되지 않은 레코드까지 읽을 수 있음

Dirty Read 가능.

Nonrepeatable Read, Phantom Read 가능

가장 낮은 수준의 일관성

### 10. Transaction Definition in SQL (SQL에서의 트랜잭션 정의)

트랜잭션 시작: SQL에서 암시적으로 시작됨

트랜잭션 종료:

COMMIT WORK: 현재 트랜잭션을 커밋하고 새로운 트랜잭션을 시작함

ROLLBACK WORK: 현재 트랜잭션을 중단(abort)시킴.

대부분의 DBMS에서 기본적으로 모든 SQL 문이 성공적으로 실행되면 암시적으로 커밋(implicit commit)됨

connection.setAutoCommit(false)와 같은 지시어로 암시적 커밋을 끌 수 있음

격리 수준 설정:

데이터베이스 수준에서 설정할 수 있음.

트랜잭션 시작 시 변경 가능함

예시: SET TRANSACTION ISOLATION LEVEL SERIALIZABLE.

## 관련 글

- [[blog/DATABASE DESIGN/index|DATABASE DESIGN]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 비용 추정을 위한 통계 2 (MATERIALIZED VIEWS)|[데이터베이스 설계] 비용 추정을 위한 통계 2 (MATERIALIZED VIEWS)]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 비용 추정을 위한 통계 1 (STATISTICS FOR COST ESTIMATION)|[데이터베이스 설계] 비용 추정을 위한 통계 1 (STATISTICS FOR COST ESTIMATION)]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 쿼리 최적화 (Query Optimization)|[데이터베이스 설계] 쿼리 최적화 (Query Optimization)]]
