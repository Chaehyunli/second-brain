---
title: "[기계학습] 선형 회귀 실습 (1인당 GDP와 삶의 만족도 예측) ( 1 )"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "AI", "CS", "Python"]
category: "AI(ML & DL)"
published: 2025-04-11
source_url: https://ch010104.tistory.com/54
---

# [기계학습] 선형 회귀 실습 (1인당 GDP와 삶의 만족도 예측) ( 1 )

## 원문

https://ch010104.tistory.com/54

## 노트 유형

`tutorial`

## 학습 목표 및 맥락

이 실습은 Aurélien Géron의 『Hands-On Machine Learning(3rd Ed.)』 기반으로 진행되며, 2020년도 OECD 국가들의 1인당 GDP와 삶의 만족도 데이터를 활용하여 선형 회귀 모델을 훈련

문제 정의 : 어떤 국가의 1인당 GDP가 주어졌을 때, 해당 국가의 삶의 만족도(Life Satisfaction) 를 예측하는 선형 회귀 모델을 구현

## 원문 기반 학습 정리

이 실습은 Aurélien Géron의 『Hands-On Machine Learning(3rd Ed.)』 기반으로 진행되며, 2020년도 OECD 국가들의 1인당 GDP와 삶의 만족도 데이터를 활용하여 선형 회귀 모델을 훈련

문제 정의 : 어떤 국가의 1인당 GDP가 주어졌을 때, 해당 국가의 삶의 만족도(Life Satisfaction) 를 예측하는 선형 회귀 모델을 구현

### 🔄 선형 회귀 모델 구현 단계

선형 회귀 모델을 구현하는 과정은 다음의 5단계로 구성됨.

### 1. 문제 정의

OECD 회원국의 1인당 GDP를 입력으로 받아, 삶의 만족도(Life Satisfaction) 를 예측하는 머신러닝 모델을 구축

### 2. 데이터 수집

이번 실습에서는 아래 두 개의 공개 데이터를 사용

gdp_per_capita.csv : IMF 제공, 국가별 1인당 GDP 데이터

oecd_bli.csv : OECD 제공, 국가별 삶의 만족도 지표 포함 ('더 나은 삶의 지수')

🔍 최종 목표 테이블 (예시)

이 표는 원본 데이터가 아닌, 원시 CSV 데이터를 적재하고 정제 및 전처리한 결과물 이 과정이 머신러닝 모델의 정확도에 큰 영향을 주므로, 데이터 전처리는 모델 훈련보다 중요

### 3. 데이터 적재, 정제, 전처리

데이터 적재 (Data Loading): 서버 또는 로컬에서 CSV 파일을 불러오는 작업

데이터 정제 (Data Cleaning): 오류, 누락값(NaN), 이상치 등을 제거하거나 수정

데이터 전처리 (Data Preprocessing): 정제된 데이터를 머신러닝 모델에 맞는 형식으로 변환 (필드명 수정, 병합, 인덱싱 등)

### ⚙️ 실습 환경 설정

1. Python 버전 체크

```text
import sys
assert sys.version_info >= (3, 7), "Python 3.7 이상이어야 함"
```

2. 필수 모듈 불러오기

```python
import numpy as np
import pandas as pd
```

3. 실행 결과 고정 (랜덤 시드)

```text
np.random.seed(42)
```

4. 그래프 설정

```text
import matplotlib.pyplot as plt

plt.rc('font', size=12)
plt.rc('axes', labelsize=14, titlesize=14)
plt.rc('legend', fontsize=12)
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)
```

### 데이터 준비

1. 1인당 GDP 데이터 적재

```text
datapath = "https://github.com/ageron/data/raw/main/lifesat/"

gdp_per_capita = pd.read_csv(
    datapath + "gdp_per_capita.csv",
    thousands='.',           # 천 단위 구분자
    encoding='latin1',       # 특수 문자 처리
    na_values="n/a"          # 결측치 처리
)
```

▶️ 출력 예시

2. 2020년 데이터만 필터링

```text
mask_gdp_2020 = gdp_per_capita["Year"] == 2020
gdp_per_capita = gdp_per_capita[mask_gdp_2020]
```

3. 불필요한 열 삭제

```text
gdp_per_capita.drop(columns=['Code', 'Year'], inplace=True)
```

4. 국가명 'South Korea' → 'Korea'로 변경

```text
gdp_per_capita.loc[gdp_per_capita['Entity'] == 'South Korea', 'Entity'] = 'Korea'
```

5. 컬럼 이름 변경 및 인덱스 설정

```text
gdp_per_capita.columns = ['Country', 'GDP per capita (USD)']
gdp_per_capita.set_index('Country', inplace=True)
```

▶️ 출력 예시

```text
gdp_per_capita.loc['Korea']

# GDP per capita (USD)    27195.0
# Name: Korea, dtype: float64
```

### OECD 삶의 만족도 데이터 적재

1. CSV 적재

```text
oecd_bli = pd.read_csv(datapath + "oecd_bli.csv", thousands=',')
```

2. 데이터 구조 확인

```text
oecd_bli.shape
# 출력 결과: (2369, 17)
```

```text
oecd_bli.head(3)
```

3. 'Life satisfaction' 여부 및 수 확인

```text
oecd_bli.Indicator.unique()
# 출력: 24개 지표

'Life satisfaction' in oecd_bli.Indicator.unique()
# 출력: True
```

```text
oecd_bli[oecd_bli.Indicator == 'Life satisfaction'].shape
# 출력: (168, 17) → 중복 포함
```

## 관련 글

- [[blog/AI(ML & DL)/index|AI(ML & DL)]]
- [[blog/AI(ML & DL)/기계학습- 선형 회귀 실습 (1인당 GDP와 삶의 만족도 예측) ( 2 )|[기계학습] 선형 회귀 실습 (1인당 GDP와 삶의 만족도 예측) ( 2 )]]
- [[blog/AI(ML & DL)/기계학습- Python Pandas 란-- ( 3 )|[기계학습] Python Pandas 란?? ( 3 )]]
- [[blog/AI(ML & DL)/기계학습- Python Pandas 란 -- ( 2 )|[기계학습] Python Pandas 란 ?? ( 2 )]]
