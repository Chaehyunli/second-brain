---
title: "[그래프 신경망과 빅데이터] GAE 모델을 활용한 소셜 네트워크 링크 예측 및 이상치 탐지"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "AI", "GAE", "GNN"]
category: "AI(GNN)"
published: 2025-09-07
source_url: https://ch010104.tistory.com/117
---

# [그래프 신경망과 빅데이터] GAE 모델을 활용한 소셜 네트워크 링크 예측 및 이상치 탐지

## 원문

https://ch010104.tistory.com/117

## 핵심 요약

- **ML, DL, GNN 비교하기** — 머신러닝 (Machine Learning, ML): "기본 레시피"
- **1단계: 데이터 준비 - 모델을 위한 교과서와 시험지 만들기** — 스탠포드 대학교에서 제공하는 ego-Facebook 데이터셋을 사용(아래의 링크에서 'facebook_combined.txt' 다운) - https://snap.stanford.edu/data/ego-Facebook.html
- **2단계: GNN 모델 설계 - 관계를 학습할 두뇌 만들기** — 핵심 엔진은 **그래프 오토인코더(Graph Autoencoder, GAE)**
- **3단계: 학습 및 평가 - AI를 학습시키기** — 모델은 교과서(train_data.edge_index)를 보고 친구 관계의 패턴을 학습하고, 중간고사(val_data)를 보며 학습 방향을 점검

## 관련 글

- [[blog/AI(GNN)/index|AI(GNN)]]
- [[blog/AI(GNN)/그래프 신경망 빅데이터- Cora 데이터셋을 이용한 GCN, GAT, FNN성능 비교|[그래프 신경망 빅데이터] Cora 데이터셋을 이용한 GCN, GAT, FNN성능 비교]]
- [[blog/AI(ML & DL)/딥러닝- 인공지능의 동향|[딥러닝] 인공지능의 동향]]
- [[blog/CLAUD COMPUTERING/클라우드 컴퓨터링- 머신러닝, 딥러닝과 빅데이터|[클라우드 컴퓨터링] 머신러닝, 딥러닝과 빅데이터]]
