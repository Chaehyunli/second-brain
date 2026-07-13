---
title: "[TypeScript] TypeScript와 유틸리티 타입"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "frontend", "TypeScript"]
category: "TYPESCRIPT"
published: 2025-06-30
source_url: https://ch010104.tistory.com/112
---

# [TypeScript] TypeScript와 유틸리티 타입

## 원문

https://ch010104.tistory.com/112

## 핵심 요약

- **1. Partial<T> - 일부만 사용할 수 있는 타입 만들기** — Partial<T>는 객체 타입 T의 모든 프로퍼티를 선택적(optional) 으로 변환
- **2. Required<T> - 모든 프로퍼티를 필수로 만들기** — Required<T>는 객체 타입 T의 모든 프로퍼티를 필수로 설정
- **3. Readonly<T> - 수정 불가능한 객체 만들기** — Readonly<T>는 객체 타입 T의 모든 프로퍼티를 읽기 전용으로 만들어 줌
- **4. Pick<T, K> - 특정 프로퍼티만 골라서 사용** — Pick<T, K>는 객체 타입 T에서 K에 해당하는 키들만 선택적으로 추출한 타입을 만듬

## 관련 글

- [[blog/TYPESCRIPT/index|TYPESCRIPT]]
- [[blog/TYPESCRIPT/TypeScript- TypeScript와 조건부 타입|[TypeScript] TypeScript와 조건부 타입]]
- [[blog/TYPESCRIPT/TypeScript- TypeScript와 타입 조작|[TypeScript] TypeScript와 타입 조작]]
- [[blog/TYPESCRIPT/TypeScript- TypeScript와 제네릭|[TypeScript] TypeScript와 제네릭]]
