---
title: "[딥러닝] Gradient 및 자동 미분(Autogradient)"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "AI", "D", "DL"]
category: "AI(ML & DL)"
published: 2025-11-11
source_url: https://ch010104.tistory.com/184
---

# [딥러닝] Gradient 및 자동 미분(Autogradient)

## 원문

https://ch010104.tistory.com/184

## 핵심 요약

- **계산 그래프 (Computation Graph)** — 정의: 입력 데이터(x)와 모델 파라미터(w)를 받아, 최종 예측값을 계산하는 과정을 일련의 연산 노드(+, *, exp, 1/x 등)로 표현한 그래프
- **계산 그래프 예시 상세** — 원리: 체인룰(Chain Rule)을 사용하여 $\frac{\partial L}{\partial x}=\frac{\partial\sigma}{\partial x}\frac{\partial L}{\partial\sigma}$ 와 같이 그래디언트를 역방향으로 전파
- **그래디언트 흐름의 패턴** — Add Gate (덧셈): 그래디언트 분배기 (Gradient Distributor)

## 관련 글

- [[blog/AI(ML & DL)/index|AI(ML & DL)]]
- [[blog/AI(ML & DL)/딥러닝- 오토인코더와 활용|[딥러닝] 오토인코더와 활용]]
- [[blog/AI(ML & DL)/딥러닝- 검증된 AI 모델 활용(Keras Applications)|[딥러닝] 검증된 AI 모델 활용(Keras Applications)]]
- [[blog/AI(ML & DL)/딥러닝- 모델 다루기 (Sequential & Functional + Inception Module 실습)|[딥러닝] 모델 다루기 (Sequential & Functional + Inception Module 실습)]]
