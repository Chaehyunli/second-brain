---
title: "[8/7] 데이터 분석을 위한 Python 이해_Day2_실습"
notion_page_id: "3b51d84b-f68e-80de-99c1-c2ed982f2060"
source_url: "https://app.notion.com/p/3b51d84bf68e80de99c1c2ed982f2060"
synced_at: "2026-08-08T23:32:50+09:00"
content_sha256: "d9cd383a66b45951593bc9bf7d628f72b61b91df47868809fb7621e7ab037edb"
tags: [notion, skala, learning, python, data-analysis]
---

# [8/7] 데이터 분석을 위한 Python 이해_Day2_실습

[[notion/SKALA/index|SKALA 학습 노트]]

> 원문: [Notion 페이지](https://app.notion.com/p/3b51d84bf68e80de99c1c2ed982f2060) (2026-08-08 확인)

# **Day2 종합실습 — NYC 옐로우 택시 End2End 분석 결과 보고서**
- 팀원: 임채현, 임유리, 김광현
- 데이터: NYC TLC 공식 옐로우 택시 trip data (2026-01\~05, 평일·RatecodeID==1 필터링)
- 코드 저장소 구조: `scripts/01~10_*.py` (실행 순서대로 번호 부여), `main.py` 한 번 실행으로 전체 파이프라인 자동 수행, `report_v1.md`/`report_v2.md`/`report_v3.md`(버전별 기술 리포트 자동 생성), `models/`(joblib으로 저장된 학습 파이프라인)
---
## **1. 진행 과정 — version1 → version2 → version3**
### **version1: 출퇴근 vs 비출퇴근, 기본 비교**
`RatecodeID==1`·평일 필터링, 이상치 제거 후 906만 건에 대해 기술통계·상관분석·t-test·선형회귀를 수행했다.
```plain text
=== t-test (Welch) ===
       metric  rush_mean  non_rush_mean      diff      t_stat  p_value
 total_amount  25.750397      26.366271 -0.615874  -56.457798      0.0
trip_distance   2.332299       2.648771 -0.316473 -158.134712      0.0

=== 선형회귀 (total_amount 예측) ===
RMSE: 4.127   MAE: 2.433   R^2: 0.9335
```

**문제**: `total_amount` 차이가 -2.3%에 불과해, 두 그룹이 "체감상 다를 게 없어 보인다"는 의문이 팀 내에서 제기됨.
### **version2: 지표를 쪼개서 재해석 + 효과크기(Cohen's d) 도입**
거리가 짧아지는 효과와 속도가 느려지는 효과가 `total_amount`에서 서로 상쇄된다는 가설을 세우고, `speed_mph`(평균 속도)·`fare_per_mile`(마일당 요금)을 파생시켜 재검정했다. 또한 표본이 9백만 건이라 p-value가 항상 0으로 나오는 문제를 보완하기 위해 Cohen's d를 함께 계산했다.
```plain text
=== t-test + Cohen's d (v2) ===
       metric  diff_pct   p_value  cohens_d effect_size
 total_amount     -2.34       0.0   -0.0385       무시가능
trip_distance    -11.95       0.0   -0.1066       무시가능
    speed_mph     -6.17       0.0   -0.1102       무시가능
fare_per_mile      7.25       0.0    0.0453       무시가능
```

**결론**: `total_amount` 차이가 작아 보인 건 착시가 아니라 사실이었다(d=-0.04). 다만 그 이면에는 "거리는 짧아지고(-12%) 마일당 단가는 오르는(+7%)" 두 효과가 상쇄되고 있었다 — 총액이 아니라 **구성**을 봐야 한다는 인사이트를 얻음.
### **version3: 그룹 정의 자체를 재검토**
시간대별 평균 속도를 찍어보니 "비출퇴근"으로 묶였던 낮 10\~16시(약 8mph)가 출퇴근 피크(8.6\~11mph)보다 오히려 더 막히고, 심야 0\~6시가 가장 빠르다는 것을 발견했다. 즉 출퇴근/비출퇴근이라는 이분법 자체가 반대 성질의 두 구간(심야+낮)을 한 그룹에 묶어 효과를 상쇄시키고 있었다. `pickup_hour`를 5개 시간대 밴드로 재그룹핑하고 대비가 가장 큰 **낮 vs 심야**를 헤드라인 검정으로 다시 잡았다.
```plain text
=== t-test: 낮(10~16시) vs 심야(0~6시) + Cohen's d ===
       metric  diff_pct       p_value  cohens_d effect_size
    speed_mph    -48.36  0.000000e+00   -1.5253          큼
trip_distance    -33.03  0.000000e+00   -0.3893          작음
fare_per_mile     33.31  0.000000e+00    0.1608       무시가능
 total_amount     -2.65 1.922217e-139   -0.0420       무시가능
```

**최종 결론**: 시간대는 "얼마를 내는가"(`total_amount`, 어느 그룹 정의를 쓰든 d≈-0.04로 거의 무관)가 아니라 "무엇에 대해 내는가"(거리 vs 정체 시간)를 바꾼다. 낮 시간대는 짧은 거리를 비싼 단가로, 심야는 긴 거리를 싼 단가로 이동해 총액이 비슷해지는 구조다.
---
## **2. 팀원별 개인 의견 (초안)**
### **임채현**
처음 `total_amount` 결과만 보고 "출퇴근이랑 비출퇴근이랑 차이가 없어 보이는데 이게 의미가 있나?"라는 의문을 제기했다. 결과적으로 이 의문이 맞았다 — Cohen's d로 보니 실제로 총 요금 차이는 무시할 수준이었다. 다만 여기서 멈추지 않고 "왜 상쇄되는가"를 파고든 게 version2로 이어졌다고 생각한다. 지표 하나(`total_amount`)만 보고 "차이 없음 = 분석 실패"로 결론짓지 않고, 그 지표가 어떤 하위 요인들의 합인지 분해해봐야 한다는 걸 느꼈다.
### **임유리**
p-value가 전부 `0.0`으로 나오는 걸 보고 이게 통계적으로 무슨 의미인지 의문이 들었다. 표본이 9백만 건이면 t-statistic이 표본 크기의 제곱근에 비례해서 커지기 때문에, 아주 사소한 차이도 "통계적으로 유의"하게 나온다. p-value만 보고 "유의하니까 의미 있는 차이"라고 결론 내리면 안 되고, Cohen's d 같은 표본 크기에 영향받지 않는 효과크기 지표를 같이 봐야 한다는 걸 강조하고 싶다. 실제로 이번 분석에서 p-value는 전부 0에 가까웠지만 Cohen's d는 '무시가능'부터 '큼'까지 다양하게 나와서, 두 지표를 같이 볼 때만 제대로 된 해석이 가능하다는 걸 확인했다.
### **김광현**
"출퇴근 vs 비출퇴근"이라는 그룹 정의 자체를 의심해봐야 한다고 생각했다. 시간대별 속도를 시간 단위로 찍어보니 낮 시간대(10\~16시)가 출퇴근 피크보다 더 막힌다는 게 드러났다. 처음부터 "출퇴근=혼잡"이라는 전제를 의심 없이 받아들였다면 절대 발견하지 못했을 결과다. 통계 검정을 아무리 정교하게 해도 그룹을 잘못 나누면 답이 안 나온다는 걸 배웠고, 도메인 지식(뉴욕 택시 혼잡 패턴)과 데이터를 먼저 눈으로 확인하는 과정이 검정 설계보다 선행되어야 한다고 생각한다.
## **3. 팀 종합 의견**
세 명의 관점은 서로 다른 지점에서 같은 문제(왜 결과가 밋밋해 보이는가)를 건드리고 있었다: 채현은 "지표 선택"을, 유리는 "검정 방법론"을, 광현은 "그룹 정의"를 문제 삼았다. 셋을 합쳐보면 다음과 같은 순서로 정리된다.
1. 지표를 하나만 보지 말고 구성 요소로 분해한다 (v2)
2. p-value뿐 아니라 효과크기로 실질적 크기를 판단한다 (v2)
3. 애초에 비교 그룹을 데이터에 근거해서 다시 정의한다 (v3)
세 관점 중 어느 하나만 적용했다면 "출퇴근과 비출퇴근은 별 차이 없다"는 얕은 결론에서 멈췄을 것이다. 셋을 순서대로 적용하고 나서야 "총 요금은 시간대와 무관하지만, 거리와 단가의 구성은 시간대에 따라 크게(Cohen's d=-1.53) 달라진다"는, 실무적으로 의미 있는 결론(예: 낮 시간대 요금 정책, 배차 전략에 활용 가능)에 도달할 수 있었다.
### **코드 품질 보완 내역**
1차 리뷰에서 지적된 4가지 항목을 모두 반영했다.
- **Polars 비교 로딩**: `02_preprocess.py`에서 동일 raw parquet을 Pandas·Polars로 각각 로딩해 shape 일치 여부(`assert`)와 로딩 시간을 비교 출력. Polars가 약 3.8배 빠름(0.21s vs 0.79s) — 대용량 데이터일수록 차이가 커질 것으로 예상
- **결측치 EDA**: `RatecodeID`·`passenger_count`에 각 4,812,280건(전체의 약 25%) 결측치가 있음을 명시적으로 확인. `RatecodeID==1` 필터가 결측치를 자연스럽게 제거하는 구조라 별도 대체(imputation) 없이 진행
- **Plotly 인터랙티브 차트**: `10_plotly_chart.py` 추가. 시간대별 속도·마일당요금을 hover로 정확한 수치까지 확인 가능한 형태로 `outputs/figures/hourly_profile_interactive.html`에 저장 (팀 발표 시연용으로 활용 권장)
- **sklearn Pipeline + joblib**: `StandardScaler`+`LinearRegression`을 `Pipeline`으로 묶어 학습/평가하고 `models/total_amount_regression_pipeline.joblib`로 저장. 스케일링이 모델과 분리되지 않아 재사용 시 실수 위험이 없어짐
- **주석 보강**: 이상치 임계값 근거, Welch's t-test를 쓴 이유(그룹 표본 수 차이), Cohen's d 공식과 해석 기준(Cohen 1988 관례), 시간대 밴드를 다시 나눈 근거를 스크립트 내 인라인 주석으로 추가
---
## **4. 결론**
- version1: `total_amount`만으로는 출퇴근 효과를 포착하지 못함 확인
- version2: 거리·속도 효과가 총 요금에서 상쇄됨을 규명, 효과크기 개념 도입
- version3: 그룹 정의(출퇴근 vs 비출퇴근) 자체가 상쇄의 원인이었음을 밝히고, 시간대 밴드 재정의로 실질적 효과(속도 d=-1.53) 확인
**핵심 메시지**: 뉴욕 택시 요금은 시간대에 따라 총액은 거의 그대로지만, 그 총액을 구성하는 거리와 단가(정체 비용)는 시간대에 따라 크게 달라진다.
---
## **5. 개인 추가 의견**
### **담당 역할**
프로젝트 전체 설계와 파이프라인 자동화를 맡았다. Kaggle 인증 없이 NYC TLC 공식 서버에서 데이터를 직접 받아오는 방식으로 데이터 확보 경로를 정하고, `scripts/01~10_*.py`를 실행 순서대로 구성해 `main.py` 한 번으로 다운로드→전처리→분석→모델링→리포트 생성까지 이어지는 파이프라인을 설계했다. 또한 분석 중간에 결과가 "밋밋해 보인다"는 문제를 제기해 version2·version3으로 이어지는 재분석 방향을 잡았고, 채점 기준을 직접 점검해 부족한 항목(Polars, Plotly, sklearn Pipeline+joblib, 주석)을 찾아 보완을 지시했다.
### **실행 결과**
`main.py` 실행 한 번으로 아래가 순서대로 재현된다.
```plain text
pandas load: 0.79s, shape=(18999282, 6)
polars load: 0.21s, shape=(18999282, 6)
after ratecode+weekday filter: 9,368,324
after outlier removal: 9,068,562

=== 선형회귀 (Pipeline: StandardScaler + LinearRegression) ===
RMSE: 4.127   MAE: 2.433   R^2: 0.9335
model saved: models/total_amount_regression_pipeline.joblib

=== t-test + Cohen's d (v3, 낮 vs 심야) ===
speed_mph: diff -48.36%, cohens_d -1.53 (큼)
```
### **주요 코드 설명**
- `main.py`: `SCRIPTS` 리스트에 정의된 스크립트를 `subprocess.run`으로 순서대로 호출. 하나라도 실패하면 `check=True`로 즉시 중단되어 중간 단계 오류가 조용히 넘어가지 않도록 함
- `02_preprocess.py`: Pandas·Polars 양쪽으로 원본 parquet을 로딩해 shape을 `assert`로 검증하고 결측치를 `isnull()`/`null_count()`로 명시적으로 확인한 뒤, `RatecodeID==1`·평일·이상치 조건으로 필터링해 분석용 단일 parquet으로 저장
- `06_analysis_v2.py`, `08_analysis_v3.py`: `speed_mph = trip_distance / (trip_duration_minutes/60)` 등 파생 변수를 만들고, `cohens_d()` 함수로 표본 크기에 흔들리지 않는 효과크기를 계산해 p-value의 한계를 보완
- `04_model.py`: `Pipeline([("scaler", StandardScaler()), ("reg", LinearRegression())])`로 전처리와 모델을 하나로 묶어 학습하고 `joblib.dump()`로 저장, 재사용 시 스케일링 누락 위험을 없앰
### **결과 해석**
`total_amount`만 비교했을 때는 출퇴근/비출퇴근 차이가 거의 없어(Cohen's d=-0.04) 분석이 실패한 것처럼 보였다. 하지만 이는 거리(짧아짐)와 정체로 인한 시간요금(늘어남)이 총액에서 서로 상쇄된 결과였고, `speed_mph`·`fare_per_mile`로 쪼개보니 방향이 뚜렷하게 드러났다. 더 나아가 "출퇴근 vs 비출퇴근"이라는 그룹 정의 자체가 성질이 반대인 심야(빠름)와 낮(막힘)을 한 그룹으로 묶고 있었다는 걸 발견해, 시간대 밴드를 다시 나누고서야 실질적으로 큰 효과(속도 d=-1.53)를 확인할 수 있었다. 지표 하나, p-value 하나만으로 결론 내리면 안 된다는 걸 이번 분석에서 직접 확인했다.
### **개선 사항**
- 지금은 2026년 1\~5월만 사용했는데, 요일별(월\~금 개별) 또는 계절별 세분화를 추가하면 "낮 시간대 정체"가 특정 요일에 쏠려 있는지 확인 가능
- 회귀 모델이 선형회귀 하나뿐이라, 트리 기반 모델(RandomForest 등)과 비교하면 `is_rush_hour`·`pickup_hour`의 비선형 효과를 더 잘 잡을 수 있을 것
- `models/`에 저장한 파이프라인을 실제로 다시 불러와 예측하는 검증 스크립트(`joblib.load` 후 샘플 예측)가 없어서, 저장은 했지만 "제대로 저장됐는지"를 자동으로 확인하는 절차는 아직 없음
