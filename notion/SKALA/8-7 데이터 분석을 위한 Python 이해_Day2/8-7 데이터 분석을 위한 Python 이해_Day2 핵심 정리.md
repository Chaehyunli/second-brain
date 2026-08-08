---
title: "[8/7] 데이터 분석을 위한 Python 이해_Day2_핵심 정리"
notion_page_id: "3b51d84b-f68e-8048-bf90-ce204a60f730"
source_url: "https://app.notion.com/p/3b51d84bf68e8048bf90ce204a60f730"
synced_at: "2026-08-08T23:32:50+09:00"
content_sha256: "a84b8840a6ac74e41f7c84e08c5d32e41cc5db508f8ff349fe1eac4a04d77b95"
tags: [notion, skala, learning, python, data-analysis]
---

# [8/7] 데이터 분석을 위한 Python 이해_Day2_핵심 정리

[[notion/SKALA/index|SKALA 학습 노트]]

> 원문: [Notion 페이지](https://app.notion.com/p/3b51d84bf68e8048bf90ce204a60f730) (2026-08-08 확인)

### Pandas — 데이터 분석 표준 라이브러리
Python 데이터 분석 생태계의 핵심 라이브러리로, 두 가지 핵심 자료구조(**DataFrame**, **Series**)를 중심으로 동작함. 내부적으로 NumPy 배열을 기반으로 구현되어 있어 연산 효율이 높음.
---
#### 핵심 자료구조
| 구조 | 차원 | 개념 | 특징 |
| --- | --- | --- | --- |
| **DataFrame** | 2D | 레이블이 붙은 표 | 행·열에 각각 인덱스/컬럼명 존재, 컬럼마다 다른 dtype 가능 |
| **Series** | 1D | 레이블이 붙은 배열 | DataFrame의 단일 컬럼에 해당, NumPy 배열 + 인덱스 구조 |
- DataFrame은 "엑셀 시트를 코드로 다루는 것"에 비유할 수 있음
- Series는 인덱스 기반으로 정렬·조인이 수월하다는 점이 강점임
---
### Pandas 2.x 핵심 변경사항
- **Copy-on-Write 기본 활성화**: 슬라이싱 결과를 수정해도 원본에 영향을 주지 않도록 동작 방식이 변경됨. 기존에 발생하던 `SettingWithCopyWarning` 문제를 구조적으로 해소함
- **ArrowDtype 지원**: Apache Arrow 기반의 dtype을 지원하여 대용량 데이터 처리 성능이 향상됨
- **메모리 효율 향상**: nullable 정수(`Int64` 등)·nullable 문자열 타입을 통해 결측값 처리가 더 명확해지고 메모리 사용이 줄어듦
---
### Pandas를 쓰기 적합한 상황
- **수백만 행 이하**의 EDA·탐색 분석 (그 이상은 Polars, Dask 등 고려)
- Matplotlib, Seaborn 등 **시각화 라이브러리 연동** 시
- **Jupyter 환경**에서 인터랙티브 탐색 위주로 작업할 때
---
### DataFrame 기초 EDA — 처음 마주칠 때
새 데이터셋을 처음 받으면 아래 순서로 구조를 파악하는 것이 기본 패턴임.
#### 주요 탐색 메서드
| 메서드 | 역할 |
| --- | --- |
| `df.shape` | (행 수, 열 수) 튜플 반환 |
| `df.info()` | 컬럼명·dtype·결측치 수·메모리 사용량 한눈에 확인 |
| `df.describe()` | 수치형 컬럼의 기술통계(평균·표준편차·사분위수 등) 자동 출력 |
| `df.describe(include='all')` | 범주형 컬럼까지 포함해 통계 출력 |
| `df.head()` / `df.tail()` / `df.sample()` | 상위·하위·무작위 행 샘플 확인 |
### 타입 확인 및 변환
- `df.dtypes`로 컬럼별 현재 dtype을 확인함
- 날짜 문자열은 `pd.to_datetime()`으로, 문자열 범주형은 `.astype('category')`로 변환해야 이후 연산과 메모리 효율이 올라감
```python
df['date']   = pd.to_datetime(df['date'])
df['region'] = df['region'].astype('category')
```
#### 컬럼 선택 및 조건 필터
```python
df['amount']              # 단일 컬럼 → Series 반환
df[['region', 'amount']]  # 복수 컬럼 → DataFrame 반환
df.loc[df['amount'] > 1000]  # 조건 필터 (loc 권장)
```
- 단일 컬럼은 `df['col']`, 복수 컬럼은 `df[&#91;'col1','col2'&#93;]`로 구분함
- 조건 필터는 `.loc[]` 안에 불리언 시리즈를 넣는 방식이 기본임
---
### 결측치·이상치 탐지 및 처리
데이터 품질 확인은 EDA 직후 반드시 수행해야 하는 단계임. 결측치의 **양**뿐 아니라 **발생 메커니즘**을 파악해야 올바른 처리 전략을 고를 수 있음.
#### 결측 메커니즘 분류
| 유형 | 의미 |
| --- | --- |
| **MCAR** (Missing Completely At Random) | 결측이 완전히 무작위 — 어떤 변수와도 무관 |
| **MAR** (Missing At Random) | 다른 관측 변수에 의존하지만, 결측된 값 자체와는 무관 |
| **MNAR** (Missing Not At Random) | 결측값 자체가 결측 여부에 영향 — 가장 처리 어려움 |
#### 결측치 파악 및 처리
python
```python
df.isna().sum()                      # 컬럼별 결측치 수
df.isna().sum() / len(df) * 100      # 결측 비율(%)
```
- 수치형 결측 → 중앙값(`median`) 대체가 이상치에 덜 민감함
- 범주형 결측 → 최빈값(`mode()[0]`) 대체
- 특정 컬럼에 결측이 있는 행만 제거할 때는 `dropna(subset=[...])` 사용
```python
df['amount'].fillna(df['amount'].median())
df['category'].fillna(df['category'].mode()[0])
df.dropna(subset=['date', 'amount'])
```
#### IQR 이상치 탐지·제거
**IQR(Interquartile Range)** = Q3 − Q1로, 데이터 중간 50% 범위를 뜻함. 이 범위에서 1.5배 벗어난 값을 이상치로 간주하는 것이 표준 방식임.
```python
Q1 = df['amount'].quantile(0.25)
Q3 = df['amount'].quantile(0.75)
IQR = Q3 - Q1
lo, hi = Q1 - 1.5*IQR, Q3 + 1.5*IQR

df_clean = df[df['amount'].between(lo, hi)]
print(f'이상치{(~df["amount"].between(lo,hi)).sum()}건 제거')
```
---
### groupby · pivot_table · merge — 집계와 결합
데이터를 그룹화하거나 여러 테이블을 합치는 핵심 연산임. SQL의 GROUP BY·PIVOT·JOIN과 직접 대응됨.
#### groupby + agg() — 다중 집계
`agg()` 안에서 `결과컬럼명=(원본컬럼, 집계함수)` 형식으로 여러 집계를 한 번에 정의할 수 있음. 이를 **named aggregation**이라 함.
```python
monthly = df.groupby('month').agg(
    revenue=('amount', 'sum'),
    cnt    =('amount', 'count'),
    avg    =('amount', 'mean')
).reset_index()
```
- `.reset_index()`를 붙이면 groupby 키가 일반 컬럼으로 내려와 이후 처리가 편해짐
#### pivot_table — 엑셀 피벗과 동일
`index`(행), `columns`(열), `values`(집계 대상)를 지정하면 엑셀 피벗 테이블과 동일한 2차원 요약 테이블을 생성함. `fill_value=0`으로 빈 칸을 0으로 채울 수 있음.
```python
pivot = df.pivot_table(
    values='amount', index='region',
    columns='category', aggfunc='sum',
    fill_value=0
)
```
#### merge vs join
| 구분 | 기준 | 사용 상황 |
| --- | --- | --- |
| `pd.merge()` | 컬럼 기준 (`on=`)<br>→ 인덱스는 고려 x | 공통 컬럼으로 두 DataFrame 결합 (SQL JOIN과 동일) |
| `df.join()` | 인덱스 기준 | 인덱스가 이미 맞춰진 경우의 간편 버전 |
`how='left'`/`'right'`/`'inner'`/`'outer'`로 JOIN 방식 지정 가능함.
```python
result = pd.merge(df_sales, df_cust,
                  on='customer_id', how='left')
```
---
### Pandas 2.x — Copy-on-Write(CoW) 동작 이해
Pandas 2.0부터 **CoW가 기본 활성화**됨. 슬라이싱으로 생성된 뷰(View)를 직접 수정하면 `ChainedAssignmentError`가 발생하므로, 명시적 복사 또는 안전한 수정 패턴을 사용해야 함.
#### 문제 상황 및 해결 패턴
```python
# ❌ Pandas 2.x에서 ChainedAssignmentError 발생
df_seoul = df[df['region'] == '서울']
df_seoul['amount'] = df_seoul['amount'] * 1.1  # 경고!
```
```python
# 방법 1: .copy() 명시 — 독립적인 복사본 생성
df_seoul = df[df['region'] == '서울'].copy()
df_seoul['amount'] *= 1.1
```
```python
# 방법 2: .loc 직접 수정 — 원본 DataFrame을 조건 지정해 수정
df.loc[df['region'] == '서울', 'amount'] *= 1.1
```
- 슬라이스 결과를 별도 변수로 저장한 뒤 수정하는 패턴은 CoW 하에서 안전하지 않음
- 원본을 유지하면서 파생 DataFrame을 만들 때는 `.copy()`, 원본 자체를 수정할 때는 `.loc` 직접 수정이 명확함
- 슬라이드 주석대로 **`assign()`**** + ****`query()`**** 체이닝 패턴**이 가장 안전하고 가독성도 좋음 — 불변 스타일로 새 DataFrame을 반환하므로 CoW 문제가 원천적으로 발생하지 않음
---
### apply vs vectorized 연산 — 성능 차이
같은 결과를 내더라도 **어떤 방식으로 연산하느냐**에 따라 속도 차이가 수십 배까지 벌어짐. 기본 원칙은 **`apply()`**** 대신 벡터화 연산을 우선 쓰는 것**임.
#### apply() vs 벡터화 연산
| 방식 | 동작 원리 | 속도 (100만 행 기준) |
| --- | --- | --- |
| `apply(lambda)` | Python 루프로 행/열 순회 | \~3.2s |
| `.str.upper()` 등 벡터화 | NumPy/C 레벨에서 일괄 처리 | \~0.08s (**약 40배 빠름**) |
```python
# ❌ 느린 방법
df['upper'] = df['name'].apply(lambda x: x.upper())

# ✅ 빠른 방법
df['upper'] = df['name'].str.upper()
```
- `apply()`는 복잡한 로직이 불가피할 때만 사용하고, 문자열·날짜·수치 연산은 전용 접근자를 쓰는 것이 원칙임
#### str 접근자 — 문자열 벡터화
- `.str.lower()`, `.str.upper()`, `.str.contains()` 등 pandas 내장 문자열 메서드로 Python `str` 함수를 Series 전체에 한 번에 적용할 수 있음
#### dt 접근자 — 날짜 벡터화
날짜 컬럼을 `pd.to_datetime()`으로 변환한 뒤 `.dt` 접근자로 연도·월·요일 등을 빠르게 추출함.
```python
df['date']    = pd.to_datetime(df['date'])
df['year']    = df['date'].dt.year
df['month']   = df['date'].dt.month
df['weekday'] = df['date'].dt.day_name()
```
---
### 왜 Polars와 DuckDB인가 — 2026 표준
Pandas는 수백만 행 규모까지는 충분하지만, 그 이상에서는 구조적 한계가 드러남. 이를 보완하는 두 도구가 **Polars**와 **DuckDB**임.
#### Pandas의 한계
- 싱글스레드 동작 — Python GIL로 인해 멀티코어 활용 불가
- 수백만 행 이상에서 속도 급격히 저하
- 메모리 사용량이 원본 데이터의 **5–10배**에 달함 (CoW 이전에는 복사가 잦았던 구조)
#### Polars — Rust + Arrow 기반
- **멀티스레드 자동 활용** — GIL 없이 코어 전체를 씀
- **Lazy API**로 실행 전에 쿼리 최적화 계획을 수립함
- Pandas 대비 **5–20배 빠름**
- Apache Arrow를 기반으로 하므로 다른 Arrow 도구와 데이터 복사 없이 연동됨
#### DuckDB — 파일 직접 SQL
- CSV·Parquet 파일을 메모리에 로딩하지 않고 바로 SQL로 분석할 수 있음
- **서버 없이** 로컬에서 DWH(Data Warehouse)급 성능을 냄
- JOIN·GROUP BY·WINDOW 함수 등 SQL 전체 기능을 지원함
#### Arrow 생태계 제로카피
Polars ↔ DuckDB ↔ PyArrow ↔ Pandas 사이에서 Apache Arrow 포맷을 공통 중간 포맷으로 사용하면 **데이터 직렬화 비용 0**, 즉 메모리 복사 없이 도구 간 전환이 가능함.
---
### Polars — Eager API vs Lazy API
Polars는 실행 방식에 따라 두 가지 모드를 제공함. 용도에 맞게 선택해야 성능을 제대로 활용할 수 있음.
#### 두 모드 비교
| 모드 | 진입점 | 실행 시점 | 적합 상황 |
| --- | --- | --- | --- |
| **Eager** | `pl.read_csv()` 등 | 즉시 | 탐색·소규모 데이터 |
| **Lazy** | `pl.scan_csv()` 등 `scan_` 계열 | `.collect()` 호출 시 | 대용량, 최적화 필요 |
#### Lazy API의 핵심 장점
- **Predicate pushdown**: 필터 조건을 파일 읽기 단계로 밀어넣어 불필요한 행 자체를 읽지 않음
- **Projection pushdown**: 필요한 컬럼만 읽어 I/O와 메모리를 줄임
- `schema_overrides`로 컬럼 타입을 명시하면 추론 비용을 없애 성능이 더 올라감
```python
result = (
    pl.scan_csv('large.csv', schema_overrides={'amount': pl.Float64})
    .filter(pl.col('region') == '서울')
    .filter(pl.col('amount') > 0)
    .group_by('category')
    .agg([pl.col('amount').sum().alias('total'),
          pl.count().alias('cnt')])
    .sort('total', descending=True)
    .collect()  # 여기서 실제 실행
)
```
- `.collect()` 전까지는 실행 계획만 쌓이고, 호출 시 한 번에 최적화된 순서로 실행됨
---
### Polars 핵심 문법 — Pandas와 비교
Polars는 Pandas와 개념은 같지만 문법이 다름. 핵심 대응 관계를 숙지해야 전환이 수월함.
#### 주요 메서드 대응
| Polars | Pandas 대응 | 역할 |
| --- | --- | --- |
| `pl.col('x')` | `df['x']` | 컬럼 참조 |
| `.filter(pl.col('x') > 0)` | `df[df['x'] > 0]` | 행 필터 |
| `.select(['a','b'])` | `df[&#91;'a','b'&#93;]` | 컬럼 선택 |
| `.with_columns(...)` | `df.assign(...)` | 컬럼 추가·수정 |
| `.group_by().agg(...)` | `df.groupby().agg(...)` | 집계 |
```python
# 컬럼 추가 (assign 대응)
df.with_columns(
    (pl.col('amount') * 1.1).alias('adjusted')
)

# 문자열·날짜 처리
df.with_columns(
    pl.col('region').str.to_uppercase(),
    pl.col('date').str.to_date('%Y-%m-%d')
)

# Pandas ↔ Polars 변환
df_pd = df.to_pandas()
df_pl = pl.from_pandas(df_pd)
```
---
### DuckDB — CSV·Parquet에 직접 SQL
DuckDB는 파일을 Python 객체로 로딩하지 않고 **SQL을 파일에 바로 실행**할 수 있다는 점이 핵심임. `duckdb.sql()` 한 줄로 시작됨.
#### 주요 기능
- `.csv`, `.parquet` 와일드카드로 폴더 내 여러 파일을 한 번에 쿼리할 수 있음
- JOIN·GROUP BY·WINDOW 함수 등 표준 SQL 전체를 지원함
- `.df()`로 Pandas DataFrame, `.pl()`로 Polars DataFrame으로 바로 변환됨
- `CREATE TABLE AS SELECT ...`로 결과를 영구 파일로 저장할 수 있음
```python
# 파일에 직접 SQL (로딩 불필요)
result = duckdb.sql("""
    SELECT region,
           SUM(amount) AS total,
           AVG(amount) AS avg,
           COUNT(*)    AS cnt
    FROM 'data/*.csv'
    WHERE year = 2024
      AND amount > 0
    GROUP BY region
    ORDER BY total DESC
""").df()

# 여러 파일 JOIN (포맷 혼합 가능)
duckdb.sql("""
    SELECT s.*, c.tier
    FROM 'sales.parquet' s
    JOIN 'customers.csv' c ON s.cid = c.id
""").show()
```
---
### 도구 선택 가이드 — Pandas vs Polars vs DuckDB
| 항목 | Pandas | Polars | DuckDB |
| --- | --- | --- | --- |
| API 스타일 | 즉시 실행(Eager) | Lazy (쿼리 최적화) | SQL |
| 멀티스레딩 | ✕ (GIL) | 자동 | 자동 |
| 메모리 효율 | 보통 | 높음 (Arrow) | 높음 (스트리밍) |
| 적합 규모 | \~수백만 행 | 수천만 행+ | 파일 직접 쿼리 |
| 학습 곡선 | 낮음 (표준) | 중간 | 낮음 (SQL) |
| Pandas 연동 | 기본 | Arrow 변환 | `.df()` 변환 |
| 권장 용도 | EDA·탐색 | 대용량 처리 | 파일 직접 분석 |
---
### Apache Arrow — 제로카피 데이터 변환 생태계
Arrow는 Polars·DuckDB·PyArrow·Pandas 간 데이터를 **복사 없이 공유할 수 있게 해주는 컬럼형 인메모리 포맷**임.
#### Arrow란?
- **컬럼형 인메모리 포맷**: 같은 컬럼의 값이 메모리에 연속 배치되어 집계·분석 연산에 최적화됨
- 모든 데이터 도구가 Arrow를 중간 포맷으로 채택하면 **직렬화 비용이 0**이 됨 — 도구 간 전환 시 데이터 복사가 발생하지 않음
#### Parquet의 장점
- 컬럼형 저장 구조 덕분에 필요한 컬럼만 선택적으로 읽을 수 있음
- CSV 대비 **읽기 속도 10배, 파일 크기 5배 작음**
#### 실전 권장 파이프라인
원본 CSV 수집 → **Parquet으로 변환 저장** → DuckDB/Polars로 대용량 분석 → 최종 탐색·시각화는 Pandas로 검토하는 흐름이 현재 표준에 가장 가까움.
#### Polars ↔ DuckDB 제로카피 전환
```plain text
pl.scan_parquet → DuckDB.execute() → pl.DataFrame
```
Arrow 포맷을 매개로 하므로 도구 전환 시 데이터 복사가 발생하지 않음.
---
### 데이터 시각화가 분석의 핵심인 이유
수치 요약만으로는 데이터의 실제 패턴을 파악하기 어려움. 시각화는 분석의 보조 수단이 아니라 **필수 첫 단계**임.
#### Anscombe의 사중주
평균·분산·상관계수가 모두 동일한 4개 데이터셋이, 시각화하면 완전히 다른 패턴(선형, 곡선, 이상치 포함 등)을 보임. **수치만으로 분석하면 근본적으로 틀릴 수 있음**을 보여주는 고전적 사례임.
#### 시각화의 주요 활용 목적
- **EDA의 첫 번째 도구**: 히스토그램·박스플롯으로 분포를, 산점도로 변수 간 상관관계를, 히트맵으로 결측치 패턴을 파악함
- **머신러닝 모델 평가**: loss 감소 곡선, confusion matrix, feature importance 등을 시각화해 모델을 숫자가 아닌 그림으로 이해하고 개선 방향을 설정함
- **데이터 기반 의사결정**: 대용량 로그·사용자 행동 데이터를 시각화해 이상 징후 감지 및 서비스 개선 인사이트를 도출함
- **효과적인 커뮤니케이션**: 인터랙티브 차트 한 장이 수치 표보다 비전공자를 빠르게 설득함. Plotly 차트는 직접 필터·줌이 가능함
- **알고리즘 분석·디버깅**: 시간 복잡도나 메모리 사용량 변화를 시각화해 병목 현상을 직관적으로 파악하고, 정렬 알고리즘의 스왑 횟수를 비교 분석함
---
### Matplotlib
Python 시각화 생태계의 근간이 되는 라이브러리임. 저수준(low-level) 제어가 가능해 거의 모든 종류의 그래프를 원하는 대로 커스터마이징할 수 있음.
#### 핵심 구조: Figure와 Axes
| 객체 | 역할 |
| --- | --- |
| **Figure (피규어)** | 전체 그림판(캔버스). 크기·해상도·배경색 등 전반 관리. 하나의 Figure 안에 여러 Axes를 담을 수 있음 |
| **Axes (축)** | 실제 데이터가 그려지는 개별 그래프(플롯). x축·y축·눈금·레이블·제목 등 구성 요소를 포함함 |
- `Axes`는 '축들의 복수형'이 아니라 **'축(axis)들이 모여 있는 공간'이라는 의미의 단수형 객체 이름**임. 혼동하기 쉬운 포인트임.
#### 주요 플롯 종류
| 함수 | 용도 |
| --- | --- |
| `plot()` | 선 그래프 — 시계열 데이터, 함수 표현 |
| `scatter()` | 산점도 — 두 변수 간 관계 |
| `bar()` / `barh()` | 막대 그래프 — 범주형 데이터 비교 |
| `hist()` | 히스토그램 — 수치형 데이터의 분포 |
| `boxplot()` | 박스 플롯 — 사분위수, 이상치 탐색 |
| `imshow()` | 이미지 데이터 시각화 — 행렬, 픽셀 데이터 |
#### 기본 그래프 작성 패턴
```python
import matplotlib.pyplot as plt

# 선 그래프
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y)
plt.title("Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
```
```python
# 막대 그래프
categories = ['A', 'B', 'C']
values = [5, 7, 3]
plt.bar(categories, values)
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()
```
- `plt.title()`, `plt.xlabel()`, `plt.ylabel()`로 제목과 축 레이블을 설정해야 그래프가 자기설명적(self-explanatory)이 됨
---
### Matplotlib 예시 — Figure/Axes 객체 기반 작성
`plt.figure()` + `fig.add_subplot()` 방식은 Figure·Axes 객체를 명시적으로 다루는 **객체지향 스타일**임. 서브플롯이 여러 개이거나 세밀한 제어가 필요할 때 권장됨.
```python
import matplotlib.pyplot as plt
import numpy as np

x  = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# 1. Figure 생성 (전체 캔버스)
fig = plt.figure(figsize=(10, 5))

# 2. Axes 추가: add_subplot(행, 열, 순서)
ax1 = fig.add_subplot(1, 2, 1)   # 1행 2열의 첫 번째
ax2 = fig.add_subplot(1, 2, 2)   # 1행 2열의 두 번째

# 3. 각 Axes에 데이터 플로팅
ax1.plot(x, y1, color='blue', label='sin(x)')
ax1.set_title('Sine Wave')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.grid(True)
ax1.legend()

ax2.plot(x, y2, color='red', linestyle='--', label='cos(x)')
ax2.set_title('Cosine Wave')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.legend()

fig.suptitle('Sine and Cosine Waves', fontsize=16)  # Figure 전체 제목
plt.tight_layout()  # 서브플롯 간 간격 자동 조정
plt.show()
```
- `ax.set_title()` / `ax.set_xlabel()` 방식은 Axes 객체에 직접 속성을 지정하는 방식으로, `plt.title()` 등 전역 함수 방식보다 서브플롯 다수 환경에서 명확함
- `plt.tight_layout()`은 레이블이 겹치는 문제를 자동으로 해소해줌
---
### 다중 그래프 그리기(subplots) — matplotlib
`plt.subplots()`는 Figure와 Axes 배열을 한 번에 반환하는 편의 함수임. `fig.add_subplot()`보다 간결하고 인덱싱이 직관적임.
#### subplots() 주요 파라미터
- `nrow`, `ncols`: 행·열 수 (서브플롯 격자 크기)
- `figsize`: 전체 Figure 크기 (인치 단위)
- `sharex`, `sharey`: X축 또는 Y축을 서브플롯 간에 공유할지 여부
#### 기본 사용 패턴

```python
import matplotlib.pyplot as plt

# 2행 2열 서브플롯 생성 → axes는 2×2 배열로 반환됨
fig, axes = plt.subplots(2, 2)

axes[0, 0].plot([1, 2, 3], [4, 5, 6])      # 좌상: 선 그래프
axes[0, 1].bar([1, 2, 3], [4, 5, 6])       # 우상: 막대 그래프
axes[1, 0].scatter([1, 2, 3], [4, 5, 6])   # 좌하: 산점도
axes[1, 1].hist([1, 2, 3, 4, 5, 6], bins=3) # 우하: 히스토그램

plt.tight_layout()
plt.show()
```
- `axes[행, 열]` 인덱싱으로 각 서브플롯에 접근함
- `plt.tight_layout()`으로 서브플롯 간 간격을 자동 조정해 레이블 겹침을 방지함
- 출력 결과(Image 10)에서 볼 수 있듯, 네 가지 플롯 유형이 하나의 Figure에 2×2 격자로 배치됨
---
### Seaborn — 개요 및 설치
Matplotlib 위에서 동작하는 **통계 데이터 시각화 특화 라이브러리**임. Matplotlib보다 적은 코드로 더 아름다운 그래프를 생성할 수 있으며, 다양한 내장 데이터셋과 고급 그래프 스타일을 제공함.
```python
# 설치
pip install seaborn

# 기본 임포트
import seaborn as sns
import matplotlib.pyplot as plt

# 내장 데이터셋 로드 (Google Colab 등에서 바로 사용 가능)
tips = sns.load_dataset('tips')
print(tips.head())
```
---
### Seaborn의 주요 그래프 그리기
#### 히스토그램 — 분포 확인
```python
sns.histplot(data=tips, x='total_bill', bins=10)
plt.title("Histogram of Total Bill")
plt.show()
```
#### 박스플롯 — 데이터 군집 및 이상치 확인
python
```python
sns.boxplot(data=tips, x='day', y='total_bill')
plt.title("Boxplot of Total Bill by Day")
plt.show()
```
#### 막대 그래프 — 범주형 × 수치형 관계
```python
sns.barplot(x='day', y='total_bill', data=tips)
plt.title("Barplot of Total Bill by Day")
plt.show()
```
#### 산점도 — 두 변수 간 관계
`hue` 옵션으로 제3의 범주형 변수를 색상으로 인코딩할 수 있음.
```python
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='time')
plt.title("Scatterplot of Total Bill vs Tip")
plt.show()
```
---
### Seaborn — pairplot · heatmap
여러 변수 간의 관계를 한눈에 파악하는 데 특화된 고급 그래프임.
#### pairplot — 다변량 탐색
데이터프레임의 모든 수치형 변수 쌍에 대한 산점도와 각 변수의 분포(히스토그램 또는 커널 밀도 추정)를 한 번에 그려줌. EDA 초기에 변수 간 관계를 빠르게 파악하는 데 매우 유용함
```python
iris = sns.load_dataset('iris')
sns.pairplot(iris, hue='species', markers=["o", "s", "D"])
plt.show()
```
#### heatmap — 상관계수 행렬 시각화
변수 간 상관계수 행렬이나 confusion matrix를 색상으로 직관적으로 보여줌. `annot=True`로 셀 안에 수치를 표시할 수 있음.
```python
correlation_matrix = iris.drop(columns='species').corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True,
            cmap='coolwarm', linewidths=.5)
plt.title('Correlation Matrix of Iris Features')
plt.show()
```
---
### Seaborn 고급 기능 — 스타일·색상·hue 옵션
#### 스타일 설정
`sns.set_style()`로 전체 그래프 배경 테마를 일괄 변경할 수 있음. 선택지: `'darkgrid'`, `'whitegrid'`, `'dark'`, `'white'`, `'ticks'`.
```python
sns.set_style('whitegrid')
sns.histplot(data=tips, x='total_bill')
plt.title("Styled Histogram")
plt.show()
```
#### 색상 팔레트 설정
`palette` 파라미터로 색상 세트를 지정함.
```python
sns.barplot(x='day', y='total_bill', data=tips, palette='Set2')
plt.title("Barplot with Custom Palette")
plt.show()
```
#### hue 옵션 — 그룹별 색상 분리
`hue`에 범주형 컬럼을 지정하면 그룹별로 색상을 다르게 표시해 한 그래프에서 세 번째 변수까지 인코딩할 수 있음.
```python
sns.boxplot(data=tips, x='day', y='total_bill', hue='sex')
plt.title("Boxplot with Hue")
plt.show()
```
---
### 다중 그래프 그리기(subplots) — Seaborn
Seaborn도 Matplotlib의 `plt.subplots()`를 그대로 사용함. 각 Seaborn 함수에 `ax=axes[행, 열]`을 전달해 원하는 서브플롯에 그래프를 배치함.
```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# 각 서브플롯에 Seaborn 그래프 배치
sns.scatterplot(x="total_bill", y="tip", data=tips, ax=axes[0, 0])
sns.boxplot(x="day", y="total_bill", data=tips, ax=axes[0, 1])

# 히트맵용 상관행렬: 수치형만 선택
corr = tips.select_dtypes(include=["float64", "int64"]).corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=axes[1, 0])

sns.barplot(x="day", y="total_bill", data=tips, ax=axes[1, 1])

plt.tight_layout()
plt.show()
```
- Seaborn 함수는 `ax` 파라미터를 받으므로, Matplotlib subplots와 자연스럽게 결합됨
- `select_dtypes(include=["float64", "int64"])`로 수치형 컬럼만 필터링한 뒤 `.corr()`을 적용해야 히트맵 오류 없이 사용할 수 있음
---
### Matplotlib — 기초부터 서브플롯까지 (종합 실전 패턴)
Matplotlib의 핵심 개념과 실전에서 자주 쓰는 설정 옵션을 종합한 패턴임.
- `Figure` = 전체 캔버스, `Axes` = 개별 그래프
- `subplot()`으로 여러 차트를 나란히 배치
- 색상·스타일(`color`, `alpha`, `lw`, `linestyle`)·범례(`legend()`)·제목·그리드 모두 Axes 메서드로 설정
- `plt.savefig()`로 PNG/PDF 고해상도 저장 가능
```python
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 라인 차트 — 색상, 선 굵기, 마커, 범례, 그리드 설정
axes[0].plot(months, revenue, color='steelblue',
             lw=2, marker='o', label='매출')
axes[0].set_title('월별 매출 추이')
axes[0].set_xlabel('월')
axes[0].set_ylabel('원')
axes[0].legend()
axes[0].grid(alpha=0.3)

# 막대 차트 — 투명도 설정
axes[1].bar(regions, values, color='teal', alpha=0.8)
axes[1].set_title('지역별 매출')

plt.tight_layout()
plt.savefig('report.png', dpi=150, bbox_inches='tight')
```
- `dpi=150`은 고해상도 저장을 위한 설정이고, `bbox_inches='tight'`는 여백을 자동으로 잘라줌
- `alpha`는 투명도(0\~1), `lw`는 선 굵기(linewidth의 축약)임
---
### Seaborn — 통계 시각화 특화 라이브러리 (종합)
Seaborn은 Matplotlib 기반의 **high-level 인터페이스**로, 통계 분석에 자주 쓰이는 그래프를 적은 코드로 생성할 수 있음.
- `hue`·`size`·`style` 파라미터로 색상·크기·마커 스타일을 통해 다차원 정보를 하나의 그래프에 인코딩할 수 있음
- `boxplot`·`violinplot`으로 그룹 간 분포를 비교함
- `heatmap`으로 상관행렬과 결측치 패턴을 시각화함
- `pairplot`으로 모든 변수 쌍의 산점도를 한 번에 확인함
- `histplot(kde=True)`로 히스토그램과 KDE(커널 밀도 추정) 곡선을 함께 표시할 수 있음
```python
# 상관 히트맵 + 분포 비교 + 히스토그램+KDE를 서브플롯으로 구성
corr = df.select_dtypes('number').corr()
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

sns.heatmap(corr, annot=True, cmap='coolwarm',
            fmt='.2f', ax=axes[0, 0])
sns.boxplot(data=df, x='region', y='amount',
            hue='category', ax=axes[0, 1])
sns.histplot(data=df, x='amount',
             kde=True, ax=axes[1, 0])

plt.tight_layout()
plt.show()
```
- `fmt='.2f'`는 히트맵 셀 내 수치의 소수점 자릿수를 제어함
- `kde=True`를 `histplot`에 추가하면 분포의 연속적인 확률 밀도 곡선을 함께 그려줌
---
### Plotly Express — 인터랙티브 시각화
Matplotlib·Seaborn이 정적 이미지를 생성하는 반면, **Plotly Express**는 줌·필터·호버가 가능한 인터랙티브 차트를 한 줄 코드로 만들 수 있음.
#### 주요 특징
- `px.scatter`, `px.bar`, `px.line`, `px.histogram`, `px.box` 등 모든 기본 차트를 한 줄로 생성함
- `color`, `size`, `hover_name` 파라미터로 세 번째·네 번째 변수를 색상·크기·툴팁으로 인코딩함
- `facet_col` / `facet_row`로 범주별 분할 서브플롯을 자동 생성함
- `fig.write_html()`로 인터랙티브 차트를 HTML 파일로 저장해 공유할 수 있음
- `fig.update_layout()`으로 제목·축·폰트 등을 커스터마이징함
```python
import plotly.express as px

# 다차원 산점도: 색상=지역, 크기=인구, 호버=국가명
fig = px.scatter(df,
    x='gdp', y='happiness',
    color='region', size='population',
    hover_name='country',
    title='GDP vs 행복지수')

# 지역×카테고리별 분할 막대 차트
fig2 = px.bar(monthly_df,
    x='month', y='revenue',
    color='category',
    facet_col='region',
    title='지역·카테고리별 월 매출')

# HTML로 저장 (브라우저에서 인터랙티브하게 공유 가능)
fig.write_html('analysis.html')
```
---
### Altair — 선언형 시각화 + 도구 선택 기준
**Altair**는 Grammar of Graphics(그래픽 문법) 이론을 기반으로 한 선언형 시각화 라이브러리임. 데이터 구조와 시각적 인코딩을 선언하면 차트가 완성되는 방식이라, EDA 프로토타이핑 속도가 매우 빠름.
#### 문법 구조
`Chart` → `mark_*(마크 종류)` → `encode(인코딩)` → `.interactive()` 순으로 체이닝함. encode 안의 `컬럼명:타입` 형식에서 `Q`는 수치형(Quantitative), `N`은 명목형(Nominal)을 의미함.
```python
import altair as alt

chart = (alt.Chart(df)
    .mark_point()
    .encode(
        x='gdp:Q',
        y='happiness:Q',
        color='region:N',
        tooltip=['country', 'gdp', 'happiness']
    ).interactive()
)

chart.save('chart.html')
```
- `.interactive()`를 붙이면 별도 설정 없이 줌·패닝이 가능한 인터랙티브 차트가 됨
- 차트를 HTML로 저장해 브라우저에서 바로 공유할 수 있음
---
### 시각화 도구 선택 — 상황별 가이드
| 도구 | 강점 | 권장 상황 |
| --- | --- | --- |
| **Matplotlib** | 커스터마이징 최강, 픽셀 수준 제어, 다른 라이브러리의 기반 | 학술 논문·보고서 품질 차트 |
| **Seaborn** | 통계 시각화 특화, hue 파라미터 하나로 다차원 정보 표현, 코드 짧음 | 분포·상관·그룹 비교 |
| **Plotly** | 줌·필터·호버를 HTML 한 파일로 공유 가능 | 비전공자 발표·인터랙티브 대시보드 |
| **Altair** | 선언형 문법, 탐색 단계에서 수십 개 차트를 빠르게 생성 | 빠른 EDA 프로토타이핑 |
- 보고서·논문 → **Matplotlib / Seaborn**
- 인터랙티브 대시보드 → **Plotly**
- 빠른 EDA → **Altair**
- 웹 공유 → **Streamlit** (별도 소개 수준으로 언급됨)
---
### 기술통계 — 데이터를 숫자로 이해하기
모델을 돌리기 전에 데이터의 분포·중심·퍼짐을 숫자로 파악하는 단계임. 시각화와 함께 EDA의 핵심을 이룸.
#### 주요 통계 개념
| 분류 | 지표 | 의미 |
| --- | --- | --- |
| 중심 경향 | 평균(mean) | 이상치에 민감 |
|  | 중앙값(median) | 이상치에 강건 |
|  | 최빈값(mode) | 범주형에 유용 |
| 산포도 | 분산·표준편차 | 평균으로부터의 퍼짐 |
|  | IQR | Q3-Q1, 이상치 탐지에 사용 |
|  | 범위(range) | 최댓값-최솟값 |
| 분포 모양 | 왜도(skewness) | 0: 대칭, 양수: 오른쪽 꼬리 |
|  | 첨도(kurtosis) | 0: 정규분포, 클수록 뾰족 |
| 관계 | 상관계수 | -1\~+1, 선형 관계 강도 |
```python
import numpy as np
from scipy import stats

# Pandas 기술통계 자동 계산
df.describe()

# 분포 모양
df['amount'].skew()    # 왜도 (0: 대칭)
df['amount'].kurt()    # 첨도 (0: 정규)
df['amount'].median()  # 중앙값

# 상관행렬: -1에 가까울수록 음의 상관, 1에 가까울수록 양의 상관
corr = df[['amount', 'visits', 'age']].corr()

# 분포 시각화
import seaborn as sns
sns.histplot(df['amount'], kde=True)

# 정규분포 검정 (Shapiro-Wilk): p < 0.05이면 정규분포가 아님
_, p = stats.shapiro(df['amount'].dropna())
print(f'정규분포 검정 p값:{p:.4f}')
```
---
### 가설 검정 기초 — t-test와 카이제곱
통계적 차이나 연관성이 **우연에 의한 것인지 아닌지**를 판단하는 검정 방법임.
#### 핵심 개념
- **귀무가설(H0)**: 차이·연관성이 없다는 기본 가정
- **대립가설(H1)**: 차이·연관성이 있다는 주장
- **유의수준 α = 0.05**: p값이 0.05 미만이면 H0를 기각 → 통계적으로 유의미한 차이가 있음
| 검정 | 사용 상황 |
| --- | --- |
| **t-test** | 두 그룹의 수치형 변수 평균 차이 검정 |
| **카이제곱** | 두 범주형 변수 간 독립성 검정 |
```python
from scipy import stats

# t-test: A/B 그룹 매출 차이 검정
group_a = df[df['group'] == 'A']['amount']
group_b = df[df['group'] == 'B']['amount']
t, p = stats.ttest_ind(group_a, group_b)
print(f't={t:.3f}, p={p:.3f}')
if p < 0.05:
    print('통계적으로 유의미한 차이 있음')
else:
    print('차이 없음 (우연일 수 있음)')
```
```python
# 카이제곱: 지역과 구매여부 독립성 검정
from scipy.stats import chi2_contingency
ct = pd.crosstab(df['region'], df['purchased'])
chi2, p, dof, expected = chi2_contingency(ct)
print(f'카이제곱={chi2:.3f}, p={p:.3f}')
```
---
### CRISP-DM — 실무 데이터 분석 방법론
실무에서 가장 널리 쓰이는 데이터 분석 프로세스 프레임워크임. **기술(tool) 중심이 아니라 문제 해결 중심**으로 설계되어 있음.
#### 6단계 프로세스
업무 이해(문제 정의) → 데이터 이해(EDA 탐색) → 데이터 준비(전처리·피처) → 모델링(알고리즘) → 평가(성능 측정) → 배포(서비스 적용)
- 좋은 분석은 알고리즘 선택이 아니라 **올바른 문제 정의**에서 시작됨
- 실제 업무에서는 전체 시간의 **80\~90%가 데이터 준비** 단계에 소요됨
---
### ### sklearn Pipeline — 전처리 + 모델 통합
전처리와 모델을 하나의 객체로 묶어 **학습-예측-저장을 일관되게** 관리하는 sklearn의 핵심 패턴임. 배포 환경에서 동일한 전처리+예측을 보장할 수 있어 MLOps의 기본 단위가 됨.
#### 핵심 구성 요소
- **ColumnTransformer**: 수치형 컬럼과 범주형 컬럼에 서로 다른 전처리를 동시에 적용함
- **Pipeline**: 전처리기와 모델을 순서대로 연결해 하나의 객체로 만듦
- `fit()`: 학습, `predict()`: 예측, `transform()`: 변환
- `joblib.dump()` / `joblib.load()`: 파이프라인 전체를 직렬화해 저장하고 불러올 수 있음
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import Ridge
import joblib

# 수치형 → StandardScaler, 범주형 → OneHotEncoder
preproc = ColumnTransformer([
    ('num', StandardScaler(), num_cols),
    ('cat', OneHotEncoder(), cat_cols)
])

# 전처리 + 모델을 하나의 Pipeline으로
model = Pipeline([
    ('prep', preproc),
    ('reg', Ridge(alpha=1.0))
])

model.fit(X_train, y_train)
print(f'R2:{model.score(X_test, y_test):.3f}')

# 파이프라인 저장 및 로딩
joblib.dump(model, 'model.pkl')
loaded = joblib.load('model.pkl')
```
---
### 통계와 ML 파이프라인이 연결되는 이유
통계 지식과 sklearn Pipeline은 별개로 존재하는 것이 아니라 **데이터 분석 전 과정에서 서로를 뒷받침하는 관계**임.
- **통계 없이 ML은 블랙박스**: 평균·분산·상관계수를 모르면 피처 선택, 이상치 처리, 결과 해석이 불가능함. 모델보다 데이터 이해가 선행되어야 함
- **CRISP-DM은 기술보다 프로세스**: 좋은 분석은 알고리즘 선택이 아니라 올바른 문제 정의에서 시작되며, 데이터 준비가 전체 공수의 80\~90%를 차지함
- **후속 과목 직결**: Feature Engineering·머신러닝 과목에서 지금 배운 sklearn Pipeline을 그대로 확장해서 사용함
- **재현 가능한 모델 관리**: `joblib`으로 Pipeline 전체를 저장하면 배포 환경에서도 동일한 전처리+예측이 보장됨 — 이것이 MLOps의 기본 단위임
---
### 왜 분석을 자동화해야 하는가
수작업 반복 분석은 시간·오류·확장성 측면에서 구조적 한계를 가짐. 자동화는 선택이 아니라 실무 필수 역량임.
- **반복 분석의 현실**: 매주 같은 매출 리포트를 수작업으로 만드는 분석가의 경우, 자동화하면 수십 분 소요가 0분으로 줄어듦
- **데이터 최신성**: 어제 시황이 반영된 리포트는 오늘 오전 5시에 이미 완성돼 있어야 함 — 수작업으로는 불가능한 타이밍임
- **오류 감소**: 수작업 복붙 오류를 제거하고, 동일한 코드가 항상 동일한 결과를 생성해 신뢰성을 높임
- **확장성**: 10개 지역 리포트를 만드나 100개를 만드나 코드는 동일하고, 규모 확장 비용이 거의 없음
---
### schedule + cron — 반복 분석 자동화
`schedule`은 Python 내에서 동작하는 간단한 스케줄러임. cron이나 macOS launchd로 OS 레벨 스케줄까지 연동하면 서버에서 완전 무인 자동화가 가능함.
#### 핵심 패턴
- `schedule.every().day.at('08:00').do(함수)` 형식으로 매일·매주·매시간 등 다양한 주기를 설정함
- 오류 발생 시 `logging`으로 기록하고 알림으로 연결하는 패턴이 필수임
- `subprocess`로 외부 스크립트 실행을 연동할 수 있음
```python
import schedule, time, logging

def run_daily_report():
    try:
        df = load_and_clean('sales.csv')
        stats = compute_stats(df)
        render_report(stats)
        logging.info('리포트 완료')
    except Exception as e:
        logging.error(f'실패:{e}')

schedule.every().day.at('08:00').do(run_daily_report)
schedule.every().monday.at('09:00').do(weekly_summary)
schedule.every(1).hours.do(check_new_data)

while True:
    schedule.run_pending()
    time.sleep(60)
```
- `while True` + `run_pending()` + `time.sleep(60)` 루프가 스케줄러를 계속 살려두는 기본 패턴임
---
### Jinja2 — 분석 리포트 자동 생성
**Jinja2**는 Python 대표 템플릿 엔진으로, HTML 파일 안에 변수·반복·조건 문법을 삽입해 분석 결과를 자동으로 리포트로 렌더링할 수 있음.
#### 주요 문법
- `{{ 변수 }}`: 값 출력
- `{% for 항목 in 목록 %}`: 반복
- `{% if 조건 %}`: 조건 분기
```python
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from datetime import datetime

env  = Environment(loader=FileSystemLoader('templates'))
tmpl = env.get_template('report.html')

html = tmpl.render(
    title='월간 판매 분석',
    generated=datetime.now().strftime('%Y-%m-%d'),
    summary=stats.to_dict(),
    chart_html=fig.to_html(full_html=False),   # Plotly 차트 삽입
    top5=df.nlargest(5, 'amount').to_dict('records')
)

out = Path('output/report.html')
out.write_text(html, encoding='utf-8')

import webbrowser
webbrowser.open(str(out.resolve()))  # 브라우저에서 바로 열기
```
- `fig.to_html(full_html=False)`로 Plotly 인터랙티브 차트를 HTML 조각으로 뽑아 템플릿에 주입할 수 있음
- `pdfkit` 라이브러리와 연동하면 HTML을 PDF로 변환해 이메일 배포까지 가능함
---
### LLM API 활용 개요 — 개념과 구조 중심
모든 LLM 벤더(OpenAI, Anthropic 등)는 **HTTP POST 방식의 유사한 API 구조**를 사용함. 벤더에 무관하게 동일한 패턴으로 호출할 수 있음.
#### 구조
- 요청: 메시지 배열(`messages`) + 모델 파라미터
- 응답: `content` 배열 안에 `text` 타입 블록으로 반환됨
- 과금: 입력 토큰 + 출력 토큰의 합산 기준
- 대량 처리 시 `httpx.AsyncClient`로 비동기 병렬 호출이 효율적임
```python
import httpx, os, asyncio

async def call_llm(text: str) -> str:
    async with httpx.AsyncClient() as c:
        r = await c.post(
            'https://api.{vendor}.com/v1/messages',
            headers={'Authorization': f'Bearer{os.getenv("API_KEY")}'},
            json={
                'model': 'model-name',
                'max_tokens': 500,
                'messages': [{'role': 'user', 'content': text}]
            },
            timeout=30
        )
        return r.json()['content'][0]['text']

# 활용: 이상치 자동 설명
result = asyncio.run(call_llm(f'다음 데이터 이상치 설명:{outliers}'))
```
---
### 분석 파이프라인 설계 — ETL 구조 원칙
좋은 파이프라인의 기준: **각 단계 분리 + 오류 기록 + 재현 가능 + 테스트 가능**
ETL 구조는 Extract(수집) → Validate(검증) → Transform(변환) → Load(저장) 단계로 분리하고, 각 단계에 로깅을 붙임. 단계를 분리하면 실패 시 어느 단계인지 즉시 파악되고, 각 단계를 독립적으로 pytest로 테스트할 수 있음.
```python
def run_pipeline(config: dict) -> dict:
    logger.info(f'파이프라인 시작:{config}')

    # E: Extract — 수집 (API / DB / 파일)
    raw = extract(config['source'])
    logger.info(f'수집 완료:{len(raw)}건')

    # V: Validate — 검증 (Pydantic 스키마 사용)
    validated, errors = validate(raw, schema=SalesRecord)
    logger.warning(f'검증 오류:{len(errors)}건') if errors else None
```
---
### Jupyter Notebook vs .py 스크립트 — 언제 무엇을?
| 상황 | Jupyter (.ipynb) | Python (.py) |
| --- | --- | --- |
| 탐색·실험 | ✅ EDA·데이터 탐색 |  |
| 시각화 중심 | ✅ 인라인 출력 |  |
| 일회성 분석 | ✅ |  |
| 보고서 변환 | ✅ nbconvert |  |
| 자동화 스크립트 |  | ✅ 반복 실행 |
| 버전 관리·협업 |  | ✅ Git + pytest |
| CI/CD 통합 |  | ✅ |
| 재사용 모듈 |  | ✅ src/ 패키지 |
---
### 분석 프로젝트 폴더 구조
6개월 뒤 동료(또는 미래의 나)가 README만 읽고 바로 실행할 수 있어야 좋은 구조임.
```plain text
data-project/
├── data/
│   ├── raw/          # 원본 데이터 (절대 수정 금지)
│   ├── processed/    # 전처리 완료 데이터
│   └── external/     # 외부 참조 데이터
├── notebooks/        # EDA·실험용 Jupyter 노트북
│   ├── 01_eda.ipynb
│   └── 02_feature_exploration.ipynb
├── src/              # 재사용 가능한 Python 모듈
│   ├── __init__.py
│   └── clean.py      # 전처리 함수
```
- `data/raw/`는 원본이므로 절대 수정하지 않음. 전처리 결과는 `processed/`에 별도 저장함
- `src/`에 `__init__.py`를 두면 폴더가 Python 패키지로 인식됨
---
### 모듈화 — 노트북 코드를 재사용 가능한 패키지로
노트북에서 검증된 코드는 `src/` 아래 `.py` 파일로 분리해 재사용 가능한 함수로 관리함. 공통 전처리는 `clean.py`, 시각화는 `viz.py`로 역할별로 분리하는 것이 기본임.
```python
# src/clean.py
from typing import Optional
import pandas as pd

def clean_nulls(df: pd.DataFrame,
                cols: Optional[list] = None,
                strategy: str = 'median') -> pd.DataFrame:
    cols = cols or df.select_dtypes('number').columns.tolist()
    if strategy == 'median':
        return df.fillna(df[cols].median())
    elif strategy == 'drop':
        return df.dropna(subset=cols)
    return df
```
```python
# notebooks/01_eda.ipynb 에서 사용
import sys
sys.path.insert(0, '..')
from src.clean import clean_nulls
from src.viz import plot_distribution
```
- 노트북에서 `sys.path.insert(0, '..')`로 프로젝트 루트를 경로에 추가한 뒤 절대 임포트로 불러옴
---
### README.md 작성 + GitHub 공유
```bash
# README.md 핵심 구성
## 프로젝트 개요
## 개발 환경 설정
git clone <url> && cd data-project
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

## 실행 방법
pytest tests/
python src/run_pipeline.py

# 노트북 HTML 변환·공유
jupyter nbconvert --to html notebooks/01_eda.ipynb

# GitHub Actions: .github/workflows/test.yml 에 pytest 자동화
```
- **배지(badge)**: 테스트 통과·커버리지 수치를 README 상단에 표시해 프로젝트 신뢰도를 시각적으로 보여줌
- **GitHub Actions**: push 시 pytest가 자동으로 실행되도록 `.github/workflows/test.yml`에 설정함
---
### 분석 코드 구조화의 핵심 원칙
- **탐색과 재사용 분리**: 노트북은 탐색·실험 전용, 검증된 함수는 `src/`로 이동해 재사용 가능한 모듈로 관리. 두 역할을 섞지 않는 것이 핵심임
- **재현성 = 신뢰성**: `requirements.txt` + `.env` 예시 + README 실행 가이드 세 가지만 있으면 누구나 동일한 결과를 재현할 수 있음
- **데이터는 git에 올리지 않는다**: `data/raw/`는 `.gitignore`에 추가하고, 대신 데이터 출처(URL·스크립트)를 README에 기록함
- **점진적 개선**: 처음부터 완벽한 구조를 만들 필요 없음. 분석이 반복되면 함수화하고, 함수가 쌓이면 모듈화하는 순서로 자연스럽게 발전시킴
---
<empty-block/>
