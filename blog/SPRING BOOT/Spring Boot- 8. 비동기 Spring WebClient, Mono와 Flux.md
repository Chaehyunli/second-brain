---
title: "[Spring Boot] 8. 비동기 Spring WebClient, Mono와 Flux"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "java", "spring boot"]
category: "SPRING BOOT"
published: 2026-03-04
source_url: https://ch010104.tistory.com/206
---

# [Spring Boot] 8. 비동기 Spring WebClient, Mono와 Flux

## 원문

https://ch010104.tistory.com/206

## 핵심 요약

- **1. 배경: 데이터의 '개수'가 아닌 '흐름'** — 기존의 List<User>나 User 객체는 데이터를 이미 다 가져온 '결과물'입니다.
- **2. Mono (0 ~ 1개의 데이터)** — *"단 한 번의 응답"**이 필요한 모든 곳에 사용합니다.
- **[실제 코드 예시: 단일 사용자 정보 조회]** — 파이썬 서버나 DB에서 특정 유저 한 명의 정보를 가져올 때의 전형적인 패턴입니다.
- **3. Flux (0 ~ N개의 데이터)** — *"데이터의 스트림(목록)"**이 필요할 때 사용합니다.

## 관련 글

- [[blog/SPRING BOOT/index|SPRING BOOT]]
- [[blog/SPRING BOOT/Spring Boot- 7. Spring Boot CORS 중복 응답(web & webflux 충돌)|[Spring Boot] 7. Spring Boot CORS 중복 응답(web & webflux 충돌)]]
- [[blog/SPRING BOOT/Spring Boot- 9. 동기 Postgres의 스케줄러 분리|[Spring Boot] 9. 동기 Postgres의 스케줄러 분리]]
- [[blog/SPRING BOOT/Spring Boot- 6. Java 21 가상 스레드 VS 기존 스레드|[Spring Boot] 6. Java 21 가상 스레드 VS 기존 스레드]]
