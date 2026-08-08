---
schema_version: 1
id: knowledge-query-planning-index-and-pagination
title: 쿼리 계획·인덱스·대용량 페이지네이션
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-06
checked_at: 2026-08-06
tags: [knowledge, initial-curation, database, sql, postgresql]
sources:
  - blog/SQL/SQL- MySql의 인덱스 설정 - BTREE INDEX.md
  - blog/DATABASE DESIGN/데이터베이스 설계- 쿼리 최적화 (Query Optimization).md
  - notion/SKALA/7-29 스마트 데이터 이해 및 활용_Day3/7-29 스마트 데이터 이해 및 활용_Day3 핵심 정리.md
---

# 쿼리 계획·인덱스·대용량 페이지네이션

## 핵심
데이터 접근 성능은 인덱스를 붙이는 행위가 아니라, 정렬·필터·조인·페이지네이션에 맞는 접근 경로와 실행 계획을 고르는 문제다.

## 연결된 근거
- [[blog/SQL/SQL- MySql의 인덱스 설정 - BTREE INDEX.md]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 쿼리 최적화 (Query Optimization).md]]
- [[notion/SKALA/7-29 스마트 데이터 이해 및 활용_Day3/7-29 스마트 데이터 이해 및 활용_Day3 핵심 정리.md]]

## 적용 기준
BTREE 인덱스의 읽기 이점과 쓰기 비용, 비용 기반 최적화, 깊은 OFFSET을 피하는 안정 정렬·커서 접근을 함께 검토한다.

## 주의점 또는 한계
DBMS별 실행 계획과 복합 인덱스 규칙은 다르므로 특정 비용 수치나 인덱스 형태를 일반화하지 않는다.
