---
title: "[Python] Searchive 프로젝트( 2 ) - KeyBert, ElasticSearch 고도화"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "ElasticSearch", "fastapi", "KeyBert", "Minio", "PostgreSQL", "Python", "searchive"]
category: "PYTHON"
published: 2025-10-11
source_url: https://ch010104.tistory.com/156
---

# [Python] Searchive 프로젝트( 2 ) - KeyBert, ElasticSearch 고도화

## 원문

https://ch010104.tistory.com/156

## 핵심 요약

- 이 시스템은 두 가지 키워드 추출 전략을 상황에 맞게 사용하는 하이브리드(Hybrid) 방식을 채택
- **2. KeyBERT 사용법 (Cold Start 용)** — KeyBERT는 BERT 모델을 기반으로 텍스트와 가장 유사한 키워드를 찾아주는 라이브러리
- **3. Elasticsearch 사용법 (Normal 단계용)** — 데이터가 일정량 이상 쌓이면, Elasticsearch의 통계 기반 기능을 활용하는 것이 더 효과적

## 관련 글

- [[blog/PYTHON/index|PYTHON]]
- [[blog/PYTHON/Python- Searchive 프로젝트( 1 ) - MinIO, ElasticSearch, KeyBert|[Python] Searchive 프로젝트( 1 ) - MinIO, ElasticSearch, KeyBert]]
- [[blog/PYTHON/Python- Elasticsearch 클라이언트 분석 및 검색 개념 정리 - Searchive 프로젝트|[Python] Elasticsearch 클라이언트 분석 및 검색 개념 정리 - Searchive 프로젝트]]
- [[blog/AI(ML & DL)/딥러닝- 모델 다루기 (Sequential & Functional + Inception Module 실습)|[딥러닝] 모델 다루기 (Sequential & Functional + Inception Module 실습)]]
