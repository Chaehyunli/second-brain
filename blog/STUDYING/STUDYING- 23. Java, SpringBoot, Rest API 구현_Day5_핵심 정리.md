---
title: "[STUDYING] 23. Java, SpringBoot, Rest API 구현_Day5_핵심 정리"
created: 2026-08-15
updated: 2026-08-15
type: blog-post
tags: ["blog", "technical-writing"]
category: "STUDYING"
published: 2026-08-14
source_url: https://ch010104.tistory.com/340
---
# [STUDYING] 23. Java, SpringBoot, Rest API 구현_Day5_핵심 정리

## 원문

https://ch010104.tistory.com/340

## 노트 유형

`guide`

## 적용 목적과 전제조건

관계형 데이터베이스의 테이블과 1:1로 매핑되는 자바 클래스를 의미함. 클래스 하나가 테이블 하나에 대응되고, 클래스의 인스턴스 하나가 테이블의 행(row) 하나에 대응됨.

@Entity : 이 클래스를 JPA가 관리할 엔티티(테이블)로 지정

## 구현 절차·검증·주의점

### Entity

관계형 데이터베이스의 테이블과 1:1로 매핑되는 자바 클래스를 의미함. 클래스 하나가 테이블 하나에 대응되고, 클래스의 인스턴스 하나가 테이블의 행(row) 하나에 대응됨.

주요 어노테이션 세 가지로 기본 구조를 구성함.

@Entity : 이 클래스를 JPA가 관리할 엔티티(테이블)로 지정

@Id : 기본키(Primary Key)로 사용할 필드에 부여

@Column : 자바 필드를 DB 테이블의 특정 컬럼으로 매핑. 예) @Column(name="user_name", nullable=false, length=50) → user_name VARCHAR(50) NOT NULL

```java
// User.java
@Entity
@Table(name = "users")
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "user_name", nullable = false, length = 50)
    private String name;
}
```

### Entity와 Table 이름 매핑

JPA는 엔티티 클래스·필드 이름이 카멜케이스(camelCase)로 작성되어 있을 때, DB 테이블명·컬럼명을 자동으로 스네이크케이스(snake_case)로 변환함.

예) 필드명 userName → DB 컬럼명 user_name

명시적으로 이름을 지정하려면 @Table(name = "...") 또는 @Column(name = "...")을 직접 사용함.

```java
// User.java - 명시적 이름 매핑 예시
@Entity
@Table(name = "users")          // 테이블명을 snake_case로 명시
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "user_name")  // camelCase → snake_case 명시적 매핑
    private String userName;

    @Column(name = "user_email") // 명시적 매핑
    private String userEmail;

    @Column(name = "total_price") // 명시적 매핑
    private BigDecimal totalPrice;
}
```

### ORM (Object-Relational Mapping)

객체와 관계형 데이터베이스 간의 매핑을 자동으로 처리해주는 기술임. ORM을 사용하면 개발자가 SQL을 직접 작성하지 않아도 엔티티 객체를 통해 DB 작업을 수행할 수 있음.

대표적인 ORM 구현체로 Hibernate가 있으며, 자바 클래스의 각 필드가 DB 테이블의 컬럼으로 자동 매핑됨.

아래 표는 객체 모델과 관계형 테이블의 대응 관계를 보여줌.

아래 예시처럼 자바 클래스에 어노테이션을 붙이면, ORM이 이를 읽어 대응하는 DDL을 자동으로 생성함.

```java
// User.java
@Entity
@Table(name = "users")
@Data
@NoArgsConstructor
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, length = 100)
    private String name;

    @Column(unique = true, nullable = false, length = 150)
    private String email;
}
```

```sql
-- ORM이 자동 생성하는 DDL
CREATE TABLE users (
    id    BIGINT AUTO_INCREMENT PRIMARY KEY,
    name  VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL
);
```

### JPA (Java Persistence API)

ORM 기술에 대한 자바 표준 명세(인터페이스 + 어노테이션)임. JPA 자체는 구현체가 아니고, Hibernate·EclipseLink 등의 구현체가 실제 동작을 담당함. Spring Boot에서는 기본적으로 Hibernate를 사용하며 다른 구현체로 교체도 가능함.

계층별 호출 흐름은 다음과 같음.

### [참고] JPA vs JDBC

JDBC(Java Database Connectivity)는 자바에서 데이터베이스에 접근하기 위한 표준 API로, SQL을 직접 작성하고 실행하는 방식임. JPA는 이 JDBC 위에 ORM 계층을 얹은 것임.

### Database 연결 설정 (application.yml)

Spring Boot에서 JPA 및 데이터베이스 연결 정보는 application.yml에 설정함.

아래는 H2 인메모리 DB를 사용하는 개발/테스트 환경 기본 설정 예시임.

```text
# application.yml - H2 기반 설정 예시
spring:
  datasource:
    url: jdbc:h2:mem:testdb
    driver-class-name: org.h2.Driver
    username: sa
    password:
  h2:
    console:
      enabled: true
      path: /h2-console     # H2 콘솔 기본 경로
  jpa:
    hibernate:
      ddl-auto: create-drop # 앱 시작 시 테이블 생성, 종료 시 삭제
    show-sql: true          # JDBC로 실행되는 실제 SQL을 System.out에 출력
    defer-datasource-initialization: true
  sql:
    init:
      mode: always
```

주요 설정 항목 정리.

ddl-auto : 스키마 자동 생성·관리 방식. create, create-drop, update, validate 등을 선택 가능

show-sql: true : 엔티티에서 JDBC로 전달되는 실제 SQL 쿼리를 콘솔에 출력

h2.console : H2 웹 콘솔 활성화, 기본 경로는 /h2-console

### Database 연결 설정 - HikariCP 커넥션 풀

Spring Boot 2.0부터 기본 데이터베이스 커넥션 풀로 HikariCP를 사용함. 세밀한 커넥션 풀 설정이 필요할 때 hikari 속성으로 조정 가능함.

```text
# application.yml - HikariCP 튜닝 (선택)
spring:
  datasource:
    hikari:
      maximum-pool-size: 10    # 최대 커넥션 수
      minimum-idle: 2          # 최소 유휴 커넥션 수
      connection-timeout: 30000 # 커넥션 획득 대기 시간(ms)
      idle-timeout: 600000     # 유휴 커넥션 유지 시간(ms)
```

HikariCP의 동작 원리는 다음과 같음.

```text
애플리케이션
  ↓ (DataSource 요청)
HikariCP (Connection Pool)
  - 미리 만들어둔 DB Connection을 보관
  - 필요 시 getConnection()으로 제공
  - 사용 후 close() → 실제로는 풀에 반납
  ↓
JDBC 드라이버
  ↓
Database
```

### [참고] MariaDB 기반 JPA 설정

```text
# application.yml - MariaDB 연결 예시
spring:
  jpa:
    open-in-view: true
    generate-ddl: true
    show-sql: false
  datasource:
    url: jdbc:mariadb://localhost:3306/skala?allowMultiQueries=true
    username: admin
    password: xxxx
    driver-class-name: org.mariadb.jdbc.Driver
    hikari:
      idle-timeout: 30000
      max-lifetime: 30000
      maximum-pool-size: 20
      connection-timeout: 10000
```

### JPA 주요 어노테이션 목록

### JPA 어노테이션 - @Entity

해당 클래스를 JPA가 관리하는 엔티티(테이블)로 지정하며, 자바 클래스와 데이터베이스 테이블을 1:1로 매핑하는 역할을 함. @Entity가 선언된 클래스는 JPA의 CRUD 대상이 되고, Persistence Context 안에서 생명주기가 관리됨.

