---
title: "[React] CLERK을 이용한 토큰 로그인"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "react", "TypeScript"]
category: "REACT"
published: 2026-03-31
source_url: https://ch010104.tistory.com/246
---

# [React] CLERK을 이용한 토큰 로그인

## 원문

https://ch010104.tistory.com/246

## 핵심 요약

- **📂 1. 프로젝트 폴더 구조** — 프로젝트는 관심사 분리(Separation of Concerns) 원칙에 따라 다음과 같이 구성되어 있습니다.
- **Step 1: 앱 시작 및 전역 설정 (app/_layout.tsx)** — ClerkProvider가 앱 전체를 감싸며, 이 순간부터 모든 화면에서 Clerk 훅을 사용할 수 있습니다.
- **Step 2: 인증 가드 (app/(tabs)/_layout.tsx)** — 로그인이 필요한 경로에 접근할 때마다 로그인 여부를 확인하여 미인증 사용자를 차단합니다.
- **Step 3: 구글 OAuth 로그인 (app/(auth)/sign-in.tsx)** — useOAuth 훅을 사용하여 구글 인증 과정을 수행하고 세션을 활성화합니다.

## 관련 글

- [[blog/REACT/index|REACT]]
- [[blog/REACT/React- param, outlet 문법|[React] param, outlet 문법]]
- [[blog/REACT/React- state 문법이란-, useEffect 문법이란|[React] state 문법이란?, useEffect 문법이란?]]
- [[blog/TYPESCRIPT/TypeScript- TypeScript와 유틸리티 타입|[TypeScript] TypeScript와 유틸리티 타입]]
