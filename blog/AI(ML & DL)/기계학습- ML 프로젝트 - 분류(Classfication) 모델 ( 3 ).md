---
title: "[기계학습] ML 프로젝트 - 분류(Classfication) 모델 ( 3 )"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "AI", "CS"]
category: "AI(ML & DL)"
published: 2025-05-27
source_url: https://ch010104.tistory.com/85
---

# [기계학습] ML 프로젝트 - 분류(Classfication) 모델 ( 3 )

## 원문

https://ch010104.tistory.com/85

## 노트 유형

`project`

## 배경·목표·적용 맥락

머신러닝 이진 분류 문제에서는 모델의 단순 정확도보다 더 세밀한 평가 지표가 필요함

특히 데이터가 불균형한 경우, 또는 False Positive / False Negative의 중요도가 다른 경우, 정밀도(Precision), 재현율(Recall), ROC 곡선, AUC 등을 통해 성능을 평가

## 구현·의사결정·결과

머신러닝 이진 분류 문제에서는 모델의 단순 정확도보다 더 세밀한 평가 지표가 필요함

특히 데이터가 불균형한 경우, 또는 False Positive / False Negative의 중요도가 다른 경우, 정밀도(Precision), 재현율(Recall), ROC 곡선, AUC 등을 통해 성능을 평가

### 1. 정밀도/재현율 기준 임계값 설정 방법

예제 1) 정밀도 0.9 이상을 만족하는 최소 임계값 찾기

```text
idx = np.argmax(precisions >= 0.9)
threshold_90_precision = thresholds[idx]
```

precisions >= 0.9 조건을 만족하는 첫 번째 인덱스를 찾고,

해당 인덱스의 thresholds[idx] 값을 가져오면 정밀도 90% 이상을 보장하는 최소 임계값

예제 2) 재현율 0.8 이상을 만족하는 최대 임계값 찾기

```text
idx = np.argmax(recalls < 0.8)
threshold_80_recall = thresholds[idx - 1]
```

recalls < 0.8인 첫 인덱스를 찾아 **그 이전 인덱스(-1)**의 임계값을 사용하면,

재현율 80% 이상을 보장하는 최대 임계값

### 2. 선택된 임계값으로 예측 수행 및 평가

선택된 임계값을 기준으로 모델 예측 수행:

```text
y_scores = sgd_clf.decision_function(X_train)
y_pred = (y_scores >= threshold_80_recall)
```

이후 precision_score()와 recall_score()을 이용해 성능 평가

### 4. ROC 곡선과 AUC

1) ROC 곡선이란?

ROC (Receiver Operating Characteristic) Curve는 임계값 변화에 따른 FPR(False Positive Rate) 와 TPR(True Positive Rate) 의 관계를 나타냄

top-left 코너에 근접할 수록 좋은 분류기임.

TPR = Recall

FPR = FP / (FP + TN)

2) roc_curve() 함수

```text
fpr, tpr, thresholds = roc_curve(y_true, y_scores)
```

다양한 임계값에서 FPR과 TPR 값을 계산

3) AUC (Area Under the Curve)

ROC 곡선 아래 면적

1에 가까울수록 좋은 분류기

모델 간 비교에 효과적

4) 정밀도/재현율 곡선

top-right 코너에 근접할 수록 좋은 성능의 분류기임.

이 곡선의 AUC 또한 1에 가까울 수록 좋은 성능의 분류기임.

### 5. ROC vs 정밀도/재현율 곡선, 언제 사용해야 할까?

예시

아이가 봐도 되는 동영상을 필터링할 때:

잘못된 영상을 허용하는 것(FP) 이 더 큰 문제

⇒ 정밀도/재현율 곡선 사용이 더 적합

### 6. 좋은 분류기의 기준

## 관련 글

- [[blog/AI(ML & DL)/index|AI(ML & DL)]]
- [[blog/AI(ML & DL)/기계학습- ML 프로젝트 - 분류(Classfication) 모델 ( 4 )|[기계학습] ML 프로젝트 - 분류(Classfication) 모델 ( 4 )]]
- [[blog/AI(ML & DL)/기계학습- ML 프로젝트 - 분류(Classfication) 모델 ( 2 )|[기계학습] ML 프로젝트 - 분류(Classfication) 모델 ( 2 )]]
- [[blog/AI(ML & DL)/기계학습- ML 프로젝트 - 분류(Classfication) 모델 ( 5 )|[기계학습] ML 프로젝트 - 분류(Classfication) 모델 ( 5 )]]
