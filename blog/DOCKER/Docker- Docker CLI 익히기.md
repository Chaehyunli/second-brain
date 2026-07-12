---
title: "[Docker] Docker CLI 익히기"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "docker"]
category: "DOCKER"
published: 2025-06-18
source_url: https://ch010104.tistory.com/96
---

# [Docker] Docker CLI 익히기

## 원문

https://ch010104.tistory.com/96

## 핵심 요약

- **📥 1. Docker 이미지(Image) 다운로드** — Docker 이미지는 특정 애플리케이션이 실행되기 위한 모든 설정, 코드, 라이브러리가 포함된 패키지
- **🔍 2. 이미지 확인 및 삭제** — ID 일부만 입력해도 됨 (단, 중복되면 삭제 불가)
- **📦 3. 컨테이너(Container) 생성과 실행** — 컨테이너는 이미지에서 실행되는 실행 단위로, 하나의 독립된 리눅스 환경이라 생각
- **🚀 4. 컨테이너 생성 + 실행 (run 명령어)** — 호스트의 4000번 포트를 컨테이너의 80번 포트와 연결

## 관련 글

- [[blog/DOCKER/index|DOCKER]]
- [[blog/DOCKER/Dokcer- Docker란 무엇일까-- (Container 란--, Image 란--)|[Dokcer] Docker란 무엇일까?? (Container 란??, Image 란??)]]
- [[blog/DOCKER/Docker- Docker Container 데이터 유실 방지하기 - Volume 사용하기|[Docker] Docker Container 데이터 유실 방지하기 - Volume 사용하기]]
- [[blog/DOCKER/Docker- Dockerfile를 사용하여 dockerimage 직접 만들기|[Docker] Dockerfile를 사용하여 dockerimage 직접 만들기]]
