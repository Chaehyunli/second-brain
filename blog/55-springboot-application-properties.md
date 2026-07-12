---
title: "[SpringBoot] application.properties 환경 분리하기"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: [blog, technical-writing]
category: "DOCKER"
published: 2025-04-12
source_url: https://ch010104.tistory.com/55
archive_method: Tistory sitemap + HTML content extraction
---

# [SpringBoot] application.properties 환경 분리하기

> 원문: https://ch010104.tistory.com/55

## 본문

지금까지 나의 프로젝트와 redis, DB 등의 연동과 관련된 설정들을 application.properties 파일에서 작성하였다.  그런데, 이번에 해당 프로젝트의 배포를 준비하면서 application.propertied 파일의 내용을 변경해야하 하는 일이 많아졌다. 예를 들어, DB의 url, username, password 같은 경우, 로컬에서 개발을 할 때는, 내 PC에 설치된 mysql을 사용하여 localhost의 주소를 사용하였지만, 배포를 할 때는 외부나 내부의 DB와 연결해야 하기 때문에 이러한 설정 변경을 필수적이다.   배포를 할 때, 이러한 항목들을 변경하면 이후 내가 다시 개발을 할 때는 에러가 날 것이다!!  때문에 application.properties를 로컬 개발 환경(local) 과 배포 환경(prod)를 분리해야함을 느꼈다.  📁 1. 설정 파일 구조   /src/main/resources/ ├── application.properties ← 공통 설정 ├── application-local.properties ← 로컬 개발 환경 설정 ├── application-prod.properties ← 배포 환경 설정 (Cloud Run 등)    2. 기본 설정: application.properties  모든 환경에서 공통으로 사용되는 설정을 여기 작성    spring.application.name=TeamProject2025 # JPA, 시간대, UTF-8 인코딩 등 공통 설정 spring.jpa.properties.hibernate.show_sql=true spring.jpa.hibernate.ddl-auto=update spring.jpa.properties.hibernate.jdbc.time_zone=Asia/Seoul spring.jackson.time-zone=Asia/Seoul spring.validation.fail-fast=true server.servlet.encoding.charset=UTF-8 server.servlet.encoding.enabled=true server.servlet.encoding.force=true    3. 로컬 개발용: application-local.properties  내 컴퓨터의 localhost MySQL 및 Redis와 연결    spring.datasource.url=jdbc:mysql://localhost:3306/teamproject2025?useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=UTC spring.datasource.username=root spring.datasource.password=로컬비밀번호 spring.data.redis.host=localhost spring.data.redis.port=6379 spring.mail.username=xxx@gmail.com spring.mail.password=xxx    4. 배포용: application-prod.properties  GCP + PlanetScale + 외부 SMTP, Redis 등과 연결되는 설정    # PlanetScale (MySQL) DB spring.datasource.url=jdbc:mysql://aws.connect.psdb.io/YOUR_DB_NAME?useSSL=true&enabledTLSProtocols=TLSv1.2 spring.datasource.username=YOUR_USERNAME spring.datasource.password=YOUR_PASSWORD # Redis (외부 서버) spring.data.redis.host=YOUR_REDIS_HOST spring.data.redis.port=6379 spring.data.redis.password=YOUR_REDIS_PASSWORD # GCP Storage spring.cloud.gcp.storage.bucket=your-bucket spring.cloud.gcp.storage.project-id=your-project-id spring.cloud.gcp.credentials.location=file:/app/gcp-key.json # 이메일 인증 spring.mail.username=kth132225@gmail.com spring.mail.password=YOUR_SMTP_PASSWORD    5. 실행 시 프로파일 지정 방법 1) 로컬에서 실행할 때  IntelliJ 또는 VSCode 실행 설정의 VM 옵션에 추가:      -Dspring.profiles.active=local      또는 application.properties 파일에  spring.profiles.active=local      2) Cloud Run에 배포할 때   gcloud run deploy backend-service \ --image=asia-northeast3-docker.pkg.dev/YOUR_PROJECT/YOUR_REPO/backend:latest \ --platform=managed \ --region=asia-northeast3 \ --allow-unauthenticated \ --update-env-vars=SPRING_PROFILES_ACTIVE=prod,DB_USERNAME=...,DB_PASSWORD=...,GCP_BUCKET=...    6. 정리      구분   사용 환경   설정 파일  실행 시 프로파일    로컬 개발 내 PC (localhost) application-local.properties local   GCP 배포 Cloud Run application-prod.properties prod      7. 장점  💡 설정 파일을 그때마다 수정하지 않아도 됨 💡 환경에 따라 자동으로 설정 분리됨 💡 개발/테스트/운영 환경이 명확히 나뉘어 실수 줄어듦
