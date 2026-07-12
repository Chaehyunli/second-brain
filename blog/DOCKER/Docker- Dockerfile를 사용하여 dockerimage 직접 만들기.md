---
title: "[Docker] Dockerfile를 사용하여 dockerimage 직접 만들기"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "docker"]
category: "DOCKER"
published: 2025-06-19
source_url: https://ch010104.tistory.com/98
---

# [Docker] Dockerfile를 사용하여 dockerimage 직접 만들기

## 원문

https://ch010104.tistory.com/98

## 핵심 요약

- **1. Dockerfile이란?** — Dockerfile은 Docker 이미지를 만들기 위한 설정 파일
- **2. Dockerfile 주요 명령어 정리 및 실습** — 초기 OS 또는 환경 설정을 위한 베이스 이미지를 지정.
- **3. 실습: 프로젝트별 Dockerfile 작성 예시** — ⚡ 4) HTML + CSS + Nginx 배포
- **4. 디버깅 팁** — 컨테이너가 자동 종료되는 것을 방지하려면 ENTRYPOINT ["/bin/bash", "-c", "sleep 500"] 추가

## 관련 글

- [[blog/DOCKER/index|DOCKER]]
- [[blog/DOCKER/Docker- Docker Container 데이터 유실 방지하기 - Volume 사용하기|[Docker] Docker Container 데이터 유실 방지하기 - Volume 사용하기]]
- [[blog/DOCKER/Docker- Docker Compose 란|[Docker] Docker Compose 란??]]
- [[blog/DOCKER/Docker- Docker CLI 익히기|[Docker] Docker CLI 익히기]]