유의 사항.

@Entity가 붙은 클래스는 반드시 기본 생성자(파라미터 없는 생성자)가 필요함

@Entity만 선언하면 클래스 이름이 그대로 테이블명으로 매핑됨

실제 운영에서는 테이블명과 클래스명이 다를 수 있으므로, 보통 @Table을 함께 사용해 테이블명을 명시함

```java
// Stock.java
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity                         // 이 클래스를 JPA가 관리하는 엔티티로 지정
@Table(name = "stocks")         // (선택) stocks 테이블에 매핑
public class Stock {

    @Id
    private String ticker;      // 주식 고유 코드 (ex: "AAPL")

    private String name;        // 주식 이름 (ex: "Apple Inc.")
    private String market;      // 시장 구분 (ex: "NASDAQ")

// getter, setter 등 생략
}
```

### JPA 어노테이션 - @Table

@Entity로 지정한 클래스가 어느 DB 테이블과 매핑될지를 명시함. 테이블 이름이 클래스명과 다를 때 사용하거나, 스키마 지정 등 추가 설정이 필요할 때 사용함. 생략 가능하며, 생략 시 클래스명이 테이블명으로 사용됨.

```java
// Stock.java - schema까지 명시하는 예시
@Entity
@Table(
    name   = "stocks",
    schema = "skala"
)
public class Stock {
    @Id
    private String ticker;
    private String name;
    private String market;
}
```

### JPA 어노테이션 - @Id

엔티티의 기본키(Primary Key) 필드를 지정함. JPA는 모든 엔티티에 반드시 하나 이상의 @Id가 필요함. @Id로 지정된 필드를 통해 엔티티 객체의 고유성이 보장됨.

단일 기본키와 자동 생성 기본키 두 가지 패턴이 주로 사용됨.

```java
// 단일 필드 기본키 - 비즈니스 키(ticker)를 직접 PK로 사용
@Entity
@Table(name = "stocks")
public class Stock {
    @Id
    private String ticker;  // 예: "AAPL"

    private String name;
    private String market;
}
```

```java
// 자동 생성 기본키 - DB의 auto_increment로 PK 자동 할당
import javax.persistence.*;

@Entity
@Table(name = "transactions")
public class Transaction {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;        // 자동 증가되는 기본키

    private String ticker;
    private int quantity;
    private double price;
    private LocalDateTime date;
}
```

### JPA 어노테이션 - @Id (복합키)

두 개 이상의 컬럼 조합이 고유해야 하는 경우에 복합키를 사용함. @Embeddable 클래스로 복합키 타입을 정의하고, 엔티티에서 @EmbeddedId로 참조하는 방식임.

```java
// UserStockId.java - 복합키 클래스
@Embeddable
public class UserStockId implements Serializable {
    private Long userId;
    private String ticker;
}

// UserStock.java - 복합키를 사용하는 엔티티
@Entity
@Table(name = "user_stocks")
public class UserStock {
    @EmbeddedId
    private UserStockId id;  // 복합키 참조

    private int quantity;
}
```

위 엔티티에 대응하는 테이블 DDL은 다음과 같음.

```sql
CREATE TABLE user_stocks (
    user_id  BIGINT       NOT NULL,
    ticker   VARCHAR(255) NOT NULL,
    quantity INT          NOT NULL,
    PRIMARY KEY (user_id, ticker)   -- 복합 PK
);
```

Repository 선언 시 제네릭 두 번째 타입에 복합키 클래스를 지정함.

```text
public interface UserStockRepository extends JpaRepository<UserStock, UserStockId> {}
```

복합키로 조회하는 예시.

```text
UserStockId id = new UserStockId();
id.setUserId(1L);
id.setTicker("AAPL");

Optional<UserStock> result = userStockRepository.findById(id);
result.ifPresent(s -> System.out.println(s.getQuantity()));
```

### JPA 어노테이션 - @GeneratedValue

기본키(PK) 값을 자동으로 생성하는 전략을 지정할 때 사용하며, 반드시 @Id와 함께 사용함. DB의 auto_increment, 시퀀스, 별도 테이블 등 다양한 자동 생성 방식을 지원함.

주요 속성.

strategy : PK 자동 생성 방식 지정

generator : 시퀀스/테이블 방식일 때 커스텀 생성기 이름 지정

strategy 값별 동작 차이.

```java
// Transaction.java - MySQL/MariaDB 기준 IDENTITY 전략
@Entity
@Table(name = "transactions")
public class Transaction {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;      // DB의 auto_increment로 자동 생성

    private String ticker;
    private int quantity;
    private double price;
    private LocalDateTime tradedAt;
}
```

### JPA 어노테이션 - @Column

엔티티 필드를 데이터베이스의 컬럼과 매핑할 때 사용함. 컬럼 이름·길이·null 허용 여부·유니크 여부·숫자 자릿수 등 DB 컬럼 속성을 세밀하게 조정할 수 있음.

종합 사용 예시.

```java
// User.java
@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "user_name", nullable = false, length = 30)
    private String name;       // DB 컬럼: user_name, NOT NULL, 최대 30자

    @Column(unique = true, length = 50)
    private String email;      // DB 컬럼: email, UNIQUE, 최대 50자

    @Column(length = 100)
    private String password;   // 비밀번호 컬럼, 길이 100자 제한

    @Column(updatable = false)
    private LocalDateTime createdAt; // 최초 생성일(수정 불가)
}
```

숫자 자릿수 지정 예시 — precision은 전체 자릿수, scale은 소수점 이하 자릿수를 의미함.

```java
// Transaction.java - 소수 자릿수 지정
@Entity
public class Transaction {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(precision = 12, scale = 4)
    private BigDecimal price;  // 최대 9999999999.9999까지 표현 가능
}
```

### JPA 어노테이션 - @Enumerated

Enum(열거형) 타입 필드를 데이터베이스에 어떻게 저장할지 지정할 때 사용함. 자바의 enum 타입은 RDB에 직접 저장할 수 없으므로, 숫자(ORDINAL) 또는 문자열(STRING)로 변환하여 저장함. 실무에서는 STRING 방식을 강력 권장함.

ORDINAL 방식은 enum 선언 순서에 따른 정수를 저장하므로, 나중에 enum 순서가 바뀌면 기존 DB 데이터와 불일치가 발생하는 문제가 있음. STRING 방식은 enum 이름 자체를 문자열로 저장하므로 안전함.

```java
// StockStatus.java
public enum StockStatus {
    ACTIVE,
    INACTIVE
}

// Stock.java
@Entity
public class Stock {
    @Id
    private String ticker;

    @Enumerated(EnumType.STRING) // "ACTIVE" 또는 "INACTIVE"로 저장됨
    @Column(length = 10)
    private StockStatus status;
}
```

### JPA 어노테이션 - @Lob

대용량 데이터(텍스트 또는 바이너리 데이터)를 DB에 저장할 때 사용함. 필드 타입에 따라 자동으로 CLOB 또는 BLOB으로 매핑됨.

CLOB (Character Large Object) : 대용량 텍스트. ex) 긴 설명, 본문 등. String 타입 필드에 매핑

BLOB (Binary Large Object) : 대용량 바이너리. ex) 이미지, 파일 등. byte[] 타입 필드에 매핑

