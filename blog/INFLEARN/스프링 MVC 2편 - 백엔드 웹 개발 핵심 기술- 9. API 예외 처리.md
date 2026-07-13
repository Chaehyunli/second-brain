---
title: "[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 9. API 예외 처리"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "inflearn", "java", "spring boot"]
category: "INFLEARN"
published: 2026-07-04
source_url: https://ch010104.tistory.com/291
---

# [스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 9. API 예외 처리

## 원문

https://ch010104.tistory.com/291

## 핵심 요약

- **목표** — HTML 페이지의 경우 4xx, 5xx와 같은 오류 페이지만 있으면 대부분의 문제를 해결할 수 있습니다.
- **WebServerCustomizer 다시 동작** — 예외가 발생했을 때 WAS가 오류 페이지 경로를 호출하도록 이전에 작성했던 WebServerCustomizer를 다시 활성화합니다.
- **ApiExceptionController (테스트용 API 컨트롤러)** — id의 값이 "ex"로 들어오면 RuntimeException이 발생합니다.
- **2. 예외 발생 호출 (문제 발생)** — HTTP Header Accept: application/json

## 관련 글

- [[blog/INFLEARN/index|INFLEARN]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 8. 예외 처리와 오류 페이지|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 8. 예외 처리와 오류 페이지]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 10. 스프링 타입 컨버터|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 10. 스프링 타입 컨버터]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 7. 로그인처리1 - 필터, 인터셉트|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 7. 로그인처리1 - 필터, 인터셉트]]
