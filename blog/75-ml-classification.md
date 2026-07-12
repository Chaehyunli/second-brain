---
title: "[기계학습] ML 프로젝트 - 분류 (Classification) 모델"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: [blog, technical-writing]
category: "AI(ML & DL)"
published: 2025-05-19
source_url: https://ch010104.tistory.com/75
archive_method: Tistory sitemap + HTML content extraction
---

# [기계학습] ML 프로젝트 - 분류 (Classification) 모델

> 원문: https://ch010104.tistory.com/75

## 본문

이전에는 회귀 모델의 ML 프로젝트를 알아보았다면, 이번에는 분류 모델의 ML 프로젝트를 알아보자.   주요 목표  MNIST 손글씨 숫자 이미지 데이터셋을 활용하여, 숫자 5인지 아닌지를 구분하는 **이진 분류기(binary classifier)**를 먼저 훈련 다양한 **분류 성능 지표(정확도, 정밀도, 재현율, AUC)**를 통해 성능을 분석   1. MNIST 데이터셋    총 70,000개의 숫자 이미지 (28×28픽셀 → 784개의 특성) 미국 고등학생과 인구조사국 직원들이 손으로 쓴 70,000개의 숫자 이미지로 구성 된 데이터셋 각 이미지의 정답 레이블은 0~9 중 하나 데이터 형태:  X.shape = (70000, 784) → 이미지 데이터 y.shape = (70000,) → 정답 레이블    1) 데이터 분할  훈련셋 (X_train, y_train): 60,000개 테스트셋 (X_test, y_test): 10,000개  2) 문제 정의  지도 학습- 각 이미지가 어떤 숫자를 나타내는지에 대한 레이블 지정되어 있음 분류- 주어진 이미지 데이터가 0부터 9까지 중 어떤 숫자에해당하는지를 예측 배치 또는 온라인 학습   2. 이진 분류기 훈련 (5-detector) 1) 목적  10개 숫자 중 5인지 아닌지만 판단하는 이진 분류기 훈련  레이블 변환  y_train_5 = (y_train == 5) → 5면 True(1), 아니면 False(0) y_test_5 = (y_test == 5)   2) SGD 분류기 (SGDClassifier)  확률적 경사 하강법(Stochastic Gradient Descent) 기반 분류기 한 번에 하나의 샘플로 파라미터 업데이트 → 온라인 학습 가능 사이킷런 SGDClassifier 사용  사용 예   from sklearn.linear_model import SGDClassifier sgd_clf = SGDClassifier() sgd_clf.fit(X_train, y_train_5) y_pred = sgd_clf.predict(X_test)    3. 분류기 성능 측정 1) 정확도 (Accuracy)   ​  전체 샘플 중 올바르게 분류한 비율 불균형 데이터에서 부적절할 수 있음  실험  Dummy 분류기: 항상 "5 아님"으로 예측 정확도 90% 이상 → 이유: 데이터의 90%가 실제로 5가 아님!- 훈련셋 샘플들의 클래스 불균형이 심한 경우에는 분류기의 성능 측정 지표로 정확도 (accuracy)는 부적합   2) 오차 행렬 (Confusion Matrix)    행: 실제 값 열: 예측 값 이진 분류기에서는 2×2 행렬 234 는 강아지로 잘못 판단한 고양이의 수를 의미함. 대각선들의 값들이 정상판단한 값들의 수를 의미        예측 : 5 예측: non - 5   실제: 5 TP FN   실제: non-5 FP TN          4. 성능 평가 지표  오차행렬에서의 2×2 행렬에서 TP,FN,FP,TN 값들을 이용해서 지표를 계산    1) 정밀도 (Precision)   ​  예측한 것 중 실제로 맞은 비율- 3530 / (3530 + 687) = 0.83708.. False Positive를 줄이고 싶을 때 중요 기본적으로 non-5 로 예측하다가 정말로 숫자 5가 확실하다고 판단되는 이미지 샘플 하나만 5로 예측-> FP=0 & TP=1 -> Precision = 1 (정밀도를 1로 조작 가능) 결과적으로 정밀도만으로는 좋은 분류기를 가려낼 수 없음 정밀도를 보완할 수 있는 성능 지표(재현율)가 추가로 필요함   2) 재현율 (Recall)   ​  실제 Positive 중에서 얼마나 잘 잡았는가- 3530 / (3530 + 1891) = 0.6511.. 놓치면 안 되는 상황 (암 진단 등)에 중요  3) F1 Score   ​  정밀도와 재현율의 조화 평균- 서로 다른 종류의 두 분류기 모델의 성능을 하나의 metric으로 비교하고자 할 때 유용 둘 간의 균형을 보고 싶을 때 사용 위의 경우에서는 정밀도와 재현율의 가중치를 1:1로 함. 중요도에 따라서 가중치를 바꿀 수 있음.    정밀도(Precision) vs 재현율(Recall) 의 중요도에 따라 가중치를 다르게 두는 것에 대한 것은 다음 글에서 다룰 예정
