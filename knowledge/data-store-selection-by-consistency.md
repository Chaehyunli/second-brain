---
schema_version: 1
id: knowledge-data-store-selection-by-consistency
title: 일관성과 작업 부하에 따른 데이터 저장소 선택
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-06
checked_at: 2026-08-06
tags: [knowledge, initial-curation]
sources:
  - notion/SKALA/7-27 스마트 데이터 이해 및 활용_Day1/7-27 스마트 데이터 이해 및 활용_Day1 핵심 정리.md
  - notion/SKALA/7-28 스마트 데이터 이해 및 활용_Day2/7-28 스마트 데이터 이해 및 활용_Day2 핵심 정리.md
  - notion/Information/2026-07-26 — Cloudflare 실전 가이드 — Workers·Pages·KV·D1·VPS·AWS·CI-CD.md
---

# 일관성과 작업 부하에 따른 데이터 저장소 선택

## 핵심
캐시·설정 저장소·트랜잭션 원장·파일·벡터 인덱스는 같은 데이터를 담을 수 있어도 일관성·조회 패턴·권한·비용이 달라 역할을 분리해야 한다.

## 연결된 근거
- [[notion/SKALA/7-27 스마트 데이터 이해 및 활용_Day1/7-27 스마트 데이터 이해 및 활용_Day1 핵심 정리.md]]
- [[notion/SKALA/7-28 스마트 데이터 이해 및 활용_Day2/7-28 스마트 데이터 이해 및 활용_Day2 핵심 정리.md]]
- [[notion/Information/2026-07-26 — Cloudflare 실전 가이드 — Workers·Pages·KV·D1·VPS·AWS·CI-CD.md]]

## 적용 기준
SQL/벡터 검색 학습과 KV·D1·Vectorize의 역할 구분을 연결한다.

## 주의점 또는 한계
특정 서비스의 consistency 보장은 제품 문서·설정에 의존하므로 캐시를 즉시 일관성이 필요한 진실 원천으로 사용하지 않는다.
