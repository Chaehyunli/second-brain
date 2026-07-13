---
title: "[모바일 프로그래밍] Listener를 이용한 두 프래그먼트 간의 통신"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "Android", "Kotlin"]
category: "MOBILE PROGRAMING"
published: 2025-11-17
source_url: https://ch010104.tistory.com/189
---

# [모바일 프로그래밍] Listener를 이용한 두 프래그먼트 간의 통신

## 원문

https://ch010104.tistory.com/189

## 핵심 요약

- **실습 목표 및 내용** — 텍스트 전달 앱: Fragment A의 EditText에 텍스트를 입력하고 "OK" 버튼을 누르면 해당 텍스트가 Fragment B의 EditText(혹은 TextView)에 표시됩니다.
- **1. 텍스트 전달 앱: Interface를 이용한 통신** — 이 실습에서는 Interface(인터페이스)를 사용하여 프래그먼트와 액티비티 간의 통신을 구현
- **1. 송신 측 (Fragment A)** — 리스너 인터페이스 정의: 데이터를 보내는 Fragment A 내부에 리스너 인터페이스(예: FragmentAListener)를 정의
- **2. 중재자 (Host Activity)** — 인터페이스 구현: MainActivity는 Fragment A (그리고 Fragment B)에서 정의한 리스너 인터페이스(예: FragmentAListener)를 implements

## 관련 글

- [[blog/MOBILE PROGRAMING/index|MOBILE PROGRAMING]]
- [[blog/MOBILE PROGRAMING/모바일 프로그래밍- 암시적 Intent와 액티비티 생명 주기|[모바일 프로그래밍] 암시적 Intent와 액티비티 생명 주기]]
- [[blog/MOBILE PROGRAMING/모바일 프로그래밍- Activity와 Intent(양방향)|[모바일 프로그래밍] Activity와 Intent(양방향)]]
- [[blog/MOBILE PROGRAMING/모바일 프로그래밍- Activity와 Intent(단방향)|[모바일 프로그래밍] Activity와 Intent(단방향)]]
