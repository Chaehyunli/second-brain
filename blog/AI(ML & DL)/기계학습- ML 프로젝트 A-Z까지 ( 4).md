---
title: "[기계학습] ML 프로젝트 A-Z까지 ( 4)"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "AI", "CS"]
category: "AI(ML & DL)"
published: 2025-05-02
source_url: https://ch010104.tistory.com/66
---

# [기계학습] ML 프로젝트 A-Z까지 ( 4)

## 원문

https://ch010104.tistory.com/66

## 노트 유형

`project`

## 배경·목표·적용 맥락

머신러닝 모델은 입력 특성 간의 스케일(값의 범위) 차이에 민감

이런 경우, total_rooms 특성의 영향력이 더 크게 작용하여 모델이 특정 특성에 편향될 위험이 있음.

## 구현·의사결정·결과

### 특성 스케일링 (Feature Scaling)

1) 왜 특성 스케일링이 필요한가?

머신러닝 모델은 입력 특성 간의 스케일(값의 범위) 차이에 민감

이런 경우, total_rooms 특성의 영향력이 더 크게 작용하여 모델이 특정 특성에 편향될 위험이 있음.

해결 방법 → 특성 스케일링

→ 모든 수치형 특성의 스케일을 통일해주는 전처리 과정 → **레이블(타깃 값)**에는 스케일링 적용 ❌

2) 대표적인 스케일링 방법

① Min-Max 스케일링 (정규화, Normalization)

값들을 0과 1 사이로 압축

변환 식

​

특징

값의 범위를 고정: [0, 1] (또는 feature_range로 지정 가능)

이상치에 매우 민감

예제 (Python + Scikit-learn)

```python
import numpy as np
from sklearn.preprocessing import MinMaxScaler

data = np.array([[1000], [2000], [3000], [100000]])  # 이상치 포함
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data)

print("정규화 결과:\n", scaled_data)
```

출력 결과

```text
정규화 결과:
[[0.     ]
 [0.0102 ]
 [0.0204 ]
 [1.     ]]
```

100000 같은 이상치 때문에 다른 값들이 0 근처로 몰림

② 표준화 (Standardization)

값들을 평균 0, 표준편차 1을 갖도록 변환

변환 식

μ\muμ: 평균값

σ\sigmaσ: 표준편차

특징

이상치에 덜 민감

선형 회귀, SVM, 로지스틱 회귀 등에서 잘 작동

예제 (Python + Scikit-learn)

```text
from sklearn.preprocessing import StandardScaler

data = np.array([[1000], [2000], [3000], [100000]])  # 이상치 포함
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

print("표준화 결과:\n", scaled_data)
```

출력 결과

```text
표준화 결과:
[[-0.5001]
 [-0.4922]
 [-0.4843]
 [ 1.4766]]
```

평균 기준으로 분산이 고려되어 이상치의 영향이 완화됨

## 관련 글

- [[blog/AI(ML & DL)/index|AI(ML & DL)]]
- [[blog/AI(ML & DL)/기계학습- ML 프로젝트 A-Z까지 ( 5 )|[기계학습] ML 프로젝트 A-Z까지 ( 5 )]]
- [[blog/AI(ML & DL)/기계학습- ML 프로젝트 A-Z까지 ( 3 )|[기계학습] ML 프로젝트 A-Z까지 ( 3 )]]
- [[blog/AI(ML & DL)/기계학습- ML 프로젝트 A - Z 까지 ( 6 )|[기계학습] ML 프로젝트 A - Z 까지 ( 6 )]]
