---
title: "[TypeScript] TypeScript와 타입 조작"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "frontend", "TypeScript"]
category: "TYPESCRIPT"
published: 2025-06-30
source_url: https://ch010104.tistory.com/110
---

# [TypeScript] TypeScript와 타입 조작

## 원문

https://ch010104.tistory.com/110

## 핵심 요약

- **1. 인덱스드 엑세스 타입 (Indexed Access Types)** — 기존 객체, 배열, 튜플에서 특정 타입을 추출할 수 있음
- **2. keyof 연산자** — 객체 타입의 프로퍼티 key들을 유니온 타입으로 추출
- **3. 맵드 타입 (Mapped Types)** — 객체의 모든 프로퍼티를 반복하여 새로운 타입을 만들 수 있음
- **4. 템플릿 리터럴 타입 (Template Literal Types)** — 템플릿 문자열을 사용해 문자열 패턴 기반 타입을 생성

## 관련 글

- [[blog/TYPESCRIPT/index|TYPESCRIPT]]
- [[blog/TYPESCRIPT/TypeScript- TypeScript와 제네릭|[TypeScript] TypeScript와 제네릭]]
- [[blog/TYPESCRIPT/TypeScript- TypeScript와 조건부 타입|[TypeScript] TypeScript와 조건부 타입]]
- [[blog/TYPESCRIPT/TypeScript- TypeScript와 유틸리티 타입|[TypeScript] TypeScript와 유틸리티 타입]]
