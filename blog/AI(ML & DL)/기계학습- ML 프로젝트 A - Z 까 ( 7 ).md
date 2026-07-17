---
title: "[기계학습] ML 프로젝트 A - Z 까 ( 7 )"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "AI", "CS"]
category: "AI(ML & DL)"
published: 2025-05-17
source_url: https://ch010104.tistory.com/73
---

# [기계학습] ML 프로젝트 A - Z 까 ( 7 )

## 원문

https://ch010104.tistory.com/73

## 노트 유형

`project`

## 배경·목표·적용 맥락

모델 학습에는 **하이퍼파라미터(Hyperparameter)**라는 설정값이 있음.

모델의 결과 예측에 영향을 많이는 주는 파라미터가 어떠한 것인지 파악하는 것이 모델의 성능 향상으로 이어짐.

## 구현·의사결정·결과

### 1. 왜 하이퍼파라미터 튜닝이 필요한가?

모델 학습에는 **하이퍼파라미터(Hyperparameter)**라는 설정값이 있음.

이는 학습 전에 직접 지정해야 하며, 성능에 큰 영향을 줌.

모델의 결과 예측에 영향을 많이는 주는 파라미터가 어떠한 것인지 파악하는 것이 모델의 성능 향상으로 이어짐.

예를 들어 랜덤 포레스트에서는:

max_features: 각 노드에서 고려할 최대 특성 수

n_estimators: 사용할 트리 수

등이 있음.

### 2. Grid Search (그리드 탐색)

1) 기본 개념

하이퍼파라미터의 모든 조합을 체계적으로 탐색하여 최적 조합을 찾는 방식

2) 예제 코드

```text
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

param_grid = {
    'preprocessing__geo__n_clusters': [5, 8, 10],
    'random_forest__max_features': [4, 6, 8]
}

grid_search = GridSearchCV(full_pipeline_with_model,
                           param_grid=param_grid,
                           cv=3,
                           scoring='neg_mean_squared_error',
                           return_train_score=True)
grid_search.fit(housing_prepared, housing_labels)
```

🔍 preprocessing__geo__n_clusters: 파이프라인 내 ClusterSimilarity 변환기의 클러스터 수 🔍 random_forest__max_features: 랜덤 포레스트가 각 분할마다 고려할 특성 수

3) 결과 확인

```text
grid_search.best_params_
```

```text
{'preprocessing__geo__n_clusters': 10, 'random_forest__max_features': 8}
```

### 3. Randomized Search (랜덤 탐색)

1) 기본 개념

모든 조합을 탐색하지 않고 지정한 수만큼 랜덤하게 샘플링

조합이 많거나 하이퍼파라미터가 연속적인 경우에 적합

2) 예제 코드

```text
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint

param_distribs = {
    'preprocessing__geo__n_clusters': randint(low=3, high=15),
    'random_forest__max_features': randint(low=2, high=10),
}

rnd_search = RandomizedSearchCV(full_pipeline_with_model,
                                param_distributions=param_distribs,
                                n_iter=10,
                                cv=3,
                                scoring='neg_mean_squared_error',
                                random_state=42)
rnd_search.fit(housing_prepared, housing_labels)
```

3) 결과 확인

```text
rnd_search.best_params_
```

```text
{'preprocessing__geo__n_clusters': 9, 'random_forest__max_features': 7}
```

### 4. 특성 중요도 분석 (Feature Importance)

튜닝된 모델을 바탕으로 어떤 특성이 예측에 중요한지 확인

```text
feature_importances = rnd_search.best_estimator_.named_steps["random_forest"].feature_importances_

extra_attribs = ["rooms_per_household", "population_per_household", "bedrooms_per_room"]
cat_encoder = full_pipeline_with_model.named_steps["preprocessing"].named_transformers_["cat"]
cat_one_hot_attribs = list(cat_encoder.get_feature_names_out())
attributes = num_attribs + extra_attribs + cat_one_hot_attribs

sorted(zip(feature_importances, attributes), reverse=True)
```

1) 출력 예시

```text
[(0.314, 'median_income'),
 (0.112, 'ocean_proximity_INLAND'),
 (0.087, 'bedrooms_per_room'),
 (0.075, 'longitude'),
 ... ]
```

median_income과 ocean_proximity_INLAND가 예측에 가장 큰 영향을 줌 중요도가 낮은 특성은 제거하여 모델 간결화 가능

### 5. 테스트셋으로 최종 모델 평가

1) 최종 모델로 예측 수행

```text
final_model = rnd_search.best_estimator_

X_test = strat_test_set.drop("median_house_value", axis=1)
y_test = strat_test_set["median_house_value"]

X_test_prepared = final_model.named_steps["preprocessing"].transform(X_test)

final_predictions = final_model.named_steps["random_forest"].predict(X_test_prepared)
```

2) RMSE 계산

```text
from sklearn.metrics import mean_squared_error
final_mse = mean_squared_error(y_test, final_predictions)
final_rmse = final_mse ** 0.5

print(f"최종 RMSE: {final_rmse:,.2f}")
```

3) 출력 결과 예시:

```text
최종 RMSE: 41,424.40
```

### 6. 정리 및 인사이트

인사이트

median_income은 예측에 절대적인 영향을 주는 주요 변수

중요도가 낮은 특성 제거 → 모델 단순화 및 성능 유지 가능

## 관련 글

- [[blog/AI(ML & DL)/index|AI(ML & DL)]]
- [[blog/AI(ML & DL)/기계학습- ML 프로젝트 - 분류 (Classification) 모델|[기계학습] ML 프로젝트 - 분류 (Classification) 모델]]
- [[blog/AI(ML & DL)/기계학습- ML 프로젝트 A - Z 까지 ( 6 )|[기계학습] ML 프로젝트 A - Z 까지 ( 6 )]]
- [[blog/AI(ML & DL)/기계학습- ML 프로젝트 A-Z까지 ( 5 )|[기계학습] ML 프로젝트 A-Z까지 ( 5 )]]
