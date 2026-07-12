---
title: "[기계학습] Python NumPy란?? ( 2 )"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "AI", "CS"]
category: "AI(ML & DL)"
published: 2025-03-24
source_url: https://ch010104.tistory.com/24
---

# [기계학습] Python NumPy란?? ( 2 )

## 원문

https://ch010104.tistory.com/24

## 핵심 요약

- **1️⃣ dtype과 itemsize** — NumPy의 배열(ndarray)은 **모든 원소가 같은 타입(dtype)**을 가져야 효율적으로 동작!!
- **2️⃣ 배열의 메모리 구조 .data** — f는 2차원 배열이지만 실제로는 1차원으로 평탄화된 형태의 바이트 버퍼에 저장됨
- **3️⃣ .shape vs .reshape()** — g.shape으로 해당 배열의 어떠한 모양의 배열인지 알 수 있음.
- **5️⃣ 산술 연산** — 산술 연산은 두 배열 간의 모양이 같을 경우에만 가능함!!

## 관련 글

- [[blog/AI(ML & DL)/index|AI(ML & DL)]]
- [[blog/AI(ML & DL)/기계학습- Python NumPy란-- ( 1 )|[기계학습] Python NumPy란?? ( 1 )]]
- [[blog/AI(ML & DL)/기계학습- ML(Machine Learning)의 주요 과제(데이터, 알고리즘 문제)|[기계학습] ML(Machine Learning)의 주요 과제(데이터, 알고리즘 문제)]]
- [[blog/AI(ML & DL)/기계학습- Python NumPy 란 -- ( 3 )|[기계학습] Python NumPy 란 ?? ( 3 )]]
