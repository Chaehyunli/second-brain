---
title: "[모바일 프로그래밍] Activity와 Intent(단방향)"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "Android", "Kotlin"]
category: "MOBILE PROGRAMING"
published: 2025-10-23
source_url: https://ch010104.tistory.com/169
---

# [모바일 프로그래밍] Activity와 Intent(단방향)

## 원문

https://ch010104.tistory.com/169

## 핵심 요약

- **1. 안드로이드 앱의 주요 구성 요소: 액티비티 (Activity)** — 액티비티는 안드로이드 앱에서 사용자가 상호작용하는 하나의 UI(사용자 인터페이스) 화면을 의미
- **2. 안드로이드 앱의 주요 구성 요소: 인텐트 (Intent)** — - 인텐트는 한 액티비티에서 다른 액티비티를 호출할 때 필요한 핵심 요소
- **3. 인텐트의 종류: 명시적 인텐트와 암시적 인텐트** — - 인텐트는 컴포넌트 간에 데이터를 주고받기 위한 메시지 객체입니다.
- **4. 명시적 인텐트를 이용한 데이터 전달 (단방향)** — - 명시적 인텐트는 SecondActivity::class.java와 같이 대상 액티비티의 클래스 참조 정보를 사용하여 인텐트 객체를 생성

## 관련 글

- [[blog/MOBILE PROGRAMING/index|MOBILE PROGRAMING]]
- [[blog/MOBILE PROGRAMING/모바일 프로그래밍- Activity와 Intent(양방향)|[모바일 프로그래밍] Activity와 Intent(양방향)]]
- [[blog/MOBILE PROGRAMING/모바일 프로그래밍- 토스트(Toast)와 대화 상자(AlertDialog)|[모바일 프로그래밍] 토스트(Toast)와 대화 상자(AlertDialog)]]
- [[blog/MOBILE PROGRAMING/모바일 프로그래밍- 암시적 Intent와 액티비티 생명 주기|[모바일 프로그래밍] 암시적 Intent와 액티비티 생명 주기]]
