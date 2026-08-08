---
schema_version: 1
id: knowledge-rag-retrieval-and-data-boundaries
title: RAG 검색 품질과 데이터 경계
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-06
checked_at: 2026-08-06
tags: [knowledge, initial-curation, Transformer, database, postgresql, sql]
sources:
  - blog/STUDYING/STUDYING- 12 - 1. 스마트 데이터 이해 및 활용_Day4_핵심 정리.md
  - notion/SKALA/7-28 스마트 데이터 이해 및 활용_Day2/7-28 스마트 데이터 이해 및 활용_Day2 핵심 정리.md
  - notion/Information/2026-07-26 — Cloudflare 실전 가이드 — Workers·Pages·KV·D1·VPS·AWS·CI-CD.md
---

# RAG 검색 품질과 데이터 경계

## 핵심
RAG는 벡터 검색 결과를 LLM 컨텍스트로 제한해 주입하는 구조이며, 검색 인덱스와 원본·권한·메타데이터의 진실 원천을 분리해야 한다.

## 연결된 근거
- [[blog/STUDYING/STUDYING- 12 - 1. 스마트 데이터 이해 및 활용_Day4_핵심 정리.md]]
- [[notion/SKALA/7-28 스마트 데이터 이해 및 활용_Day2/7-28 스마트 데이터 이해 및 활용_Day2 핵심 정리.md]]
- [[notion/Information/2026-07-26 — Cloudflare 실전 가이드 — Workers·Pages·KV·D1·VPS·AWS·CI-CD.md]]

## 적용 기준
chunking·필터·reranking·freshness·provenance와 embeddings·pgvector 흐름, 관계형/객체 저장소의 원본·권한 역할을 연결한다.

## 주의점 또는 한계
검색 결과가 출처의 진실성을 자동 보장하지 않으므로 인용·권한 확인·출력 검증이 필요하다.
