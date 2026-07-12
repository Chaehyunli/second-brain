---
title: "[Spring Boot] 5. mock 테스트 코드 작성"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "java", "spring boot"]
category: "SPRING BOOT"
published: 2026-03-03
source_url: https://ch010104.tistory.com/199
---

# [Spring Boot] 5. mock 테스트 코드 작성

## 원문

https://ch010104.tistory.com/199

## 핵심 요약

- **1. 테스트 계층별 요약표** — 각 계층은 서로 다른 목적을 가지고 있으며, 사용하는 도구도 다릅니다.
- **① Controller 테스트: "사용자를 어디로 보낼 것인가?"** — 서버 전체를 띄우지 않고 HTTP 요청과 응답만 가짜로 시뮬레이션합니다.
- **② Service 테스트: "로직이 수학적으로 맞는가?"** — DB 연결을 완전히 끊고, 순수 자바 코드의 논리(if문, exception 등)만 검증합니다.
- **③ Repository 테스트: "DB 테이블과 쿼리가 맞는가?"** — 실제 DB(H2, Docker 등)에 쿼리를 날려 봅니다.

## 관련 글

- [[blog/SPRING BOOT/index|SPRING BOOT]]
- [[blog/SPRING BOOT/Spring Boot- 6. Java 21 가상 스레드 VS 기존 스레드|[Spring Boot] 6. Java 21 가상 스레드 VS 기존 스레드]]
- [[blog/SPRING BOOT/Spring Boot- 3. 로컬 파일 업로드 권한 문제 → supabase|[Spring Boot] 3. 로컬 파일 업로드 권한 문제 → supabase]]
- [[blog/SPRING BOOT/Spring Boot- 2. Flyway 마이그래이션 규칙|[Spring Boot] 2. Flyway 마이그래이션 규칙]]
