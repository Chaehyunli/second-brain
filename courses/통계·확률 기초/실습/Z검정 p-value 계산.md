---
type: "course-note"
source_archive: "7a35b440ed3d4588.zip"
source_original_file: "p_valuetest.py"
---
# Z검정 p-value 계산

상위: [[courses/통계·확률 기초/index|통계·확률 기초]]

## 실습 목적
모표준편차를 안다는 가정 아래 과자 평균 무게가 기준 100g과 다른지 **양측 Z검정**으로 판단한다.

## 코드 흐름
1. 기준 평균 `mu_0=100`, 모표준편차 `sigma=5`, 표본 수 `n=50`, 표본 평균 `x_bar=101.5`를 둔다.
2. 표준오차 $SE=σ/√n$, Z통계량 $Z=(x̄-μ_0)/SE$를 계산한다.
3. `norm.cdf`로 양측 p-value $2(1-Φ(|Z|))$를 구한다.
4. $p<α=0.05$이면 귀무가설을 기각한다.

## 원문 코드
```python
import numpy as np
from scipy.stats import norm

std_error = sigma / np.sqrt(n)
z_score = (x_bar - mu_0) / std_error
p_value = 2 * (1 - norm.cdf(abs(z_score)))
```

## 연결
개념 설명: [[courses/통계·확률 기초/09 p-value와 Z검정|p-value·Z검정]] · 표준화: [[courses/통계·확률 기초/08 표준정규분포|표준정규분포]]
