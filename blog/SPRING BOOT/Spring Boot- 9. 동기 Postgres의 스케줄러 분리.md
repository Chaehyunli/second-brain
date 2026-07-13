---
title: "[Spring Boot] 9. 동기 Postgres의 스케줄러 분리"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "java", "spring boot"]
category: "SPRING BOOT"
published: 2026-03-04
source_url: https://ch010104.tistory.com/207
---

# [Spring Boot] 9. 동기 Postgres의 스케줄러 분리

## 원문

https://ch010104.tistory.com/207

## 핵심 요약

- **1. 서두: 성능 최적화를 위한 아키텍처 설계 상황** — 현재 프로젝트의 성능을 극대화하기 위해 Full-Async 지향 구조를 설계했습니다.
- **2. 전략: 스케줄러 분리와 자원 동기화** — Postgres는 현재 JPA(동기) 방식을 사용하므로, 메인 비동기 일꾼(Event Loop)이 DB 작업 때문에 멈추는 것을 방지하기 위해 **boundedElastic**이라는 별도의 주차장(스레드 풀)을 할당했습니다.
- **🔧 설정 1: 환경 변수 (.env 또는 application.properties)** — DB 커넥션(열쇠)의 개수를 명확히 정의합니다.
- **3. 왜 '열쇠'와 '일꾼'의 수가 동일해야 하는가?** — 일꾼(Thread) > 열쇠(Connection): 일꾼은 많은데 열쇠가 부족하면, 남은 일꾼들은 열쇠가 날 때까지 주차장에서 대기하며 메모리만 낭비하고 컨텍스트 스위칭 비용만 발생시킵니다.

## 관련 글

- [[blog/SPRING BOOT/index|SPRING BOOT]]
- [[blog/SPRING BOOT/Spring Boot- 8. 비동기 Spring WebClient, Mono와 Flux|[Spring Boot] 8. 비동기 Spring WebClient, Mono와 Flux]]
- [[blog/SPRING BOOT/Spring Boot- 7. Spring Boot CORS 중복 응답(web & webflux 충돌)|[Spring Boot] 7. Spring Boot CORS 중복 응답(web & webflux 충돌)]]
- [[blog/SPRING BOOT/Spring Boot- 6. Java 21 가상 스레드 VS 기존 스레드|[Spring Boot] 6. Java 21 가상 스레드 VS 기존 스레드]]
