---
title: "[데이터베이스 설계] 비용 추정을 위한 통계 1 (STATISTICS FOR COST ESTIMATION)"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "Database", "Design"]
category: "DATABASE DESIGN"
published: 2025-10-27
source_url: https://ch010104.tistory.com/171
---

# [데이터베이스 설계] 비용 추정을 위한 통계 1 (STATISTICS FOR COST ESTIMATION)

## 원문

https://ch010104.tistory.com/171

## 노트 유형

`guide`

## 적용 목적과 전제조건

- 데이터베이스 시스템 카탈로그는 비용 추정을 위해 다음 통계 정보를 유지함

f_r: 릴레이션 r의 블로킹 팩터 (하나의 디스크 블록에 저장할 수 있는 최대 튜플 수)

## 구현 절차·검증·주의점

### 비용 추정을 위한 통계 정보

- 데이터베이스 시스템 카탈로그는 비용 추정을 위해 다음 통계 정보를 유지함

n_r: 릴레이션 r의 튜플 수

l_r: 릴레이션 r의 튜플 크기

b_r: 릴레이션 r의 튜플을 포함하는 블록 수

f_r: 릴레이션 r의 블로킹 팩터 (하나의 디스크 블록에 저장할 수 있는 최대 튜플 수)

V(A, r): 릴레이션 r의 속성 A에 나타나는 고유 값(distinct values)의 수

이는 Pi_A(r)의 크기와 동일함

만약 A가 키(key)라면, 튜플 수(n_r)와 동일함

릴레이션 r의 튜플이 물리적으로 파일에 함께 저장되는 경우, 블록 수 b_r는 [n_r / f_r]로 계산됨

### 비용 추정을 위한 근사치 접근 (페이지 28)

통계 정보는 매번 계산하기에 비용이 크므로 근사치를 이용해 계산

정확한 통계를 유지하기 위해 릴레이션이 수정될 때마다 통계를 업데이트하면 상당한 오버헤드가 발생함

대부분의 시스템은 매번 수정 시 통계를 업데이트하는 대신, 시스템 부하가 적은 기간(light system load)에 통계를 업데이트함

이로 인해 쿼리 처리 전략 선택에 사용되는 통계가 완전히 정확하지 않을 수 있음

하지만 통계 업데이트 간격 사이에 수정이 많지 않다면, 통계는 충분히 정확

히스토그램

실제 옵티마이저들은 비용 추정의 정확도를 높이기 위해 추가적인 통계 정보를 유지함

대부분의 데이터베이스는 각 속성의 값 분포(distribution of values)를 히스토그램으로 저장함

히스토그램은 속성 도메인의 단순 범위(예: 1-25)뿐만 아니라, 그 값들이 사이에 어떤 분포를 가지고 있는지를 보여줌

활용 예시:

(차트에서) 11-15 범위의 값이 30개의 빈도(frequency)를 가지므로, 이 범위 내의 특정 값은 대략 6개 정도 있을 것이라고 참고하여 계산함

이는 완전히 정확한 추정(estimate)은 아니지만, 근사값을 이용해 통계 정보를 사용하는 방식

🔍 선택(Selection) 크기 추정

히스토그램 같은 분포 정보가 있다면 그것을 사용하지만, 정보가 없다면 모든 값이 균등하게 분포(uniform distribution)되어 있다고 가정하고 추정함

등가 선택

결과를 만족하는 레코드 수 추정치: n_r / V(A, r)

V(A, r)은 속성 A가 가질 수 있는 값의 수. n_r / V(A, r)은 해당 속성의 한 값이 평균 몇 개의 튜플을 가질지 예상하는 값임

속성 A에 히스토그램이 있다면 더 정확한 추정이 가능함

범위 선택

c를 조건을 만족하는 추정 튜플 수라고 할 때

만약 카탈로그에 min(A, r)과 max(A, r) 값이 있다면:

v < min(A, r) 이면 c = 0

c = n_r * { v - min(A, r) } / {max(A, r) - min(A, r)} (전체 값 범위에서 v가 차지하는 비율만큼으로 추정)

히스토그램 정보가 있다면, 이 추정치는 더 개선될 수 있음

통계 정보가 없는 경우, c는 n_r / 2 로 가정함

복합 선택(Complex Selections) 크기 추정

선택도 (Selectivity):

특정 WHERE 조건절이 얼마나 까다로운지(specific)를 0과 1 사이의 비율(확률)로 나타낸 값

조건 theta_i의 선택도는 릴레이션의 튜플이 theta_i를 만족할 확률임

s_i가 theta_i를 만족하는 튜플 수일 때, 선택도는 s_i / n_r

Conjunction (AND 연산):

각 조건이 독립적(independence)이라고 가정함

결과 튜플 추정치: n_r * {s1 * s2 * .... * sn} / n_r^2

복합 선택(Complex Selections) 크기 추정

Disjunction (OR 연산):

추정 튜플 수: n_r \cdot (1 - (1 - \frac{s_1}{n_r}) \cdot (1 - \frac{s_2}{n_r}) \cdot ... \cdot (1 - \frac{s_n}{n_r}))

(설명: 전체 1에서 (s1을 만족하지 않을 확률) $\times$ (s2를 만족하지 않을 확률) $\times$ ... 을 뺀 값)

Negation (NOT 연산):

추정 튜플 수: n_r - \text{size}(\sigma_{\theta}(r))

## 관련 글

- [[blog/DATABASE DESIGN/index|DATABASE DESIGN]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 비용 추정을 위한 통계 2 (MATERIALIZED VIEWS)|[데이터베이스 설계] 비용 추정을 위한 통계 2 (MATERIALIZED VIEWS)]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 쿼리 최적화 (Query Optimization)|[데이터베이스 설계] 쿼리 최적화 (Query Optimization)]]
- [[blog/DATABASE DESIGN/데이터베이스 설계- 트랜젝션과 Serializability|[데이터베이스 설계] 트랜젝션과 Serializability]]
