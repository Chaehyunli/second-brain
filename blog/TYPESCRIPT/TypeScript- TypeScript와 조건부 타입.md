---
title: "[TypeScript] TypeScript와 조건부 타입"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "frontend", "TypeScript"]
category: "TYPESCRIPT"
published: 2025-06-30
source_url: https://ch010104.tistory.com/111
---

# [TypeScript] TypeScript와 조건부 타입

## 원문

https://ch010104.tistory.com/111

## 핵심 요약

- **3. 제네릭 조건부 타입** — 제네릭을 사용하면 입력 타입에 따라 결과 타입이 동적으로 바뀌어 재사용성과 안전성이 높아짐
- **4. 조건부 타입 적용 (with 오류 발생)** — as any를 사용하면 오류는 사라지지만, 타입 안전성이 사라짐
- **5. 안전한 방법: 함수 오버로딩 사용** — 오버로딩을 이용하면 타입 추론도 정확하고 타입 안정성도 유지할 수 있음
- **6. 분산 조건부 타입 (Distributive Conditional Types)** — 조건부 타입에 유니언 타입을 넣으면 각 타입별로 개별적으로 조건 평가 후 다시 합침

## 관련 글

- [[blog/TYPESCRIPT/index|TYPESCRIPT]]
- [[blog/TYPESCRIPT/TypeScript- TypeScript와 타입 조작|[TypeScript] TypeScript와 타입 조작]]
- [[blog/TYPESCRIPT/TypeScript- TypeScript와 유틸리티 타입|[TypeScript] TypeScript와 유틸리티 타입]]
- [[blog/TYPESCRIPT/TypeScript- TypeScript와 제네릭|[TypeScript] TypeScript와 제네릭]]
