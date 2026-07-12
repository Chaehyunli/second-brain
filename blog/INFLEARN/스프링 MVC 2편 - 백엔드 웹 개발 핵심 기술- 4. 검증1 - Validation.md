---
title: "[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 4. 검증1 - Validation"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "inflearn", "spring boot"]
category: "INFLEARN"
published: 2026-05-31
source_url: https://ch010104.tistory.com/280
---

# [스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 4. 검증1 - Validation

## 원문

https://ch010104.tistory.com/280

## 핵심 요약

- **1) 상품 관리 시스템 검증 요구사항** — 새로운 상품을 등록하거나 수정할 때, 올바르지 않은 값이 들어오면 검증 오류를 발생시켜야 합니다.
- **2) 클라이언트 검증 vs 서버 검증** — 웹 애플리케이션의 검증은 크게 두 가지 영역으로 나뉘며, 상호 보완적으로 사용되어야 합니다.
- **2. 검증 직접 처리 (V1)** — 스프링이 제공하는 검증 기능을 사용하기 전에, 순수 자바 Map을 사용하여 직접 검증 로직을 구현하는 흐름을 살펴봅니다.
- **1) 아키텍처 흐름도** — 성공 흐름: GET /add (상품 등록 폼) → 사용자 입력 → POST /add (컨트롤러에서 검증 성공) → 상품 저장 → Redirect /items/{id} → GET /items/{id} (상품 상세 뷰)

## 관련 글

- [[blog/INFLEARN/index|INFLEARN]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 3. 메시지와 국제화|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 3. 메시지와 국제화]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 2. 타임리프 - 스프링 통합과 폼|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 2. 타임리프 - 스프링 통합과 폼]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 5.검증2 - Bean Validation|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 5.검증2 - Bean Validation]]
