---
title: "[딥러닝] Gradient 및 자동 미분(Autogradient)"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: [blog, technical-writing]
category: "AI(ML & DL)"
published: 2025-11-11
source_url: https://ch010104.tistory.com/184
archive_method: Tistory sitemap + HTML content extraction
---

# [딥러닝] Gradient 및 자동 미분(Autogradient)

> 원문: https://ch010104.tistory.com/184

## 본문

계산 그래프 (Computation Graph)  정의: 입력 데이터(x)와 모델 파라미터(w)를 받아, 최종 예측값을 계산하는 과정을 일련의 연산 노드(+, *, exp, 1/x 등)로 표현한 그래프 예시 함수:      계산 그래프 예시 상세 1. 초기값 설정  w0 = 2.00 x0 = -1.00 w1 = -3.00 x1 = -2.00 w2 = -3.00  2. Forward Pass (순전파)   3. Backward Pass (역전파)  원리: 체인룰(Chain Rule)을 사용하여 $\frac{\partial L}{\partial x}=\frac{\partial\sigma}{\partial x}\frac{\partial L}{\partial\sigma}$ 와 같이 그래디언트를 역방향으로 전파 용어: Downstream Gradient = Upstream Gradient $\times$ Local Gradient 시작: 최종 출력(0.73)의 그래디언트를 1.00으로 가정하고 시작. 1) $1/x$ 노드:  입력값: 1.37 Local Gradient ( $f(x)=1/x$ 의 미분 $\rightarrow -1/x^2$ ): $-1 / (1.37^2) Upstream Gradient: 1.00 Downstream Gradient: $1.00 \times (-1 / 1.37^2) = \mathbf{-0.53}$   2) $+1$ 노드:  입력값: 0.37 Local Gradient ( $f(x)=c+x$ 의 미분 $\rightarrow 1$ ): $1$ Upstream Gradient: -0.53 Downstream Gradient: $-0.53 \times 1 = \mathbf{-0.53}$    3) $exp$ 노드:  입력값: -1.00 Local Gradient ( $f(x)=e^x$ 의 미분 $\rightarrow e^x$ ): $e^{-1}$ Upstream Gradient: -0.53 Downstream Gradient: $-0.53 \times e^{-1} = \mathbf{-0.20}$   4) $\times -1$ 노드:  입력값: 1.00 Local Gradient ( $f(x)=ax$ 의 미분 $\rightarrow a$ ): $-1$ Upstream Gradient: -0.20 Downstream Gradient: $-0.20 \times -1 = \mathbf{0.20}$   5) $+$ 노드 ( $q4 = q3 + w2$ ):  Local Gradient ( $\frac{dq4}{dq3}$ 및 $\frac{dq4}{dw2}$ ): 둘 다 1 Upstream Gradient: 0.20 Downstream Gradient ( $q3$ 으로): $0.20 \times 1 = \mathbf{0.20}$ Downstream Gradient ( $w2$ 로): $0.20 \times 1 = \mathbf{0.20}$ ( $\leftarrow$ w2의 그래디언트 )   6) $+$ 노드 ( $q3 = q1 + q2$ ):  Upstream Gradient: 0.20 ( $q3$ 에서 전달됨) Downstream Gradient ( $q1$ 으로): $0.20 \times 1 = \mathbf{0.20}$ Downstream Gradient ( $q2$ 로): $0.20 \times 1 = \mathbf{0.20}$   7) $\times$ 노드 ( $q1 = w0 \times x0$ ):  Upstream Gradient: 0.20 ( $q1$ 에서 전달됨) Local Gradient ( $w0$ 에 대해): $x0 = -1.00$ Local Gradient ( $x0$ 에 대해): $w0 = 2.00$ Downstream Gradient ( $w0$ 로): $0.20 \times -1.00 = \mathbf{-0.20}$ ( $\leftarrow$ w0의 그래디언트 ) Downstream Gradient ( $x0$ 로): $0.20 \times 2.00 = \mathbf{0.40}$ ( $\leftarrow$ x0의 그래디언트 )   (참고) Sigmoid 블록의 미분:  시그모이드 함수 $\sigma(x)$의 미분은 $(1-\sigma(x))\sigma(x)$ Forward Pass에서 $\sigma(1.00) = 0.73$ 이었음 Local Gradient: $(1 - 0.73) \times 0.73 \approx 0.20$ 이는 $\times -1$, $exp$, $+1$, $1/x$ 노드들을 통과한 그래디언트 값 0.20과 일치함     그래디언트 흐름의 패턴   Add Gate (덧셈): 그래디언트 분배기 (Gradient Distributor)  업스트림 그래디언트를 두 입력에 그대로 복사하여 전달함   Mul Gate (곱셈): 스왑 승수 (Swap Multiplier)   업스트림 그래디언트에 다른 쪽 입력의 값을 곱하여 전달함.  하나의 입력이 여러 노드로 분기된 경우, 각 브랜치에서 역전파된 그래디언트들을 모두 더함     Copy Gate (복사): 그래디언트 덧셈기 (Gradient Adder)  입력 중 최대값을 가졌던 노드에만 업스트림 그래디언트를 전달하고, 나머지는 0을 전달함.   Max Gate (최대값): 그래디언트 라우터 (Gradient Router)
