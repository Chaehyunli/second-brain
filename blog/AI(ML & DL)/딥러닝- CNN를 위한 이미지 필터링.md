---
title: "[딥러닝] CNN를 위한 이미지 필터링"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "AI", "CNN", "DL"]
category: "AI(ML & DL)"
published: 2025-10-14
source_url: https://ch010104.tistory.com/159
---

# [딥러닝] CNN를 위한 이미지 필터링

## 원문

https://ch010104.tistory.com/159

## 핵심 요약

- **1. 이미지의 본질** — - 디지털 이미지는 강도(intensity) 값들의 격자(grid)로 표현
- **2. 노이즈 감소 문제** — - 정지된 장면을 촬영할 때 카메라 노이즈를 어떻게 줄일 것인가?
- **3. 선형 필터링의 원리** — 즉, 이웃 픽셀에 가중치를 곱하고 모두 합산하는 방식입
- **4. 교차상관과 컨볼루션** — 커널 H를 이미지 F 위에서 슬라이딩하면서 계산

## 관련 글

- [[blog/AI(ML & DL)/index|AI(ML & DL)]]
- [[blog/AI(ML & DL)/딥러닝- CNN|[딥러닝] CNN]]
- [[blog/AI(ML & DL)/딥러닝- CNN의 역사, Dropout과 Batch Normalization|[딥러닝] CNN의 역사, Dropout과 Batch Normalization]]
- [[blog/AI(ML & DL)/딥러닝- 모델 다루기 (Sequential & Functional + Inception Module 실습)|[딥러닝] 모델 다루기 (Sequential & Functional + Inception Module 실습)]]
