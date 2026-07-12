---
title: "[딥러닝] CNN"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "CNN", "DL"]
category: "AI(ML & DL)"
published: 2025-10-16
source_url: https://ch010104.tistory.com/162
---

# [딥러닝] CNN

## 원문

https://ch010104.tistory.com/162

## 핵심 요약

- **CNN (Convolutional Neural Network) 개요** — 필터 (Filter)의 역할: 이미지에서 찾고 싶은 특정 모양(특징)을 감지함.
- **Convolution 연산의 구성 요소** — Stride: 필터를 이미지 위에서 이동시키는 간격.
- **Convolution Layer와 Dense Layer 비교** — 3차원의 이미지 데이터를 1차원으로 펼쳐서 처리해야 함 (예: 32x32x3 -> 3072x1).
- **CNN 프로그래밍 (Keras API)** — Conv2D: 2D Convolution 레이어를 생성.

## 관련 글

- [[blog/AI(ML & DL)/index|AI(ML & DL)]]
- [[blog/AI(ML & DL)/딥러닝- CNN를 위한 이미지 필터링|[딥러닝] CNN를 위한 이미지 필터링]]
- [[blog/AI(ML & DL)/딥러닝- CNN의 역사, Dropout과 Batch Normalization|[딥러닝] CNN의 역사, Dropout과 Batch Normalization]]
- [[blog/AI(ML & DL)/딥러닝- 모델 다루기 (Sequential & Functional + Inception Module 실습)|[딥러닝] 모델 다루기 (Sequential & Functional + Inception Module 실습)]]
