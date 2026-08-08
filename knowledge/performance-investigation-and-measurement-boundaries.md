---
schema_version: 1
id: knowledge-performance-investigation-and-measurement-boundaries
title: 성능 조사와 측정 근거 경계
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-06
checked_at: 2026-08-06
tags: [knowledge, initial-curation]
sources:
  - entities/projects/searchive.md
  - raw/sources/searchive-code-update-2026-07-13.md
  - knowledge/query-planning-index-and-pagination.md
---

# 성능 조사와 측정 근거 경계

## 핵심
성능 개선은 알고리즘·쿼리·네트워크 왕복을 분리해 병목을 찾고, 수치는 데이터·환경·반복 조건과 함께 기록해야 한다.

## 연결된 근거
- [[entities/projects/searchive.md]]
- [[raw/sources/searchive-code-update-2026-07-13.md]]
- [[knowledge/query-planning-index-and-pagination.md]]

## 적용 기준
Searchive의 O(N×M) 비교·pgvector·`_msearch` 배치와 제한된 5-keyword 측정, 실행 계획 원칙을 연결한다.

## 주의점 또는 한계
250ms→10ms와 5→1 왕복은 기록된 조건의 관측값이며 시스템 전체의 일반 성능 주장으로 확대하지 않는다.
