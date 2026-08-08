---
schema_version: 1
id: knowledge-query-planning-index-and-pagination
title: 쿼리 계획·인덱스·대용량 페이지네이션
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-08
checked_at: 2026-08-08
tags: [knowledge, initial-curation, database, sql, postgresql]
sources:
  - blog/SQL/SQL- MySql의 인덱스 설정 - BTREE INDEX.md
  - blog/DATABASE DESIGN/데이터베이스 설계- 쿼리 최적화 (Query Optimization).md
  - notion/SKALA/7-29 스마트 데이터 이해 및 활용_Day3/7-29 스마트 데이터 이해 및 활용_Day3 핵심 정리.md
---

# 쿼리 계획·인덱스·대용량 페이지네이션

## 성능 문제를 정의하는 모양
필터, 조인, 정렬, cardinality, 페이지 깊이가 함께 query shape를 만든다. 인덱스 추가는 이 모양과 실행 계획을 읽은 뒤의 선택이다.

## 실행 계획에서 볼 것
접근 경로, 예상·실제 행 수, 정렬, 조인 전략을 확인해 병목 가설을 세운다. 비용 기반 최적화는 DBMS별 통계와 구현에 따라 다르게 동작한다.

## 인덱스의 트레이드오프
BTREE와 복합 인덱스는 읽기를 도울 수 있지만 쓰기 비용·저장 공간·선택도를 함께 바꾼다. 정렬과 필터의 순서를 실제 질의로 확인한다.

## 페이지네이션 선택
깊은 OFFSET은 건너뛸 행이 늘어날 수 있다. 안정 정렬과 cursor 접근은 대안이지만 정렬 키와 사용자 경험을 함께 정해야 한다.

## 캐시·측정과의 구분
[[knowledge/cache-layers-and-invalidation]]은 저장·신선도 정책이고, [[knowledge/performance-investigation-and-measurement-boundaries]]는 사례의 측정 경계다. 각각을 인덱스의 대체 수단으로 말하지 않는다.

## 근거와 불확실성
- [[blog/SQL/SQL- MySql의 인덱스 설정 - BTREE INDEX]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 쿼리 최적화 (Query Optimization)]]
- [[notion/SKALA/7-29 스마트 데이터 이해 및 활용_Day3/7-29 스마트 데이터 이해 및 활용_Day3 핵심 정리]]
