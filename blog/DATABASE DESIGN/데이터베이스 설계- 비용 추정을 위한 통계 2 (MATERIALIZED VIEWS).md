---
title: "[데이터베이스 설계] 비용 추정을 위한 통계 2 (MATERIALIZED VIEWS)"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "Database", "Design"]
category: "DATABASE DESIGN"
published: 2025-10-29
source_url: https://ch010104.tistory.com/174
---

# [데이터베이스 설계] 비용 추정을 위한 통계 2 (MATERIALIZED VIEWS)

## 원문

https://ch010104.tistory.com/174

## 핵심 요약

- **조인 연산 예시** — 비용 추정 예시를 위한 student 및 takes 테이블의 카탈로그 정보:
- **조인 크기 추정** — Cartesian Product (r x s): n_r * n_s 개의 튜플을 포함
- **기타 연산 크기 추정** — Projection \prod_A(r): 추정 크기 = V(A, r) (A의 고유값 수)
- **📈 실행 계획 선택** — 실행 계획(Evaluation Plan): 각 연산에 사용할 알고리즘과 연산 실행 순서를 정의

## 관련 글

- [[blog/DATABASE DESIGN/index|DATABASE DESIGN]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 비용 추정을 위한 통계 1 (STATISTICS FOR COST ESTIMATION)|[데이터베이스 설계] 비용 추정을 위한 통계 1 (STATISTICS FOR COST ESTIMATION)]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 트랜젝션과 Serializability|[데이터베이스 설계] 트랜젝션과 Serializability]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 쿼리 최적화 (Query Optimization)|[데이터베이스 설계] 쿼리 최적화 (Query Optimization)]]
