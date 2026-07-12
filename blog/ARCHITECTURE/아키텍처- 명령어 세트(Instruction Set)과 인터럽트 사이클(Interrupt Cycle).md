---
title: "[아키텍처] 명령어 세트(Instruction Set)과 인터럽트 사이클(Interrupt Cycle)"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "architecture", "CS"]
category: "ARCHITECTURE"
published: 2025-04-09
source_url: https://ch010104.tistory.com/50
---

# [아키텍처] 명령어 세트(Instruction Set)과 인터럽트 사이클(Interrupt Cycle)

## 원문

https://ch010104.tistory.com/50

## 핵심 요약

- **1. 인터럽트 사이클 (Interrupt Cycle)** — **인터럽트(interrupt)**는 프로그램 실행 중에 CPU가 현재 명령어의 흐름을 중단하고, 외부 장치나 내부 요청에 의해 다른 작업을 처리하도록 하는 메커니즘
- **2. 간접 사이클 (Indirect Cycle)** — 간접 주소지정 방식이 사용된 명령어의 경우, 명령어에 포함된 주소가 직접 데이터의 주소가 아님
- **3. 명령어 파이프라이닝 (Instruction Pipelining)** — CPU의 처리 속도를 높이기 위한 대표적인 기술

## 관련 글

- [[blog/ARCHITECTURE/index|ARCHITECTURE]]
- [[blog/ARCHITECTURE/아키텍처- 제어 유니트(Control Unit) 란|[아키텍처] 제어 유니트(Control Unit) 란?]]
- [[blog/ARCHITECTURE/아키텍처- 명령어 형식과 주소지정 방식|[아키텍처] 명령어 형식과 주소지정 방식]]
- [[blog/ARCHITECTURE/아키텍처- 반도체 기억장치와 설계|[아키텍처] 반도체 기억장치와 설계]]
