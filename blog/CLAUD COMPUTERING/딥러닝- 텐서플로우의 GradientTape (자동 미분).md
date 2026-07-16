---
title: "[딥러닝] 텐서플로우의 GradientTape (자동 미분)"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "AI", "DL"]
category: "CLAUD COMPUTERING"
published: 2025-10-30
source_url: https://ch010104.tistory.com/175
---

# [딥러닝] 텐서플로우의 GradientTape (자동 미분)

## 원문

https://ch010104.tistory.com/175

## 노트 유형

`guide`

## 적용 목적과 전제조건

- 텐서플로우의 GradientTape는 연산 과정을 '테이프'에 녹화(기록)하여 자동 미분을 수행하는 기능

핵심 목적: 모델 학습 과정에서 각 파라미터(가중치)가 최종 Loss(오류)에 얼마나 영향을 미쳤는지 계산하기 위함

## 구현 절차·검증·주의점

- 텐서플로우의 GradientTape는 연산 과정을 '테이프'에 녹화(기록)하여 자동 미분을 수행하는 기능

핵심 목적: 모델 학습 과정에서 각 파라미터(가중치)가 최종 Loss(오류)에 얼마나 영향을 미쳤는지 계산하기 위함

동작 방식: tape는 연산의 최종 값(예: y=9, x=3)만 저장하는 것이 아니라, "숫자 3.0을 입력받아($x$), 그것을 제곱(**2)해서 y를 만들었다"는 계산 과정(연산 그래프) 자체를 기록

학습 활용: 이 기록을 바탕으로 Loss를 각 가중치로 미분하여, Loss를 줄이는 방향으로 가중치를 조절(학습)

### 1. 기본 GradientTape 예제

단순 변수의 Gradient를 계산하는 예제

```text
# x는 3.0 값을 가진 변수(Variable)
x = tf.Variable(3.0)

# GradientTape 컨텍스트 시작 (연산 기록 시작)
with tf.GradientTape() as tape:
  y = x**2

# y를 x로 미분 (dy/dx = 2x)
# x가 3.0이므로, 2 * 3 = 6.0이 됨
dy_dx = tape.gradient(y, x)
dy_dx.numpy()
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

결과: 6.0

### 2. 모델 학습 예제

하나의 Loss 함수를 모델의 모든 학습 가능한 파라미터(가중치 $w$, 편향 $b$)로 미분하여 Gradient를 계산하는 예제

```text
# 2개의 출력 뉴런을 가진 Dense 레이어 정의
layer = tf.keras.layers.Dense(2, activation='relu')
# 입력 데이터 (1개의 샘플, 3개의 특성)
x = tf.constant([[1., 2., 3.]])

with tf.GradientTape() as tape:
  # 1. Forward pass (순전파)
  y = layer(x)

  # 2. Loss 계산 (y^2의 평균을 최종 Loss 값으로 사용)
  loss = tf.reduce_mean(y**2)

# 3. Gradient 계산
# loss를 layer의 모든 학습 가능한 변수(가중치 w, 편향 b)로 미분
grad = tape.gradient(loss, layer.trainable_variables)

# 4. 결과 출력
for var, g in zip(layer.trainable_variables, grad):
  print(f'{var.name}, shape: {g.shape}')
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### AutoGrad의 응용: Heatmap 활성화

- AutoGrad 개념은 모델 학습뿐만 아니라, 모델의 판단 근거를 시각화(Heatmap)하는 데에도 응용

시각화 목적: 모델이 이미지를 특정 클래스(예: '코끼리')로 판단했다면, **"대체 이미지의 어느 부분을 보고 그렇게 판단했는가?"**를 알아내기 위함

Heatmap: 데이터 값의 크기나 밀도를 색상으로 표현하는 시각화 기법

이 방식은 모델 학습 시의 자동 미분과 목표가 다름

1. 미분 대상의 차이

모델 학습 (AutoGrad): **"전체 Loss 함수"**에 대해 미분

Heatmap 시각화: **"특정 클래스(예: 386번 코끼리)의 예측 점수($y^{386}$)"**에 대해서만 미분

2. 미분 변수의 차이

모델 학습 (AutoGrad): "전체 가중치($W$)"(모든 학습 파라미터)에 대해 미분

Heatmap 시각화: **"특정 레이어(예: 'block5-conv3')의 피처 맵(feature map)"**에 대해서 미분

3. 시각화 과정

Convolution 레이어의 출력(피처 맵)은 원본 이미지(WxH)와 크기(W'xH')가 다름

하지만 Convolution은 위치 정보의 순서를 보존

따라서 계산된 Heatmap(W'xH')을 원본 입력 크기(WxH)에 맞게 늘리면(resize), 이미지의 어느 부분을 활성화했는지 시각화할 수 있음

## 관련 글

- [[blog/CLAUD COMPUTERING/index|CLAUD COMPUTERING]]
- [[blog/CLAUD COMPUTERING/클라우드 컴퓨터링- 머신러닝, 딥러닝과 빅데이터|[클라우드 컴퓨터링] 머신러닝, 딥러닝과 빅데이터]]
- [[blog/AI(ML & DL)/딥러닝- 검증된 AI 모델 활용(Keras Applications)|[딥러닝] 검증된 AI 모델 활용(Keras Applications)]]
- [[blog/AI(ML & DL)/딥러닝- 오토인코더와 활용|[딥러닝] 오토인코더와 활용]]
