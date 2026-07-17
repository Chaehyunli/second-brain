---
title: "[딥러닝] 딥러닝 - MINST 손글씨 인식"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing"]
category: "AI(ML & DL)"
published: 2025-09-23
source_url: https://ch010104.tistory.com/139
---

# [딥러닝] 딥러닝 - MINST 손글씨 인식

## 원문

https://ch010104.tistory.com/139

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

- MNIST는 사람들이 직접 쓴 0부터 9까지의 손글씨 숫자 이미지 데이터셋 28×28 픽셀 크기의 흑백 이미지

- 손글씨 이미지를 보고 어떤 숫자인지 정확하게 맞추는 모델을 만드는 것이 목표

## 원문 기반 개념 정리

### 1단계: 데이터 준비하기 - MNIST란 ?

- MNIST는 사람들이 직접 쓴 0부터 9까지의 손글씨 숫자 이미지 데이터셋 28×28 픽셀 크기의 흑백 이미지

- 손글씨 이미지를 보고 어떤 숫자인지 정확하게 맞추는 모델을 만드는 것이 목표

먼저, Keras 라이브러리를 사용해 MNIST 데이터를 불러옴

데이터는 모델 학습에 사용될 훈련 셋(training set)과 모델의 성능을 검증하기 위한 테스트 셋(test set)으로 나눔

```text
from keras.datasets import mnist

# 데이터를 훈련 셋과 테스트 셋으로 불러오기
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
```

훈련 데이터: 60,000개의 이미지와 각 이미지에 해당하는 정답(레이블)이 있음.

테스트 데이터: 10,000개의 이미지와 정답 레이블이 있음. 이 데이터는 모델 학습에 사용되지 않고, 오직 성능 평가에만 사용

matplotlib 라이브러리를 사용하면 데이터에 포함된 이미지를 직접 눈으로 확인할 수 있음

```text
import matplotlib.pyplot as plt

# 훈련 데이터의 5번째 이미지(인덱스 4)를 확인
digit = train_images[4]
plt.imshow(digit, cmap=plt.cm.binary)
plt.show()
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### 2단계: 신경망 모델 만들기

- Keras의 Sequential 모델은 각 레이어(layer)를 레고 블록처럼 순차적으로 쌓아 만드는 간단하고 직관적인 방법

```text
from keras import models
from keras import layers

network = models.Sequential()
# 입력 데이터 형태는 28*28=784차원 벡터
network.add(layers.Input(shape=(28*28,)))
# 512개의 뉴런을 가진 Dense 레이어, 활성화 함수로 'relu' 사용
network.add(layers.Dense(512, activation='relu'))
# 10개의 뉴런을 가진 출력 레이어, 활성화 함수로 'softmax' 사용
network.add(layers.Dense(10, activation='softmax'))
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

Dense 레이어: - '완전 연결 계층'이라고도 불림 - 이전 레이어의 모든 뉴런과 다음 레이어의 모든 뉴런이 서로 연결된 가장 기본적인 형태의 레이어 - 이 연결(가중치)들을 조절하며 데이터의 특징을 학습

활성화 함수(Activation Function): 뉴런의 출력값을 변환하는 함수

relu: 일반적으로 중간 레이어에서 많이 사용되는 활성화 함수

softmax: 모델의 마지막 출력층에서 사용되며, 출력 결과를 0과 1 사이의 확률값으로 변환 - 예를 들어, 이미지가 숫자 '3'일 확률 80%, '5'일 확률 15% 등으로 나타냄. 총합은 항상 1.

Logits: Sigmoid함수나 Softmax함수와는 반대로 확률값이 주어졌을 경우, 실제 값으로 매핑하고 싶을 경우

### 3단계: 모델 컴파일하기 (학습 과정 설정)

- 모델이 어떻게 학습할지를 정하는 '컴파일' 단계가 필요

- 이 단계에서는 옵티마이저, 손실 함수, 측정 지표를 설정

```text
network.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])
```

옵티마이저(Optimizer): - 모델이 데이터와 손실 함수를 기반으로 가중치(weight)를 업데이트하는 메커니즘

