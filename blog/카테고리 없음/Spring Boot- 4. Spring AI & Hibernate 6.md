---
title: "[Spring Boot] 4. Spring AI & Hibernate 6"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing"]
category: "카테고리 없음"
published: 2026-03-03
source_url: https://ch010104.tistory.com/198
---

# [Spring Boot] 4. Spring AI & Hibernate 6

## 원문

https://ch010104.tistory.com/198

## 핵심 요약

- **1. Spring AI: AI 서버(Python)와의 통격 및 객체 변환** — Spring AI는 파이썬 에이전트가 보내주는 복잡한 JSON 데이터를 자바의 **Type-safe한 객체(Record)**로 자동 변환하는 역할을 합니다.
- **2. Hibernate 6: 자바 객체를 PostgreSQL JSONB에 저장** — Hibernate 6는 위에서 Spring AI가 만들어준 자바 객체를 별도의 변환 과정 없이 PostgreSQL의 JSONB 컬럼에 그대로 저장합니다.

## 관련 글

- [[blog/카테고리 없음/index|카테고리 없음]]
- [[blog/카테고리 없음/네트워크- 네트워크 계층(Network Layer) 의 구조|[네트워크] 네트워크 계층(Network Layer) 의 구조]]
- [[blog/카테고리 없음/Spring Boot- 11. Spring Weflux에서의 Transaction 관리|[Spring Boot] 11. Spring Weflux에서의 Transaction 관리]]
- [[blog/카테고리 없음/React - Spring Boot- 프론트엔드, 백엔드 프로젝트 구조|[React / Spring Boot] 프론트엔드, 백엔드 프로젝트 구조]]
