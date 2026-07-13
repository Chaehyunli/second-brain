---
title: "[Spring Boot] 1. Spring Boot의 FeignClient 설정(python 포함)"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "java", "spring boot"]
category: "SPRING BOOT"
published: 2026-03-03
source_url: https://ch010104.tistory.com/195
---

# [Spring Boot] 1. Spring Boot의 FeignClient 설정(python 포함)

## 원문

https://ch010104.tistory.com/195

## 핵심 요약

- **왜 사용하는가? (The Why)** — 원래 Java에서 외부 서버에 데이터를 요청하려면 RestTemplate이나 WebClient를 써서 복잡한 코드를 짜야 했습니다.
- **언제 사용하는가? (The When)** — MSA(마이크로서비스) 구조에서 서버 A가 서버 B의 데이터가 필요할 때.
- **2. Spring ↔ Spring 통신 (내부망 통신)** — 같은 Java 환경끼리의 통신이므로 객체 구조가 복잡해도 공유하기 쉽습니다.
- **[Java] 1. 의존성 및 설정** — 파일명: CommonConfig.java (또는 Application 클래스)

## 관련 글

- [[blog/SPRING BOOT/index|SPRING BOOT]]
- [[blog/SPRING BOOT/Spring Boot- 2. Flyway 마이그래이션 규칙|[Spring Boot] 2. Flyway 마이그래이션 규칙]]
- [[blog/SPRING BOOT/Spring Boot- 3. 로컬 파일 업로드 권한 문제 → supabase|[Spring Boot] 3. 로컬 파일 업로드 권한 문제 → supabase]]
- [[blog/SPRING BOOT/Spring Boot- 5. mock 테스트 코드 작성|[Spring Boot] 5. mock 테스트 코드 작성]]
