---
title: "[Python] Elasticsearch 클라이언트 분석 및 검색 개념 정리 - Searchive 프로젝트"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "ElasticSearch", "Python"]
category: "PYTHON"
published: 2026-03-28
source_url: https://ch010104.tistory.com/245
---

# [Python] Elasticsearch 클라이언트 분석 및 검색 개념 정리 - Searchive 프로젝트

## 원문

https://ch010104.tistory.com/245

## 핵심 요약

- **1. 엘라스틱서치 핵심 쿼리 개념 (Query DSL)** — 엘라스틱서치에서 bool 쿼리는 여러 조건을 조합할 때 사용하며, 4가지 핵심 인자를 가집니다.
- **예시 코드 (쇼핑몰 검색 시나리오)** — "삼성 노트북 중에서 100만원 이하이거나 리뷰 점수가 높은 상품을 검색 (단, 품절 상품은 제외)"
- **각 항목의 의미** — must (반드시 포함): 조건이 반드시 참이어야 하며 점수 계산에 반영됩니다.
- **2. 인덱스 설정 분석 (Nori 및 인프라 설정)** — 프로젝트의 create_index_if_not_exists 메서드에 구현된 설정입니다.

## 관련 글

- [[blog/PYTHON/index|PYTHON]]
- [[blog/PYTHON/Python- Searchive 프로젝트( 2 ) - KeyBert, ElasticSearch 고도화|[Python] Searchive 프로젝트( 2 ) - KeyBert, ElasticSearch 고도화]]
- [[blog/PYTHON/Python- Searchive 프로젝트( 1 ) - MinIO, ElasticSearch, KeyBert|[Python] Searchive 프로젝트( 1 ) - MinIO, ElasticSearch, KeyBert]]
- [[blog/CODINGTEST/코딩테스트- 현대오토 2026-04-05 회고|[코딩테스트] 현대오토 2026-04-05 회고]]
