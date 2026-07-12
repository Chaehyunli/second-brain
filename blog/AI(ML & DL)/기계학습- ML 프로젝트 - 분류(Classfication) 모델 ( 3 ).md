---
title: "[기계학습] ML 프로젝트 - 분류(Classfication) 모델 ( 3 )"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "AI", "CS"]
category: "AI(ML & DL)"
published: 2025-05-27
source_url: https://ch010104.tistory.com/85
---

# [기계학습] ML 프로젝트 - 분류(Classfication) 모델 ( 3 )

## 원문

https://ch010104.tistory.com/85

## 핵심 요약

- 머신러닝 이진 분류 문제에서는 모델의 단순 정확도보다 더 세밀한 평가 지표가 필요함
- **1. 정밀도/재현율 기준 임계값 설정 방법** — 예제 1) 정밀도 0.9 이상을 만족하는 최소 임계값 찾기
- **2. 선택된 임계값으로 예측 수행 및 평가** — 이후 precision_score()와 recall_score()을 이용해 성능 평가
- **4. ROC 곡선과 AUC** — ROC (Receiver Operating Characteristic) Curve는 임계값 변화에 따른 FPR(False Positive Rate) 와 TPR(True Positive Rate) 의 관계를 나타냄

## 관련 글

- [[blog/AI(ML & DL)/index|AI(ML & DL)]]
- [[blog/AI(ML & DL)/기계학습- ML 프로젝트 - 분류(Classfication) 모델 ( 4 )|[기계학습] ML 프로젝트 - 분류(Classfication) 모델 ( 4 )]]
- [[blog/AI(ML & DL)/기계학습- ML 프로젝트 - 분류(Classfication) 모델 ( 2 )|[기계학습] ML 프로젝트 - 분류(Classfication) 모델 ( 2 )]]
- [[blog/AI(ML & DL)/기계학습- ML 프로젝트 - 분류(Classfication) 모델 ( 5 )|[기계학습] ML 프로젝트 - 분류(Classfication) 모델 ( 5 )]]
