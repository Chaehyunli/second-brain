---
title: "[STUDYING] 9 - 1. 스마트 데이터 이해 및 활용_Day1_핵심 정리"
created: 2026-07-27
updated: 2026-07-27
type: blog-post
tags: ["blog", "technical-writing"]
category: "STUDYING"
published: 2026-07-27
source_url: https://ch010104.tistory.com/321
---
# [STUDYING] 9 - 1. 스마트 데이터 이해 및 활용_Day1_핵심 정리

## 원문

https://ch010104.tistory.com/321

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

여러 사람과 프로그램이 함께 접근할 수 있도록, 구조화된 형태로 저장하고 관리하는 데이터의 모음을 의미함. 단순히 데이터를 쌓아두는 저장 공간이 아니라, 데이터 간의 구조·관계·규칙까지 함께 관리한다는 점이 핵심임.

단순한 "파일 창고"와 구분됨. 파일 창고가 데이터를 그냥 모아두는 것이라면, 데이터베이스는 데이터의 구조·관계·규칙까지 함께 관리함

## 원문 기반 개념 정리

### 데이터베이스(Database)란?

여러 사람과 프로그램이 함께 접근할 수 있도록, 구조화된 형태로 저장하고 관리하는 데이터의 모음을 의미함. 단순히 데이터를 쌓아두는 저장 공간이 아니라, 데이터 간의 구조·관계·규칙까지 함께 관리한다는 점이 핵심임.

단순한 "파일 창고"와 구분됨. 파일 창고가 데이터를 그냥 모아두는 것이라면, 데이터베이스는 데이터의 구조·관계·규칙까지 함께 관리함

데이터베이스 자체는 데이터를 담아두는 저장소를 가리키는 개념임

그 저장소의 데이터를 실제로 다루는(조회·수정·삭제 등) 소프트웨어는 DBMS(Database Management System)로, 데이터베이스와 구별되는 별개의 개념임

### DBMS(Database Management System)란?

데이터베이스에 저장된 데이터를 실제로 다루는 소프트웨어로, 크게 네 가지 핵심 기능을 담당함.

### DBMS의 종류: 관계형 vs NoSQL

DBMS는 데이터를 저장하는 구조에 따라 크게 관계형(RDBMS)과 NoSQL로 나뉨.

### ERD(Entity-Relationship Diagram)란?

테이블(개체)과 테이블 간의 관계를 코드를 짜기 전에 그림으로 미리 설계하는 다이어그램을 의미함.

집을 짓기 전에 설계도를 그리듯, 테이블을 만들기 전에 전체 데이터 구조를 미리 그려보는 과정임

개발자·기획자·데이터 분석가가 함께 데이터 구조를 이해하고 소통하는 공용 언어 역할을 함

### OpenAI, PostgreSQL로 8억 명 사용자 지원하기

OpenAI가 샤딩된 분산 DB로 전면 전환하지 않고, 검증된 기술(PostgreSQL)을 한계까지 최적화해 대규모 서비스를 운영하는 사례임.

핵심 인프라 구조

단일 프라이머리(Azure PostgreSQL Flexible Server) 1대가 모든 쓰기를 처리함

초당 수백만 건 쿼리(QPS)를 처리하면서, p99 지연시간을 낮은 두 자릿수 밀리초로 유지함

읽기 트래픽은 지역별로 분산된 복제본으로 오프로드해 프라이머리 부하를 낮춤

### OpenAI의 문제와 대응 전략

단일 프라이머리 아키텍처를 유지하면서 마주친 주요 문제와, 각각에 대응한 전략을 정리한 표임.

### OpenAI의 문제와 대응 전략(상세) — 쓰기 확장·MVCC

앞 표의 문제 중 쓰기 확장과 MVCC를 왜 문제인지와 해결책 관점으로 풀어 설명함.

MVCC는 여러 트랜잭션이 동시에 접근해도 서로 방해받지 않도록 데이터의 여러 버전을 유지하는 방식임. 대신 낡은 버전이 계속 남기 때문에 vacuum으로 주기적으로 정리해줘야 함.

### OpenAI의 문제와 대응 전략(상세) — 스키마 변경·연결·복제본

나머지 세 문제(스키마 변경, 연결 폭주, 복제본 부하)를 같은 형식으로 정리함.

WAL은 실제 데이터 파일을 바꾸기 전에 변경 내용을 먼저 기록하는 로그로, 장애 복구와 복제의 기반이 됨.

### 벡터 검색, 그래프 DB의 표준 기능이 되다 (TigerVector)

RAG(검색 증강 생성)를 구성할 때 보통 벡터 DB와 그래프 DB를 별도 시스템으로 분리해 운영함. TigerVector는 이 둘을 TigerGraph(MPP 기반 그래프 DB) 하나 안에서 처리할 수 있게 만든 시스템임.

기술적으로 한 일은 세 가지임.

그래프의 정점(vertex, 노드)에 임베딩(embedding) 타입을 새 속성으로 추가해, 각 노드가 벡터값도 함께 가질 수 있게 함

해당 벡터를 빠르게 검색하는 전용 인덱스를 만들고, MPP 그래프 엔진과 통합함

그래프 쿼리 언어 GSQL을 확장해 "벡터로 유사한 것 찾고 → 그 결과에서 그래프 관계 따라가기" 같은 복합 쿼리를 한 번에 작성 가능하게 함

