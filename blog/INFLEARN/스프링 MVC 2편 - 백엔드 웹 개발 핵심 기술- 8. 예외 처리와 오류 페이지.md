---
title: "[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 8. 예외 처리와 오류 페이지"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "inflearn", "java", "spring boot"]
category: "INFLEARN"
published: 2026-07-04
source_url: https://ch010104.tistory.com/290
---

# [스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 8. 예외 처리와 오류 페이지

## 원문

https://ch010104.tistory.com/290

## 핵심 요약

- **1. 서블릿 예외 처리 - 시작** — 스프링 프레임워크가 없는 순수 서블릿 컨테이너(WAS) 환경에서는 기본적으로 다음 2가지 방식으로 예외 처리를 지원합니다.
- **자바 직접 실행 시** — 실행 도중 예외를 잡지 못하고 main() 메서드를 넘어서 던져지면, 에러 로그를 남기고 해당 쓰레드는 종료됩니다.
- **웹 애플리케이션 실행 시** — 사용자 요청별로 독립적인 쓰레드가 할당되어 서블릿 컨테이너 안에서 동작합니다.
- **ServletExController - 예외 발생 컨트롤러 코드** — WAS는 서버 내부에서 복구되지 못한 Exception을 500 오류로 처리합니다.

## 관련 글

- [[blog/INFLEARN/index|INFLEARN]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 7. 로그인처리1 - 필터, 인터셉트|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 7. 로그인처리1 - 필터, 인터셉트]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 9. API 예외 처리|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 9. API 예외 처리]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 6. 로그인처리1 - 쿠키, 세션|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 6. 로그인처리1 - 쿠키, 세션]]
