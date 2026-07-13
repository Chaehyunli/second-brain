---
title: "[기계학습] Python NumPy 란 ?? ( 3 )"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "AI", "CS"]
category: "AI(ML & DL)"
published: 2025-03-28
source_url: https://ch010104.tistory.com/32
---

# [기계학습] Python NumPy 란 ?? ( 3 )

## 원문

https://ch010104.tistory.com/32

## 핵심 요약

- **1️⃣ Iterating( ndarray 반복 )** — for m in c: 의 경우, 배열 c에 대해서 가장 바깥쪽 차원(3차원일 경우 z, 2차원일 경우 y)을 기준으로 m[0], ...
- **2️⃣ 배열 쌓기 (Stacking Arrays)** — vstack은 매개변수로 들어온 배열 q1, q2, q3 를 y축 새로 방향으로 합침.(2차원 배열에 대해서만 가능)
- **3️⃣ 배열 분할( Splitting arrays )** — vsplit과 hsplit은 vstack과 hstack과 반대로 하나의 배열을 쪼개는 것
- **4️⃣ 전치 ( Transposing arrays )** — 3차원 배열 (z, y, x) 의 경우 axis 0 = z, axis 1 = y, axis 2 = x 임.

## 관련 글

- [[blog/AI(ML & DL)/index|AI(ML & DL)]]
- [[blog/AI(ML & DL)/기계학습- Python NumPy란-- ( 2 )|[기계학습] Python NumPy란?? ( 2 )]]
- [[blog/AI(ML & DL)/기계학습- Python Pandas 란 -- ( 2 )|[기계학습] Python Pandas 란 ?? ( 2 )]]
- [[blog/AI(ML & DL)/기계학습- Python NumPy란-- ( 1 )|[기계학습] Python NumPy란?? ( 1 )]]