```java
// User.java
@Entity
public class User {
    @Id
    @GeneratedValue
    private Long id;

    private String name;

    @Lob
    private String description;   // @Lob + String → CLOB(대용량 텍스트)으로 매핑

    @Lob
    private byte[] profileImage;  // @Lob + byte[] → BLOB(대용량 바이너리)으로 매핑
}
```

@Lob vs @Column(columnDefinition = "TEXT") 비교.

@Lob : JPA 표준 방식, DB 독립적. 유지보수·확장성에 유리함

columnDefinition : DB 종속적, 유연성이 낮음. 특별한 경우에만 사용함

### JPA 어노테이션 - @Transient

엔티티 필드 중에서 DB 컬럼과 매핑하지 않을 필드에 사용함. 해당 필드는 DB 테이블에 컬럼으로 생성되지 않으며, JPA의 영속화(저장/조회) 대상이 아님을 명시함.

계산값, 임시 데이터, 화면 출력 전용 속성, 비밀번호 확인 필드 등에 주로 활용함.

```java
// User.java
@Entity
public class User {
    @Id
    @GeneratedValue
    private Long id;

    private String password;

    @Transient
    private String passwordConfirm; // 입력폼 전용, DB 저장 X
}
```

실무 참고 사항 — DTO 객체를 사용하여 내부에서 임시 저장하고, 실제 데이터베이스 저장 시에만 Entity를 사용하는 구조로 설계하면 @Transient가 필요한 상황 자체가 줄어듦.

### JPA 어노테이션 - @Transient

엔티티 필드 중에서 DB 컬럼과 매핑하지 않을 필드에 사용함. 해당 필드는 DB 테이블에 컬럼으로 생성되지 않으며, JPA의 영속화(저장/조회) 대상이 아님을 명시함.

계산값, 임시 데이터, 화면 출력 전용 속성, 비밀번호 확인 필드 등에 주로 활용함.

```java
// User.java
@Entity
public class User {
    @Id
    @GeneratedValue
    private Long id;

    private String password;

    @Transient
    private String passwordConfirm; // 입력폼 전용, DB 저장 X
}
```

실무 참고 사항 — DTO 객체를 사용하여 내부에서 임시 저장하고, 실제 데이터베이스 저장 시에만 Entity를 사용하는 구조로 설계하면 @Transient가 필요한 상황 자체가 줄어듦.

### JPA Repository 정의

JPA에서 Repository는 데이터베이스와 직접적인 상호작용을 담당하는 인터페이스임. Spring Data JPA가 제공하는 JpaRepository를 상속하면 기본적인 CRUD(Create, Read, Update, Delete) 기능을 별도의 SQL 코드 없이 사용할 수 있음.

```java
// com/example/study/repository/UserRepository.java
package com.example.study.repository;

import com.example.study.model.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface UserRepository extends JpaRepository<User, Long> {
// JpaRepository를 상속받으면 기본적인 CRUD 메서드 제공
// save(), findById(), findAll(), delete() 등
}
```

내부 동작 원리 — JpaRepository가 구현한 메서드(findAll, findById, save, delete)를 상속받아 제공하는 구조임. Spring이 UserRepository를 상속받은 Proxy를 동적으로 생성해서 Bean으로 등록함.

### JPA Repository 계층 구조

Spring Data JPA가 제공하는 인터페이스로, JPA를 더 쉽게 다루기 위한 추상화 계층임. 개발자가 DAO(Data Access Object)를 직접 구현하지 않아도 데이터베이스 조작이 가능한 인터페이스 기반의 프레임워크임.

상속 계층은 위에서 아래로 다음과 같이 구성됨.

### JPA Repository 기본 Method

JpaRepository 선언 시 자동으로 구성되는 기본 메서드 목록.

삭제 메서드 성능 비교 — deleteAllById()는 엔티티를 먼저 조회한 후 삭제하는 반면, deleteAllByIdInBatch()는 조회 없이 한 번의 SQL 쿼리로 바로 삭제함. 대량 데이터 삭제 시 deleteAllByIdInBatch()가 성능이 더 좋음.

### JPA Repository 기본 Method - flush()

저장·수정 관련 메서드 시그니처와 리턴값 정리.

flush()는 JPA에서 영속성 컨텍스트(Persistence Context)의 변경 내용을 즉시 DB에 반영(동기화)하도록 하는 메서드임. JPA는 기본적으로 트랜잭션이 커밋(commit)되는 시점에 자동으로 flush를 호출하여 DB에 쿼리를 실행함. 즉, 저장·수정·삭제를 해도 즉시 DB 쿼리가 실행되는 것이 아니라, 영속성 컨텍스트에 반영된 뒤 트랜잭션이 커밋될 때 한 번에 반영(Flush)되는 구조임.

flush()를 직접 호출하는 대표적인 상황.

DB에 즉시 쿼리를 반영해야 할 때 — 바로 이후에 Native Query 또는 다른 JDBC 작업을 수행해야 할 때, 변경 내용을 DB에 먼저 반영해야 하는 경우

트랜잭션 내에서 쿼리 동작 순서를 명확히 해야 할 때 — 예) insert 후 select를 실행해야 할 때, 영속성 컨텍스트의 변경이 DB에 반영되어야 원하는 결과가 나올 때

JPA 이벤트 리스너나 복잡한 이벤트 처리 로직 — 엔티티의 상태를 DB에 반영해야만 이벤트가 정상적으로 처리되는 경우

### JPA 사용자 쿼리 메서드 (Query Methods)

JPA가 정한 약속된 메서드 명명 규칙에 맞춰 인터페이스에 선언만 하면 동적으로 쿼리가 자동 생성되는 방식임.

장점 : 쉽고 빠르며, 실수 방지. 단순 조건·검색·정렬에 매우 효율적

단점 : 조인, 복잡한 논리(AND/OR 혼합), 그룹/집계, 복잡한 동적 쿼리에는 적합하지 않음. 이름이 너무 길어지면 @Query로 전환을 고려함

JpaRepository 인터페이스에 메서드를 선언만 하면 실제 쿼리 구현체가 자동 생성됨.

```text
// UserRepository.java - 쿼리 메서드 선언 예시
public interface UserRepository extends JpaRepository<User, Long> {

// 1. 이름과 나이로 사용자 찾기 → WHERE name = ? AND age > ?
    List<User> findByNameAndAgeGreaterThan(String name, int age);

// 2. 상태와 이메일로 사용자 검색(첫 번째 1개만) → WHERE status = ? AND email = ? LIMIT 1
    Optional<User> findByStatusAndEmail(UserStatus status, String email);

// 3. 생성일 기준 정렬, 페이징 → WHERE created_at > ? (+ 페이징)
    Page<User> findByCreatedAtAfter(LocalDateTime date, Pageable pageable);
}
```

### JPA 메서드를 위한 사전 정의 키워드 (1/2) — 동사 키워드

리턴 타입은 선언에 따라 자동 구성됨. 단건 조회 시 Optional`<T>` 사용을 권장하며, 여러 건 리턴 시에는 Optional을 사용하지 않음.

### JPA 메서드를 위한 사전 정의 키워드 (2/2) — 조건 연산자

### [참고] JPA 사용자 쿼리 메서드 전체 키워드 정리

### JPA 사용자 쿼리 메서드 - @Query 어노테이션 (1/2)

메서드 명명 방식으로 표현하기 어려운 복잡한 쿼리를 직접 작성할 때 사용함. 복잡 조건·조인·집계(AVG, COUNT)·부분 컬럼 추출 등에 적합함. 동적 조건이 많으면 코드가 복잡해지고 컴파일러 타입 체크가 어렵다는 단점이 있음. 반복되는 복잡 쿼리는 QueryDSL이나 커스텀 리포지토리로 이전을 고려함.

