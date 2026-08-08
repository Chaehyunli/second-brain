---
schema_version: 1
id: knowledge-cache-layers-and-invalidation
title: 캐시 계층·범위·무효화 전략
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-06
checked_at: 2026-08-06
tags: [knowledge, initial-curation]
sources:
  - blog/INFLEARN/모든 개발자를 위한 HTTP 웹 기본 지식- 7. HTTP 헤더 - 캐시와 조건부 요청.md
  - blog/NETWORK/네트워크- 쿠키 (Cookies)와 Proxy Servers.md
  - blog/JAVA/SpingBoot- Api 호출시 Redis를 활용한 캐시 저장.md
---

# 캐시 계층·범위·무효화 전략

## 핵심
캐시는 브라우저·프록시·애플리케이션처럼 위치별 책임이 다르며, 키 범위·유효 기간·변경 뒤 무효화 또는 재검증을 함께 설계해야 한다.

## 연결된 근거
- [[blog/INFLEARN/모든 개발자를 위한 HTTP 웹 기본 지식- 7. HTTP 헤더 - 캐시와 조건부 요청.md]]
- [[blog/NETWORK/네트워크- 쿠키 (Cookies)와 Proxy Servers.md]]
- [[blog/JAVA/SpingBoot- Api 호출시 Redis를 활용한 캐시 저장.md]]

## 적용 기준
`Cache-Control`·조건부 요청은 HTTP 계층의 신선도 제어이고, Redis TTL·`@CacheEvict`는 애플리케이션 데이터 변경과 결합된 정책이다.

## 주의점 또는 한계
인덱스나 캐시를 성능 만능 수단으로 취급하지 않는다. 민감 응답의 저장 범위와 무효화 시점은 서비스별로 검토한다.
