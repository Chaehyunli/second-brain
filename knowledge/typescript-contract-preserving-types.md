---
schema_version: 1
id: knowledge-typescript-contract-preserving-types
title: TypeScript 계약 보존형 타입 설계
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-08
checked_at: 2026-08-08
tags: [knowledge, initial-curation]
sources:
  - blog/TYPESCRIPT/TypeScript- TypeScript와 타입 조작.md
  - blog/TYPESCRIPT/TypeScript- TypeScript와 조건부 타입.md
---

# TypeScript 계약 보존형 타입 설계

## 지키려는 계약
입력 객체의 키·값 관계를 잃지 않고 API 출력 타입을 변환하거나 제한하는 것이 목표다.

## 정보 보존 도구
`keyof`, indexed access, generic은 객체·배열의 타입 정보를 참조한다. mapped type과 conditional type은 입력 조건에 따라 출력 계약을 계산하고, `infer`는 그 내부 일부를 추출한다.

## 선택의 갈림길
반환 타입이 입력에 따라 달라질 때 conditional type과 overload를 비교한다. `any` 캐스팅은 빠르지만 호출자와 구현 사이의 계약을 지우므로 마지막 수단으로 둔다.

## 안전한 사용의 기준
public API 경계에서 필요한 수준만 노출하고, 실제 호출 예시로 추론 결과를 확인한다. 요청·응답 payload의 계약이라는 점에서 [[knowledge/request-response-and-server-events]]와 보완 관계지만, 동일한 TypeScript 구현 사례를 이 출처가 직접 보여 주지는 않는다.

## 복잡도 경계
복잡한 타입은 가독성과 컴파일 시간 비용을 낳을 수 있다. 타입 체조 자체를 목적화하지 않는다.

## 근거
- [[blog/TYPESCRIPT/TypeScript- TypeScript와 타입 조작]]
- [[blog/TYPESCRIPT/TypeScript- TypeScript와 조건부 타입]]
