---
title: "[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 6. 로그인처리1 - 쿠키, 세션"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "inflearn", "java", "spring boot"]
category: "INFLEARN"
published: 2026-07-02
source_url: https://ch010104.tistory.com/288
---

# [스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 6. 로그인처리1 - 쿠키, 세션

## 원문

https://ch010104.tistory.com/288

## 핵심 요약

- **1) 화면 흐름 및 UI 요구사항** — 회원 가입: 로그인 ID, 비밀번호, 이름 입력
- **2) 보안 요구사항** — 로그인한 사용자만 상품에 접근하고 관리할 수 있어야 함.
- **2. 패키지 구조 설계** — 비즈니스 룰을 담는 핵심 영역인 도메인(Domain)과 사용자 화면 및 요청 처리를 담당하는 웹(Web) 영역을 명확히 분리하여 설계해야 한다.
- **도메인과 웹의 의존관계 원칙** — 도메인(Domain): 화면, UI, 기술 인프라 등등의 영역을 제외한 시스템이 구현해야 하는 핵심 비즈니스 업무 영역.

## 관련 글

- [[blog/INFLEARN/index|INFLEARN]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 5.검증2 - Bean Validation|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 5.검증2 - Bean Validation]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 7. 로그인처리1 - 필터, 인터셉트|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 7. 로그인처리1 - 필터, 인터셉트]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 8. 예외 처리와 오류 페이지|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 8. 예외 처리와 오류 페이지]]
