---
title: "[기계학습] ML 프로젝트 - 분류(Classfication) 모델 ( 4 )"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: [blog, technical-writing]
category: "AI(ML & DL)"
published: 2025-05-30
source_url: https://ch010104.tistory.com/90
archive_method: Tistory sitemap + HTML content extraction
---

# [기계학습] ML 프로젝트 - 분류(Classfication) 모델 ( 4 )

> 원문: https://ch010104.tistory.com/90

## 본문

머신러닝 분류 문제는 단순히 두 개의 클래스를 구분하는 **이진 분류(binary classification)**에서 출발 하지만, 현실 세계에서는 세 개 이상의 클래스를 분류해야 할 때가 많음 이런 문제를 해결하기 위해 사용하는 것이 바로 **다중 클래스 분류(Multiclass Classification)**   1. 다중 클래스 분류란?  정의: 주어진 샘플이 3가지 이상의 클래스 중 어느 클래스에 속하는지를 예측하는 문제 다른 이름: **다항 분류기(Multinomial Classifier)**라고도 불림  예시  숫자 손글씨 이미지(0~9)를 분류하는 문제 → 10개 클래스 분류   2. 사이킷런의 다중 클래스 분류기     유형 분류기 예시   ✅ 다중 클래스 기본 지원 LogisticRegression, RandomForestClassifier, GaussianNB   ⚠️ 이진 분류만 지원 SGDClassifier, SVC         → 이진 분류만 가능한 분류기를 사용하는 경우, 여러 개의 이진 분류기를 조합하여 다중 분류 문제를 해결해야 함    3. 이진 분류기를 활용한 다중 클래스 분류 전략 1) OvR (One-vs-Rest / One-vs-All)    각 클래스를 다른 모든 클래스와 구분하는 이진 분류기를 하나씩 만듦 총 N개의 분류기 필요 (N = 클래스 수)  예시  숫자 0~9 분류: 0-detector, 1-detector, ..., 9-detector → 총 10개 새로운 샘플에 대해 가장 높은 decision score를 낸 분류기의 클래스로 예측   2) OvO (One-vs-One)    클래스들 간 모든 쌍 조합마다 이진 분류기를 만듦 총 N(N-1)/2개의 분류기 필요  예시  숫자 0~9 분류 → 0-1, 0-2, ..., 8-9 → 총 45개 새로운 샘플에 대해 45개 분류기 실행 → 가장 많이 예측된 클래스를 최종 예측   4. OvR vs OvO     항목 OvR OvO   분류기 개수 N N(N-1)/2   훈련 데이터 전체 데이터 사용 각 분류기는 두 클래스 데이터만 사용   장점 구현 단순, 효율적 훈련셋이 작을수록 빠름 (SVM에 유리)   단점 클래스 간 경계가 모호할 수 있음 분류기 수가 많아짐            SVM(Support Vector Machine)처럼 훈련 데이터 크기에 민감한 알고리즘은 OvO가 유리함 대부분의 경우에는 OvR을 기본 전략으로 사용     5. SVM(Support Vector Machine) 분류기 예제   from sklearn.svm import SVC svm_clf = SVC() svm_clf.fit(X_train[:2000], y_train[:2000])    기본적으로 OvO 전략을 사용 (총 45개 이진 분류기) 새로운 샘플 some_digit을 예측하면, 45개 분류기의 결과를 바탕으로 최종 클래스를 결정 클래스 정보는 .classes_ 속성에 저장됨   6. OvO 또는 OvR 전략 강제 적용 방법  사이킷런에서는 기본 전략 외에 명시적으로 전략을 설정할 수 있음    from sklearn.multiclass import OneVsOneClassifier, OneVsRestClassifier # OvO 전략 적용 ovo_clf = OneVsOneClassifier(SVC()) ovo_clf.fit(X_train, y_train) # OvR 전략 적용 ovr_clf = OneVsRestClassifier(SVC()) ovr_clf.fit(X_train, y_train)      7. SGDClassifier 사용 시  SGDClassifier는 이진 분류만 지원 다중 클래스 데이터로 훈련시키면 내부적으로 OvR 전략 적용    from sklearn.linear_model import SGDClassifier sgd_clf = SGDClassifier() sgd_clf.fit(X_train, y_train) sgd_clf.predict([some_digit])    decision_function()으로 클래스별 점수를 확인 가능 가장 높은 점수를 가진 클래스가 예측값이 됨   8. 성능 평가 방법 1) 교차 검증 (Cross-validation)  분류기의 성능을 일반화된 방식으로 평가 StratifiedKFold 등 계층적 분할이 유리    from sklearn.model_selection import cross_val_score cross_val_score(sgd_clf, X_train, y_train, cv=3, scoring="accuracy")     2) 스케일링  StandardScaler()로 특성 스케일링 → 성능 향상에 큰 도움    from sklearn.preprocessing import StandardScaler scaler = StandardScaler() X_train_scaled = scaler.fit_transform(X_train.astype(np.float64))    9. 정리     항목 내용   다중 클래스 분류기 3개 이상 클래스를 예측하는 분류기   대표 모델 LogisticRegression, RandomForest, GaussianNB   전략 OvR(One-vs-Rest), OvO(One-vs-One)   OvO가 유리한 경우 SVM 같이 훈련셋 크기에 민감한 모델   교차검증 cross_val_score()로 정확도 평가   스케일링 StandardScaler()로 전처리 권장