JPQL(Java Persistence Query Language)은 JPA Entity 객체 명과 필드명을 사용하는 객체 지향 쿼리 언어임. 특정 DB 종류(MySQL, Oracle, PostgreSQL 등)에 종속되지 않음.

```sql
// UserRepository.java - @Query(JPQL) 예시

// JPQL - 엔티티 객체 대상으로 쿼리 (테이블명 아닌 클래스명 User 사용)
@Query("select u from User u where u.status = :status and u.age >= :minAge")
List<User> findActiveUsers(@Param("status") UserStatus status, @Param("minAge") int minAge);

// 조인 포함 (User, Order 엔티티 조인)
@Query("select u from User u join u.orders o where o.price > :minPrice")
List<User> findByOrderPriceGreaterThan(@Param("minPrice") int minPrice);

// 특정 컬럼만 추출
@Query("select u.name, u.email from User u where u.status = :status")
List<Object[]> findUserNamesAndEmails(@Param("status") UserStatus status);
```

→ column 명이 아닌 객체의 이름 user u를 기준으로 작성

### JPA 사용자 쿼리 메서드 - @Query 어노테이션 (2/2)

Native SQL(nativeQuery = true)은 실제 DB의 테이블명 및 컬럼명을 그대로 사용하는 방식임. DB 전용 함수, 윈도우 함수(OVER()), 복잡한 집계 쿼리 등 DB 특화 기능을 그대로 활용할 때 사용함.

```sql
// UserRepository.java - @Query(nativeQuery = true) 예시

// Native SQL - 실제 테이블명(users) 사용
@Query(value = "SELECT * FROM users u WHERE u.status = :status AND u.age >= :minAge",
       nativeQuery = true)
List<User> findActiveUsers(@Param("status") UserStatus status, @Param("minAge") int minAge);

// 조인 포함 (users, orders 테이블 직접 조인)
@Query(value = "SELECT DISTINCT u.* FROM users u " +
               "JOIN orders o ON u.id = o.user_id " +
               "WHERE o.price > :minPrice", nativeQuery = true)
List<User> findByOrderPriceGreaterThan(@Param("minPrice") int minPrice);

// 특정 컬럼만 추출
@Query(value = "SELECT u.name, u.email FROM users u WHERE u.status = :status",
       nativeQuery = true)
List<Object[]> findUserNamesAndEmails(@Param("status") UserStatus status);
```

Native SQL을 사용하면 Database 의존 관계가 발생하므로 가급적 사용을 최소화해야 함.

### [참고] JPQL 주요 함수

### 영속성 컨텍스트 (Persistence Context) 상태 관리

Entity를 저장하거나 검색하는 경우에는 영속화(Persistence Context) 상태로 전환됨. 엔티티는 생명주기에 따라 네 가지 상태를 가짐.

상태 전이 흐름.

각 상태별 코드 예시.

```text
// 비영속 상태 - 순수 자바 객체 생성
Member member = new Member();
member.setId("member1");
member.setUsername("회원1");

// 영속 상태 - persist() 호출로 영속성 컨텍스트에 등록
EntityManager em = emf.createEntityManager();
em.getTransaction().begin();
em.persist(member); // 이 시점에 영속 컨텍스트에 등록, 아직 DB에 INSERT 되지 않음

// 준영속 상태 - 영속성 컨텍스트에서 분리
em.detach(member);

// 삭제 상태 - 삭제 표시
em.remove(member);
```

### 영속성 컨텍스트 상태 전이 핵심 메서드

영속성 컨텍스트 상태 다이어그램에서 각 화살표에 해당하는 메서드의 역할을 정리하면 다음과 같음.

flush()는 트랜잭션 커밋 시점에 자동 호출되지만, 필요에 따라 수동으로 직접 호출할 수도 있음. flush() 이후에도 영속성 컨텍스트 자체는 유지되며, 엔티티 상태가 초기화되지는 않음.

### 관계 연관 매핑

객체 지향 언어의 객체 참조와 관계형 데이터베이스의 외래키(FK) 간의 차이를 연결해 주는 과정임.

객체 모델에서는 Member 클래스가 Team team 필드로 Team 객체를 직접 참조하는 반면, 테이블 모델에서는 MEMBER 테이블이 TEAM_ID(FK) 컬럼으로 TEAM 테이블을 참조함. JPA의 관계 매핑 어노테이션이 이 두 방식의 차이를 자동으로 연결해줌.

### 관계 매핑 : ManyToOne

여러 Member가 하나의 Team에 속하는 N:1 관계임. FK가 있는 쪽(MEMBER 테이블)이 연관관계의 주인이 되며, @ManyToOne과 @JoinColumn을 함께 사용함.

```java
// Member.java - 연관관계 주인 (FK 보유)
@Entity
public class Member {
    @Id @GeneratedValue
    private Long id;

    private String username;

    @ManyToOne                          // N:1 관계 선언
    @JoinColumn(name = "TEAM_ID")       // MEMBER 테이블의 FK 컬럼명 지정
    private Team team;
}
```

```java
// Team.java
@Entity
public class Team {
    @Id @GeneratedValue
    @Column(name = "TEAM_ID")
    private Long id;

    private String name;
}
```

### 관계 매핑 : OneToMany

하나의 Team이 여러 Member를 가지는 1:N 관계임. @OneToMany는 FK가 없는 쪽(Team)에 선언하며, mappedBy 속성으로 연관관계의 주인 필드명을 지정함. DB에서 FK는 여전히 MEMBER 테이블에 존재함.

```java
// Team.java - 연관관계의 비주인 (mappedBy 사용)
@Entity
public class Team {
    @Id @GeneratedValue
    @Column(name = "TEAM_ID")
    private Long id;

    private String name;

    @OneToMany(mappedBy = "team")               // Member 엔티티의 team 필드가 연관관계 주인
    private List<Member> members = new ArrayList<>();
}
```

mappedBy = "team"은 "Member 클래스의 team 필드가 이 관계의 주인"임을 의미함. 실제 FK 관리(INSERT/UPDATE)는 @ManyToOne을 가진 Member 쪽에서 이루어짐.

→ @OneToMany(mappedBy = "team", fetch = FetchType.LAZY) 처럼 사용시, 지연 로딩이 됨(Team을 가저올 때, Member를 모두 다 가져오는 것 비효율적)

### JPA 어노테이션 - 관계 매핑

객체 간의 관계를 데이터베이스 테이블의 외래키(FK)와 연결하는 방법을 정의함. 다중성(1:1, 1:N, N:1, N:M)과 방향성(단방향, 양방향)을 조합하여 설정함.

어노테이션 관계 대표 예시

연관관계의 주인은 FK가 있는 쪽이 됨.

@OneToMany(mappedBy = "user")라면 추가/삭제/변경의 주체는 @ManyToOne을 가진 Entity임

SQL은 항상 주체 쪽 변경을 기준으로 생성됨

### FetchType.LAZY vs EAGER

연관관계 매핑 시 연관된 엔티티를 언제 DB에서 조회할지를 결정하는 전략임.

@OneToMany의 기본값 : FetchType.LAZY

@ManyToOne의 기본값 : FetchType.EAGER

FetchType.LAZY 처리 흐름 예시.

```text
// Product.java - LAZY 설정
@ManyToOne(fetch = FetchType.LAZY)  // N:1 관계, 지연 로딩
@JoinColumn(name = "user_id")       // products 테이블에 user_id FK 컬럼 생성
private User user;                  // 이 상품을 등록한 사용자
```

