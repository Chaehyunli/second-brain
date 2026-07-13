---
title: "[데이터베이스 설계] 쿼리 처리(Query Processing) - A4 ~ A10"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "Database", "Design"]
category: "DATABASE DESIGN"
published: 2025-09-29
source_url: https://ch010104.tistory.com/147
---

# [데이터베이스 설계] 쿼리 처리(Query Processing) - A4 ~ A10

## 원문

https://ch010104.tistory.com/147

## 핵심 요약

- **1. Secondary Index를 이용한 동등(Equality) 조건 선택 (A4)** — - Secondary Index는 Primary Index와 달리 데이터가 물리적으로 정렬되어 있지 않은 경우에 사용
- **2. 인덱스를 이용한 비교(Comparison) 조건 선택 (A5, A6)** — - > 또는 <와 같은 비교 연산자를 사용하는 선택 연산은 데이터의 정렬 여부에 따라 효율이 크게 달라짐
- **3. 복합(Complex) 조건 선택 처리** — - 여러 조건이 AND나 OR로 결합된 복합 선택 연산은 다음과 같은 전략을 사용

## 관련 글

- [[blog/DATABASE DESIGN/index|DATABASE DESIGN]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 쿼리 처리(Query Processing) - 비용 측정부터 선택 연산(A1-A3)|[데이터베이스 설계] 쿼리 처리(Query Processing) -  비용 측정부터 선택 연산(A1-A3)]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 쿼리 처리(Query Processiong) - 정렬(Sorting)과 조인(Join)|[데이터베이스 설계] 쿼리 처리(Query Processiong) - 정렬(Sorting)과 조인(Join)]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 함수 종속성 이론과 스키마 분해|[데이터베이스 설계]  함수 종속성 이론과 스키마 분해]]