Neo4j, Amazon Neptune, 전문 벡터 DB Milvus 대비 우수한 성능을 실험으로 입증했고, 2024년 12월 TigerGraph v4.2 정식 제품에 반영됨. SIGMOD 2025(DB 분야 최고 학회)의 산업 트랙에도 채택된 사례로, 학술 아이디어에 그치지 않고 실제 상용 제품이 됐다는 점이 핵심임.

이 흐름이 시사하는 바는, 벡터 검색이 더 이상 별도의 특수 DB가 아니라 관계형·그래프 DB의 표준 기능으로 흡수되고 있다는 것임.

### [참고] MPP(Massively Parallel Processing)

여러 개의 독립된 컴퓨팅 노드(프로세서+메모리+디스크)가 데이터 처리 작업을 나누어 동시에 실행하는 구조임.

Shared Nothing 구조: 각 노드가 자신만의 메모리·디스크를 독자적으로 사용하며 서로 자원을 공유하지 않음

데이터가 커지면 서버(노드)를 옆으로 추가하기만 하면 되므로, 확장성(Scale-out)이 강점임

대표 활용 영역: 대규모 데이터 웨어하우스(DW) 및 빅데이터 분석 플랫폼(Amazon Redshift, Snowflake, Google BigQuery, Teradata 등)

단일 DB 인덱스(예: B-Tree)는 데이터가 수억~수십억 건 이상이 되면 MPP 분산 환경을 지원하기 어려움. MPP의 핵심 이점은 분산 탐색 극대화(각 노드가 자기 파티션 안에서만 찾아 Full Scan 최소화)와 병렬 조회 성능 향상(여러 노드가 인덱스 기반으로 동시에 처리)임.

### LLM × 벡터 DB 결합 연구 동향

이 주제를 다룬 주요 논문 두 편을 참고 자료로 소개함.

arXiv:2402.01763 — LLM과 벡터 DB(VecDB) 결합의 이론적 근거, 응용 프로토타입 분류, 연구·엔지니어링 과제를 체계적으로 정리한 서베이. LLM의 환각(hallucination)을 줄이기 위해 벡터 DB에서 검색한 사실을 근거로 답하게 하는 구조(RAG) 등을 유형화함

arXiv:2310.11703 (v4, 2026.3 개정) — 고차원 벡터 데이터가 기존 DBMS의 한계를 넘어서며 벡터 DB가 LLM과 결합되는 과정을 스토리지·검색 두 축에서 추적한 서베이. 2026년 3월까지 계속 개정 중인 "살아있는" 논문임

### 반증 사례: "코어를 늘려도 더 빨라지지 않는다"

Argonne 국립연구소 등이 실제 슈퍼컴퓨터(Polaris, Aurora) 2대에서 Qdrant, Milvus, Weaviate 세 벡터 DB를 최대 256개 워커까지 확장하며 테스트한 실험임 (자체 과학 데이터셋 Pes2o-VE: 임베딩 8,800만 개, 843.56GB).

원인은 벡터 DB의 내부 동시성 제어 방식이 클라우드 환경을 기준으로 설계되어 있어, HPC의 고성능 네트워크·스토리지 환경과 맞지 않아 오히려 병목이 발생했기 때문임.

→ 최신 기술 = 무조건 좋다가 아니라 "설계된 환경(클라우드)과 실제 배치 환경(HPC)이 다르면 성능이 역행할 수 있다"

### 데이터베이스 개요

### ACID 속성

데이터베이스 트랜잭션이 지켜야 할 4가지 기본 원칙임.

### DBMS별 ACID 지원 차이

ACID는 모든 DBMS에서 교과서적으로는 지원하나, 엔진·설정·클라우드 옵션에 따라 실제 보장 수준이 다름.

### [참고] WAL(Write-Ahead Logging) — 지속성 구현 원리

변경 사항을 실제 데이터 파일에 쓰기 전에 로그(저널)에 먼저 기록하는 방식임. "로그가 먼저(WAL)"라는 이름 그대로임.

동작 순서:

트랜잭션 실행 → WAL 버퍼에 변경 내용 기록 (로그 우선 원칙)

Shared Buffer(메모리)에 페이지 변경 반영

아직 디스크 데이터 파일에는 미기록 상태 (dirty page)

COMMIT 시 WAL에 로그 기록 후 fsync(디스크 동기화) → 이후 Checkpoint 시점에 데이터 파일에 실제 반영

장애 복구 시: pg_wal/ 디렉토리의 로그를 순서대로 재실행(Redo), COMMIT되지 않은 트랜잭션은 Undo 처리함.

장점은 장애 복구 가능성 확보, 쓰기 성능 개선(순차 기록 → 랜덤 I/O 최소화)이며, PostgreSQL, SQL Server, Oracle, MySQL(InnoDB) 등 대부분의 DBMS가 사용함.

### [참고] Consensus 기반 (합의 알고리즘)

분산 DB(Cloud DB, 분산 트랜잭션 DB)에서는 여러 노드가 동일한 데이터를 가진 상태를 유지해야 함. 네트워크 지연·장애가 발생해도 모든 노드가 같은 결과(합의)를 가지도록 하는 알고리즘임.

동작 과정:

클라이언트가 트랜잭션 요청 → Leader 노드가 WAL에 기록

다른 Follower 노드들과 투표를 통해 과반수가 같은 로그에 동의해야 Commit 확정

모든 노드에 같은 순서의 로그(트랜잭션)가 쌓이므로 Strong Consistency 보장

