---
title: "[데이터베이스 설계] 데이터베이스의 정규화(Normalization)란? ( 2 ) - BCNF 와 3NF"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "Database", "Design"]
category: "DATABASE DESIGN"
published: 2025-09-17
source_url: https://ch010104.tistory.com/131
---

# [데이터베이스 설계] 데이터베이스의 정규화(Normalization)란? ( 2 ) - BCNF 와 3NF

## 원문

https://ch010104.tistory.com/131

## 핵심 요약

- 데이터베이스를 설계할 때 가장 중요한 목표 중 하나는 '불필요한 데이터 중복을 최소화'하는 것
- **1. 정규화의 초석: 함수 종속성(Functional Dependency) 파헤치기** — - 정규화를 이해하기 위해서는 먼저 함수 종속성(Functional Dependency, FD)의 개념을 확실히 알아야 함
- **2. 좋은 분해(Decomposition)의 조건** — 정규화는 중복을 줄이기 위해 테이블을 분해하는 과정
- **3. 정규형(Normal Forms): BCNF와 3NF** — 1) BCNF (Boyce-Codd Normal Form)

## 관련 글

- [[blog/DATABASE DESIGN/index|DATABASE DESIGN]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 데이터베이스의 정규화(Normalization)란- ( 1 )|[데이터베이스 설계] 데이터베이스의 정규화(Normalization)란? ( 1 )]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 함수 종속성 이론과 스키마 분해|[데이터베이스 설계]  함수 종속성 이론과 스키마 분해]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- E-R 모델(관계 표현과 스키마 변환)|[데이터베이스 설계] E-R 모델(관계 표현과 스키마 변환)]]