```sql
// LAZY 동작 확인
em.getTransaction().begin();

Product p = em.find(Product.class, 1L); // Product SELECT, user는 프록시로 채움

User u = p.getUser();           // 아직 쿼리 안 나감 (프록시 반환)
String name = u.getName();      // 이 시점에 User SELECT 쿼리 발생 (초기화)

em.getTransaction().commit();
```

LAZY인 경우 Product를 조회할 때 user는 즉시 쿼리로 가져오지 않고 Proxy로 채움. getName()처럼 실제 필드에 접근하는 순간 별도 SELECT가 나가며 초기화됨.

### EntityManager

JPA에서 엔티티(객체)를 DB와 동기화하기 위해 사용하는 핵심 관리 객체임. 엔티티의 생성·조회·수정·삭제(CRUD)와 트랜잭션, 영속성 컨텍스트 관리 등을 수행하며, JPA가 DB와 대화하는 모든 기능의 중심임.

웹 애플리케이션이 구동되는 시점에 EntityManagerFactory를 생성하여 보유하고 있으며, 사용자의 요청이 있을 때 EntityManager를 생성하여 커넥션 풀(Connection Pool)을 사용해서 DB를 핸들링함. 각 요청(스레드)마다 별도의 EntityManager 인스턴스가 할당됨.

### EntityManager의 주요 메서드

Spring Boot + JPA(Hibernate)에서 가장 자주 쓰는 메서드는 find, persist, merge, remove, flush, clear임.

### EntityManager vs JpaRepository

JpaRepository는 EntityManager를 더 쓰기 쉽게 감싸놓은 상위 수준의 추상화 도구임. 내부적으로 JpaRepository는 결국 EntityManager를 사용해 동작함.

### 영속성 컨텍스트 (Persistence Context)

EntityManager는 하나의 트랜잭션별로 Persistence Context를 생성·관리함. @Transactional을 사용하여 Persistence Context를 활성화함.

영속성 컨텍스트는 엔티티 객체를 1차 캐시로 보관하여, 해당 엔티티와 데이터베이스 레코드를 동기화하기 위해 상태를 추적·관리하는 메모리 공간임. findById, findAll 등으로 DB에서 조회한 엔티티는 Persistence Context에 올라와 관리되며, 트랜잭션 커밋 시 flush를 통해 DB에 반영됨.

### 영속성 컨텍스트 (Persistence Context) 역할

JPA의 작업장을 모아두는 1차 캐시 + 변경 감지 시스템임.

EntityManager와 Persistence Context의 관계 — EntityManager는 단순한 컨트롤러이고, Persistence Context는 실제 엔티티를 저장하고 관리하는 공간임. 둘은 1:1로 대응됨.

### [참고] JpaRepository와 EntityManager 내부 호출 흐름

JpaRepository는 인터페이스만 선언해도 자동으로 구현체가 생성되는데, Proxy pattern으로 EntityManager를 생성하여 호출하는 구조로 지원함. userRepository.save(user) 호출 시 내부적으로 다음 흐름으로 처리됨.

```sql
1. UserRepository.save(user)
      ↓ proxy를 통해 기본 JpaRepository 호출
2. SimpleJpaRepository.save(user)          -- Spring Data JPA 기본 구현체
      ↓ EntityManager.persist 호출
3. EntityManager.persist(user)             -- JPA 표준 Interface 정의한 구현체
      ↓ Hibernate의 Persistence Context 저장 요청
4. Hibernate: session.persist(user)|flush|commit  -- Hibernate의 Persistence Context 저장
      ↓ JDBC API 호출
5. JDBC: PreparedStatement.executeUpdate() -- JDBC 드라이버
      ↓ SQL 실행 요청
6. Database: (INSERT INTO user VALUES (...))  -- DB에 SQL 실행
```

### EntityManager 사용 예시

모든 메서드에 @Transactional을 설정하여 사용함. Spring에서는 @PersistenceContext로 주입받은 em은 실제 EntityManager가 아니라 Proxy EntityManager임. 요청마다 트랜잭션에 맞는 실제 EntityManager를 대신 호출해주는 구조임.

```java
// UserService.java
@Service
@Transactional  // Class Level 적용 - 모든 메서드에 트랜잭션 적용
public class UserService {

    @PersistenceContext
    private EntityManager em;  // 실제 EntityManager가 아니라 Proxy EntityManager

    public void saveUser() {
        User user = new User("홍길동");
        em.persist(user);       // INSERT 실행 (트랜잭션 commit 시점)
    }

    public User getUser(Long id) {
        return em.find(User.class, id); // SELECT 실행
    }

    public void deleteUser(Long id) {
        User user = em.find(User.class, id);
        em.remove(user);        // DELETE 실행
    }
}
```

### JPA 트랜잭션 (Transaction)

트랜잭션은 데이터베이스에서 일련의 작업들을 하나의 논리적 단위로 묶어서 처리하는 것임. 모든 작업이 성공해야만 실제로 DB에 반영되고, 중간에 오류가 발생하면 전체 작업이 취소(롤백)됨. JPA의 변경 내용(저장/수정/삭제)은 트랜잭션이 있을 때만 데이터베이스에 안전하게 반영됨.

트랜잭션의 원칙 — ACID.

JPA에서는 서비스 계층에서 트랜잭션을 시작하며, 스프링은 @Transactional 어노테이션을 사용해 트랜잭션을 자동 관리함.

### @Transactional

트랜잭션 관리를 지원하는 선언적 어노테이션임. 메서드(또는 클래스)에 붙이면 해당 범위 내의 모든 데이터베이스 작업을 트랜잭션 단위로 처리함. 모든 작업이 성공하면 커밋(commit), 중간에 예외가 발생하면 자동으로 롤백(rollback) 처리됨.

org.springframework.transaction.annotation.Transactional을 사용해야 함.

```java
// UserService.java
@Service
@Transactional(readOnly = true) // class Level 적용 - 기본값을 조회 전용으로 설정
public class UserService {

// 1. 위의 클래스 레벨 설정을 그대로 이어받아 readOnly = true로 동작 (조회 전용)
    public UserProfile getUserProfile(Long userId) {
        return userRepository.findById(userId).orElseThrow();
    }

// 2. 쓰기 작업이 필요한 메서드는 readOnly = false(기본값)로 덮어쓰기
    @Transactional
    public void registerUser(UserDto userDto) {
        userRepository.save(userDto.toEntity());
    }
}
```

readOnly = true 일 때 특징 — 변경 감지(Dirty Checking)와 추적을 수행하지 않기 때문에 성능이 향상됨.

readOnly = false 일 때는 변경을 확인해야하기 때문에 변경 감지(Dirty Checking) 로직이 필요함.

### @Transactional 사용 케이스

DB 변경이 있는 오퍼레이션을 수행하는 서비스 메서드에는 @Transactional을 꼭 사용하는 것이 권장됨. 너무 남발하면 트랜잭션 범위가 넓어져 DB lock·동시성 저하 등 성능 문제가 생길 수 있음.

@Transactional을 붙이지 않으면 save 시 commit이 일어나지 않나? — JpaRepository를 사용하는 경우 기본적으로 save 호출 시 @Transactional을 method에 붙이고 있음. 하지만 원자성 및 성능 저하/비효율이 발생하므로, 서비스 레이어에서 직접 트랜잭션을 관리하는 것이 올바른 방식임.

### [참고] @Transactional 설정 범위 예시

