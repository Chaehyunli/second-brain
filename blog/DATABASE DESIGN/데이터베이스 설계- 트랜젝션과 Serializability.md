---
title: "[데이터베이스 설계] 트랜젝션과 Serializability"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "Database", "Design"]
category: "DATABASE DESIGN"
published: 2025-11-05
source_url: https://ch010104.tistory.com/181
---

# [데이터베이스 설계] 트랜젝션과 Serializability

## 원문

https://ch010104.tistory.com/181

## 핵심 요약

- **1. Serializability (직렬 가능성)** — 기본 가정: 각 트랜잭션은 데이터베이스의 일관성(consistency)을 보존함
- **2. Conflicting Instructions (충돌 명령어)** — 트랜잭션 T_i의 명령어 I_i와 T_j의 명령어 I_j가 충돌하는 경우는 다음과 같음:
- **3. Conflict Serializability (충돌 직렬 가능성)** — 충돌 동등(Conflict Equivalent): 스케줄 S가 충돌하지 않는 명령어들의 일련의 교환(swaps)을 통해 스케줄 S'로 변환될 수 있을 때
- **4. View Serializability (뷰 직렬 가능성)** — 뷰 동등(View Equivalent): 두 스케줄 S와 S'가 다음 세 가지 조건을 만족할 때:

## 관련 글

- [[blog/DATABASE DESIGN/index|DATABASE DESIGN]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 비용 추정을 위한 통계 2 (MATERIALIZED VIEWS)|[데이터베이스 설계] 비용 추정을 위한 통계 2 (MATERIALIZED VIEWS)]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 비용 추정을 위한 통계 1 (STATISTICS FOR COST ESTIMATION)|[데이터베이스 설계] 비용 추정을 위한 통계 1 (STATISTICS FOR COST ESTIMATION)]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 쿼리 최적화 (Query Optimization)|[데이터베이스 설계] 쿼리 최적화 (Query Optimization)]]
