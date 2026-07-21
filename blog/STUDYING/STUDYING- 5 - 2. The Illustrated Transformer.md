---
title: "[STUDYING] 5 - 2. The Illustrated Transformer"
created: 2026-07-21
updated: 2026-07-21
type: blog-post
tags: ["blog", "technical-writing"]
category: "STUDYING"
published: 2026-07-21
source_url: https://ch010104.tistory.com/306
---
# [STUDYING] 5 - 2. The Illustrated Transformer

## 원문

https://ch010104.tistory.com/306

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

https://jalammar.github.io/illustrated-transformer/

이 노트는 원문의 학습 흐름을 바탕으로 재구성한 참고 노트다. 아래 도식은 원문의 핵심 시각 자료이며, Jay Alammar, CC BY-NC-SA 4.0으로 출처를 밝힌다. 원문은 이해를 돕기 위한 직관적 설명이므로, 세부 구현·최신 Transformer 변형은 원 논문과 공식 구현으로 교차 확인한다.

## 원문 기반 개념 정리

### 원문·이미지 라이선스

https://jalammar.github.io/illustrated-transformer/

이 노트는 원문의 학습 흐름을 바탕으로 재구성한 참고 노트다. 아래 도식은 원문의 핵심 시각 자료이며, Jay Alammar, CC BY-NC-SA 4.0으로 출처를 밝힌다. 원문은 이해를 돕기 위한 직관적 설명이므로, 세부 구현·최신 Transformer 변형은 원 논문과 공식 구현으로 교차 확인한다.

### 1. 큰 그림: 번역 모델에서 Encoder–Decoder로

Transformer는 입력 문장을 받아 출력 문장을 생성하는 encoder–decoder 구조다. 원 논문 예시는 기계번역이지만, 핵심은 입력 토큰을 문맥화하고 목표 토큰을 순차 생성하는 과정이다.

Encoder는 입력 시퀀스를 여러 층으로 처리해 문맥 표현을 만든다.

Decoder는 이전에 생성한 출력과 encoder의 표현을 참고해 다음 토큰을 예측한다.

원 논문은 encoder·decoder를 각각 6층 쌓았지만, 층 수는 고정 규칙이 아닌 설계 선택이다.

### 2. Encoder 블록: 토큰 간 관계와 위치별 변환

각 encoder 층은 Self-Attention과 position-wise Feed-Forward Network로 구성된다. Self-Attention은 현재 토큰을 인코딩할 때 다른 입력 토큰을 참고하게 하고, FFN은 각 토큰 위치에 독립적으로 동일한 비선형 변환을 적용한다.

입력 토큰은 먼저 임베딩 벡터가 된다. 최하위 encoder는 token embedding을 받지만, 그 위 층들은 바로 아래 encoder의 출력을 입력으로 받는다.

### 3. Self-Attention: 현재 토큰을 문맥으로 다시 표현하기

Self-Attention은 한 토큰이 같은 문장 안의 어떤 토큰을 얼마나 참고할지 계산한다. 예를 들어 대명사 it을 처리할 때 관련 명사를 더 강하게 참고할 수 있다. 이는 단어 자체를 고정 벡터로 보지 않고, 주변 문맥이 반영된 벡터로 바꾸는 과정이다.

### Q, K, V와 계산 흐름

입력 행렬 X를 서로 다른 학습 가중치로 변환해 Q, K, V를 만든다.

QKᵀ: Query와 Key의 내적으로 토큰 쌍의 관련성 점수를 만든다.

/√d_k: 차원이 클 때 score가 과도하게 커지는 문제를 완화한다.

softmax: 각 Query가 모든 Key를 참고하는 비중을 정규화한다.

×V: 비중에 따라 Value를 가중합해 새 문맥 벡터를 만든다.

### 4. Multi-Head Attention: 하나의 관계만 보지 않기

여러 head는 서로 다른 W_Q, W_K, W_V로 입력을 각기 다른 표현 공간에 투영한 뒤 attention을 병렬 계산한다. 각 head의 출력 Z_i를 이어 붙이고 W_O로 투영해 하나의 출력으로 합친다.

여러 head는 문법적 연결·의미적 유사성·장거리 의존성 등 서로 다른 관계를 포착할 수 있는 표현 용량을 준다. 다만 특정 head 하나에 사람이 읽을 수 있는 역할이 항상 고정된다고 단정해서는 안 된다.

### 5. Positional Encoding: 병렬 처리에 순서를 다시 넣기

Self-Attention은 입력을 병렬로 보므로 토큰 위치를 자동으로 알지 못한다. Transformer는 token embedding에 positional encoding을 더해 순서·상대 거리 단서를 제공한다.

원 논문 방식은 각 위치·차원에 사인·코사인 함수를 사용한다. 값의 범위가 제한되고, 차원별 주기가 달라 서로 다른 위치를 구분할 수 있다. 최신 모델에는 학습형 위치 임베딩·RoPE 등 다른 방식도 있다.

### 6. Residual Connection과 Layer Normalization

각 Self-Attention·FFN sub-layer는 residual connection으로 입력을 더하고 LayerNorm을 적용한다.

Residual connection은 원래 표현과 gradient 흐름을 보존하고, LayerNorm은 학습을 안정화한다.

### 7. Decoder: 미래를 보지 않고 다음 토큰 생성하기

Decoder는 이전 출력 토큰을 임베딩·위치 인코딩한 뒤 masked self-attention을 적용한다. 미래 위치의 score를 softmax 전 차단해 현재 위치가 아직 생성되지 않은 정답 토큰을 볼 수 없게 한다. 이어 encoder–decoder attention이 encoder의 K·V를 참고하고, FFN이 다음 표현을 만든다.

Decoder의 autoregressive 생성과 mask 흐름 — 출처: Jay Alammar

마지막 선형층과 softmax는 decoder 표현을 vocabulary 전체의 다음 토큰 확률분포로 바꾼다. 학습에서는 정답 토큰과 예측 분포를 비교하는 loss를 최소화하고, 추론에서는 이전에 생성한 토큰을 다음 단계 입력으로 사용한다.

## 관련 글

- [[blog/STUDYING/index|STUDYING]]