대표 알고리즘: Paxos(이론적으로 가장 유명), Raft(구현이 단순해 실제 제품에서 널리 활용 — AWS Aurora, Etcd, CockroachDB 등), Google Spanner(Paxos + TrueTime API로 전역 시계 동기화).

장점: 분산 환경에서도 Consistency 유지, 장애 시 Leader 재선출로 고가용성 확보.

단점: 네트워크 지연이 늘어나면 성능 저하 (특히 글로벌 DB에서 latency 증가).

### WAL vs Consensus 비교

WAL = 한 DB 안에서 장애 대비 안전장치, Consensus = 여러 DB가 흩어져 있어도 모두 같은 결과를 보장하는 안전장치.

### [참고] Isolation Level

트랜잭션 동시성에서 발생하는 대표 이상 현상 3가지:

Dirty Read: 아직 커밋되지 않은 값을 다른 트랜잭션이 읽는 현상

Non-Repeatable Read: 같은 행을 두 번 읽었는데 값이 달라짐 (다른 트랜잭션이 그 행을 UPDATE/DELETE)

Phantom Read: 같은 조건으로 두 번 조회했는데 행의 개수가 달라짐 (다른 트랜잭션이 INSERT 또는 범위 내 행을 추가/삭제)

### ANSI 격리 수준별 이상 현상 허용 여부

표준 정의상 RR은 Phantom을 허용하지만, DBMS 구현에 따라 범위 잠금·스냅샷으로 실질적으로 막히는 경우 존재함.

### DBMS별 기본값과 구현 차이

### [참고] Phantom Read 예시

orders 테이블에서 amount >= 100인 건수를 동일 트랜잭션 내에서 두 번 조회하는 상황임. Session 1이 첫 번째 조회(결과: 5)를 마친 사이, Session 2가 amount = 150인 행을 INSERT 후 커밋하면 두 번째 조회 결과가 달라짐.

격리 수준별 결과:

READ COMMITTED: 5 → 6으로 증가. 팬텀 발생

REPEATABLE READ (InnoDB/PG 스냅샷 구현): 5 → 5 유지. 같은 트랜잭션 내 같은 스냅샷을 보기 때문. 단, Session 1이 SELECT ... FOR UPDATE나 같은 범위를 UPDATE/DELETE로 잠그면 범위 잠금으로 Session 2의 INSERT 자체를 사전 차단

SERIALIZABLE: 팬텀 원천 차단. Session 2의 INSERT는 Session 1이 끝날 때까지 대기하거나 충돌로 롤백됨

### 관계형 데이터 모델링이란?

현실 세계의 데이터를 관계형 포맷(표)으로 변환하는 과정임. 컴퓨터 프로그램이 데이터를 처리하려면 구조화된 형태로 바꿔야 하고, 여러 명이 동시에 통합적으로 작업할 수 있도록 구성이 필요함. 관계(Relation)란 열과 행을 지니는 형태로, 대표적 예는 "표"임.

### 핵심 구성 요소

### 테이블 간 관계(Relationship)

### [참고] 외래키 제약 조건 옵션 비교

### 정규화 단계별 예시 (PK·FK 부여 흐름)

정규화는 데이터 중복을 제거하고 무결성을 높이기 위해 테이블을 분리하는 과정임.

1정규형: PK를 부여해 각 행을 고유하게 식별할 수 있는 상태. 예: (사번, 전공코드)를 복합 PK로 설정

2정규형: PK에 종속되지 않은 컬럼을 별도 테이블로 분리. 분리된 테이블과 원래 테이블을 연결하는 열이 FK가 됨. 예: 전공코드별 역할상세를 "전공정보" 테이블로 분리

3정규형: PK가 아닌 컬럼 간 종속(이행적 종속)까지 분리. 예: 직위코드→직위, 회사코드→회사명을 각각 별도 테이블로 분리. 식별자가 아니더라도 중복·재정의 가능성이 있으면 분리 검토

### 관계형 데이터 모델링과 SQL 관계

완료된 데이터 모델링을 토대로 DBMS에 테이블을 생성하고 데이터를 입력·조회·삭제·수정하는 데 SQL(Structured Query Language)을 사용함. 데이터 모델링 없이 바로 테이블을 만들 수는 있으나, 데이터가 많아지거나 복잡해지면 중복·오류 등 품질 문제가 발생함.

### NoSQL 데이터 모델링 이해

SQL과 NoSQL은 다루는 데이터의 성격과 일관성 요구 수준에 따라 선택함.

SQL은 데이터의 관계에 집중해 분석하고, NoSQL은 표현되는 데이터의 형태와 정렬 특징에 집중해 분석함. 트랜잭션을 보장하는 ACID 수준에 따라 SQL/NoSQL을 선택적으로 적용할 수 있음.

### 관계형 데이터 모델 검증

설계된 모델이 실제 데이터 저장 및 관리 요구사항을 충족하는지 확인하는 단계임.

### 정규화 단계별 정리

정규화는 데이터 중복과 이상현상을 제거하기 위해 테이블을 단계적으로 분리하는 과정임.

### 제1정규형 (1NF)

각 셀에 단일값만 존재해야 하고, 반복되는 그룹이 없어야 함. 모든 속성이 원자값(atomic)이어야 하는 상태임.

비정규화 상태 (1NF 위반):

1NF 적용 후:

한 셀에 여러 값이 들어가거나 반복 그룹이 있으면 1NF 위반임.

### 제2정규형 (2NF)

