---
title: "[Spring Boot] Websocket + STOMP를 이용한 세션 기반 채팅"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "java", "springboot", "STOMP", "Websocket"]
category: "JAVA"
published: 2025-09-23
source_url: https://ch010104.tistory.com/140
---

# [Spring Boot] Websocket + STOMP를 이용한 세션 기반 채팅

## 원문

https://ch010104.tistory.com/140

## 핵심 요약

- **1. 전체 아키텍처** — Spring Boot채팅 시스템은 RESTful API와 WebSocket API를 조합한 하이브리드 아키텍처를 채택
- **2. WebSocket + STOMP 설정** — - 모든 실시간 통신의 기반이 되는 설정은 WebSocketConfig.java 파일에서 정의
- **3. 메시지 플로우** — - 사용자가 보낸 메시지는 다음과 같은 명확한 흐름을 통해 처리되고 다시 모든 참여자에게 전달
- **4. 핵심 컴포넌트** — 실시간 메시지 처리의 진입점으로, 클라이언트로부터 메시지를 받아 서비스 계층으로 연결

## 관련 글

- [[blog/JAVA/index|JAVA]]
- [[blog/JAVA/SpingBoot- Api 호출시 Redis를 활용한 캐시 저장|[SpingBoot] Api 호출시 Redis를 활용한 캐시 저장]]
- [[blog/JAVA/프로그래머스- 가장 많이 받은 선물(2024 KAKAO WINTER INTERNSHIP)|[프로그래머스] 가장 많이 받은 선물(2024 KAKAO WINTER INTERNSHIP)]]
- [[blog/JAVA/Spring Boot- 빈(Bean)이란- Autowired 란|[Spring Boot] 빈(Bean)이란? Autowired 란?]]
