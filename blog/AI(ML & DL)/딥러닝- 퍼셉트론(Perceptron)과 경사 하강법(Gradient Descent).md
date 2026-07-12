---
title: "[딥러닝] 퍼셉트론(Perceptron)과 경사 하강법(Gradient Descent)"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "AI", "DL"]
category: "AI(ML & DL)"
published: 2025-09-18
source_url: https://ch010104.tistory.com/133
---

# [딥러닝] 퍼셉트론(Perceptron)과 경사 하강법(Gradient Descent)

## 원문

https://ch010104.tistory.com/133

## 핵심 요약

- **1. 목표: 점들을 가르는 최적의 직선 찾기** — 위와 같이 파란 점과 빨간 점, 두 그룹의 데이터가 주어졌다고 가정
- **2. 퍼셉트론 알고리즘의 원리** — 퍼셉트론은 아주 간단하고 직관적인 방식으로 학습
- **3. 퍼셉트론의 한계와 경사 하강법** — 단순히 '잘못 분류했는가'에만 의존할 뿐, '얼마나 많이 잘못 분류했는가'의 정도는 고려하지 않는다는 점
- **4. 정리** — 퍼셉트론: 구현이 간단하고 직관적이지만, 오차의 정도를 반영하지 못하는 한계가 있습니다.

## 관련 글

- [[blog/AI(ML & DL)/index|AI(ML & DL)]]
- [[blog/AI(ML & DL)/딥러닝- 인공지능의 동향|[딥러닝] 인공지능의 동향]]
- [[blog/AI(ML & DL)/딥러닝- CNN를 위한 이미지 필터링|[딥러닝] CNN를 위한 이미지 필터링]]
- [[blog/AI(ML & DL)/딥러닝- CNN의 역사, Dropout과 Batch Normalization|[딥러닝] CNN의 역사, Dropout과 Batch Normalization]]
