---
title: "[스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술] 5. MVC 프레임워크 만들기"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "inflearn", "spring boot"]
category: "INFLEARN"
published: 2026-04-09
source_url: https://ch010104.tistory.com/259
---

# [스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술] 5. MVC 프레임워크 만들기

## 원문

https://ch010104.tistory.com/259

## 핵심 요약

- **특징** — 프론트 컨트롤러 서블릿 하나로 클라이언트의 요청을 받음
- **2. 프론트 컨트롤러 도입 - v1 (구조 맞추기)** — 기존 로직을 최대한 유지하면서 프론트 컨트롤러만 도입하는 단계입니다.
- **3. View 분리 - v2 (중복 제거)** — 모든 컨트롤러에서 중복되는 forward 로직을 별도의 MyView 객체로 분리합니다.
- **4. Model 추가 - v3 (서블릿 종속성 제거)** — 컨트롤러가 서블릿 기술을 몰라도 동작할 수 있도록 파라미터는 Map으로, 응답은 ModelView 객체로 처리합니다.

## 관련 글

- [[blog/INFLEARN/index|INFLEARN]]
- [[blog/INFLEARN/스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술- 4. 서블릿, JSP, MVC 패턴|[스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술] 4. 서블릿, JSP, MVC 패턴]]
- [[blog/INFLEARN/스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술- 6. 스프링 MVC - 구조 이해|[스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술] 6. 스프링 MVC - 구조 이해]]
- [[blog/INFLEARN/스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술- 1. 웹 애플리케이션의 이해 - 서블릿(Servlet)과 쓰레드(Thread)|[스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술] 1. 웹 애플리케이션의 이해 - 서블릿(Servlet)과 쓰레드(Thread)]]
