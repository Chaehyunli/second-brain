---
title: "[Docker] Docker를 사용해서 Spring boot + React 배포하기 ( 1 )"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "backend", "docker", "frontend", "GCP", "react", "springboot", "배포"]
category: "DOCKER"
published: 2025-04-07
source_url: https://ch010104.tistory.com/45
---

# [Docker] Docker를 사용해서 Spring boot + React 배포하기 ( 1 )

## 원문

https://ch010104.tistory.com/45

## 핵심 요약

- 현재 진행 중인 동아리 게시물 웹 프로젝트가 어느덧 배포 단계까지 오게되었다.
- **📁 프로젝트 구조 (예시: 동아리 게시물 프로젝트)** — 나의 동아리 게시물 프로젝트에서는 따로 backend 폴더가 존재하지 않고, TeamProject2025 프로젝트 파일 아래에 둠
- **1. 백엔드(Spring Boot)** — 1) 📄 Dockerfile (/TeamProject2025/Dockerfile)
- **✅ 2. 프론트엔드(React)** — 1) 📄 Dockerfile (/TeamProject2025/frontend/Dockerfile)

## 관련 글

- [[blog/DOCKER/index|DOCKER]]
- [[blog/DOCKER/SpringBoot- application.properties 환경 분리하기|[SpringBoot] application.properties 환경 분리하기]]
- [[blog/카테고리 없음/React - Spring Boot- 프론트엔드, 백엔드 프로젝트 구조|[React / Spring Boot] 프론트엔드, 백엔드 프로젝트 구조]]
- [[blog/GCP/GCP- GCP로 프로젝트 배포하기 - ( 5 ) GCP VPC 란|[GCP] GCP로 프로젝트 배포하기 - ( 5 ) GCP VPC 란?]]
