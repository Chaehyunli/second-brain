---
title: "[Spring Boot] 11. Cluster DB"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "cluster", "DB", "spring boot"]
category: "SPRING BOOT"
published: 2026-05-20
source_url: https://ch010104.tistory.com/276
---

# [Spring Boot] 11. Cluster DB

## 원문

https://ch010104.tistory.com/276

## 핵심 요약

- **1.1 Q. "클러스터로 쓴다"는 것의 정의와 핵심 목적** — 데이터베이스를 "클러스터로 구성하여 사용한다"는 것은 물리적 혹은 가상으로 분리된 여러 대의 데이터베이스 서버를 네트워크로 묶어, 백엔드 애플리케이션 입장에서는 마치 하나의 단일 시스템처럼 작동하도록 설계하는 것을 의미합니다.
- **1.2 Q. "개인 캡스톤 프로젝트나 소규모 환경에서도 가능할까요? Supabase에선 어떨까요?"** — Supabase 환경 분석: Supabase는 백엔드 인프라가 완전히 추상화된 Managed(완전 관리형) PostgreSQL 서비스입니다.
- **2.1 WAL 스트리밍 복제 (Streaming Replication)** — PostgreSQL의 실시간 복제 기술은 WAL (Write-Ahead Log, 미리 쓰기 로그) 백업 매커니즘을 기반으로 수행됩니다.
- **2.2 Q. "docker-compose의 depends_on 설정 때문에 자동으로 동기화와 고장 대체가 되** — depends_on의 명확한 역할: 절대 아닙니다.

## 관련 글

- [[blog/SPRING BOOT/index|SPRING BOOT]]
- [[blog/INFLEARN/스프링 DB 1편 - 데이터 접근 핵심 원리- 1. JDBC 이해|[스프링 DB 1편 - 데이터 접근 핵심 원리] 1. JDBC 이해]]
- [[blog/INFLEARN/스프링 DB 1편 - 데이터 접근 핵심 원리- 2. 커넥션풀과 데이터소스 이해|[스프링 DB 1편 - 데이터 접근 핵심 원리] 2. 커넥션풀과 데이터소스 이해]]
- [[blog/INFLEARN/스프링 DB 1편 - 데이터 접근 핵심 원리- 3. 트랜잭션 이해|[스프링 DB 1편 - 데이터 접근 핵심 원리] 3. 트랜잭션 이해]]