- rmsprop, Adam 등이 널리 사용

손실 함수(Loss Function): - 모델의 예측이 정답과 얼마나 다른지를 측정하는 방법 - 모델은 이 손실 값을 최소화하는 방향으로 학습 - 이번 예제처럼 여러 카테고리 중 하나를 맞추는 문제에서는 categorical_crossentropy를 사용

측정 지표(Metrics): - 학습과 테스트 과정을 모니터링하기 위한 지표 - 가장 직관적인 **정확도(accuracy)**를 사용해 모델의 성능을 평가

### 4단계: 데이터 전처리

- 모델에 데이터를 입력하기 전에, 모델이 이해할 수 있는 형태로 가공하는 과정이 필요

데이터 형태 변환: - 우리가 만든 Dense 레이어는 1차원 벡터 형태의 입력을 기대 - 따라서 28×28 크기의 2차원 이미지를 784개의 원소를 가진 1차원 벡터로 변환

정규화: - 이미지의 각 픽셀 값은 0에서 255 사이의 값을 가짐 - 이 값을 0과 1 사이의 실수로 변환(정규화)하면 모델이 더 안정적으로 학습

레이블 인코딩: - 현재 정답 레이블은 5, 0, 4 같은 숫자 - 하지만 모델의 최종 출력은 10개의 확률값이므로, 정답 데이터도 같은 형식으로 바꿔줘야 함 - 3은 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0] 과 같은 10차원 벡터로 바뀜 - to_categorical 함수를 사용해 레이블을 '원-핫 인코딩(one-hot encoding)' 형태로 변환

```text
# 1. 이미지 데이터 형태 변환 및 정규화
v_train_images = train_images.reshape((60000, 28 * 28))
v_train_images = v_train_images.astype('float32') / 255

v_test_images = test_images.reshape((10000, 28 * 28))
v_test_images = v_test_images.astype('float32') / 255

# 2. 레이블 원-핫 인코딩
from keras.utils import to_categorical

v_train_labels = to_categorical(train_labels)
v_test_labels = to_categorical(test_labels)
```

### 5단계: 모델 학습시키기

- fit 메소드를 호출하여 훈련 데이터로 모델을 학습

```text
network.fit(v_train_images, v_train_labels, epochs=5, batch_size=128)
```

epochs: - 전체 훈련 데이터셋을 몇 번 반복하여 학습할지를 의미 - 여기서는 전체 데이터를 5번 학습

batch_size: - 한 번에 학습할 데이터의 개수 - 60,000개의 데이터를 128개씩 나누어 학습을 진행

학습이 진행되면서 각 epoch마다 손실(loss)은 점차 줄어들고 정확도(accuracy)는 올라가는 것을 확인할 수 있음

### 6단계: 모델 성능 평가하기

- 학습이 완료된 모델이 얼마나 뛰어난 성능을 보이는지 확인 - 학습에 전혀 사용되지 않은 테스트 데이터를 사용하여 모델을 평가

```text
test_loss, test_acc = network.evaluate(v_test_images, v_test_labels)
print('test_acc:', test_acc)

# 출력 예시
# test_acc: 0.979200005531311
```

결과를 보면 약 97.9%의 정확도를 보여줌

이는 우리가 만든 간단한 신경망 모델이 처음 보는 손글씨 이미지 100개 중 약 98개를 정확하게 맞춘다는 의미

## 관련 글

- [[blog/AI(ML & DL)/index|AI(ML & DL)]]
- [[blog/AI(ML & DL)/딥러닝- 퍼셉트론(Perceptron)과 경사 하강법(Gradient Descent)|[딥러닝] 퍼셉트론(Perceptron)과 경사 하강법(Gradient Descent)]]
- [[blog/AI(ML & DL)/딥러닝- 머신러닝- 학습(Learning)과 모델(Model)|[딥러닝] 머신러닝: 학습(Learning)과 모델(Model)]]
- [[blog/AI(ML & DL)/딥러닝- 인공지능의 동향|[딥러닝] 인공지능의 동향]]
