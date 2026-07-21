---
title: "[STUDYING] 4. 회귀실습 - UCI Bike Sharing Dataset의 일별 자료"
created: 2026-07-21
updated: 2026-07-21
type: blog-post
tags: ["blog", "technical-writing"]
category: "STUDYING"
published: 2026-07-21
source_url: https://ch010104.tistory.com/310
---
# [STUDYING] 4. 회귀실습 - UCI Bike Sharing Dataset의 일별 자료

## 원문

https://ch010104.tistory.com/310

## 노트 유형

`tutorial`

## 학습 목표 및 맥락

이 실습은 UCI Bike Sharing Dataset의 일별 자료로 cnt(일별 총대여량)를 예측하는 다중선형회귀 분석이다. 문제 정의 → EDA·전처리 → 단순·다중선형회귀 비교 → 회귀계수·유의성 해석 → 운영 인사이트 순서로 진행한다.

목표: 날씨, 계절, 근무일 등의 요인으로 일별 공유 자전거 대여 수요를 예측하고, 자전거 재배치와 운영 인력 계획에 활용할 수 있는 요인을 확인한다.

## 원문 기반 학습 정리

### 상세 학습 노트

이 실습은 UCI Bike Sharing Dataset의 일별 자료로 cnt(일별 총대여량)를 예측하는 다중선형회귀 분석이다. 문제 정의 → EDA·전처리 → 단순·다중선형회귀 비교 → 회귀계수·유의성 해석 → 운영 인사이트 순서로 진행한다.

### 1. 분석 문제와 변수 설계

목표: 날씨, 계절, 근무일 등의 요인으로 일별 공유 자전거 대여 수요를 예측하고, 자전거 재배치와 운영 인력 계획에 활용할 수 있는 요인을 확인한다.

종속변수: cnt.

연속형 독립변수: temp, hum, windspeed.

범주형 독립변수: season, weathersit, holiday, workingday, yr.

instant는 행 식별자이므로 제외했다. atemp는 temp와 정보가 겹쳐 다중공선성 가능성이 있어 제외했다. mnth, weekday는 각각 season, workingday와 일부 정보가 중복되므로 이번 모델에서는 제외했다.

### 데이터 누수 방지

casual + registered = cnt가 모든 행에서 성립한다. 따라서 casual, registered를 입력 변수로 쓰면 예측 시점에 알 수 없는 종속변수 구성 정보를 미리 주는 데이터 누수가 된다.

```text
cnt_check = (df["cnt"] == df["casual"] + df["registered"]).all()
print("cnt = casual + registered가 모든 행에서 성립하는가?", cnt_check)
```

### 2. 데이터 품질과 탐색적 분석

원본 day.csv는 731개 행, 16개 변수로 구성된다.

결측치와 중복 행은 모두 없어서 별도의 제거·대체는 수행하지 않았다.

일별 평균 대여량은 약 4,504대, 중앙값은 4,548대, 최솟값은 22대, 최댓값은 8,714대다. 왜도가 0에 가까우며 극단적인 이상치가 두드러지지 않아 cnt의 로그 변환·이상치 제거는 하지 않았다.

계절별 평균 대여량은 가을 약 5,644대, 여름 약 4,992대, 겨울 약 4,728대, 봄 약 2,604대 순이다.

날씨별 평균은 맑은 날 약 4,877대, 흐림·안개 약 4,036대, 약한 비·눈 약 1,803대로 감소한다.

temp와 cnt의 상관계수는 약 0.628로 양의 관계를 보였다. windspeed는 약 -0.23, hum은 약 -0.10으로 나타났다. 상관계수만으로 원인을 확정하지 않고 산점도와 다른 변수의 영향을 함께 확인해야 한다.

### 3. 범주형 전처리와 기준 범주

숫자로 저장된 범주형 변수는 크기·간격을 뜻하지 않으므로 원-핫 인코딩한다. drop_first=True로 기준 범주 하나를 제외해 절편과 더미변수 사이의 완전한 선형관계(더미변수 함정)를 피한다.

```text
categorical_columns = [
    "season", "weathersit", "holiday", "workingday", "yr"
]
y = analysis_df["cnt"]
X_original = analysis_df.drop(columns="cnt")
X = pd.get_dummies(
    X_original,
    columns=categorical_columns,
    drop_first=True,
    dtype=int
)
```

기준 범주는 봄(season=1), 맑은 날(weathersit=1), 비공휴일(holiday=0), 비근무일(workingday=0), 2011년(yr=0)이다. 전처리 뒤 731개 관측치와 11개 독립변수를 사용한다.

### 4. 단순선형회귀와 다중선형회귀 비교

