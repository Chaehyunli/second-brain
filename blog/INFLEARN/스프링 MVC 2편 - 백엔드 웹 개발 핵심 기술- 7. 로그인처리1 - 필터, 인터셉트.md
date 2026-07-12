---
title: "[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 7. 로그인처리1 - 필터, 인터셉트"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "inflearn", "java", "spring boot"]
category: "INFLEARN"
published: 2026-07-02
source_url: https://ch010104.tistory.com/289
---

# [스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 7. 로그인처리1 - 필터, 인터셉트

## 원문

https://ch010104.tistory.com/289

## 핵심 요약

- **공통 관심 사항 (Cross-Cutting Concern)** — 해결 방향: 모든 컨트롤러 로직(등록, 수정, 삭제, 조회 등)에서 공통으로 로그인 여부를 체크해야 합니다.
- **1) 필터 흐름** — 필터는 서블릿이 지원하는 수문장 역할을 합니다.
- **2) 필터 제한** — 필터는 부적절한 요청을 서블릿 단계로 넘기지 않고 차단할 수 있습니다.
- **3) 필터 체인** — 필터는 체인 형태로 구성되며 자유롭게 중간에 필터를 추가할 수 있습니다.

## 관련 글

- [[blog/INFLEARN/index|INFLEARN]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 6. 로그인처리1 - 쿠키, 세션|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 6. 로그인처리1 - 쿠키, 세션]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 8. 예외 처리와 오류 페이지|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 8. 예외 처리와 오류 페이지]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 5.검증2 - Bean Validation|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 5.검증2 - Bean Validation]]
