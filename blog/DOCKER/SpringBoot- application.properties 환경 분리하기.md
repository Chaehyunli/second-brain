---
title: "[SpringBoot] application.properties 환경 분리하기"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "backend", "GCP", "springboot", "배포"]
category: "DOCKER"
published: 2025-04-12
source_url: https://ch010104.tistory.com/55
---

# [SpringBoot] application.properties 환경 분리하기

## 원문

https://ch010104.tistory.com/55

## 핵심 요약

- 지금까지 나의 프로젝트와 redis, DB 등의 연동과 관련된 설정들을 application.properties 파일에서 작성하였다.
- **2. 기본 설정: application.properties** — 모든 환경에서 공통으로 사용되는 설정을 여기 작성
- **3. 로컬 개발용: application-local.properties** — 내 컴퓨터의 localhost MySQL 및 Redis와 연결
- **4. 배포용: application-prod.properties** — GCP + PlanetScale + 외부 SMTP, Redis 등과 연결되는 설정

## 관련 글

- [[blog/DOCKER/index|DOCKER]]
- [[blog/DOCKER/Docker- Docker를 사용해서 Spring boot + React 배포하기 ( 1 )|[Docker] Docker를 사용해서 Spring boot + React 배포하기 ( 1 )]]
- [[blog/GCP/GCP- GCP로 프로젝트 배포하기 - ( 5 ) GCP VPC 란|[GCP] GCP로 프로젝트 배포하기 - ( 5 ) GCP VPC 란?]]
- [[blog/GCP/GCP- GCP로 프로젝트 배포하기 - ( 6 ) GCP VPC 생성하기|[GCP] GCP로 프로젝트 배포하기 - ( 6 ) GCP VPC 생성하기]]