1NF를 만족하면서, 비키(Non-key) 속성이 기본키의 일부분에만 종속되는 부분 함수 종속을 제거한 상태임. 복합키일 경우 모든 비키 속성이 기본키 전체에 완전히 종속되어야 함.

비정규화 상태 (2NF 위반 — 고객이름이 복합키 중 고객ID에만 종속):

2NF 적용 후 — 고객이름을 별도 테이블로 분리:

고객 테이블:

주문 테이블:

제품 테이블:

### 제3정규형 (3NF)

2NF를 만족하면서, 비키 속성이 다른 비키 속성에 함수적으로 종속(이행적 종속)되지 않는 상태임. 비키가 기본키가 아닌 다른 비키의 값으로 결정될 수 없어야 함.

이행적 종속 예 (3NF 위반 — 제품ID → 제품명 → 공급업체명):

공급업체명이 기본키(제품ID)가 아닌 제품명에 종속되므로 3NF 위반임. 분리 후:

주문 테이블, 고객 테이블, 제품 테이블(공급업체명 제거) + 공급업체 테이블로 분리해 이행적 종속 제거.

### 보이스-코드 정규형 (BCNF)

3NF보다 엄격한 형태로, 모든 종속성을 제거하는 가장 높은 수준의 정규화임. 모든 결정자(Determinant)가 후보키여야 함.

실무에서는 보통 3NF까지 정규화하고, 성능이 중요한 구간은 의도적으로 반정규화(denormalization)를 적용하기도 함.

### Entity(엔티티, 개체) — 개념 및 종류

엔티티는 데이터베이스에서 관리하고자 하는 대상 객체를 의미함.

엔티티 집합(Entity Set)은 동일한 특성을 가진 엔티티들의 모임임. 예: 모든 학생들의 집합 = "학생" 엔티티 집합.

### Attribute(속성) — 종류 및 특성

엔티티가 가지는 고유한 특성이나 성질임. 예: 학생 엔티티의 속성 — 학번, 이름, 이메일, 학과, 학년, 입학일 등.

### ERD 작성 단계

요구사항 수집 → 엔티티 도출 → 속성 정의 → 관계 설정 → 카디널리티 명시 → ERD 도구 시각화 → 검토 및 수정 순으로 진행함.

엔티티 도출: 관리 대상의 주요 객체 추출 후 명사로 정의. 예: 학생(Student), 강의(Course), 교수(Professor)

관계 설정: 엔티티 간 연관성 파악. 예: 학생과 강의는 '수강한다', 교수와 강의는 '담당한다'

카디널리티 명시: 관계의 수(1:1, 1:N, N:M)를 명확히 표시. 예: 한 학생은 여러 강의 수강(1:N), 학생-강의는 N:M

ERD 도구: Lucidchart, GitMind, Aquerytool, DBdiagram 등 무료 도구 활용. ERD 표기 도형은 사각형(엔티티), 타원(속성), 마름모(관계 다이어그램)

### IE 표기법 (까마귀발 표기법, Crow's Foot)

ERD에서 관계의 수(카디널리티)를 선 끝 기호로 표현하는 방식임.

관계선은 두 종류임. 식별 관계(실선)는 FK가 자식의 PK 일부인 경우로 부모 없이 자식이 존재할 수 없는 약한 엔티티 관계임. 비식별 관계(점선)는 FK가 자식의 일반 컬럼인 경우로 부모 없이도 자식이 존재 가능함.

### dbdiagram.io DBML 문법으로 ERD 작성

dbdiagram.io는 SQL 없이 DBML(Database Markup Language) 코드를 왼쪽에 작성하면 오른쪽에 ERD가 자동 생성되는 도구임. PNG/SQL 내보내기도 가능함.

관계 방향 표기: > 다대일, < 일대다, - 일대일, <> 다대다.

```text
Table students {
  id          bigint    [pk, increment]
  student_no  varchar(20) [unique, not null, note: '학번']
  name        varchar(100) [not null]
  email       varchar(200) [unique, not null]
  major_id    int       [ref: > majors.id, note: 'FK → 학과']
  grade       smallint  [not null, note: '1~4학년']
  created_at  timestamp [default: 'now()']
}

Table enrollments {  // N:M 교차 테이블
  student_id  bigint  [ref: > students.id]
  course_id   int     [ref: > courses.id]
  score       decimal(5,2)
  enrolled_at date    [not null]
  Indexes {
    (student_id, course_id) [pk]  // 복합 PK
  }
}
```

### 개념적 vs 논리적 데이터 모델링

데이터 모델링은 개념적 → 논리적 → 물리적 3단계로 진행됨.

### 물리적 데이터 모델링 핵심 항목

논리 모델을 특정 DBMS 환경에 최적화된 물리적 스키마로 변환하는 단계임. 주요 결정 항목은 7가지임.

### ① 데이터 타입 결정 — DBMS별 최적 타입 선택

금액: NUMERIC(10,2) — 부동소수점 오류 방지

시간: TIMESTAMPTZ(타임존 포함) — 글로벌 서비스 필수

문자열: VARCHAR(n) vs TEXT — PostgreSQL은 TEXT 제한 없음

### ② 인덱스 설계 — WHERE/JOIN/ORDER BY 컬럼에 인덱스 추가

### ③ 파티셔닝

대용량 데이터를 연도/지역별로 분할 저장해 쿼리 성능과 관리 효율을 높임.

### ④ 클러스터형 vs 비클러스터형 인덱스

