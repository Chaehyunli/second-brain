---
title: "[아키텍처] 제어 유니트(Control Unit) 란?"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "architecture", "CS"]
category: "ARCHITECTURE"
published: 2025-04-09
source_url: https://ch010104.tistory.com/52
---

# [아키텍처] 제어 유니트(Control Unit) 란?

## 원문

https://ch010104.tistory.com/52

## 핵심 요약

- **1. 제어 유니트의 기능** — CPU 내에서 **명령어 사이클(인출 → 간접 → 실행 → 인터럽트)**이 순차적으로 수행되도록 제어 신호를 발생시킴.
- **2. 제어 유니트의 구조** — 제어 기억장치는 ROM 형태이며, 마이크로명령어의 루틴들을 저장.
- **3. 마이크로명령어 형식** — 수직적 마이크로프로그래밍: 연산 필드 값은 코딩되어 있고, 디코더를 통해 제어 신호 확장 (용량 ↓, 속도 ↓)
- **4 마이크로프로그래밍** — 1) 인출 사이클 루틴 (Fetch Cycle Routine)

## 관련 글

- [[blog/ARCHITECTURE/index|ARCHITECTURE]]
- [[blog/ARCHITECTURE/아키텍처- 명령어 세트(Instruction Set)과 인터럽트 사이클(Interrupt Cycle)|[아키텍처] 명령어 세트(Instruction Set)과 인터럽트 사이클(Interrupt Cycle)]]
- [[blog/ARCHITECTURE/아키텍처- 반도체 기억장치와 설계|[아키텍처] 반도체 기억장치와 설계]]
- [[blog/ARCHITECTURE/아키텍처- 명령어 형식과 주소지정 방식|[아키텍처] 명령어 형식과 주소지정 방식]]
