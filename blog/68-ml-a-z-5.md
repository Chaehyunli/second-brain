---
title: "[기계학습] ML 프로젝트 A-Z까지 ( 5 )"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: [blog, technical-writing]
category: "AI(ML & DL)"
published: 2025-05-05
source_url: https://ch010104.tistory.com/68
archive_method: Tistory sitemap + HTML content extraction
---

# [기계학습] ML 프로젝트 A-Z까지 ( 5 )

> 원문: https://ch010104.tistory.com/68

## 본문

1. 변환기란?  변환기(Transformer)는 입력 데이터를 분석, 변환, 정규화, 인코딩 등 다양한 방식으로 전처리하여 머신러닝 모델이 학습할 수 있도록 도와주는 객체 사이킷런(sklearn)에서는 fit()과 transform() 메서드를 가지는 객체를 변환기로 간주   2. 변환기 사용 시 주의사항  fit() 함수는 훈련셋에만 사용해야 함→ 테스트셋에는 절대 사용 ❌ transform() 함수는 훈련셋, 테스트셋 모두에 사용 가능→ 단, fit()이 선행되어야 함 일반적으로는 훈련셋을 이용해 변환기를 학습(fit)한 후, 해당 변환기를 사용해 전체 데이터(훈련+테스트)를 변환(transform)하는 방식으로 사용   3. 변환기 구현 방법 ✅ 방법 1: FunctionTransformer 사용  간단한 변환을 할 경우 적합 예시 1: 로그 변환 (heavy tail 처리) 예시 2: 두 특성의 비율 계산 예시 3: 특정 지점과의 거리 기반 유사도 추가→ rbf_kernel()을 사용해 특정 지점과의 거리 기반 유사도를 새 특성으로 추가    from sklearn.preprocessing import FunctionTransformer import numpy as np log_transformer = FunctionTransformer(np.log1p, validate=True)         ✅ 방법 2: 사용자 정의 클래스 직접 구현  복잡한 변환이나 학습이 필요한 경우 예시: KMeans 클러스터링을 통해 각 샘플과 클러스터 중심의 유사도 계산    from sklearn.base import BaseEstimator, TransformerMixin from sklearn.cluster import KMeans from sklearn.metrics.pairwise import rbf_kernel class ClusterSimilarity(BaseEstimator, TransformerMixin): def __init__(self, n_clusters=10, gamma=1.0, random_state=None): self.n_clusters = n_clusters self.gamma = gamma self.random_state = random_state def fit(self, X, y=None, sample_weight=None): self.kmeans_ = KMeans(n_clusters=self.n_clusters, random_state=self.random_state) self.kmeans_.fit(X, sample_weight=sample_weight) return self def transform(self, X): return rbf_kernel(X, self.kmeans_.cluster_centers_, gamma=self.gamma)    4. 변환 파이프라인(Pipeline)의 구성   from sklearn.pipeline import Pipeline from sklearn.impute import SimpleImputer from sklearn.preprocessing import StandardScaler num_pipeline = Pipeline([ ('impute', SimpleImputer()), ('scale', StandardScaler()) ])    마지막 객체만 predictor, 나머지는 모두 transformer여야 함 fit(), transform(), fit_transform() 모두 가능   5. ColumnTransformer로 특성별 전처리 ColumnTransformer를 사용하면 수치형과 범주형 특성을 따로 변환기로 처리 가능 from sklearn.compose import ColumnTransformer from sklearn.preprocessing import OneHotEncoder from sklearn.impute import SimpleImputer from sklearn.pipeline import Pipeline cat_pipeline = Pipeline([ ('impute', SimpleImputer(strategy='most_frequent')), ('encode', OneHotEncoder()) ]) full_pipeline = ColumnTransformer([ ('num', num_pipeline, make_column_selector(dtype_include=np.number)), ('cat', cat_pipeline, make_column_selector(dtype_include=object)) ])     🎯 간편 생성 함수  make_pipeline(): 이름 자동 생성 (e.g., "standardscaler") make_column_transformer(): column transformer도 이름 자동 생성 가능 make_column_selector(): 자동으로 수치형/범주형 컬럼 선택 가능