데이터를 물리적으로 어떤 순서로 디스크에 배치할지를 결정하는 항목임. 클러스터형은 인덱스 순서대로 실제 데이터가 저장되고, 비클러스터형은 인덱스와 데이터 저장 위치가 별개임.

### ⑤ 저장 공간 최적화

압축, 컬럼 기반 저장(Columnstore), 아카이빙 전략을 통해 디스크 사용량과 I/O를 줄임.

### ⑥ 트랜잭션 로드 테스트

동시 사용자를 고려해 Lock 전략(낙관적/비관적)을 선택하고, 실제 부하 환경에서 성능을 검증함.

### 낙관적 Lock vs 비관적 Lock

### 약한 엔티티와 N:M 관계 설계 패턴

### 약한 엔티티 (Weak Entity) 설계 원칙

자기 혼자서는 고유하게 식별(구분)할 수 없는 엔티티로, 다른 강한 엔티티와 같이 있어야 식별 가능한 데이터 구조임.

독자적인 PK 없음 → 강한 엔티티의 PK + 자신의 부분키로 복합 PK 구성

ON DELETE CASCADE 필수: 부모(강한 엔티티) 삭제 시 자식(약한 엔티티)도 함께 삭제

이름이나 코드만으로는 유일하지 않으므로 혼자서 구분 불가

복합키(PK+FK) 사용 시 성능/가독성 고려 필요

예시:

OrderItem(OrderID, ItemNo) — Order 없이 존재 불가

Dependent(EmployeeID, DependentName) — Employee 없이 존재 불가

### 다대다(N:M) 관계

두 엔티티가 상호 다수의 레코드를 연결하는 관계로, DB에서 직접 구현이 불가하므로 반드시 교차(중간) 테이블이 필요함.

조인 테이블 설계 전략:

두 엔티티의 FK를 포함하는 교차 테이블 필수

복합 PK(FK1 + FK2) 또는 대체 PK(surrogate key, AUTO_INCREMENT id) 선택

복합 PK: 데이터 무결성 강화 (중복 등록 원천 방지)

자동 증가 ID: 구조 단순화, 단 의미 없는 키

교차 테이블에 추가 속성 부여 가능 → 예: 수강(enrolled_at, score), 주문상품(quantity, unit_price)

예시 구조 (학생-강의 수강신청):

Student (PK: StudentID) ↔ Enrollment (StudentID(FK), CourseID(FK), EnrollmentDate) ↔ Course (PK: CourseID)

### 인덱스 전략

WHERE 조건을 어느 컬럼으로 거느냐에 따라 인덱스를 양방향으로 만들어두는 전략이 유효함. Non-Clustered Index 추가로 양방향 검색 성능 최적화.

예시 — Enrollment 테이블:

INDEX(student_id, course_id) — "이 학생이 수강한 강의 목록" 조회

INDEX(course_id, student_id) — "이 강의를 수강한 학생 목록" 조회

파티셔닝: 대용량 데이터 시 Enrollment 테이블을 학기별로 분할

### 약한 엔티티 및 N:M 교차 테이블 DDL

```sql
-- 약한 엔티티 예시: OrderItem (Order 없이 존재 불가)
CREATE TABLE order_items (
  order_id   INT         REFERENCES orders(id) ON DELETE CASCADE,
  item_no    SMALLINT    NOT NULL,              -- 부분키 (약한 엔티티)
  product_id INT         REFERENCES products(id),
  quantity   INT         NOT NULL CHECK (quantity > 0),
  unit_price NUMERIC(10,2) NOT NULL,
  PRIMARY KEY (order_id, item_no)              -- 복합 PK
);

-- N:M 교차 테이블: 학생-강좌 수강신청
CREATE TABLE enrollments (
  student_id  BIGINT REFERENCES students(id) ON DELETE CASCADE,
  course_id   INT    REFERENCES courses(id)  ON DELETE CASCADE,
  enrolled_at DATE   NOT NULL DEFAULT CURRENT_DATE,
  score       NUMERIC(5,2) CHECK (score BETWEEN 0 AND 100),
  PRIMARY KEY (student_id, course_id),         -- 복합 PK로 중복 방지
  CONSTRAINT chk_score CHECK (score IS NULL OR score BETWEEN 0 AND 100)
);

-- 양방향 조회 최적화 인덱스
CREATE INDEX idx_enroll_course ON enrollments (course_id, student_id);
```

WHERE 조건이 어느 컬럼을 자주 쓰느냐에 따라 Index는 별도로 조정해야 하며, Non-Clustered Index 사용을 권장함.

### 스키마 기반 멀티 프로젝트 설계 전략

스키마(Schema)는 테이블/뷰/함수 등 DB 객체를 그룹화하는 논리적 네임스페이스임.

### 멀티 테넌시 3가지 패턴

### Bridge Model 구조 예시

하나의 DB 인스턴스 안에서 스키마로 공통/프로젝트별 영역을 분리하는 방식임.

maindb/global — 공통 테이블: users, products, exchange_rates

maindb/prj_alpha — 프로젝트 A 전용: orders, promotions

maindb/prj_beta — 프로젝트 B 전용: inventory, suppliers

### Bridge Model 주요 장점

물리적 자원 효율성: 단일 인스턴스로 운영하므로 서버 비용 절감

스키마 단위 접근 제어: 프로젝트별로 권한을 분리해 보안 관리 가능

버전 관리: 스키마 단위로 마이그레이션 독립 적용 가능

성능 최적화: 프로젝트별로 독립적인 인덱스/파티셔닝 전략 적용 가능

