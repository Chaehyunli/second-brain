---
title: "[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 1. 타임리프(Thymeleaf) 기본 기능"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "inflearn", "springboot", "thymeleaf"]
category: "INFLEARN"
published: 2026-05-02
source_url: https://ch010104.tistory.com/269
---

# [스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 1. 타임리프(Thymeleaf) 기본 기능

## 원문

https://ch010104.tistory.com/269

## 핵심 요약

- **핵심 개념** — 서버 사이드 HTML 렌더링 (SSR): 백엔드 서버에서 HTML을 동적으로 생성하여 클라이언트에 전달합니다.
- **타임리프 사용 선언** — HTML 파일 상단 <html> 태그에 아래 속성을 추가해야 합니다.
- **개념 설명** — Escape: HTML에서 사용하는 특수 문자(<, >)를 HTML 엔티티(&lt;, &gt;)로 변경하는 것.
- **소스코드** — [파일 경로: src/main/java/hello/thymeleaf/basic/BasicController.java]

## 관련 글

- [[blog/INFLEARN/index|INFLEARN]]
- [[blog/INFLEARN/스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술- 3. Servlet|[스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술] 3. Servlet]]
- [[blog/INFLEARN/스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술- 2. HTML, HTTP API, CSR, SSR|[스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술] 2. HTML, HTTP API, CSR, SSR]]
- [[blog/INFLEARN/스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술- 8. 스프링 MVC - 웹 페이지 만들기|[스프링 MVC 1편 - 백엔드 웹 개발 핵심 기술] 8. 스프링 MVC - 웹 페이지 만들기]]
