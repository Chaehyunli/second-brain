---
title: "[Java] 비트마스킹 기본"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing"]
category: "CODINGTEST"
published: 2026-06-21
source_url: https://ch010104.tistory.com/285
---

# [Java] 비트마스킹 기본

## 원문

https://ch010104.tistory.com/285

## 핵심 요약

- **1. 비트마스킹을 왜 쓸까요?** — 압도적인 속도: CPU가 가장 빠르게 처리할 수 있는 비트 단위 연산자(AND, OR, XOR 등)를 사용하므로 수행 시간이 O(1)에 가깝습니다.
- **3. 핵심 비트마스킹 연산 공식 (Cheat Sheet)** — 정수 S를 집합(Set)으로 생각하고, $i$번째 비트가 존재하면 $i$가 집합에 포함되어 있음을 뜻한다고 가정합니다.
- **① 원소 추가 (SET): $i$번째 비트를 1로 만들기** — 이미 있으면 그대로 두고, 없으면 1을 채워 넣습니다.
- **② 원소 삭제 (CLEAR): $i$번째 비트를 0로 만들기** — 이미 0이면 그대로 두고, 1이면 0으로 지웁니다.

## 관련 글

- [[blog/CODINGTEST/index|CODINGTEST]]
- [[blog/CODINGTEST/Java-Python- 타입 확인 및 replace|[Java/Python] 타입 확인 및 replace]]
- [[blog/CODINGTEST/코딩테스트- 현대오토 2026-04-05 회고|[코딩테스트] 현대오토 2026-04-05 회고]]
