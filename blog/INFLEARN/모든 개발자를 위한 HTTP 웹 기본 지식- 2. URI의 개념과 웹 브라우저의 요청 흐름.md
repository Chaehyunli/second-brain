---
title: "[모든 개발자를 위한 HTTP 웹 기본 지식] 2. URI의 개념과 웹 브라우저의 요청 흐름"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "http", "inflearn"]
category: "INFLEARN"
published: 2026-03-27
source_url: https://ch010104.tistory.com/242
---

# [모든 개발자를 위한 HTTP 웹 기본 지식] 2. URI의 개념과 웹 브라우저의 요청 흐름

## 원문

https://ch010104.tistory.com/242

## 핵심 요약

- **1. URI (Uniform Resource Identifier)의 이해** — URI는 리소스를 식별하는 통일된 방식을 의미하며, 크게 URL과 URN으로 분류됩니다.
- **URL의 전체 문법과 구조** — scheme://[userinfo@]host[:port][/path][?query][#fragment]
- **2. 웹 브라우저 요청 흐름** — 사용자가 URL을 입력했을 때, 서버로부터 결과를 받기까지의 과정은 다음과 같습니다.
- **1단계: 요청 메시지 생성 및 패킷 전달** — DNS 조회: 도메인명을 통해 서버의 IP 주소를 확인하고 포트 번호를 파악합니다.

## 관련 글

- [[blog/INFLEARN/index|INFLEARN]]
- [[blog/INFLEARN/모든 개발자를 위한 HTTP 웹 기본 지식- 1. 인터넷 네트워크|[모든 개발자를 위한 HTTP 웹 기본 지식] 1. 인터넷 네트워크]]
- [[blog/INFLEARN/모든 개발자를 위한 HTTP 웹 기본 지식- 4. HTTP 메서드 활용 및 API 설계|[모든 개발자를 위한 HTTP 웹 기본 지식] 4. HTTP 메서드 활용 및 API 설계]]
- [[blog/INFLEARN/모든 개발자를 위한 HTTP 웹 기본 지식- 5. HTTP 상태코드 (HTTP Status Codes)|[모든 개발자를 위한 HTTP 웹 기본 지식] 5. HTTP 상태코드 (HTTP Status Codes)]]
