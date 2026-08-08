---
schema_version: 1
id: knowledge-machine-learning-lifecycle-and-validation
title: ML 수명주기와 검증 경계
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-08
checked_at: 2026-08-08
tags: [knowledge, initial-curation]
sources:
  - blog/AI(ML & DL)/기계학습- ML 프로젝트 A-Z 까지 ( 1 ).md
  - blog/AI(ML & DL)/기계학습- ML 프로젝트 A - Z 까지 ( 6 ).md
  - entities/projects/nosogong.md
---

# ML 수명주기와 검증 경계

## 수명주기 지도
ML 결과물은 문제·성공 기준, 데이터와 분할, 전처리·후보 모델, 비교·검증, 배포·모니터링이 이어진 체계다.

## 데이터에서 모델까지
A–Z 학습 기록은 데이터 탐색, 전처리, 모델 비교, RMSE/MAE와 과소·과적합 진단을 연결한다. 지표는 목표와 데이터 분할 맥락 안에서만 해석한다.

## 배포 뒤에도 남는 일
운영 데이터 변화, 모니터링, 재학습 조건을 정의하지 않으면 한 번의 테스트 점수로 수명주기를 닫을 수 없다.

## 제품 사례로 적용할 때
[[knowledge/cold-start-ml-product-boundaries]]의 노소공 사례는 합성 규칙 데이터와 XGBoost API 통합을 보여 준다. 그 수치는 합성 분포의 검증이며 실제 사용자 일반화·운영 효과는 별도 검증 대상이다.

## 지표 해석의 한계
RMSE/MAE나 R² 하나로 공정성, 사용자 가치, 장기 성능을 단정하지 않는다.

## 근거
- [[blog/AI(ML & DL)/기계학습- ML 프로젝트 A-Z 까지 ( 1 )]]
- [[blog/AI(ML & DL)/기계학습- ML 프로젝트 A - Z 까지 ( 6 )]]
- [[entities/projects/nosogong]]
