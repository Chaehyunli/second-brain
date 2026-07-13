---
title: "[스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술] 1. 웹 애플리케이션의 이해 - 서블릿(Servlet)과 쓰레드(Thread)"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "inflearn", "spring boot"]
category: "INFLEARN"
published: 2026-04-01
source_url: https://ch010104.tistory.com/252
---

# [스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술] 1. 웹 애플리케이션의 이해 - 서블릿(Servlet)과 쓰레드(Thread)

## 원문

https://ch010104.tistory.com/252

## 핵심 요약

- **서블릿(Servlet) 개념 및 동작 원리 정리** — 서블릿은 자바를 사용하여 웹 페이지를 동적으로 생성하는 서버측 프로그램 사양을 의미합니다.
- **코드 구조 분석** — URL 매핑: @WebServlet 어노테이션의 urlPatterns에 지정된 URL(예: /hello)이 호출되면 해당 서블릿 코드가 실행됩니다.
- **2. 서블릿 컨테이너 (Servlet Container)** — 톰캣(Tomcat)처럼 서블릿을 지원하는 WAS를 서블릿 컨테이너라고 부릅니다.
- **쓰레드란?** — 애플리케이션 코드를 하나하나 순차적으로 실행하는 주체입니다.

## 관련 글

- [[blog/INFLEARN/index|INFLEARN]]
- [[blog/INFLEARN/스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술- 4. 서블릿, JSP, MVC 패턴|[스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술] 4. 서블릿, JSP, MVC 패턴]]
- [[blog/INFLEARN/스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술- 5. MVC 프레임워크 만들기|[스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술] 5. MVC 프레임워크 만들기]]
- [[blog/INFLEARN/스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술- 6. 스프링 MVC - 구조 이해|[스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술] 6. 스프링 MVC - 구조 이해]]
