---
title: "[딥러닝] 텐서플로우의 GradientTape (자동 미분)"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "AI", "DL"]
category: "CLAUD COMPUTERING"
published: 2025-10-30
source_url: https://ch010104.tistory.com/175
---

# [딥러닝] 텐서플로우의 GradientTape (자동 미분)

## 원문

https://ch010104.tistory.com/175

## 핵심 요약

- - 텐서플로우의 GradientTape는 연산 과정을 '테이프'에 녹화(기록)하여 자동 미분을 수행하는 기능
- **2. 모델 학습 예제** — 하나의 Loss 함수를 모델의 모든 학습 가능한 파라미터(가중치 $w$, 편향 $b$)로 미분하여 Gradient를 계산하는 예제
- **AutoGrad의 응용: Heatmap 활성화** — - AutoGrad 개념은 모델 학습뿐만 아니라, 모델의 판단 근거를 시각화(Heatmap)하는 데에도 응용

## 관련 글

- [[blog/CLAUD COMPUTERING/index|CLAUD COMPUTERING]]
- [[blog/CLAUD COMPUTERING/클라우드 컴퓨터링- 머신러닝, 딥러닝과 빅데이터|[클라우드 컴퓨터링] 머신러닝, 딥러닝과 빅데이터]]
- [[blog/AI(ML & DL)/딥러닝- 검증된 AI 모델 활용(Keras Applications)|[딥러닝] 검증된 AI 모델 활용(Keras Applications)]]
- [[blog/AI(ML & DL)/딥러닝- 오토인코더와 활용|[딥러닝] 오토인코더와 활용]]