먼저 temp만으로 단순선형회귀를 만들고, 이어서 습도·풍속·계절·날씨·공휴일·근무일·연도를 포함한 다중선형회귀를 구축한다. 전체 데이터를 80:20으로 나누어 학습 584개, 테스트 147개를 사용하며 random_state=42로 재현성을 확보한다.

```text
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

multiple_model = LinearRegression()
multiple_model.fit(X_train, y_train)
multiple_pred = multiple_model.predict(X_test)

multiple_r2 = r2_score(y_test, multiple_pred)
multiple_rmse = np.sqrt(mean_squared_error(y_test, multiple_pred))
multiple_mae = mean_absolute_error(y_test, multiple_pred)
```

R²는 일별 대여량 변동의 설명력이다.

RMSE는 큰 예측 오차에 더 민감한 오차 지표다.

MAE는 평균적으로 몇 대를 틀리는지 대수 단위로 해석한다.

원문 분석에서는 여러 환경 요인을 함께 쓴 다중선형회귀가 기온만 사용한 단순선형회귀보다 더 높은 R²와 더 낮은 RMSE·MAE를 보여 최종 모델로 선택됐다.

### 5. 예측 경향과 회귀계수 해석

실제값·예측값 산점도에서 대각선에 가까울수록 예측이 정확하다. 저수요(3,000대 이하), 중수요(3,001~6,000대), 고수요(6,000대 초과)로 나누어 평균 예측 오차를 확인했다.

저수요 구간은 실제보다 평균 약 370대 과대 예측했다.

중수요 구간의 평균 오차는 약 72대였다.

고수요 구간은 실제보다 평균 약 590대 과소 예측했다.

따라서 고수요가 예상되는 날에는 모델 예측값만 사용하지 말고 여유 자전거와 운영 인력을 확보해야 한다.

scikit-learn 모델은 p-value를 제공하지 않으므로, 학습 데이터에 한해 statsmodels OLS를 별도로 적합해 회귀계수·p-value·95% 신뢰구간을 확인한다.

```text
X_train_sm = sm.add_constant(X_train.astype(float))
ols_model = sm.OLS(y_train.astype(float), X_train_sm).fit()

coefficient_result = pd.DataFrame({
    "회귀계수": ols_model.params,
    "p-value": ols_model.pvalues,
    "신뢰구간_하한": ols_model.conf_int()[0],
    "신뢰구간_상한": ols_model.conf_int()[1]
})
```

다른 조건이 같을 때 원문 결과는 다음과 같이 해석했다.

temp가 0.1 증가하면 약 524대 증가, 실제 기온이 1°C 상승하면 약 128대 증가.

hum이 0.1 증가하면 약 115대 감소.

windspeed가 0.1 증가하면 약 252대 감소.

흐림·안개(weathersit_2)는 맑은 날보다 약 488대 감소, 약한 비·눈(weathersit_3)은 약 1,748대 감소.

공휴일은 약 546대 감소, 근무일은 약 152대 증가.

2012년은 다른 조건이 같을 때 2011년보다 약 1,992대 많게 나타났다.

p-value가 0.05보다 작으면 통계적으로 유의한 관계로 보지만, 이것이 직접적 인과관계를 증명하는 것은 아니다. 변수 단위·기준 범주·관측되지 않은 요인을 함께 고려해야 한다.

### 6. 표준화 계수와 운영 인사이트

단위가 다른 연속형·범주형 변수의 상대적 영향력을 비교하기 위해 독립변수와 종속변수를 표준화했다. 영향력이 큰 변수는 yr_1, temp, 계절 변수, 날씨 상태 변수 순으로 나타났다. 다만 두 연도 자료만으로 서비스 성장의 지속성을 단정할 수는 없다.

기온이 높고 날씨가 맑은 날에는 주요 대여소의 자전거와 재배치 인력을 사전 확대한다.

비·눈이 예상되는 날에는 재배치 수요 감소를 고려하고, 정비 업무 비중을 조정한다.

고수요 구간의 과소 예측을 보완할 안전 재고와 추가 인력을 확보한다.

### 7. 한계와 다음 검증

이 자료는 2011~2012년 미국 워싱턴 D.C. 데이터이므로 다른 지역·현재 시점에 그대로 일반화하기 어렵다. 선형성 가정, 지역 행사·강수량·대여소 위치 같은 누락 변수, 무작위 학습·테스트 분할의 한계가 있다. 미래 수요 예측으로 확장할 때는 과거로 학습하고 이후 기간으로 평가하는 시간 순서 기반 검증을 고려한다.

### 원본 실습 파일

7반6조.ipynb 0.66MB

## 관련 글

- [[blog/STUDYING/index|STUDYING]]

## 학습 기준본

- [[notion/SKALA/7-20 데이터 분석 개요 및 기초통계 2/7-20 데이터 분석 - 회귀 실습|SKALA 상세 학습 노트]]
