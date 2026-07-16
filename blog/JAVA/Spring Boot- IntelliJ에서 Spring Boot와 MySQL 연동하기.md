---
title: "[Spring Boot] IntelliJ에서 Spring Boot와 MySQL 연동하기"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "IntelliJ", "MySQL", "spring boot"]
category: "JAVA"
published: 2025-02-19
source_url: https://ch010104.tistory.com/1
---

# [Spring Boot] IntelliJ에서 Spring Boot와 MySQL 연동하기

## 원문

https://ch010104.tistory.com/1

## 노트 유형

`guide`

## 적용 목적과 전제조건

Mysql과 IntelliJ가 설치되어 있다는 가정하에 연동을 준비하겠습니다.

IntelliJ에서는 프로젝트를 만들 때 의존성을 " Dependencies" 에서 추가할 수 있기 때문에 필요한 의존성을 미리 설정한다.

## 구현 절차·검증·주의점

Mysql과 IntelliJ가 설치되어 있다는 가정하에 연동을 준비하겠습니다.

IntelliJ에서는 프로젝트를 만들 때 의존성을 " Dependencies" 에서 추가할 수 있기 때문에 필요한 의존성을 미리 설정한다.

Spring Boot DevTools // 개발 중 변경사항을 자동으로 감지하여 서버를 다시 시작하지 않고도 적용

Spring Web // 웹 애플리케이션 개발을 위한 기본 필수 의존성

Spring Data JPA // Java Persistence API(JPA)를 쉽게 사용할 수 있도록 지원하는 모듈

MySQL Driver // MySQL 데이터베이스와 Java 애플리케이션을 연결하기 위한 JDBC 드라이버

Lombok (선택 사항) // Getter, Setter, Constructor 등의 코드를 자동 생성해주는 라이브러리

프로젝트 생성 후에 " application.properties " 파일에서 데이터베이스에 관한 설정을 해야함. 이전에 먼저 Mysql에서 연동할 데이터 베이스를 만들는 것이 좋다.

```text
# 데이터베이스 연결 설정

spring.datasource.url=jdbc:mysql://localhost:3306/{mql의 내 데이터베이스 이름}?useSSL=false&serverTimezone=Asia/Seoul
spring.datasource.username={DB 계정 이름. 기본 root}
spring.datasource.password={비밀번호}
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver

# JPA 설정 (자동 테이블 생성)
spring.jpa.hibernate.ddl-auto=update // 추가할 때마다 entity에서 자동으로 데이터베이스 테이블을 생성해줌
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.MySQL8Dialect
spring.jpa.show-sql=true // SQL 쿼리를 실행할 때 콘솔에 출력되도록 설정
```

spring.jpa.hibernate.ddl-auto=update

Hibernate가 자동으로 테이블을 생성하거나 변경할지 결정하는 옵션

none: 테이블 자동 생성/변경 비활성화 (운영 환경에서 추천).

update: 기존 테이블 구조를 유지하면서 필요한 경우 변경 (개발 환경에서 자주 사용).

create: 애플리케이션 실행 시 기존 테이블 삭제 후 새로 생성 (데이터 초기화됨).

create-drop: create와 동일하지만 애플리케이션 종료 시 테이블 삭제.

validate: 기존 테이블과 매핑되는 엔티티가 일치하는지 검증 (변경은 없음)

spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.MySQL8Dialect

Hibernate가 MySQL에 맞게 SQL 쿼리를 최적화하도록 설정

MySQL8Dialect는 MySQL 8버전에 최적화

## 관련 글

- [[blog/JAVA/index|JAVA]]
- [[blog/JAVA/Spring Boot- 빈(Bean)이란- Autowired 란|[Spring Boot] 빈(Bean)이란? Autowired 란?]]
- [[blog/카테고리 없음/React - Spring Boot- 프론트엔드, 백엔드 프로젝트 구조|[React / Spring Boot] 프론트엔드, 백엔드 프로젝트 구조]]
- [[blog/SPRING BOOT/Spring Boot- 1. Spring Boot의 FeignClient 설정(python 포함)|[Spring Boot] 1. Spring Boot의 FeignClient 설정(python 포함)]]
