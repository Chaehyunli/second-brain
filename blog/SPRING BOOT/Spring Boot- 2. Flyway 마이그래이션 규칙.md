---
title: "[Spring Boot] 2. Flyway 마이그래이션 규칙"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "java", "spring boot"]
category: "SPRING BOOT"
published: 2026-03-03
source_url: https://ch010104.tistory.com/196
---

# [Spring Boot] 2. Flyway 마이그래이션 규칙

## 원문

https://ch010104.tistory.com/196

## 핵심 요약

- **1. Flyway 장애 원인 요약 (Post-Mortem)** — 문제: 공용 DB(public)의 장부에는 20260210102236 기록이 있는데, 내 로컬 폴더(가방)에는 해당 파일이 없음.
- **① 테이블 생성 (Create Table)** — 테이블이 이미 존재할 경우 에러가 나는 것을 방지합니다.
- **② 컬럼 이름 변경 (Rename Column) - 질문하신 핵심 쿼리** — 이미 이름이 바뀌어 있거나, 컬럼이 없는 경우에도 에러 없이 실행됩니다.
- **③ 컬럼 추가 및 코멘트 (Add Column & Comment)** — 컬럼이 이미 추가되어 있을 때 중복 추가 에러를 방지합니다.

## 관련 글

- [[blog/SPRING BOOT/index|SPRING BOOT]]
- [[blog/SPRING BOOT/Spring Boot- 1. Spring Boot의 FeignClient 설정(python 포함)|[Spring Boot] 1. Spring Boot의 FeignClient 설정(python 포함)]]
- [[blog/SPRING BOOT/Spring Boot- 3. 로컬 파일 업로드 권한 문제 → supabase|[Spring Boot] 3. 로컬 파일 업로드 권한 문제 → supabase]]
- [[blog/SPRING BOOT/Spring Boot- 5. mock 테스트 코드 작성|[Spring Boot] 5. mock 테스트 코드 작성]]
