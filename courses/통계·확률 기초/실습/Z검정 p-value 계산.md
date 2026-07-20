---
type: "course-note"
source_archive: "7a35b440ed3d4588.zip"
source_original_file: "p_valuetest.py"
---

# Z검정 p-value 계산

## 실습 목표
모집단 표준편차를 알고 있다는 가정에서 표본 평균이 기준 모평균과 다른지 **양측 Z검정**으로 판정한다. 계산식·코드·판단 기준을 하나의 흐름으로 연결한다.

## 문제 설정과 가설
- 기준 모평균: $\mu_0=100$
- 모집단 표준편차: $\sigma=5$
- 표본 수: $n=50$
- 표본 평균: $\bar{x}=101.5$
- 유의수준: $\alpha=0.05$
- 귀무가설 $H_0$: 평균은 100g이다.
- 대립가설 $H_1$: 평균은 100g과 다르다. (양측 검정)

## 계산 흐름
표본 평균을 검정하므로 개별 관측치의 표준편차가 아니라 **표본 평균의 표준오차**를 사용한다.

$$SE=\frac{\sigma}{\sqrt{n}}, \qquad Z=\frac{\bar{x}-\mu_0}{SE}$$

양측 p-value는 표준정규분포 누적분포함수 $\Phi$를 사용해 다음과 같이 구한다.

$$p=2\left(1-\Phi(|Z|)\right)$$

이 예제에서는 $SE\approx0.7071$, $Z\approx2.1213$, $p\approx0.0339$이다. 따라서 $p<0.05$이므로 귀무가설을 기각하며, 표본 평균은 100g과 통계적으로 유의하게 다르다고 해석한다.

## 원문 코드
```python
import numpy as np
from scipy.stats import norm

# 1. 시나리오 데이터
mu_0 = 100 # 귀무가설의 모평균 (기준 무게)
sigma = 5 # 모집단 표준편차 (알고 있다고 가정)
n = 50 # 표본 크기
x_bar = 101.5  # 표본 평균
alpha = 0.05 # 유의수준

# 2. 검정 통계량 Z 계산 (Z-score calculation)
std_error = sigma / np.sqrt(n)
z_score = (x_bar - mu_0) / std_error

# --- P-값 계산 부분 ---
# 3. P-값 계산
# 양측 검정 P-값: P = 2 * P(Z > |Z_score|)
# norm.cdf(Z_score)는 Z_score보다 작거나 같은 확률을 반환합니다.
# 1 - norm.cdf(|Z_score|)는 |Z_score|보다 크거나 같은 (꼬리) 확률을 반환합니다.
p_value = 2 * (1 - norm.cdf(abs(z_score)))
# --------------------

print(f"표준 오차 (Standard Error): {std_error:.3f} g")
print(f"계산된 검정 통계량 Z-score: {z_score:.3f}")
print(f"계산된 **P-값 (P-value)**: **{p_value:.4f}**")

# 양측 검정 임계 Z값 (Z-critical for Two-Tailed Test)
z_critical_two = norm.ppf(1 - alpha/2)

print("\n##  2. P-값 기반 최종 결론")
print(f"P-값: {p_value:.4f}")
print(f"유의수준 (alpha): {alpha:.4f}")

if p_value < alpha:
    print(f" {p_value:.4f} < {alpha:.4f} 이므로, 귀무가설 **기각**")
    print("해석: 과자 무게는 통계적으로 유의미하게 100g과 **다르다**고 결론 내릴 수 있습니다.")
else:
    print(" 귀무가설 기각 **실패**")
    print("해석: 과자 무게가 100g과 다르다고 볼 통계적 증거가 충분하지 않습니다.")
```

## 코드 읽기
1. `std_error`는 표본 평균의 변동성인 표준오차를 계산한다.
2. `z_score`는 표본 평균이 기준 평균에서 표준오차 몇 배만큼 떨어졌는지 나타낸다.
3. `norm.cdf(abs(z_score))`는 $|Z|$ 이하의 누적확률이고, `1 - ...`는 한쪽 꼬리확률이다.
4. 양측 검정이므로 꼬리확률을 2배 해 `p_value`를 만든다.
5. p-value를 유의수준과 비교해 기각 여부를 판단한다.

## 주의점
- p-value는 “귀무가설이 참일 확률”이 아니라, **귀무가설이 참이라고 가정할 때 현재만큼 또는 더 극단적인 결과가 나올 확률**이다.
- p-value가 크다고 귀무가설이 참으로 증명되는 것은 아니다. 기각할 증거가 부족하다는 뜻이다.
- Z검정은 모집단 표준편차를 알고 있거나 그 가정이 정당할 때 사용한다. 표준편차를 모르면 일반적으로 [[courses/통계·확률 기초/11 t검정|t검정]]을 검토한다.

## 연결
개념 설명: [[courses/통계·확률 기초/09 p-value와 Z검정|p-value·Z검정]] · 표준화: [[courses/통계·확률 기초/08 표준정규분포|표준정규분포]]