외부 API 호출·파일 IO 등 장시간 작업이 포함된 메서드 전체에 @Transactional을 걸면 트랜잭션 범위가 너무 넓어짐. DB 작업만 별도 메서드로 분리하고 그 메서드에만 @Transactional을 적용하는 것이 올바른 방식임.

```java
// 나쁜 예 - 트랜잭션 범위가 너무 넓음
@Service
public class FileService {

    @Transactional
    public void processAndSave(User user, MultipartFile file) throws IOException {
        String filePath = saveFileToDisk(file);     // 파일 저장 (네트워크/디스크 IO)
        user.setProfileImagePath(filePath);
        userRepository.save(user);                  // DB 저장
        notifyExternalSystem(user);                 // 외부 API 호출
    }
}

// 좋은 예 - 트랜잭션 범위를 DB 작업에만 한정
@Service
public class FileService {

    public void processAndSave(User user, MultipartFile file) throws IOException {
        String filePath = saveFileToDisk(file);             // 파일 저장
        saveUserProfileImagePath(user, filePath);           // DB 저장 (트랜잭션 적용)
        notifyExternalSystem(user);                         // 외부 API 호출
    }

    @Transactional  // DB 오퍼레이션에만 트랜잭션 적용
    public void saveUserProfileImagePath(User user, String filePath) {
        user.setProfileImagePath(filePath);
        userRepository.save(user);
    }
}
```

트랜잭션은 AOP Proxy를 통해 호출되므로, 내부 사용 함수지만 public으로 선언해야 함.

### JPA 트랜잭션 커밋(Commit) 시점

JPA에서 트랜잭션이 커밋되는 시점은 기본적으로 트랜잭션을 시작한 메서드가 성공적으로 종료될 때임. 스프링 환경에서는 @Transactional 어노테이션이 붙은 메서드가 예외 없이 실행을 마치는 시점에 커밋이 발생함.

@Transactional 동작 원리.

스프링에서 서비스 클래스의 메서드에 @Transactional을 붙이면, 스프링 컨테이너는 해당 서비스 객체 대신 트랜잭션 기능이 포함된 프록시(Proxy) 객체를 생성하여 빈(Bean)으로 등록함. 서비스 메서드를 호출하면 실제로는 이 프록시 객체의 메서드가 먼저 호출됨

메서드 시작 시점 : 프록시는 데이터베이스 트랜잭션을 시작(BEGIN)

메서드 종료 시점 : 메서드가 정상적으로 종료되면 프록시는 트랜잭션을 커밋(COMMIT). 메서드 실행 중 예외(기본적으로 RuntimeException)가 발생하면 트랜잭션을 롤백(ROLLBACK) 처리

영속성 컨텍스트(Persistence Context)와 쓰기 지연.

트랜잭션이 시작되면, JPA는 영속성 컨텍스트라는 논리적인 영역을 생성함. 이곳은 엔티티(Entity)를 임시로 저장하고 관리하는 일종의 1차 캐시이자 작업 공간임

repository.save(entity)를 호출하면, 엔티티는 데이터베이스에 바로 저장되는 것이 아니라 영속성 컨텍스트에 저장되고, 실행해야 할 SQL(INSERT, UPDATE, DELETE 등)은 쓰기 지연 SQL 저장소에 쌓이게 됨

이렇게 SQL을 바로 실행하지 않고 모아두는 것을 쓰기 지연(Write-Behind)이라고 함

### 트랜잭션 전파 (Propagation)

트랜잭션이 이미 존재할 때, 현재 실행 중인 메서드에서 트랜잭션을 어떻게 처리할지를 결정하는 옵션임. 기존 트랜잭션에 참여할지, 새로운 트랜잭션을 생성할지, 아니면 트랜잭션 없이 실행할지를 선택함.

### 트랜잭션 전파 오류 - Self Invocation 문제

하나의 클래스 내에서 @Transactional이 붙은 다른 메서드를 호출하면 트랜잭션 전파 설정이 적용되지 않음. 이는 프록시를 거치지 않고 실제 객체의 내부 메서드를 직접 호출하기 때문임.

```java
// 문제 있는 코드 - Self Invocation
@Service
public class UserService {

    @Transactional  // propagation = Propagation.REQUIRED (기본값)
    public void outerMethod() {
// DB 작업 1
        innerMethod(); // 프록시를 거치지 않아 REQUIRES_NEW가 적용되지 않음
    }

    @Transactional(propagation = Propagation.REQUIRES_NEW)
    public void innerMethod() {
// DB 작업 2
    }
}
```

해결 방안 — 트랜잭션 단위가 다른 메서드는 별도의 클래스(Bean)로 분리하여 주입받아 사용함.

### 트랜잭션 전파 오류 - 해결 방안

```java
// OuterService.java - 별도 클래스로 분리하여 DI
@Service
public class OuterService {
    @Autowired
    private InnerService innerService;

    @Transactional  // propagation = Propagation.REQUIRED
    public void outerMethod() {
// DB 작업 1
        innerService.innerMethod(); // AOP Proxy를 통해 호출 → REQUIRED로 처리
// DB 작업 3
    }
}

// InnerService.java
@Service
public class InnerService {
    @Transactional  // propagation = Propagation.REQUIRED
    public void innerMethod() {
// DB 작업 2
// 만약 여기서 예외가 발생하여 롤백 되면, outerMethod의 'DB 작업 1'까지 모두 롤백 됨
    }
}
```

InnerService는 OuterService Bean 생성 시점에 AOP Proxy로 Wrapping된 후 InnerService가 DI되어 개별 트랜잭션으로 처리됨.

### [참고] 트랜잭션 예외와 롤백 규칙

@Transactional은 기본적으로 RuntimeException(Unchecked Exception)과 Error가 발생했을 때만 롤백함.

Checked Exception(Exception을 상속받는)을 try-catch로 잡고 아무것도 하지 않으면, 트랜잭션은 정상적으로 커밋되어 데이터 정합성 문제가 발생할 수 있음

모든 예외(Exception)에 대해 롤백하고 싶다면 rollbackFor 속성을 사용함

```text
@Transactional(rollbackFor = Exception.class)
public void process() throws MyCustomException {
// ... 로직 ...
}
```

예외 계층 구조 정리.

```text
Throwable
├── Error (코드 문제는 알아서 → RuntimeException에 포함)
└── Exception
    ├── RuntimeException (Unchecked Exception)
    │     NullPointerException, IllegalArgumentException 등
    │     → @Transactional 기본 롤백 대상
    └── Non RuntimeException (Checked Exception)
          IOException, FileNotFoundException, ClassNotFoundException,
          SQLException (DB 접근 오류) 등
          → 기본적으로 롤백하지 않음
```

복구 가능한 예외(Recoverable Exception)에 대한 대책 예시.

네트워크 임시 오류 → 재시도

파일 잠김 → 대기 후 재시도

DB Lock 대기 → sleep 후 retry

외부 API → BackOff

### 트랜잭션 동시성 제어 (Consistency Control)

여러 사용자가 동시에 데이터에 접근하고 수정할 때 발생할 수 있는 데이터 불일치 문제(Multi-Thread, Multi-Process)임. JPA에서 동시성 제어(concurrency control)는 @Transactional 자체가 해결해주는 것이 아님.

### 트랜잭션 동시성 제어 - 낙관적 락 (Optimistic Lock)

데이터 충돌이 드물 것이라고 낙관적으로 가정하고, 락을 걸지 않은 채 자유롭게 읽고 수정하되 커밋 시점에 충돌을 감지하여 처리하는 방식임.

