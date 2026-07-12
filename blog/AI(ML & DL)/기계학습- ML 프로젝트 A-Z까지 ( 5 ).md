---
title: "[기계학습] ML 프로젝트 A-Z까지 ( 5 )"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "AI", "CS"]
category: "AI(ML & DL)"
published: 2025-05-05
source_url: https://ch010104.tistory.com/68
---

# [기계학습] ML 프로젝트 A-Z까지 ( 5 )

## 원문

https://ch010104.tistory.com/68

## 핵심 요약

- **1. 변환기란?** — 변환기(Transformer)는 입력 데이터를 분석, 변환, 정규화, 인코딩 등 다양한 방식으로 전처리하여 머신러닝 모델이 학습할 수 있도록 도와주는 객체
- **2. 변환기 사용 시 주의사항** — fit() 함수는 훈련셋에만 사용해야 함 → 테스트셋에는 절대 사용 ❌
- **3. 변환기 구현 방법** — ✅ 방법 1: FunctionTransformer 사용
- **4. 변환 파이프라인(Pipeline)의 구성** — 마지막 객체만 predictor, 나머지는 모두 transformer여야 함

## 관련 글

- [[blog/AI(ML & DL)/index|AI(ML & DL)]]
- [[blog/AI(ML & DL)/기계학습- ML 프로젝트 A-Z까지 ( 4)|[기계학습] ML 프로젝트 A-Z까지 ( 4)]]
- [[blog/AI(ML & DL)/기계학습- ML 프로젝트 A - Z 까지 ( 6 )|[기계학습] ML 프로젝트 A - Z 까지 ( 6 )]]
- [[blog/AI(ML & DL)/기계학습- ML 프로젝트 A-Z까지 ( 3 )|[기계학습] ML 프로젝트 A-Z까지 ( 3 )]]
