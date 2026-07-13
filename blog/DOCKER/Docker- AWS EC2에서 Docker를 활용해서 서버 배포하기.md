---
title: "[Docker] AWS EC2에서 Docker를 활용해서 서버 배포하기"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "docker"]
category: "DOCKER"
published: 2025-06-22
source_url: https://ch010104.tistory.com/102
---

# [Docker] AWS EC2에서 Docker를 활용해서 서버 배포하기

## 원문

https://ch010104.tistory.com/102

## 핵심 요약

- **1. Ubuntu에서 Docker 및 Docker Compose 설치하기** — EC2의 가상 인스턴스에 연결해서 설치를 해야함
- **2. AWS ECR (Elastic Container Registry) 개념 및 이유** — docker를 사용하지 않고 EC2에서 깃허브 클론해서 배포하는 방식
- **3. AWS CLI 설치 및 ECR 사용 준비** — 1) AWS CLI 설치 (Ubuntu 기준)
- **5. EC2에서 컨테이너 실행 (Docker CLI 방식)** — ❗️ 만약 이후 docker compose up에서 아키텍처 불일치 에러가 발생한다면 --platform linux/amd64 옵션을 추가하여 빌드!

## 관련 글

- [[blog/DOCKER/index|DOCKER]]
- [[blog/DOCKER/Docker- AWS EC2에 서버 배포하기(Express 서버 배포하기)|[Docker] AWS EC2에 서버 배포하기(Express 서버 배포하기)]]
- [[blog/DOCKER/Docker- DockerCompose에 2개 이상의 Container 관리하기|[Docker] DockerCompose에 2개 이상의 Container 관리하기]]
- [[blog/DOCKER/Docker- Docker Compose 란|[Docker] Docker Compose 란??]]
