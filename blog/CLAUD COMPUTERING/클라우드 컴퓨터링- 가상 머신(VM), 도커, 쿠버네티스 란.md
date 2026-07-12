---
title: "[클라우드 컴퓨터링] 가상 머신(VM), 도커, 쿠버네티스 란?"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "claud", "docker", "k8s"]
category: "CLAUD COMPUTERING"
published: 2025-09-23
source_url: https://ch010104.tistory.com/138
---

# [클라우드 컴퓨터링] 가상 머신(VM), 도커, 쿠버네티스 란?

## 원문

https://ch010104.tistory.com/138

## 핵심 요약

- **1. 하이퍼바이저 심층 분석: Xen 아키텍처** — - Xen은 하드웨어 위에 직접 설치되어 실행되는 Type-1(Bare-metal) 하이퍼바이저
- **2. 하이브리드 전략** — - 현대의 하이퍼바이저들은 성능을 극대화하기 위해 한 가지 방식만 고집하지 않고, 작업의 종류에 따라 최적의 기술을 선택하는 하이브리드 전략을 사용
- **3. 컨테이너 가상화와 Docker** — - 가상 머신(VM)은 앱 하나를 실행하기 위해 매번 무거운 게스트 OS까지 설치해야 하는 오버헤드가 있음
- **4. 대규모 컨테이너 관리(오케스트레이션과 쿠버네티스)** — - 수백, 수천 개의 컨테이너를 수동으로 관리하는 것은 거의 불가능

## 관련 글

- [[blog/CLAUD COMPUTERING/index|CLAUD COMPUTERING]]
- [[blog/CLAUD COMPUTERING/클라우드 컴퓨터링- 빅데이터와 클라우드란|[클라우드 컴퓨터링] 빅데이터와 클라우드란?]]
- [[blog/DOCKER/Docker- AWS EC2에서 Docker를 활용해서 서버 배포하기|[Docker] AWS EC2에서 Docker를 활용해서 서버 배포하기]]
- [[blog/DOCKER/Docker- AWS EC2에 서버 배포하기(Express 서버 배포하기)|[Docker] AWS EC2에 서버 배포하기(Express 서버 배포하기)]]
