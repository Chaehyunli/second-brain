---
title: "[Spring Boot] 3. 로컬 파일 업로드 권한 문제 → supabase"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "java", "spring boot"]
category: "SPRING BOOT"
published: 2026-03-03
source_url: https://ch010104.tistory.com/197
---

# [Spring Boot] 3. 로컬 파일 업로드 권한 문제 → supabase

## 원문

https://ch010104.tistory.com/197

## 핵심 요약

- **상황** — Spring Boot 서버에서 userUpload/DOC 경로에 파일을 저장하려 시도.
- **결과 (빈 껍데기 현상)** — DB(장부): "파일이 저장되었다"고 데이터는 기록됨 (성공).
- **2. 해결책의 진화: 로컬에서 클라우드로** — 이 문제를 해결하려면 "누구의 컴퓨터도 아닌, 모두가 접근 가능한 공용 창고"가 필요합니다.
- **Supabase란?** — 정의: 오픈소스 기반의 서비스형 백엔드(BaaS).

## 관련 글

- [[blog/SPRING BOOT/index|SPRING BOOT]]
- [[blog/SPRING BOOT/Spring Boot- 2. Flyway 마이그래이션 규칙|[Spring Boot] 2. Flyway 마이그래이션 규칙]]
- [[blog/SPRING BOOT/Spring Boot- 1. Spring Boot의 FeignClient 설정(python 포함)|[Spring Boot] 1. Spring Boot의 FeignClient 설정(python 포함)]]
- [[blog/SPRING BOOT/Spring Boot- 5. mock 테스트 코드 작성|[Spring Boot] 5. mock 테스트 코드 작성]]
