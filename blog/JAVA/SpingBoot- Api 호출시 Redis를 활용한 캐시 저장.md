---
title: "[SpingBoot] Api 호출시 Redis를 활용한 캐시 저장"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "cache", "java", "springboot"]
category: "JAVA"
published: 2025-04-04
source_url: https://ch010104.tistory.com/44
---

# [SpingBoot] Api 호출시 Redis를 활용한 캐시 저장

## 원문

https://ch010104.tistory.com/44

## 핵심 요약

- 백엔드에서는 controller에서 Api를 호출하면, service에서 이를 처리해서 반환함.
- **1. Redis 캐시 설정** — 캐시를 설정하기 위해 CacheConfig 클래스를 생성하고, Redis 캐시 매니저를 설정
- **2. 캐시 적용 예시 – 동아리 목록** — 사용자의 대학교 ID를 기반으로 동아리 목록을 캐싱하는 방법(사용자 이름을 기반으로 하면, 사용자마다 캐시 생성)
- **3. 캐시 삭제 (Evict)** — 동아리 생성, 삭제, 썸네일 변경 등 동아리 목록에 변동이 생길 때 해당 캐시를 삭제하여 최신 데이터를 유지

## 관련 글

- [[blog/JAVA/index|JAVA]]
- [[blog/JAVA/Spring Boot- Websocket + STOMP를 이용한 세션 기반 채팅|[Spring Boot] Websocket + STOMP를 이용한 세션 기반 채팅]]
- [[blog/JAVA/프로그래머스- 가장 많이 받은 선물(2024 KAKAO WINTER INTERNSHIP)|[프로그래머스] 가장 많이 받은 선물(2024 KAKAO WINTER INTERNSHIP)]]
- [[blog/JAVA/Spring Boot- 빈(Bean)이란- Autowired 란|[Spring Boot] 빈(Bean)이란? Autowired 란?]]
