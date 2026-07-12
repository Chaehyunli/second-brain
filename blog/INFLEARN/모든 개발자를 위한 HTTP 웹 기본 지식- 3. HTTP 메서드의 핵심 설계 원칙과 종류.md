---
title: "[모든 개발자를 위한 HTTP 웹 기본 지식] 3. HTTP 메서드의 핵심 설계 원칙과 종류"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "http", "infleran"]
category: "INFLEARN"
published: 2026-03-27
source_url: https://ch010104.tistory.com/243
---

# [모든 개발자를 위한 HTTP 웹 기본 지식] 3. HTTP 메서드의 핵심 설계 원칙과 종류

## 원문

https://ch010104.tistory.com/243

## 핵심 요약

- **1. API URI 설계의 핵심: 리소스 식별** — 좋은 URI 설계를 위해서는 행위(동사)와 리소스(명사)를 분리하는 것이 가장 중요합니다.
- **2. 주요 HTTP 메서드 종류** — 기타 메서드: 헤더 정보만 조회하는 HEAD, 통신 가능 옵션을 설명하는 OPTIONS, 터널 설정을 위한 CONNECT, 경로 테스트용 TRACE 등이 있습니다.
- **3. HTTP 메서드의 속성** — 메서드의 특성을 이해하면 안정적인 시스템 설계가 가능합니다.
- **① 안전 (Safe)** — 해당 메서드: GET, HEAD, OPTIONS, TRACE.

## 관련 글

- [[blog/INFLEARN/index|INFLEARN]]
- [[blog/INFLEARN/모든 개발자를 위한 HTTP 웹 기본 지식- 2. URI의 개념과 웹 브라우저의 요청 흐름|[모든 개발자를 위한 HTTP 웹 기본 지식] 2. URI의 개념과 웹 브라우저의 요청 흐름]]
- [[blog/INFLEARN/모든 개발자를 위한 HTTP 웹 기본 지식- 4. HTTP 메서드 활용 및 API 설계|[모든 개발자를 위한 HTTP 웹 기본 지식] 4. HTTP 메서드 활용 및 API 설계]]
- [[blog/INFLEARN/모든 개발자를 위한 HTTP 웹 기본 지식- 1. 인터넷 네트워크|[모든 개발자를 위한 HTTP 웹 기본 지식] 1. 인터넷 네트워크]]
