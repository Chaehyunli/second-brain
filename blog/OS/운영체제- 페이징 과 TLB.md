---
title: "[운영체제] 페이징 과 TLB"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing"]
category: "OS"
published: 2025-05-14
source_url: https://ch010104.tistory.com/72
---

# [운영체제] 페이징 과 TLB

## 원문

https://ch010104.tistory.com/72

## 핵심 요약

- **1. 페이징의 기본 구조** — 운영체제는 **각 프로세스마다 페이지 테이블(Page Table)**을 하나씩 가짐 - 즉, 페이지 테이블은 주기억장치에 위치 ( OS 주소 공간 내)
- **2. 메모리 접근 시간과 성능 문제** — 프로세스가 메모리 내 데이터를 읽기 위해서는 다음과 같은 두 번의 접근이 필요
- **3. 성능 향상을 위한 해결책: TLB** — 이 문제를 해결하기 위해 등장한 것이 바로 **TLB (Translation Lookaside Buffer)**
- **4. TLB 성능 연습문제 예시** — TLB 접근 시간 = 10ns,메인 메모리 접근 시간 = 20ns

## 관련 글

- [[blog/OS/index|OS]]
- [[blog/OS/운영체제- 페이지 테이블 구조 란|[운영체제] 페이지 테이블 구조 란??]]
- [[blog/OS/운영체제- 기억장치의 관리란|[운영체제] 기억장치의 관리란??]]
- [[blog/OS/운영체제- 교착상태 란|[운영체제] 교착상태 란??]]
