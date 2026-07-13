---
title: "[데이터베이스 설계] E-R 모델(관계 표현과 스키마 변환)"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "Database", "Design"]
category: "DATABASE DESIGN"
published: 2025-09-10
source_url: https://ch010104.tistory.com/123
---

# [데이터베이스 설계] E-R 모델(관계 표현과 스키마 변환)

## 원문

https://ch010104.tistory.com/123

## 핵심 요약

- **1. 카디널리티 제약조건의 표현** — － E-R 다이어그램에서 엔티티 간의 관계에 참여하는 엔티티의 수를 표현하는 것을 '카디널리티'라고 함
- **2. 관계 참여도: 전체 참여와 부분 참여** — 전체 참여 (Total Participation):
- **3. 관계의 기본 키(Primary Key) 설정** — - 관계 셋의 기본 키는 관계에 참여하는 엔티티들의 기본 키 조합으로 결정
- **4. 약한 엔티티 셋 (Weak Entity Set)** — - 약한 엔티티 셋은 스스로의 속성만으로는 고유하게 식별될 수 없는 개체

## 관련 글

- [[blog/DATABASE DESIGN/index|DATABASE DESIGN]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 데이터베이스의 정규화(Normalization)란- ( 1 )|[데이터베이스 설계] 데이터베이스의 정규화(Normalization)란? ( 1 )]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- ER 다이어그램이란|[데이터베이스 설계] ER 다이어그램이란?]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 데이터베이스의 정규화(Normalization)란- ( 2 ) - BCNF 와 3NF|[데이터베이스 설계] 데이터베이스의 정규화(Normalization)란? ( 2 ) - BCNF 와 3NF]]
