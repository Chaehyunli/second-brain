---
title: "[데이터베이스 설계] 데이터베이스의 정규화(Normalization)란? ( 1 )"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "Database", "Design"]
category: "DATABASE DESIGN"
published: 2025-09-15
source_url: https://ch010104.tistory.com/126
---

# [데이터베이스 설계] 데이터베이스의 정규화(Normalization)란? ( 1 )

## 원문

https://ch010104.tistory.com/126

## 핵심 요약

- **1. 기본 개념 (Basic Concepts)** — 목표: 불필요한 중복(redundancy) 없이 필요한 정보를 모두 표현(저장)할 수 있는 Schema
- **2. 스키마 결합의 문제점** — 예시: instructor와 department 결합
- **3. 분해(Decomposition)와 함수 종속성** — 부서별 정보가 중복되어 저장되므로 다음과 같은 문제 발생:
- **4. 잘못된 분해의 예** — employee(ID, name, street, city, salary)를 다음과 같이 분해:

## 관련 글

- [[blog/DATABASE DESIGN/index|DATABASE DESIGN]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- E-R 모델(관계 표현과 스키마 변환)|[데이터베이스 설계] E-R 모델(관계 표현과 스키마 변환)]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 데이터베이스의 정규화(Normalization)란- ( 2 ) - BCNF 와 3NF|[데이터베이스 설계] 데이터베이스의 정규화(Normalization)란? ( 2 ) - BCNF 와 3NF]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- ER 다이어그램이란|[데이터베이스 설계] ER 다이어그램이란?]]
