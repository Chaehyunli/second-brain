---
title: "[기계학습] ML 프로젝트 - 분류(Classfication) 모델 ( 5 )"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "AI", "CS"]
category: "AI(ML & DL)"
published: 2025-06-02
source_url: https://ch010104.tistory.com/93
---

# [기계학습] ML 프로젝트 - 분류(Classfication) 모델 ( 5 )

## 원문

https://ch010104.tistory.com/93

## 노트 유형

`project`

## 배경·목표·적용 맥락

행 기준 정규화: 각 실제 클래스별 예측 분포 (가로 합 = 100%)

열 기준 정규화: 각 예측 결과에 대한 실제 클래스 분포 (세로 합 = 100%)

## 구현·의사결정·결과

### 1. 오차 행렬 (Confusion Matrix) 이란?

1) 오차 행렬이란?

모델의 예측 결과 vs 실제 값을 행렬로 정리한 것

각 행: 실제 클래스

각 열: 모델이 예측한 클래스

2) 정규화된 오차 행렬

행 기준 정규화: 각 실제 클래스별 예측 분포 (가로 합 = 100%)

열 기준 정규화: 각 예측 결과에 대한 실제 클래스 분포 (세로 합 = 100%)

3) 예시 분석

행 정규화 기준

숫자 '7'의 이미지 중:

34% → 숫자 '8'로 오분류

36% → 숫자 '9'로 오분류 → 즉, 7을 8이나 9로 자주 착각함

열 정규화 기준

숫자 '7'로 분류된 이미지 중:

56%는 실제로 '9'였음 → 숫자 '9'가 자주 '7'로 오분류됨

4) 오차 행렬을 통해 할 수 있는 인사이트

어떤 클래스에서 오류가 많이 발생하는지 파악 가능

자주 혼동되는 숫자 쌍(예: 8과 5, 7과 9 등)을 구별할 수 있도록 추가 특성 도입 고려

예: → 동심원 개수 특성 추가 (8은 2개, 6은 1개, 5는 0개)

5) 데이터 증식 (Data Augmentation)

왜 필요한가?

더 좋은 성능을 내려면 더 많은 훈련 이미지가 필요

하지만 새로운 이미지를 확보하는 것은 현실적으로 어려움

해결책: 기존 이미지 변형

회전

이동

반전

확대/축소 등

이렇게 생성된 데이터를 훈련 세트에 추가하는 방법을 데이터 증식(Data Augmentation) 이라고 부름.

### 2. 다중 레이블 분류 (Multi-label Classification)

하나의 이미지에 대해 여러 개의 타깃 레이블을 부여하는 방식

1) 데이터 준비

```python
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# 타깃 레이블: 7 이상인지 여부 / 홀수인지 여부
y_train_large = (y_train >= 7)
y_train_odd = (y_train % 2 == 1)
y_multilabel = np.c_[y_train_large, y_train_odd]
```

2) 모델 훈련 및 예측

```text
knn_clf = KNeighborsClassifier()
knn_clf.fit(X_train, y_multilabel)

# 예측
some_digit = X_train[0]
knn_clf.predict([some_digit])  # 출력 예: [[True, False]]
```

예측 결과 [True, False]는 숫자가 7 이상이고 짝수임을 의미

### 3. 다중 출력 분류 (Multioutput Classification)

이미지의 각 픽셀에 대해 다중 클래스(0~255) 값을 예측하는 방식

예: 이미지 노이즈 제거

1) 노이즈 추가 및 데이터 생성

```text
np.random.seed(42)
noise = np.random.randint(0, 100, size=X_train.shape)
X_train_mod = X_train + noise
y_train_mod = X_train.copy()

noise_test = np.random.randint(0, 100, size=X_test.shape)
X_test_mod = X_test + noise_test
y_test_mod = X_test.copy()
```

2) 모델 훈련

```text
knn_clf = KNeighborsClassifier()
knn_clf.fit(X_train_mod, y_train_mod)
```

3) 예측 및 시각화

```python
import matplotlib.pyplot as plt

def plot_digit(data):
    image = data.reshape(28, 28)
    plt.imshow(image, cmap="binary")
    plt.axis("off")
    plt.show()

# 원본 / 노이즈 추가 / 복원 예측 결과
cleaned_image = knn_clf.predict([X_test_mod[0]])

print("노이즈 이미지:")
plot_digit(X_test_mod[0])

print("복원된 이미지:")
plot_digit(cleaned_image)
```

모델이 노이즈가 낀 이미지로부터 원본 이미지를 복원하는 다중 출력 분류를 수행

## 관련 글

- [[blog/AI(ML & DL)/index|AI(ML & DL)]]
- [[blog/AI(ML & DL)/기계학습- ML 프로젝트 - 분류(Classfication) 모델 ( 4 )|[기계학습] ML 프로젝트 - 분류(Classfication) 모델 ( 4 )]]
- [[blog/AI(ML & DL)/기계학습- ML 프로젝트 - 분류(Classfication) 모델 ( 3 )|[기계학습] ML 프로젝트 - 분류(Classfication) 모델 ( 3 )]]
- [[blog/AI(ML & DL)/기계학습- ML 프로젝트 - 분류(Classfication) 모델 ( 2 )|[기계학습] ML 프로젝트 - 분류(Classfication) 모델 ( 2 )]]