장점 : DB에 직접적인 lock을 걸지 않으므로 부하가 적고 성능이 좋음. 읽기 작업이 많은 환경에 유리

단점 : 충돌이 발생하면 개발자가 직접 예외를 처리하고 재시도 로직 등을 구현해야 함

동작 방식.

엔티티에 @Version 어노테이션이 붙은 필드(주로 숫자 타입)를 추가

데이터를 조회할 때 이 버전 정보도 함께 가져옴

데이터를 수정하고 트랜잭션을 커밋할 때, 현재 데이터베이스의 버전과 내가 조회했던 시점의 버전을 비교

버전이 일치하면 데이터를 수정하고 버전을 1 증가시킴

버전이 일치하지 않으면(다른 트랜잭션이 먼저 수정했다는 의미) → ObjectOptimisticLockingFailureException 예외 발생 → 재 실행 과정 필요

```java
// Article.java - 낙관적 락 설정
@Entity
public class Article {
    @Id
    @GeneratedValue
    private Long id;

    private String content;

    @Version
    private Long version; // 버전을 관리할 필드
}
```

@Version을 Entity에 설정하고 @Lock을 @Transactional에서 사용하지 않으면 자동으로 낙관적 Lock으로 동작함.

→ 최근 트렌드는 낙관적 락임

### 낙관적 락 (Optimistic Lock) Retry

낙관적 Lock은 @Transactional이 종료되면서 commit 시점에 다른 곳에서 업데이트를 먼저 했으면 Failure가 발생함. 재 처리를 위해서는 @Retryable을 사용해서 재처리함.

→ 요청이나 작업이 실패했을 때, 바로 다시 찌르지 않고, 시간을 두고 다시 시도하는 전략

```java
// StockService.java - @Retryable로 낙관적 락 충돌 재시도
@Service
@RequiredArgsConstructor
public class StockService {
    private final ProductRepository productRepository;

    @Retryable(
        include = { OptimisticLockingFailureException.class, OptimisticLockException.class },
        maxAttempts = 3,
        backoff = @Backoff(delay = 100, multiplier = 2) // 100ms → 200ms → 400ms 간격으로 재시도
    )
    @Transactional
    public void decreaseStock(Long productId, int qty) {
        var p = productRepository.findById(productId).orElseThrow();
        if (p.getStock() < qty) throw new IllegalArgumentException("재고 부족");
        p.setStock(p.getStock() - qty); // flush/commit 시 버전 체크
    }

    @Recover
    public void recover(OptimisticLockingFailureException e, Long productId, int qty) {
// 재시도 끝나도 실패하면 알림/대안 처리
        throw e;
    }
}
```

### 비관적 락 (Pessimistic Lock)

데이터 충돌이 자주 발생할 것이라고 비관적으로 가정하고, 데이터를 조회하는 순간부터 다른 트랜잭션이 읽거나 수정하지 못하도록 DB에 락을 걸어 충돌을 사전에 차단하는 방식임.

장점 : 데이터 정합성을 확실하게 보장. 충돌이 잦은 환경에서 데이터 무결성을 유지하는 데 효과적

단점 : 데이터베이스에 직접 락을 걸기 때문에 성능 저하가 발생 가능. 다른 트랜잭션의 대기 시간이 길어져 전체적인 시스템 성능에 영향을 주고 데드락 발생 가능

Lock 모드 종류.

PESSIMISTIC_WRITE : 데이터를 수정하기 위해 설정. 다른 트랜잭션은 해당 데이터를 읽거나 쓸 수 없음

PESSIMISTIC_READ : 다른 트랜잭션이 해당 데이터를 수정하는 것을 방지. DB에 따라 읽기는 허용될 수 있음

default는 NONE : 그냥 조회만 하고 DB 락 없음

```sql
// ArticleRepository.java - 비관적 락 사용
public interface ArticleRepository extends JpaRepository<Article, Long> {

    @Lock(LockModeType.PESSIMISTIC_WRITE)
    @Query("select a from Article a where a.id = :id")
    Optional<Article> findByIdWithWriteLock(@Param("id") Long id);
}
```

### REST API 문서화 (springdoc-openapi)

Spring Boot 3.0 이상 버전에서는 springdoc-openapi 라이브러리를 사용하여 API 문서 자동화를 지원함. OpenAPI 3 명세 기반의 문서와 Swagger UI를 자동 생성함.

springdoc : Open API Specification(OAS) 문서를 자동 생성

swagger-ui : 그 문서를 보기 쉽게 시각적으로 표시

의존성 추가 방법 (pom.xml).

xml

```text
<!-- Tomcat 기반 (Spring MVC) OpenAPI 지원 -->
<dependency>
    <groupId>org.springdoc</groupId>
    <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
    <version>3.0.3a</version>
</dependency>

<!-- WebFlux (Netty 기반) OpenAPI 지원 -->
<dependency>
    <groupId>org.springdoc</groupId>
    <artifactId>springdoc-openapi-starter-webflux-ui</artifactId>
    <version>3.0.3</version>
</dependency>
```

별도의 추가 설정 없이 위 의존성만 추가하면 기본 문서가 생성됨.

Swagger UI : http://localhost:8080/swagger-ui/index.html

OpenAPI JSON 문서 : http://localhost:8080/v3/api-docs

### REST API 문서화 - application.yml 설정

```text
# application.yml - springdoc 설정
springdoc:
  api-docs:
    path: /api-docs      # OpenAPI JSON 문서 경로 변경
    enabled: true
  swagger-ui:
    path: /swagger-ui.html        # Swagger UI 경로 변경
    enabled: true
    operations-sorter: alpha      # API 목록을 알파벳순으로 정렬
    tags-sorter: alpha            # 태그를 알파벳순으로 정렬
    display-request-duration: true  # 요청 처리 시간 표시
    try-it-out-enabled: true      # Swagger UI에서 직접 요청 테스트 활성화
  show-actuator: false            # Actuator 엔드포인트 문서 표시 여부
```

설정 후 접근 경로.

Swagger UI : http://localhost:8080/swagger-ui.html

OpenAPI JSON 문서 : http://localhost:8080/api-docs

### [참고] OAS 어노테이션 태그

컨트롤러·메서드·DTO에 어노테이션을 부여하여 Swagger 문서를 더 상세하게 작성할 수 있음.

### [참고] OAS 문서 작성 예시

컨트롤러·메서드·DTO에 어노테이션으로 부가정보를 기입하면 Swagger UI에 자동으로 반영됨.

```java
// HelloController.java
@Tag(name = "Hello API", description = "Hello 엔드포인트 관련 API")
@RestController
public class HelloController {

    @Operation(summary = "Hello 메시지 반환",
               description = "입력받은 이름을 이용하여 환영 메시지를 반환합니다.")
    @ApiResponses({
        @ApiResponse(responseCode = "200", description = "정상적인 인사"),
        @ApiResponse(responseCode = "400", description = "잘못된 요청")
    })
    @GetMapping("/hello")
    public HelloResponse hello(
        @Parameter(description = "사용자 이름", example = "홍길동")
        @RequestParam String name
    ) {
        return new HelloResponse("안녕하세요, " + name + "님!");
    }
}

// HelloResponse.java - DTO 스키마 문서화
public class HelloResponse {

    @Schema(description = "환영 메시지", example = "안녕하세요, 홍길동님!")
    private String message;

// getter, setter
}
```

