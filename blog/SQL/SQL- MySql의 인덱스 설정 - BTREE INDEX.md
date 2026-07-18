---
title: "[SQL] MySql의 인덱스 설정 - BTREE INDEX"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "Database", "springboot"]
category: "SQL"
published: 2025-04-03
source_url: https://ch010104.tistory.com/41
---

# [SQL] MySql의 인덱스 설정 - BTREE INDEX

## 원문

https://ch010104.tistory.com/41

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

인덱스(Index)는 데이터베이스에서 원하는 데이터를 빠르게 찾기 위해 사용하는 자료구조

책의 "색인"처럼 작동하며, 검색 속도를 획기적으로 향상시킬 수 있음

## 원문 기반 개념 정리

### 1. 인덱스란?

인덱스(Index)는 데이터베이스에서 원하는 데이터를 빠르게 찾기 위해 사용하는 자료구조

책의 "색인"처럼 작동하며, 검색 속도를 획기적으로 향상시킬 수 있음

기본적으로 springboot에서 JPA로 자동으로 인덱스가 생성되는 것은 BTREE 인덱스를 따름

✅ 인덱스의 장점

빠른 검색 속도

정렬/필터링 최적화

조인 성능 향상

❗️단점

인덱스를 많이 만들수록 쓰기(INSERT/UPDATE) 성능 저하

디스크 공간 추가 사용

### 2. B-Tree 인덱스와 조회 방식 비교

BTREE 인덱스

📌 인덱스가 없는 경우 (Full Table Scan)

데이터를 맨 앞부터 끝까지 하나씩 비교하며 검색

시간 복잡도: O(n)

📌 인덱스가 있는 경우 (B-Tree)

MySQL은 기본적으로 B-Tree 인덱스를 사용

이진 탐색 구조로 빠르게 원하는 값을 찾아감

시간 복잡도: O(log n)

위의 그림에서 8이라는 데이터를 찾기 위해서 7< 8 < 15, 8 < 9 로 2번만 판단하면 됨. -> 모든 열을 다 조회하는 것이 아닌, 위의 예시에서 모든 데이터에 대해 최대 2번만에 접근 가능

예를 들어, 100만 명 중 한 명의 이메일을 검색할 때:

❌ 인덱스 없음: 100만 명 전부 비교

✅ 인덱스 있음: 몇 번만 비교해도 찾음 (로그 탐색)

### 3. 인덱스를 사용할 수 없는 경우: LIKE '%abc%'

📌 이런 쿼리는 인덱스를 사용할 수 없음

```sql
SELECT * FROM users WHERE username LIKE '%hong';
```

%가 앞에 있으면 MySQL이 B-Tree 인덱스를 사용할 수 없음

이유: 트리의 시작 지점을 알 수 없기 때문

✅ 인덱스를 사용하려면

```sql
SELECT * FROM users WHERE username LIKE 'hong%'; # ✅ 사용 가능
```

🔁 해결 방법

중간 검색이 필요하다면 Full-Text Index를 고려

### 4. MySQL에서 인덱스 설정 & 사용 확인 방법

✅ 인덱스 생성

```text
CREATE INDEX idx_users_email ON users(email);
```

✅ 인덱스 확인

```text
SHOW INDEX FROM users;
```

✅ 인덱스 사용 확인 (EXPLAIN)

```sql
EXPLAIN SELECT * FROM users WHERE email = 'abc@example.com';
```

key에 인덱스 이름이 보이면 실제 사용 중!!!

### 5. Primary 키 & Foreign 키의 자동 인덱스 생성

📌 외래키도 JPA가 JOIN 성능 향상을 위해 자동으로 인덱스를 생성

### 6. Spring Boot 엔티티에서 인덱스 자동 생성 설정

✅ 방법 1: @Column(unique = true)

```text
@Column(unique = true) private String email;
```

→ Hibernate가 자동으로 UNIQUE 인덱스 생성

✅ 방법 2: @Table(uniqueConstraints = {...})

```text
@Table(uniqueConstraints = { @UniqueConstraint(columnNames = {"club_id", "user_id"}) })
```

→ 복합 유니크 인덱스 생성 (예: 동일 동아리에 중복 가입 방지)

⚠️ 주의: 둘 다 동시에 쓰면 중복 인덱스가 생성됨!! -> 불필요(성능 저하)

@Column(unique = true) 또는 @UniqueConstraint 중 하나만 사용 권장

### 7. 실전 예시: 이메일로 사용자 조회

```text
Optional<User> findByEmail(String email);
```

JPA → Hibernate → SQL 변환:

```sql
SELECT * FROM users WHERE email = 'abc@example.com';
```

email 컬럼에 인덱스가 있다면 빠르게 검색됨

EXPLAIN으로 인덱스 사용 여부 확인 가능

이메일 인증으로 통해 아이디나 비밀번호 찾기 기능을 지원하는 로그인 기능의 경우, 이메일 인덱스를 활용해 조회 속도를 높일 수 있음

## 관련 글

- [[blog/SQL/index|SQL]]
- [[blog/SQL/SQL- ORM에서의 N + 1 문제|[SQL] ORM에서의 N + 1 문제]]
- [[blog/JAVA/SpingBoot- Api 호출시 Redis를 활용한 캐시 저장|[SpingBoot] Api 호출시 Redis를 활용한 캐시 저장]]
- [[blog/DOCKER/Docker- Docker를 사용해서 Spring boot + React 배포하기 ( 1 )|[Docker] Docker를 사용해서 Spring boot + React 배포하기 ( 1 )]]