Vector DB 연계 시 프로젝트별 임베딩 저장 스키마를 분리 설계할 수 있어 AI 서비스 구조에도 유리함

### 주요 RDBMS 특징 비교

### MySQL / MariaDB

경량 & 빠른 성능으로 웹 서비스 초기에 많이 사용됨. LAMP 스택(Linux, Apache, MySQL, PHP/Python)의 핵심 DB임. InnoDB 스토리지 엔진을 통해 트랜잭션, FK, MVCC를 지원함. MariaDB는 MySQL의 오픈소스 분기(Fork)로, 커뮤니티 중심으로 개발되며 MySQL과 호환되면서 JSON, Window Functions 같은 기능을 빠르게 반영함.

### PostgreSQL

"가장 진보한 오픈소스 RDBMS"로 불림. 표준 SQL 호환성이 뛰어나고 ANSI SQL:2016까지 잘 반영됨. JSONB, PostGIS(지리정보 GIS), 사용자 정의 함수/자료형 등 확장성이 강점이며, MVCC 기반으로 동시성 처리에 강함.

확장 기능:

JSONB: JSON 데이터를 바이너리 형태로 저장하는 방식임. 일반 JSON 타입과 달리 저장 시 파싱·인덱싱이 가능해 조회 성능이 훨씬 빠름. 반정형 데이터를 관계형 DB 안에서 효율적으로 다룰 수 있어 NoSQL 없이도 유연한 데이터 구조를 처리할 수 있음

PostGIS: PostgreSQL의 지리정보 확장 모듈임. 좌표·거리·면적 계산, 특정 반경 내 위치 검색 등 공간 쿼리를 SQL로 처리할 수 있게 해줌. 배달앱 경로 탐색, 지도 기반 서비스 등 GIS 기반 서비스에 활용됨

### Oracle

대기업 시장을 장악한 전통 강자 RDBMS임. RAC(Real Application Clusters)를 통해 여러 서버가 동시에 DB를 공유하여 고가용성/확장성을 제공하며, 보안·성능 최적화·분산 트랜잭션·Data Guard(재해복구) 등 고급 기능을 갖춤.

### Microsoft SQL Server

MS 생태계(.NET, Visual Studio, Windows Server)와 밀접하게 통합된 RDBMS임. OLAP(Online Analytical Processing) 기반으로 BI(비즈니스 인텔리전스)와 데이터 분석이 강점이며, SSIS/SSAS/SSRS를 통해 데이터 통합·분석·리포팅 기능을 제공함.

### Cloud Database (관리형 RDBMS)

### 주요 포인트 요약

### CREATE DATABASE: "컨테이너" 만들기

벤더마다 데이터베이스의 의미/단위가 조금씩 다름.

### MySQL / MariaDB

하나의 서버 안에 여러 database(schema)를 만들고 그 안에 테이블을 생성하는 구조임. 문자셋/콜레이션을 반드시 지정해야 한국어/다국어 처리가 가능함.

```text
-- MySQL 8 / MariaDB 권장
CREATE DATABASE appdb
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;  -- 한국어/다국어 무난
```

### PostgreSQL

서버(cluster) → 여러 database → 각 database 안에 여러 schema로 구성되는 3단 계층 구조임. 인코딩/로케일을 함께 정해야 함.

```text
CREATE DATABASE appdb
  WITH ENCODING 'UTF8'
  LC_COLLATE 'en_US.UTF-8'
  LC_CTYPE 'en_US.UTF-8'
  TEMPLATE template0;
```

### SQL Server

인스턴스 → 여러 database → 각 database 안에 schema(기본: dbo) 구조임. 한국어/UTF-8을 쓰려면 콜레이션을 지정해야 함.

```text
CREATE DATABASE AppDb
  COLLATE Korean_100_CI_AS_SC_UTF8;
```

### Oracle

"데이터베이스"는 인스턴스/스토리지 단위로 관리자(DBA)가 생성하는 개념임. 개발자는 보통 사용자=스키마를 만들어 씀.

```sql
-- DBA가 수행 (개발 학습용 예시)
CREATE USER appuser IDENTIFIED BY "StrongPW1!"
  DEFAULT TABLESPACE users QUOTA UNLIMITED ON users;

GRANT CREATE SESSION, CREATE TABLE, CREATE SEQUENCE TO appuser;
```

### CREATE TABLE: 테이블 설계의 표준 뼈대

products 테이블을 각 DBMS 문법으로 만든 예시임. 컬럼 구성: id(정수, 식별자) / name(문자) / price(금액: 소수 고정 자리수) / attrs(JSON 속성) / created_at(생성 시각).

### MySQL / MariaDB (InnoDB 전제)

```sql
CREATE TABLE products (
  id         INT AUTO_INCREMENT PRIMARY KEY,
  name       VARCHAR(200) NOT NULL,
  price      DECIMAL(10,2) NOT NULL CHECK (price >= 0), -- MySQL 8.0.16+ / MariaDB 10.2+ 유효
  attrs      JSON NULL,                                  -- MariaDB는 내부적으로 LONGTEXT + JSON 함수
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB
  DEFAULT CHARSET = utf8mb4;
```

CHECK는 MySQL 8.0.16 미만에선 파싱만 하고 무시되던 역사 있음 → 버전 확인 필수

MariaDB의 JSON은 물리적으로 LONGTEXT로 저장되므로 인덱싱 시 가상컬럼+인덱스 패턴 사용

### PostgreSQL

