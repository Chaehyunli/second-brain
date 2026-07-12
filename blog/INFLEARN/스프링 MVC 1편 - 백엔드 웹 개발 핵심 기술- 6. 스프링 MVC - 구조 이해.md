---
title: "[스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술] 6. 스프링 MVC - 구조 이해"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "inflearn", "spring boot"]
category: "INFLEARN"
published: 2026-04-14
source_url: https://ch010104.tistory.com/261
---

# [스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술] 6. 스프링 MVC - 구조 이해

## 원문

https://ch010104.tistory.com/261

## 핵심 요약

- **1. 스프링 MVC 전체 구조** — 스프링 MVC는 프론트 컨트롤러 패턴으로 구현되어 있으며, 그 핵심은 DispatcherServlet입니다.
- **1.1 직접 만든 프레임워크 vs 스프링 MVC 비교** — FrontController → DispatcherServlet
- **1.2 DispatcherServlet 구조** — org.springframework.web.servlet.DispatcherServlet
- **1.3 동작 순서 (중요)** — 핸들러 조회: 핸들러 매핑을 통해 URL에 매핑된 핸들러(컨트롤러)를 조회한다.

## 관련 글

- [[blog/INFLEARN/index|INFLEARN]]
- [[blog/INFLEARN/스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술- 5. MVC 프레임워크 만들기|[스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술] 5. MVC 프레임워크 만들기]]
- [[blog/INFLEARN/스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술- 4. 서블릿, JSP, MVC 패턴|[스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술] 4. 서블릿, JSP, MVC 패턴]]
- [[blog/INFLEARN/스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술- 1. 웹 애플리케이션의 이해 - 서블릿(Servlet)과 쓰레드(Thread)|[스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술] 1. 웹 애플리케이션의 이해 - 서블릿(Servlet)과 쓰레드(Thread)]]
