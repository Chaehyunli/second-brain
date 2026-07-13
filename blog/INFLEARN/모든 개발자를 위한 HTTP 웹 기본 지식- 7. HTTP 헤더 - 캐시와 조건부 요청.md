---
title: "[모든 개발자를 위한 HTTP 웹 기본 지식] 7. HTTP 헤더 - 캐시와 조건부 요청"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "http", "inflearn"]
category: "INFLEARN"
published: 2026-03-31
source_url: https://ch010104.tistory.com/250
---

# [모든 개발자를 위한 HTTP 웹 기본 지식] 7. HTTP 헤더 - 캐시와 조건부 요청

## 원문

https://ch010104.tistory.com/250

## 핵심 요약

- **캐시가 없을 때** — 데이터가 변경되지 않아도 계속 네트워크를 통해 데이터를 다운로드해야 함
- **캐시가 적용** — 첫 번째 요청: 서버가 응답 헤더에 cache-control: max-age=60을 포함하여 전송 (60초간 유효)
- **캐시 시간 초과 후의 상황** — 서버에서 기존 데이터를 변경하지 않음 (이 경우 데이터를 다시 받는 대신 캐시 재사용 가능)
- **Last-Modified와 If-Modified-Since** — 검증 헤더: Last-Modified (데이터 최종 수정일)

## 관련 글

- [[blog/INFLEARN/index|INFLEARN]]
- [[blog/INFLEARN/모든 개발자를 위한 HTTP 웹 기본 지식- 6. HTTP 일반 헤더|[모든 개발자를 위한 HTTP 웹 기본 지식] 6. HTTP 일반 헤더]]
- [[blog/INFLEARN/모든 개발자를 위한 HTTP 웹 기본 지식- 5. HTTP 상태코드 (HTTP Status Codes)|[모든 개발자를 위한 HTTP 웹 기본 지식] 5. HTTP 상태코드 (HTTP Status Codes)]]
- [[blog/INFLEARN/모든 개발자를 위한 HTTP 웹 기본 지식- 4. HTTP 메서드 활용 및 API 설계|[모든 개발자를 위한 HTTP 웹 기본 지식] 4. HTTP 메서드 활용 및 API 설계]]