```sql
CREATE TABLE products (
  id         BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, -- SERIAL 대신 최신 표준
  name       VARCHAR(200) NOT NULL,
  price      NUMERIC(10,2) NOT NULL CHECK (price >= 0),
  attrs      JSONB,                                            -- 강력한 JSONB 연산/인덱스
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- JSONB 특정 키 인덱싱 예시
CREATE INDEX idx_products_attrs_color
  ON products ((attrs->>'color'));
```

### SQL Server

```sql
CREATE TABLE dbo.Products (
  Id        BIGINT IDENTITY(1,1) PRIMARY KEY,
  Name      NVARCHAR(200) NOT NULL,
  Price     DECIMAL(10,2) NOT NULL
            CONSTRAINT CK_Products_Price CHECK (Price >= 0),
  Attrs     NVARCHAR(MAX) NULL,   -- JSON 전용 타입 없음: NVARCHAR에 저장, JSON_VALUE/OPENJSON 사용
  CreatedAt DATETIME2 NOT NULL
            CONSTRAINT DF_Products_CreatedAt DEFAULT SYSUTCDATETIME()
);
```

### Oracle

```sql
CREATE TABLE products (
  id         NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY, -- 12c+ IDENTITY
  name       VARCHAR2(200 CHAR) NOT NULL,                         -- CHAR semantics 권장
  price      NUMBER(10,2) NOT NULL,
  attrs      CLOB,                                                 -- 12c~: IS JSON 제약, 21c~: JSON 타입
  created_at TIMESTAMP WITH TIME ZONE DEFAULT SYSTIMESTAMP NOT NULL,
  CONSTRAINT ck_products_price CHECK (price >= 0)
);

-- 12c 이상에서 JSON 유효성 제약 추가
ALTER TABLE products ADD CONSTRAINT ck_products_attrs_json
  CHECK (attrs IS JSON);
```

### 데이터 타입 차이 핵심 정리

SQL Server/Oracle에서 ENUM 대신 참조 테이블 + FK를 쓰는 패턴 예시:

```sql
-- 상태값을 따로 테이블로 만듦 (Oracle 기준)
CREATE TABLE status_types (
  status_code  VARCHAR2(20) PRIMARY KEY,
  description  VARCHAR2(100)
);

INSERT INTO status_types VALUES ('ACTIVE',  '활성 사용자');
INSERT INTO status_types VALUES ('BLOCKED', '차단됨');
INSERT INTO status_types VALUES ('PENDING', '승인 대기');

-- users 테이블이 status_code를 참조
CREATE TABLE users (
  id          NUMBER PRIMARY KEY,
  email       VARCHAR2(200) NOT NULL,
  status_code VARCHAR2(20) NOT NULL,
  CONSTRAINT fk_users_status FOREIGN KEY (status_code)
    REFERENCES status_types(status_code)
);
```

### 제약조건: 무결성의 4대장

FK 벤더별 지원 차이:

### 이식성(Portable SQL) 팁

DBMS마다 타입 이름이 제각각이므로, 호환성 좋은 표준 타입을 쓰는 것이 중요함.

타입은 표준/보편형으로 INTEGER, NUMERIC(p,s), VARCHAR(n), TIMESTAMP 중심으로 사용