실행 후 http://localhost:8080/swagger-ui.html에 접속하면 컨트롤러별로 그룹핑된 API 목록을 확인할 수 있으며, 각 엔드포인트의 파라미터·요청 바디·응답 스키마·응답 코드가 자동으로 문서화되어 표시됨. http://localhost:8080/v3/api-docs에서는 해당 내용이 OpenAPI 3.1.0 JSON 형식으로 제공됨.

### Actuator란?

Spring Boot Actuator는 애플리케이션의 모니터링 및 관리를 위한 다양한 기능을 제공하는 라이브러리임. 운영 환경에서 애플리케이션의 상태(health), 메트릭(metrics), 환경 설정(properties), 로그 설정 등을 확인하고 관리할 수 있게 지원함.

의존성 추가 방법.

```java
<!-- Actuator -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>

<!-- Actuator metrics 정보를 Prometheus 포맷으로 노출 지원 -->
<dependency>
    <groupId>io.micrometer</groupId>
    <artifactId>micrometer-registry-prometheus</artifactId>
</dependency>
```

### Actuator 설정 방법

```text
# application.yml - Actuator 활성화 설정
management:
  server:
    port: 8080                      # Actuator 포트 설정
  endpoints:
    web:
      exposure:
        include: "*"                # 모든 endpoint 노출 (Prometheus endpoint 포함)
  endpoint:
    health:
      probes:
        enabled: true               # LivenessState, ReadinessState 활성화
  health:
    livenessState:
      enabled: true                 # LivenessState 활성화
    readinessState:
      enabled: true                 # ReadinessState 활성화
  metrics:
    enable:
      all: true                     # 모든 기본 메트릭 활성화
```

### Actuator 접속 방법 및 제공 API

기본 접속 주소는 http://localhost:8080/actuator이며, management.server.port 지정에 따라 포트가 변경될 수 있음. 기본값은 server.port와 동일함. 접속 시 활성화된 모든 엔드포인트 목록이 JSON _links 형태로 반환됨.

Spring Boot 애플리케이션의 상태 확인·시스템 모니터링·관리(Management)·운영 자동화 등을 위한 운영용 엔드포인트(REST API)를 자동으로 제공함.

### Actuator - Logging Level 설정

Spring Boot Actuator의 Loggers 엔드포인트(POST /actuator/loggers/{name})는 애플리케이션을 재배포하거나 재시작하지 않고도 특정 패키지/클래스의 로깅 레벨을 동적으로 변경할 수 있음.

주요 유스케이스.

운영 장애 추적 : 평소 로깅 레벨 INFO, 운영 에러 추적 시 DEBUG/TRACE로 전환

특정 써드파티 라이브러리/프레임워크 내부 쿼리/동작 확인 : 사용 중인 라이브러리 패키지만 핀포인트로 로그 레벨 조정. 예) org.hibernate.SQL 또는 org.springframework.security 패키지 level 변경

현재 로거 목록 조회 — GET `<http://localhost:8080/actuator/loggers>`

응답 필드 설명.

configuredLevel : 사용자가 명시적으로 설정한 로그 레벨 (application.yaml 설정 값)

effectiveLevel : 실제 로거에 적용되는 레벨. 사용자의 설정이 명시적으로 없으면 상위 레벨을 상속받아 결정됨

로그 레벨 동적 변경 — POST `<http://localhost:8080/actuator/loggers/{packageName}>`

```text
{
    "configuredLevel": "TRACE"
}
```

root 대신 자신의 패키지 명을 지정해서 패키지별 로그 레벨을 변경할 수 있음. 예) http://localhost:8080/actuator/loggers/com.sk.skala.myapp.controller

### Actuator - Health

기본 엔드포인트 /actuator/health에서 애플리케이션의 전반적인 상태를 표시함.

Health 상태 유형.

UP : 애플리케이션 및 주요 컴포넌트가 정상 동작 중

DOWN : 핵심 컴포넌트 중 하나라도 장애 발생

OUT_OF_SERVICE : 애플리케이션이 살아있으나 외부 요청을 처리할 수 없는 상태 (예: 관리자가 의도적으로 서비스 중지)

UNKNOWN : 상태를 알 수 없음 (HealthIndicator 미구현 or 예외 발생)

기본 제공 Health Indicator.

사용자가 Indicator를 별도 구성 가능함 (HealthIndicator를 상속받아서 구현).

### Actuator - Readiness / Liveness Probe

Spring Boot의 생존 여부와 준비 상태를 모니터링하기 위한 상태 정보를 제공함. 단지 정보를 제공만 하며, 실제 실행은 외부 상태 확인 및 Post-Action을 담당하는 별도 플랫폼이 필요함 (Kubernetes 연동).

### Actuator - Health Readiness Probe 상세

기본 엔드포인트 /actuator/health/readiness. 애플리케이션이 요청을 받을 준비가 되었는지 확인함.

정상(UP) 상태가 되면 200 OK 응답

비정상(DOWN, OUT_OF_SERVICE) 상태가 되면 기본적으로 503 Service Unavailable 응답

정상(UP) 조건.

Spring Boot 애플리케이션이 완전히 초기화 완료됨

HealthIndicator가 모든 구성 요소가 정상(UP)이라고 판단

비정상(DOWN)이 되는 경우.

데이터베이스 연결 실패 : DataSourceHealthIndicator가 DOWN을 리턴하면 전체 Readiness도 DOWN

외부 API 또는 필수 서비스 연결 불가 : Redis, Kafka, API Gateway 등

애플리케이션이 종료 중(OUT_OF_SERVICE) 상태 : Kubernetes가 SIGTERM을 보내고 종료 과정 중이면 Readiness가 OUT_OF_SERVICE로 변경됨

### Actuator - Health Liveness Probe 상세

기본 엔드포인트 /actuator/health/liveness. 애플리케이션 프로세스가 정상 동작 가능한지 확인함.

정상(UP) 상태가 되면 200 OK 응답

비정상(DOWN) 상태가 되면 기본적으로 500 Internal Server Error 응답

정상(UP) 조건.

애플리케이션이 기본적인 동작을 수행 가능한 상태

SpringContext가 정상적으로 유지되고 있음

비정상(DOWN)이 되는 경우.

JVM이 OutOfMemory(OOM) 에러 발생 : Heap Memory 부족 → DOWN

스레드가 Blocked 또는 Deadlock 발생 : synchronized 블록에서 대기 무한 루프

애플리케이션 내부적으로 치명적인 에러 발생 : 중요 구성 요소(예: Message Queue Consumer)가 작동 불가능한 상태

### Actuator - k8s 기반 상태 모니터링 및 PostAction

Spring Boot 애플리케이션이 컨테이너로 Kubernetes 환경에 배포될 경우, 컨테이너 내 애플리케이션(Spring Boot)의 준비 상태와 운영 상태를 확인하기 위해 Actuator Health의 Liveness Probe와 Readiness Probe를 사용함.

Kubernetes의 kubelet이 주기적으로 두 엔드포인트를 탐침(probe)하여 다음과 같이 동작함.

Readiness Probe (/actuator/health/readiness) : Container가 트래픽을 받을 수 있는 상태인지 확인. 최초 실행 시 Success인 경우에만 트래픽 수신 시작. 지속적 탐침 후 리턴코드 200이 아닌 경우 트래픽 수신 차단

Liveness Probe (/actuator/health/liveness) : 컨테이너 실행 중 정상적으로 동작하는지를 지속적으로 확인. FailureThreshold를 초과하는 경우 재시작 처리

## 관련 글

- [[blog/STUDYING/index|STUDYING]]
