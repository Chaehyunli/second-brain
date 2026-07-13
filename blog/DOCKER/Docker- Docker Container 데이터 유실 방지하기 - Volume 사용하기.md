---
title: "[Docker] Docker Container 데이터 유실 방지하기 - Volume 사용하기"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "docker"]
category: "DOCKER"
published: 2025-06-19
source_url: https://ch010104.tistory.com/97
---

# [Docker] Docker Container 데이터 유실 방지하기 - Volume 사용하기

## 원문

https://ch010104.tistory.com/97

## 핵심 요약

- Docker를 활용하면 특정 프로그램을 컨테이너로 띄워서 간편하게 실행할 수 있음
- **📌 1. Docker Volume(도커 볼륨) 이란?** — Docker Volume은 도커 컨테이너에서 데이터를 영속적으로 저장하기 위한 방법
- **🧪 2. 실습: Docker로 MySQL 실행하기** — 1) 기본 MySQL 컨테이너 실행 (Volume 미사용)
- **🧪 3. 실습: MySQL에 직접 접속해보기** — 이처럼 Volume을 쓰지 않으면 데이터도 함께 사라지게 됨.

## 관련 글

- [[blog/DOCKER/index|DOCKER]]
- [[blog/DOCKER/Docker- Docker CLI 익히기|[Docker] Docker CLI 익히기]]
- [[blog/DOCKER/Docker- Dockerfile를 사용하여 dockerimage 직접 만들기|[Docker] Dockerfile를 사용하여 dockerimage 직접 만들기]]
- [[blog/DOCKER/Dokcer- Docker란 무엇일까-- (Container 란--, Image 란--)|[Dokcer] Docker란 무엇일까?? (Container 란??, Image 란??)]]