예약어/식별자 따옴표 지양: 벤더별 따옴표가 다름(", ```, []) → 스네이크케이스 소문자 권장

DEFAULT의 함수명은 통일 불가 → 마이그레이션 스크립트에서 DBMS별로 분기 처리

CHECK/ENUM 남용 금지: 규칙이 바뀌면 스키마 변경이 불가해짐 → 값이 많아지면 Lookup 테이블 + FK로 모델링

JSON은 스키마-리스지만, 접근 경로가 자주 쓰이면 가상컬럼/인덱스로 최적화

### 체크리스트 (스키마 리뷰용)

PK는 단일/숫자/불변인가? (자연키 대신 대체키 권장)

FK에 필요한 인덱스가 있는가?

금액/수량은 DECIMAL/NUMERIC으로 스케일을 고정했는가?

시간 컬럼은 기본값/타임존 정책이 일관적인가?

JSON 컬럼은 꼭 필요한가? 자주 쓰는 키에 인덱스 계획이 있는가?

CHECK/ENUM이 변경 가능성을 과도하게 제한하진 않는가?

### ALTER TABLE — 컬럼 추가/수정 및 운영 주의사항

```text
-- 컬럼 추가 (일반적으로 안전)
ALTER TABLE students ADD COLUMN phone VARCHAR(20);
ALTER TABLE students ADD COLUMN birth_date DATE;

-- 컬럼 타입 변경 (주의: 대용량 테이블에서는 전체 재작성 발생)
ALTER TABLE students ALTER COLUMN phone TYPE VARCHAR(30);  -- PostgreSQL

-- NOT NULL 추가 (기존 NULL 없는 경우만)
ALTER TABLE students ALTER COLUMN phone SET NOT NULL;

-- 제약조건 추가
ALTER TABLE students
  ADD CONSTRAINT chk_email_format CHECK (email LIKE '%@%');

-- 컬럼 삭제 (신중히 — CASCADE: 의존 뷰/인덱스 함께 삭제)
ALTER TABLE students DROP COLUMN IF EXISTS phone CASCADE;

-- 인덱스 생성 (운영 중 잠금 없이)
CREATE INDEX CONCURRENTLY idx_students_grade ON students (grade);
-- CONCURRENTLY: PostgreSQL에서 테이블 잠금 없이 인덱스 생성 (운영 환경 권장)
```

TRUNCATE vs DELETE 차이:

운영 중 DDL 변경(대용량 테이블) 시 도구 활용:

MySQL: pt-online-schema-change

PostgreSQL: pg_repack

### INSERT / UPDATE / DELETE 기본 패턴

DML(Data Manipulation Language)의 삽입·수정·삭제 구문 패턴을 정리함.

### INSERT

단건 삽입: INSERT INTO 테이블 (컬럼목록) VALUES (값목록) 형태로 한 행을 넣음.

다건 삽입: VALUES 뒤에 (...), (...), (...)처럼 여러 튜플을 콤마로 나열하면 여러 행을 한 번에 넣을 수 있음.

### UPDATE

형태: UPDATE 테이블 SET 컬럼 = 값 [, ...] WHERE 조건

SET에서 grade = grade + 1처럼 기존 값을 참조해 갱신 가능.

WHERE 없이 실행하면 전체 행이 수정되므로 필수로 붙여야 함.

### DELETE

형태: DELETE FROM 테이블 WHERE 조건

조건에 서브쿼리(WHERE id IN (SELECT ...))를 넣어 다른 테이블 조건으로 삭제 대상을 지정할 수 있음.

WHERE 없이 실행하면 전체 행이 삭제되므로 필수로 붙여야 함.

### 유의점 (커밋 동작)

MySQL: 기본 autocommit이 ON이라 DML 실행 즉시 커밋됨.

PostgreSQL: BEGIN; 없이 실행한 DML은 자동 커밋됨.

대용량 DELETE는 한 번에 지우지 말고 LIMIT + 루프로 나눠서 처리하는 것이 권장됨(락·부하 완화).

### SELECT 기본 구조 및 논리적 실행 순서

SELECT 문의 절 구성과, 작성 순서와 다른 논리적 실행 순서를 정리함.

### 논리적 실행 순서

작성하는 순서와 실제 처리되는 순서가 다름:

FROM → JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT

### 주요 절 구성

SELECT: 조회·가공할 컬럼 지정. 표현식에 AS로 별칭 부여 가능.

FROM / JOIN: 대상 테이블과 결합 조건(ON) 지정.

WHERE: 집계 이전 단계의 행 필터.

ORDER BY: 정렬 기준(DESC 내림차순, ASC 오름차순).

LIMIT ... OFFSET ...: 페이지네이션(가져올 개수·건너뛸 개수).

### 예시에 쓰인 가공 표현식

UPPER(s.email): 이메일을 대문자로 변환.

EXTRACT(YEAR FROM s.created_at): 날짜에서 연도만 추출.

COALESCE(s.phone, '미등록'): NULL이면 대체값으로 표시.

CASE ... WHEN ... THEN ... ELSE ... END: 조건별로 다른 라벨 부여(예: grade 1 → 신입생, 4 → 졸업반).

### 유의점 (별칭과 실행 순서)

SELECT는 WHERE보다 나중에 처리되므로, WHERE 절에서는 SELECT 절에서 만든 별칭(alias)을 사용할 수 없음.

ORDER BY는 SELECT 이후에 처리되므로, ORDER BY 절에서만 SELECT 별칭을 사용할 수 있음.

### 자주 쓰는 문자열 / 날짜 / NULL 처리 함수

실무에서 자주 쓰는 함수들을 세 범주로 정리함.

### 문자열 함수

### 날짜/시간 함수 (PostgreSQL 기준)

CURRENT_DATE: 오늘 날짜.

CURRENT_TIMESTAMP: 현재 일시 + 타임존.

EXTRACT(YEAR FROM now()): 연도 추출.

DATE_TRUNC('month', now()): 해당 월의 첫날로 절삭.

now() - INTERVAL '30 days': 30일 전 시점 계산.

TO_CHAR(now(), 'YYYY-MM-DD'): 지정 형식으로 포맷팅.

### NULL 처리 함수

COALESCE(NULL, NULL, '세 번째'): 인자를 앞에서부터 보아 첫 번째 비-NULL 값을 반환(→ 세 번째).

NULLIF(a, b): 두 값이 같으면 NULL, 다르면 첫 번째 값 반환. NULLIF(10, 10) → NULL, NULLIF(10, 20) → 10.

CASE WHEN val IS NULL THEN 0 ELSE val END: 조건식으로 NULL을 직접 대체.

### 유의점 (DBMS별 NULL 함수)

COALESCE: SQL 표준이므로 모든 DBMS에서 사용 가능.

NVL: Oracle 전용.

ISNULL: SQL Server 전용.

### WHERE 절 — 조건 패턴 및 NULL 주의사항

WHERE 절에서 쓰는 조건 패턴을 범주별로 정리함.

### 조건 패턴

### NULL 처리

NULL 여부는 = NULL이 아니라 반드시 IS NULL / IS NOT NULL로 검사해야 함.

NULL = NULL의 결과는 TRUE가 아니라 UNKNOWN이므로 WHERE 조건에서 걸러지지 않음.

NULL이 포함된 연산은 결과도 NULL임(NULL + 5 = NULL). 대체하려면 COALESCE(NULL, 0) → 0.

### 연산자 우선순위

AND / OR / NOT 조합 시 우선순위는 NOT > AND > OR.

의도한 조건을 보장하려면 괄호로 명확하게 묶어 표현해야 함.

## 관련 글

- [[blog/STUDYING/index|STUDYING]]
