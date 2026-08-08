---
schema_version: 1
id: knowledge-rag-retrieval-and-data-boundaries
title: RAG 검색 품질과 데이터 경계
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-08
checked_at: 2026-08-08
tags: [knowledge, initial-curation, Transformer, database, postgresql, sql]
sources:
  - blog/STUDYING/STUDYING- 12 - 1. 스마트 데이터 이해 및 활용_Day4_핵심 정리.md
  - notion/SKALA/7-28 스마트 데이터 이해 및 활용_Day2/7-28 스마트 데이터 이해 및 활용_Day2 핵심 정리.md
  - notion/Information/2026-07-26 — Cloudflare 실전 가이드 — Workers·Pages·KV·D1·VPS·AWS·CI-CD.md
---

# RAG 검색 품질과 데이터 경계

## 데이터 흐름 지도
원본 → chunk·metadata → embedding/index → retrieval·reranking → context → response의 흐름에서 각 단계는 다른 책임을 가진다.

## 진실 원천과 인덱스
검색 인덱스는 원본을 찾기 위한 파생물이고, 원본·권한·메타데이터의 진실 원천을 대체하지 않는다. 관계형·객체 저장소와 벡터 검색 역할을 분리한다.

## 품질을 좌우하는 선택
chunking, 필터, reranking, freshness, provenance는 검색 결과의 쓰임을 정한다. retrieval 결과는 [[knowledge/context-engineering-and-tool-grounding]]에서 말하는 근거 입력이 될 수 있지만 답변의 사실성을 자동 보장하지 않는다.

## 권한과 출력 검증
검색 전에 접근 권한을 확인하고, 응답에서는 인용·출처·출력 제약을 검증한다.

## 실패 모드와 한계
오래된 인덱스, 권한 누출, 검색 성공을 사실성으로 오인하는 오류를 구분한다. [[knowledge/cache-layers-and-invalidation]]과 freshness 문제가 닿지만 RAG의 provenance·권한 문제를 일반 캐시 무효화로 환원하지 않는다.

## 근거
- [[blog/STUDYING/STUDYING- 12 - 1. 스마트 데이터 이해 및 활용_Day4_핵심 정리]]
- [[notion/SKALA/7-28 스마트 데이터 이해 및 활용_Day2/7-28 스마트 데이터 이해 및 활용_Day2 핵심 정리]]
- [[notion/Information/2026-07-26 — Cloudflare 실전 가이드 — Workers·Pages·KV·D1·VPS·AWS·CI-CD]]
