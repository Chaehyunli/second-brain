---
title: "[SpringBoot] application.properties 환경 분리하기"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "backend", "GCP", "springboot", "배포"]
category: "DOCKER"
published: 2025-04-12
source_url: https://ch010104.tistory.com/55
---

# [SpringBoot] application.properties 환경 분리하기

## 원문

https://ch010104.tistory.com/55

## 노트 유형

`guide`

## 적용 목적과 전제조건

지금까지 나의 프로젝트와 redis, DB 등의 연동과 관련된 설정들을 application.properties 파일에서 작성하였다.

그런데, 이번에 해당 프로젝트의 배포를 준비하면서 application.propertied 파일의 내용을 변경해야하 하는 일이 많아졌다.

## 구현 절차·검증·주의점

지금까지 나의 프로젝트와 redis, DB 등의 연동과 관련된 설정들을 application.properties 파일에서 작성하였다.

그런데, 이번에 해당 프로젝트의 배포를 준비하면서 application.propertied 파일의 내용을 변경해야하 하는 일이 많아졌다.

예를 들어, DB의 url, username, password 같은 경우, 로컬에서 개발을 할 때는, 내 PC에 설치된 mysql을 사용하여 localhost의 주소를 사용하였지만, 배포를 할 때는 외부나 내부의 DB와 연결해야 하기 때문에 이러한 설정 변경을 필수적이다.

배포를 할 때, 이러한 항목들을 변경하면 이후 내가 다시 개발을 할 때는 에러가 날 것이다!!

때문에 application.properties를 로컬 개발 환경(local) 과 배포 환경(prod)를 분리해야함을 느꼈다.

### 📁 1. 설정 파일 구조

```text
/src/main/resources/
├── application.properties             ← 공통 설정
├── application-local.properties       ← 로컬 개발 환경 설정
├── application-prod.properties        ← 배포 환경 설정 (Cloud Run 등)
```

### 2. 기본 설정: application.properties

모든 환경에서 공통으로 사용되는 설정을 여기 작성

```text
spring.application.name=TeamProject2025

# JPA, 시간대, UTF-8 인코딩 등 공통 설정
spring.jpa.properties.hibernate.show_sql=true
spring.jpa.hibernate.ddl-auto=update
spring.jpa.properties.hibernate.jdbc.time_zone=Asia/Seoul
spring.jackson.time-zone=Asia/Seoul
spring.validation.fail-fast=true
server.servlet.encoding.charset=UTF-8
server.servlet.encoding.enabled=true
server.servlet.encoding.force=true
```

### 3. 로컬 개발용: application-local.properties

내 컴퓨터의 localhost MySQL 및 Redis와 연결

```text
spring.datasource.url=jdbc:mysql://localhost:3306/teamproject2025?useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=UTC
spring.datasource.username=root
spring.datasource.password=로컬비밀번호

spring.data.redis.host=localhost
spring.data.redis.port=6379

spring.mail.username=xxx@gmail.com
spring.mail.password=xxx
```

### 4. 배포용: application-prod.properties

GCP + PlanetScale + 외부 SMTP, Redis 등과 연결되는 설정

```text
# PlanetScale (MySQL) DB
spring.datasource.url=jdbc:mysql://aws.connect.psdb.io/YOUR_DB_NAME?useSSL=true&enabledTLSProtocols=TLSv1.2
spring.datasource.username=YOUR_USERNAME
spring.datasource.password=YOUR_PASSWORD

# Redis (외부 서버)
spring.data.redis.host=YOUR_REDIS_HOST
spring.data.redis.port=6379
spring.data.redis.password=YOUR_REDIS_PASSWORD

# GCP Storage
spring.cloud.gcp.storage.bucket=your-bucket
spring.cloud.gcp.storage.project-id=your-project-id
spring.cloud.gcp.credentials.location=file:/app/gcp-key.json

# 이메일 인증
spring.mail.username=kth132225@gmail.com
spring.mail.password=YOUR_SMTP_PASSWORD
```

### 5. 실행 시 프로파일 지정 방법

1) 로컬에서 실행할 때

IntelliJ 또는 VSCode 실행 설정의 VM 옵션에 추가:

```text
-Dspring.profiles.active=local
```

또는 application.properties 파일에

```text
spring.profiles.active=local
```

2) Cloud Run에 배포할 때

```bash
gcloud run deploy backend-service \
  --image=asia-northeast3-docker.pkg.dev/YOUR_PROJECT/YOUR_REPO/backend:latest \
  --platform=managed \
  --region=asia-northeast3 \
  --allow-unauthenticated \
  --update-env-vars=SPRING_PROFILES_ACTIVE=prod,DB_USERNAME=...,DB_PASSWORD=...,GCP_BUCKET=...
```

### 6. 정리

### 7. 장점

💡 설정 파일을 그때마다 수정하지 않아도 됨

💡 환경에 따라 자동으로 설정 분리됨

💡 개발/테스트/운영 환경이 명확히 나뉘어 실수 줄어듦

## 관련 글

- [[blog/DOCKER/index|DOCKER]]
- [[blog/DOCKER/Docker- Docker를 사용해서 Spring boot + React 배포하기 ( 1 )|[Docker] Docker를 사용해서 Spring boot + React 배포하기 ( 1 )]]
- [[blog/GCP/GCP- GCP로 프로젝트 배포하기 - ( 5 ) GCP VPC 란|[GCP] GCP로 프로젝트 배포하기 - ( 5 ) GCP VPC 란?]]
- [[blog/GCP/GCP- GCP로 프로젝트 배포하기 - ( 6 ) GCP VPC 생성하기|[GCP] GCP로 프로젝트 배포하기 - ( 6 ) GCP VPC 생성하기]]
