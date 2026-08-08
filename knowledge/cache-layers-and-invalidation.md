---
schema_version: 1
id: knowledge-cache-layers-and-invalidation
title: 캐시 계층·범위·무효화 전략
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-08
checked_at: 2026-08-08
tags: [knowledge, initial-curation]
sources:
  - blog/INFLEARN/모든 개발자를 위한 HTTP 웹 기본 지식- 7. HTTP 헤더 - 캐시와 조건부 요청.md
  - blog/NETWORK/네트워크- 쿠키 (Cookies)와 Proxy Servers.md
  - blog/JAVA/SpingBoot- Api 호출시 Redis를 활용한 캐시 저장.md
---

# 캐시 계층·범위·무효화 전략

## 결정해야 하는 대상
같은 “캐시”라도 브라우저, proxy/CDN, 애플리케이션 Redis는 저장 위치·공유 범위·제어 수단이 다르다.

## 계층 지도
HTTP 계층은 `Cache-Control`과 조건부 요청으로 신선도를 협상한다. 애플리케이션 계층은 Redis TTL과 `@CacheEvict`처럼 데이터 변경과 연결된 정책을 둔다.

## 키와 신선도의 관계
캐시 키는 사용자별·권한별 응답을 공유하지 않도록 범위를 표현해야 한다. TTL만으로 충분한지, 변경 시 명시적 무효화나 재검증이 필요한지는 데이터 변경 흐름에서 정한다.

## 성능 수단을 구분하기
[[knowledge/query-planning-index-and-pagination]]의 인덱스는 원본 조회의 접근 경로이고 캐시는 이미 계산·조회한 응답의 저장 정책이다. 어느 하나가 다른 하나의 검증을 대체하지 않는다.

## 실패 예방과 한계
오래된 응답, 잘못된 키, 민감 응답 공유를 점검한다. 적절한 TTL·무효화 시점과 성능 효과는 서비스별 데이터 갱신·권한 모델을 확인해야 한다.

## 확인한 근거
- [[blog/INFLEARN/모든 개발자를 위한 HTTP 웹 기본 지식- 7. HTTP 헤더 - 캐시와 조건부 요청]]
- [[blog/NETWORK/네트워크- 쿠키 (Cookies)와 Proxy Servers]]
- [[blog/JAVA/SpingBoot- Api 호출시 Redis를 활용한 캐시 저장]]
