---
schema_version: 1
id: knowledge-typescript-contract-preserving-types
title: TypeScript 계약 보존형 타입 설계
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-06
checked_at: 2026-08-06
tags: [knowledge, initial-curation]
sources:
  - blog/TYPESCRIPT/TypeScript- TypeScript와 타입 조작.md
  - blog/TYPESCRIPT/TypeScript- TypeScript와 조건부 타입.md
---

# TypeScript 계약 보존형 타입 설계

## 핵심
`keyof`, indexed access, conditional type, generic은 입력 객체의 정보를 잃지 않고 API 출력 계약을 변환하는 도구다.

## 연결된 근거
- [[blog/TYPESCRIPT/TypeScript- TypeScript와 타입 조작.md]]
- [[blog/TYPESCRIPT/TypeScript- TypeScript와 조건부 타입.md]]

## 적용 기준
객체/배열 타입 접근과 조건부 반환 타입·overload를 연결해 `any` 캐스팅 대신 타입 수준 계약을 유지하는 방향을 정리한다.

## 주의점 또는 한계
복잡한 타입은 가독성과 컴파일 시간 비용을 낳을 수 있으므로 public API 경계에서 필요한 수준만 사용한다.
