---
title: "[기계학습] 선형 회귀 실습 (1인당 GDP와 삶의 만족도 예측) ( 2 )"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "AI", "CS", "Python"]
category: "AI(ML & DL)"
published: 2025-04-14
source_url: https://ch010104.tistory.com/57
---

# [기계학습] 선형 회귀 실습 (1인당 GDP와 삶의 만족도 예측) ( 2 )

## 원문

https://ch010104.tistory.com/57

## 노트 유형

`tutorial`

## 학습 목표 및 맥락

원문에서 추출한 학습·구현 내용을 구조화했습니다.

## 원문 기반 학습 정리

### 1. OECD 삶의 만족도 데이터

```text
oecd_bli = pd.read_csv(datapath + "oecd_bli.csv", thousands=",")
```

2. INEQUALITY 값 확인

```text
oecd_bli.INEQUALITY.unique()

# array(['TOT', 'MN', 'WMN', 'HGH', 'LW'], dtype=object)
```

### 3. 각 기준별 행 개수 확인

```text
arr1 = oecd_bli.INEQUALITY.unique()
for ineq in arr1:
    print(f'{ineq:>3} : {(oecd_bli.INEQUALITY == ineq).sum()} rows')

# TOT : 911 rows
#  MN : 578 rows
# WMN : 578 rows
# HGH : 164 rows
#  LW : 138 rows
```

### 4. 전체 인구 기준(TOT)만 필터링

```text
oecd_bli = oecd_bli[oecd_bli.INEQUALITY == 'TOT']

oecd_bli.shape
# (911, 17)
```

### 5. Pivot 테이블 생성: 행(Country), 열(Indicator), 값(Value)

```text
oecd_bli = oecd_bli.pivot(index='Country', columns='Indicator', values='Value')

oecd_bli.shape
# (41, 24)

oecd_bli.head()
# Indicator	Air pollution	Employment rate	Life satisfaction	...
# Australia	13.97	73.57	7.3	...
# Austria	14.00	71.23	6.9	...
# Belgium	14.03	62.10	6.9	...
# Canada	13.80	72.56	7.4	...
# Chile	16.10	62.53	6.4	...

oecd_bli.loc["Korea"]
# Air pollution                24.3
# Employment rate              66.6
# Life satisfaction             5.8
# ... 생략 ...

oecd_bli["Life satisfaction"].head()
# Country
# Australia    7.3
# Austria      6.9
# Belgium      6.9
# Canada       7.4
# Chile        6.4
# Name: Life satisfaction, dtype: float64
```

### 데이터 병합

```text
oecd_country_stats = pd.merge(left=gdp_per_capita['GDP per capita (USD)'],
                              right=oecd_bli['Life satisfaction'],
                              left_index=True, right_index=True)

# left_index=True, right_index=True: 국가명을 기준으로 병합
# 공통된 국가만 병합되며, 최종적으로 OECD 국가 중심의 테이블이 만들어짐

oecd_country_stats.shape
# (37, 2)

oecd_country_stats.head()
# Country	GDP per capita (USD)	Life satisfaction
# Australia	50967.419	7.3
# Austria	49860.144	6.9
# Belgium	45354.408	6.9
# Canada	44800.084	7.4
# Chile	24458.532	6.4

oecd_country_stats.sort_values(by='GDP per capita (USD)', inplace=True)
# GDP per capita (USD) 를 기준으로 오름차순으로 정렬
# --> 이 데이터 셋을 통해 선형 모델의 학습을 함
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### 훈련용 데이터셋 구성

제외할 9개 국가: 극단적 GDP

```text
omitted_indices = [0, 1, 2, 3, 4, 33, 34, 35, 36]
kept_indices = list(set(range(37)) - set(omitted_indices))

missing_data = oecd_country_stats.iloc[omitted_indices]
sample_data = oecd_country_stats.iloc[kept_indices]

sample_data.shape
# (28, 2)
```

### 모델 훈련

1) 선형 회귀 모델 선언 및 훈련

```text
from sklearn import linear_model

lin1 = linear_model.LinearRegression()

Xsample = sample_data['GDP per capita (USD)'].to_numpy().reshape(28, 1)
Ysample = sample_data['Life satisfaction'].to_numpy().reshape(28, 1)

lin1.fit(Xsample, Ysample)
```

2) 학습된 모델 파라미터 확인

```text
t0 = lin1.intercept_[0]
t1 = lin1.coef_[0][0]

print(f"절편: {t0}")
print(f"기울기: {t1}")

# 절편: 3.7317217296614067
# 기울기: 6.759315474700707e-05
```

### 📈 시각화: 예측 선 그리기

```text
sample_data.plot(kind='scatter', x="GDP per capita (USD)", y='Life satisfaction', figsize=(5,3))
plt.xlabel("GDP per capita (USD)")
plt.axis([10000, 70000, 0, 10])

X = np.linspace(0, 70000, 1000)
plt.plot(X, t0 + t1 * X, "b")

plt.text(15000, 3.1, r"$\theta_0$ = {:.2f}".format(t0), fontsize=14, color="b")
plt.text(15000, 2.2, r"$\theta_1$ = {:.2e}".format(t1), fontsize=14, color="b")

plt.show()
```

### 모델 활용 - 예측

1) 키프러스(Cyprus)의 삶의 만족도 예측

```text
cyprus_gdp = gdp_per_capita.loc['Cyprus']['GDP per capita (USD)']
cyprus_predicted = lin1.predict([[cyprus_gdp]])

print(f"예측된 삶의 만족도: {cyprus_predicted[0][0]:.2f}")

# 예측된 삶의 만족도: 6.28
```

### 🔄 훈련 데이터 추가 실험

9개 국가를 포함한 전체 데이터로 훈련:

```text
full_data = pd.concat([sample_data, missing_data])
X_full = full_data[["GDP per capita (USD)"]].values
y_full = full_data["Life satisfaction"].values

from sklearn.linear_model import LinearRegression
model_full = LinearRegression()
model_full.fit(X_full, y_full)

t0_full = model_full.intercept_
t1_full = model_full.coef_[0]
```

전체 그래프 그리기

```text
sample_data.plot(kind='scatter', x="GDP per capita (USD)", y="Life satisfaction", figsize=(8, 3))
plt.axis([0, 120000, 0, 10])

# 기존 모델: 파란 점선
plt.plot(X, t0 + t1*X, "b:", label="Model w/o 9 countries")

# 새 모델: 검정 실선
plt.plot(X, t0_full + t1_full * X, "k-", label="Model w/ all countries")

plt.xlabel("GDP per capita (USD)")
plt.ylabel("Life satisfaction")
plt.legend()
plt.show()
```

## 관련 글

- [[blog/AI(ML & DL)/index|AI(ML & DL)]]
- [[blog/AI(ML & DL)/기계학습- 선형 회귀 실습 (1인당 GDP와 삶의 만족도 예측) ( 1 )|[기계학습] 선형 회귀 실습 (1인당 GDP와 삶의 만족도 예측) ( 1 )]]
- [[blog/AI(ML & DL)/기계학습- Python Pandas 란-- ( 3 )|[기계학습] Python Pandas 란?? ( 3 )]]
- [[blog/AI(ML & DL)/기계학습- Python Pandas 란 -- ( 2 )|[기계학습] Python Pandas 란 ?? ( 2 )]]
