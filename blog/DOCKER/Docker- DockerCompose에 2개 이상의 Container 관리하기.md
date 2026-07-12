---
title: "[Docker] DockerCompose에 2개 이상의 Container 관리하기"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "docker"]
category: "DOCKER"
published: 2025-06-20
source_url: https://ch010104.tistory.com/100
---

# [Docker] DockerCompose에 2개 이상의 Container 관리하기

## 원문

https://ch010104.tistory.com/100

## 핵심 요약

- **1. 기본 구성: Docker Compose로 MySQL, Redis 실행하기** — 📌 주의: YAML 문법에서는 들여쓰기가 매우 중요.
- **2. Spring Boot + MySQL 연동 컨테이너 구성** — https://start.spring.io 에서 아래와 같이 설정 후 프로젝트를 생성
- **3. Redis 연동까지 추가하기** — 🧾 2) application.yml에 Redis 설정 추가

## 관련 글

- [[blog/DOCKER/index|DOCKER]]
- [[blog/DOCKER/Docker- Docker Compose 란|[Docker] Docker Compose 란??]]
- [[blog/DOCKER/Docker- AWS EC2에 서버 배포하기(Express 서버 배포하기)|[Docker] AWS EC2에 서버 배포하기(Express 서버 배포하기)]]
- [[blog/DOCKER/Docker- Dockerfile를 사용하여 dockerimage 직접 만들기|[Docker] Dockerfile를 사용하여 dockerimage 직접 만들기]]
