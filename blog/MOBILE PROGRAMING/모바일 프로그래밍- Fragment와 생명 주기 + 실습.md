---
title: "[모바일 프로그래밍] Fragment와 생명 주기 + 실습"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing"]
category: "MOBILE PROGRAMING"
published: 2025-11-05
source_url: https://ch010104.tistory.com/180
---

# [모바일 프로그래밍] Fragment와 생명 주기 + 실습

## 원문

https://ch010104.tistory.com/180

## 핵심 요약

- **디자인 철학 및 특징 (Design Philosophy & Characteristics)** — 도입 배경: Android 3.0 (API level 11)에서 태블릿과 같은 큰 화면에서 동적이고 유연한 UI 디자인을 지원하기 위해 도입
- **프래그먼트 라이프사이클 (Fragment Lifecycle)** — 유사성: 프래그먼트 라이프사이클은 액티비티의 라이프사이클과 유사함
- **프래그먼트 구현 (Fragment Implementation)** — Fragment 클래스를 상속함 (Extend Fragment class)
- **액티비티에 프래그먼트 추가 (Adding Fragment to Activity)** — 정적 추가 (Statically): 액티비티의 레이아웃 내부에 <android.fragment.FragmentContainerView> 태그를 사용하여 추가

## 관련 글

- [[blog/MOBILE PROGRAMING/index|MOBILE PROGRAMING]]
- [[blog/MOBILE PROGRAMING/모바일 프로그래밍- 암시적 Intent와 액티비티 생명 주기|[모바일 프로그래밍] 암시적 Intent와 액티비티 생명 주기]]
- [[blog/MOBILE PROGRAMING/모바일 프로그래밍- 프래그먼트 간 통신 실습|[모바일 프로그래밍] 프래그먼트 간 통신 실습]]
- [[blog/MOBILE PROGRAMING/모바일 프로그래밍- Activity와 Intent(양방향)|[모바일 프로그래밍] Activity와 Intent(양방향)]]
