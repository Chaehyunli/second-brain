---
schema_version: 1
id: knowledge-performance-investigation-and-measurement-boundaries
title: 성능 조사와 측정 근거 경계
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-08
checked_at: 2026-08-08
tags: [knowledge, initial-curation]
sources:
  - entities/projects/searchive.md
  - raw/sources/searchive-code-update-2026-07-13.md
  - knowledge/query-planning-index-and-pagination.md
---

# 성능 조사와 측정 근거 경계

## 조사 질문
느려진 이유가 계산량, DB 접근, 네트워크 왕복, 초기화 중 어디에 있는지 분리해 확인한다.

## 병목 가설과 변경 경로
Searchive는 새 키워드 M개와 기존 태그 N개의 전수 비교를 pgvector 유사도 검색으로 옮기고, 남은 순차 요청을 Elasticsearch `_msearch` 배치로 줄였다. 계산 복잡도와 통신 방식이 서로 다른 병목이라는 해석이다.

## 관측 결과
기록된 키워드 5개 예시에서 왕복은 5회→1회, 검색 지연은 약 250ms→10ms이고 배치 쿼리 시간은 90% 이상 단축됐다. 최근 코드 변경에는 lazy initialization lock과 KeyBERT 후보 조합 제거가 포함되지만 end-to-end 재현 시험은 이 Wiki 반영에서 수행되지 않았다.

## 결과를 읽는 범위
이 수치는 기록된 입력·조건의 관측값이다. 데이터 규모·동시성·하드웨어가 다른 전체 시스템 성능으로 확대하지 않는다.

## 다음 조사와의 관계
[[knowledge/query-planning-index-and-pagination]]은 실행 계획·인덱스·페이지네이션의 일반 진단 원칙을 다룬다. 이 노트는 특정 사례의 가설·개입·측정 경계를 유지한다.

## 근거
- [[entities/projects/searchive]]
- [[raw/sources/searchive-code-update-2026-07-13]]
- [[knowledge/query-planning-index-and-pagination]]
