---
title: "[데이터베이스 설계] 쿼리 처리(Query Processing) -  비용 측정부터 선택 연산(A1-A3)"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "Database", "Design"]
category: "DATABASE DESIGN"
published: 2025-09-24
source_url: https://ch010104.tistory.com/142
---

# [데이터베이스 설계] 쿼리 처리(Query Processing) -  비용 측정부터 선택 연산(A1-A3)

## 원문

https://ch010104.tistory.com/142

## 핵심 요약

- **쿼리 처리의 3가지 기본 단계** — - 쿼리 처리는 크게 구문 분석 및 변환, 최적화, 그리고 평가의 세 단계로 이루어짐
- **쿼리 비용은 어떻게 측정할까?** — - 쿼리 최적화에서 '비용'은 곧 실행 시간을 의미
- **선택(Selection) 연산 알고리즘과 비용( A1 ~ A6 )** — - 선택(σ) 연산은 특정 조건을 만족하는 튜플을 찾는 가장 기본적인 연산

## 관련 글

- [[blog/DATABASE DESIGN/index|DATABASE DESIGN]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 쿼리 처리(Query Processing) - A4 ~ A10|[데이터베이스 설계] 쿼리 처리(Query Processing) - A4 ~ A10]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 함수 종속성 이론과 스키마 분해|[데이터베이스 설계]  함수 종속성 이론과 스키마 분해]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 데이터베이스의 정규화(Normalization)란- ( 2 ) - BCNF 와 3NF|[데이터베이스 설계] 데이터베이스의 정규화(Normalization)란? ( 2 ) - BCNF 와 3NF]]
