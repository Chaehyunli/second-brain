---
title: "[스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술] 3. Servlet"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "inflearn", "springboot"]
category: "INFLEARN"
published: 2026-04-07
source_url: https://ch010104.tistory.com/256
---

# [스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술] 3. Servlet

## 원문

https://ch010104.tistory.com/256

## 핵심 요약

- **1.1 스프링 부트 서블릿 환경 구성** — 스프링 부트는 서블릿을 직접 등록해서 사용할 수 있도록 @ServletComponentScan을 지원합니다.
- **1.2 서블릿 등록 및 호출** — 서블릿은 HttpServlet을 상속받아 구현하며, HTTP 요청이 매핑된 URL로 들어오면 서블릿 컨테이너는 service 메서드를 실행합니다.
- **1.3 HTTP 요청 메시지 로그 확인** — 개발 단계에서 서버가 받은 HTTP 요청 메시지 전체를 로그로 확인하려면 application.properties에 설정을 추가합니다.
- **2.1 역할** — HTTP 요청 메시지 파싱: 개발자 대신 HTTP 요청 메시지를 파싱하여 그 결과를 객체에 담아 제공합니다.

## 관련 글

- [[blog/INFLEARN/index|INFLEARN]]
- [[blog/INFLEARN/스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술- 2. HTML, HTTP API, CSR, SSR|[스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술] 2. HTML, HTTP API, CSR, SSR]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 1. 타임리프(Thymeleaf) 기본 기능|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 1. 타임리프(Thymeleaf) 기본 기능]]
- [[blog/INFLEARN/스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술- 4. 서블릿, JSP, MVC 패턴|[스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술] 4. 서블릿, JSP, MVC 패턴]]
