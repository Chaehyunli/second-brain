---
title: "[Spring Boot] 10. Redis Pub/Sub 기반 실시간 알림 시스템"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "java", "spring boot"]
category: "SPRING BOOT"
published: 2026-03-27
source_url: https://ch010104.tistory.com/241
---

# [Spring Boot] 10. Redis Pub/Sub 기반 실시간 알림 시스템

## 원문

https://ch010104.tistory.com/241

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

보통의 웹은 클라이언트가 질문(요청)을 해야 서버가 답(응답)을 주는 방식이지만, 알림은 서버가 사건이 터졌을 때 먼저 알려줘야 합니다. 이를 위해 사용하는 기술이 바로 SSE입니다.

작동 방식: 서버와 클라이언트 사이의 연결 통로를 계속 열어둡니다. 이벤트(알림)가 발생할 때마다 서버는 이 통로로 데이터를 툭툭 던져줍니다.

## 원문 기반 개념 정리

### 1. SSE (Server-Sent Events)란?

보통의 웹은 클라이언트가 질문(요청)을 해야 서버가 답(응답)을 주는 방식이지만, 알림은 서버가 사건이 터졌을 때 먼저 알려줘야 합니다. 이를 위해 사용하는 기술이 바로 SSE입니다.

작동 방식: 서버와 클라이언트 사이의 연결 통로를 계속 열어둡니다. 이벤트(알림)가 발생할 때마다 서버는 이 통로로 데이터를 툭툭 던져줍니다.

장점:

가벼움: WebSocket보다 구현이 훨씬 단순하고 리소스를 적게 먹습니다.

자동 재연결: 네트워크 불안정으로 연결이 끊기면 브라우저/앱이 알아서 재연결을 시도합니다.

HTTP 기반: 별도의 프로토콜 설정 없이 기존 웹 환경에서 아주 잘 돌아갑니다.

### 2. 기술 비교: WebSocket vs SSE

우리가 대화하며 정리한 채팅과 알림의 기술적 선택 기준입니다.

구분 WebSocket (웹소켓) SSE (Server-Sent Events)

💡 결론: 카카오톡처럼 내가 메시지를 보낼 때(요청)는 일반 API를 쓰고, 남이 보낸 메시지 알림을 받을 때(수신)는 SSE를 쓰는 것이 가장 효율적인 조합입니다.

### 3. Redis Pub/Sub: 멀티 인스턴스의 구원자

서버가 1번, 2번, 3번으로 늘어났을 때, 특정 사용자가 어떤 서버에 연결되어 있더라도 알림을 놓치지 않게 하는 **'중계 시스템'**입니다.

문제 상황: 사용자 A는 1번 서버에 연결되어 있는데, 알림을 보내야 하는 로직은 3번 서버에서 실행될 때, 1번 서버는 알림이 온 줄 모릅니다.

해결 (Redis Pub/Sub):

발행(Publish): 3번 서버가 Redis에 **"사용자 A에게 알림 보내!"**라고 신호를 쏩니다.

구독(Subscribe): 모든 서버(1~3번)는 Redis를 실시간으로 듣고 있다가, A와 연결된 1번 서버가 이 신호를 낚아챕니다.

전달(Push): 1번 서버가 자신이 꽉 잡고 있는 SSE 통로를 통해 사용자 A의 앱에 알림을 최종 전달합니다.

### 4. 전체 시스템 요약

구성 요소 역할 비유

### 5. 이 구조의 핵심 장점

실시간성: 폴링(Polling)처럼 "새 소식 있나요?"라고 묻지 않아도 소식이 발생하는 즉시 배달됩니다.

확장성: 서버를 100대로 늘려도 Redis가 중앙에서 신호를 맞춰주므로 무한 확장이 가능합니다.

효율성: 클라이언트가 계속 요청을 보내지 않아도 되므로 서버 부하가 적고 스마트폰 배터리 소모가 적습니다.

## 관련 글

- [[blog/SPRING BOOT/index|SPRING BOOT]]
- [[blog/SPRING BOOT/Spring Boot- 9. 동기 Postgres의 스케줄러 분리|[Spring Boot] 9. 동기 Postgres의 스케줄러 분리]]
- [[blog/SPRING BOOT/Spring Boot- 8. 비동기 Spring WebClient, Mono와 Flux|[Spring Boot] 8. 비동기 Spring WebClient, Mono와 Flux]]
- [[blog/SPRING BOOT/Spring Boot- 7. Spring Boot CORS 중복 응답(web & webflux 충돌)|[Spring Boot] 7. Spring Boot CORS 중복 응답(web & webflux 충돌)]]
