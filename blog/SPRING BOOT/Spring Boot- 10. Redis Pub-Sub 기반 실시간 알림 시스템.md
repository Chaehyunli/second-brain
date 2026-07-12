---
title: "[Spring Boot] 10. Redis Pub/Sub 기반 실시간 알림 시스템"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "java", "spring boot"]
category: "SPRING BOOT"
published: 2026-03-27
source_url: https://ch010104.tistory.com/241
---

# [Spring Boot] 10. Redis Pub/Sub 기반 실시간 알림 시스템

## 원문

https://ch010104.tistory.com/241

## 핵심 요약

- **1. SSE (Server-Sent Events)란?** — 보통의 웹은 클라이언트가 질문(요청)을 해야 서버가 답(응답)을 주는 방식이지만, 알림은 서버가 사건이 터졌을 때 먼저 알려줘야 합니다.
- **2. 기술 비교: WebSocket vs SSE** — 우리가 대화하며 정리한 채팅과 알림의 기술적 선택 기준입니다.
- **3. Redis Pub/Sub: 멀티 인스턴스의 구원자** — 서버가 1번, 2번, 3번으로 늘어났을 때, 특정 사용자가 어떤 서버에 연결되어 있더라도 알림을 놓치지 않게 하는 **'중계 시스템'**입니다.
- **5. 이 구조의 핵심 장점** — 실시간성: 폴링(Polling)처럼 "새 소식 있나요?"라고 묻지 않아도 소식이 발생하는 즉시 배달됩니다.

## 관련 글

- [[blog/SPRING BOOT/index|SPRING BOOT]]
- [[blog/SPRING BOOT/Spring Boot- 9. 동기 Postgres의 스케줄러 분리|[Spring Boot] 9. 동기 Postgres의 스케줄러 분리]]
- [[blog/SPRING BOOT/Spring Boot- 8. 비동기 Spring WebClient, Mono와 Flux|[Spring Boot] 8. 비동기 Spring WebClient, Mono와 Flux]]
- [[blog/SPRING BOOT/Spring Boot- 7. Spring Boot CORS 중복 응답(web & webflux 충돌)|[Spring Boot] 7. Spring Boot CORS 중복 응답(web & webflux 충돌)]]
