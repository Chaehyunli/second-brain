---
title: "[Spring Boot] 7. Spring Boot CORS 중복 응답(web & webflux 충돌)"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "java", "spring boot"]
category: "SPRING BOOT"
published: 2026-03-04
source_url: https://ch010104.tistory.com/205
---

# [Spring Boot] 7. Spring Boot CORS 중복 응답(web & webflux 충돌)

## 원문

https://ch010104.tistory.com/205

## 핵심 요약

- **1. 배경 및 문제 식별** — 프로젝트 구조: React Native(Web/App) → Spring Boot(Java) → FastAPI(Python) 문제 현상: 웹 브라우저에서 Java 서버로 API 호출 시, 아래와 같은 CORS 에러 발생하며 통신 차단.
- **의존성 (build.gradle)** — 전통적인 REST API를 위한 spring-boot-starter-web과 FastAPI와의 비동기 통신을 위한 spring-boot-starter-webflux를 동시에 사용.
- **CORS 설정 (WebConfig.java)** — 처음에는 WebMvcConfigurer를 사용했으나, 우선순위 문제 해결을 위해 CorsFilter를 Bean으로 직접 등록하는 정석적인 방식을 채택함.
- **3. 해결 시도 과정 및 시행착오** — 좀비 프로세스 확인: netstat과 taskkill을 통해 이전 설정이 남은 서버가 중복 실행 중인지 확인 (확인 결과 단일 실행 중).

## 관련 글

- [[blog/SPRING BOOT/index|SPRING BOOT]]
- [[blog/SPRING BOOT/Spring Boot- 8. 비동기 Spring WebClient, Mono와 Flux|[Spring Boot] 8. 비동기 Spring WebClient, Mono와 Flux]]
- [[blog/SPRING BOOT/Spring Boot- 9. 동기 Postgres의 스케줄러 분리|[Spring Boot] 9. 동기 Postgres의 스케줄러 분리]]
- [[blog/SPRING BOOT/Spring Boot- 6. Java 21 가상 스레드 VS 기존 스레드|[Spring Boot] 6. Java 21 가상 스레드 VS 기존 스레드]]
