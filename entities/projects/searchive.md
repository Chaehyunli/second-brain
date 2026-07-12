---
title: Searchive
created: 2026-07-10
updated: 2026-07-10
type: entity
tags:
  [
    project,
    backend,
    python,
    fastapi,
    search,
    rag,
    ai,
    database,
    infrastructure,
    performance,
  ]
sources: [raw/sources/employment-zip-2026-07-10.md]
confidence: high
---

# Searchive — AI document knowledge platform

## Overview

2025-10~2025-12에 1인으로 기획·개발한 개인 문서 관리 플랫폼. 업로드 문서의 AI 분석·자동 태깅, 하이브리드 검색, 요약, RAG 기반 문서 대화를 목표로 했다.

## Architecture and role

- Frontend: React, TypeScript, Vite, Zustand, axios.
- Backend: FastAPI를 인증·문서·태그·AI 도메인으로 분리.
- Infra/data: PostgreSQL + pgvector, MinIO, Elasticsearch, Redis, Ollama를 Docker Compose로 통합.
- 문제 정의와 ERD/API 설계부터 구현까지 전 과정을 담당했다.

## Problem → decision → result

1. 새 키워드 `M`개와 기존 태그 `N`개를 전수 비교하던 O(N×M) 중복 판별 병목을 발견했다.
2. 태그 임베딩과 pgvector 유사도 검색을 도입해 의미적으로 가까운 기존 태그를 재사용하도록 정규화했다.
3. 다중 키워드가 순차 요청을 발생시키는 후속 병목을 확인하고 Elasticsearch `_msearch`로 배치 처리했다.
4. 키워드 추출 직후와 저장 직전의 이중 필터(한·영 불용어, 길이·숫자·다중 단어 조건)를 구현했다.
5. 키워드 5개 처리 예시에서 네트워크 왕복을 5회→1회, 검색 지연을 약 250ms→10ms로 줄였다.

## Portfolio evidence

이 프로젝트는 [[concepts/backend-portfolio-narrative]]의 대표 성능 개선 사례다. [[entities/lim-chae-hyun]]의 검색·RAG·성능 설계 역량을 가장 직접적으로 보여준다.
