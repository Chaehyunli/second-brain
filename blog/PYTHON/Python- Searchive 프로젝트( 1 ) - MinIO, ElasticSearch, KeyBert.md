---
title: "[Python] Searchive 프로젝트( 1 ) - MinIO, ElasticSearch, KeyBert"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "ElasticSearch", "fastapi", "KeyBert", "Minio", "PostgreSQL", "Python", "searchive"]
category: "PYTHON"
published: 2025-10-11
source_url: https://ch010104.tistory.com/155
---

# [Python] Searchive 프로젝트( 1 ) - MinIO, ElasticSearch, KeyBert

## 원문

https://ch010104.tistory.com/155

## 핵심 요약

- - 단순히 파일을 저장하는 것을 넘어, 파일의 내용을 이해하고 자동으로 분류하며, 강력한 검색 기능을 제공하는 AI 기반 문서 관리 API 서버입니다.
- **1단계: 관문 - API 엔드포인트와 UploadFile** — 모든 프로세스는 documents/controller.py의 API 엔드포인트에서 시작
- **2단계: 저장 준비 - Path와 uuid로 고유 경로 생성** — - 데이터 무결성을 보장하고 파일명 충돌을 방지하기 위해, 서버에 저장될 고유한 경로와 파일명을 생성
- **3단계: 파일 안치 - MinIO 객체 스토리지에 저장** — - 생성된 고유 경로를 사용하여 실제 파일 데이터를 영구 저장소인 MinIO에 업로드

## 관련 글

- [[blog/PYTHON/index|PYTHON]]
- [[blog/PYTHON/Python- Searchive 프로젝트( 2 ) - KeyBert, ElasticSearch 고도화|[Python] Searchive 프로젝트( 2 ) - KeyBert, ElasticSearch 고도화]]
- [[blog/PYTHON/Python- Elasticsearch 클라이언트 분석 및 검색 개념 정리 - Searchive 프로젝트|[Python] Elasticsearch 클라이언트 분석 및 검색 개념 정리 - Searchive 프로젝트]]
- [[blog/AI(ML & DL)/딥러닝- 모델 다루기 (Sequential & Functional + Inception Module 실습)|[딥러닝] 모델 다루기 (Sequential & Functional + Inception Module 실습)]]
