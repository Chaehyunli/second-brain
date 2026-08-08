---
schema_version: 1
id: knowledge-cold-start-ml-product-boundaries
title: 콜드스타트 ML의 제품 통합 경계
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-08
checked_at: 2026-08-08
tags: [knowledge, initial-curation]
sources:
  - entities/projects/nosogong.md
  - raw/sources/nosogong-detail-2026-03-08.md
  - knowledge/machine-learning-lifecycle-and-validation.md
---

# 콜드스타트 ML의 제품 통합 경계

## 제품 제약
노소공은 실제 플레이 로그가 없는 상태에서 펫 행동에 따른 감정 변화를 일관되게 다뤄야 했다.

## 선택한 출발점
동물·행동 선호도, 현재 감정, 편애도·반복, 방치 일수 규칙으로 10,000개 입력과 답을 만든 뒤 범주형 전처리와 XGBoost Regressor를 연결했다. 이는 제품 규칙을 초기 API 흐름에 연결한 선택이다.

## 현재 검증이 말해 주는 것
기록된 테스트셋 R² 0.9964, RMSE 0.22는 합성 규칙 패턴에 대한 측정이다. 감정 변화 API 흐름이 구성됐다는 사실과 실제 사용자 행동 예측의 일반화는 다른 주장이다.

## 전환 조건
실사용 로그가 누적되면 데이터 품질, 분할 방식, 재학습·배포 후 검증을 새로 정해야 한다. [[knowledge/machine-learning-lifecycle-and-validation]]은 이 사례가 이어서 충족해야 할 수명주기 검증 경계를 설명한다.

## 이 사례에서 말하지 않는 것
합성 데이터 점수는 운영 효과, 사용자 만족도, 실제 행동 분포에 대한 성능을 증명하지 않는다.

## 출처
- [[entities/projects/nosogong]]
- [[raw/sources/nosogong-detail-2026-03-08]]
- [[knowledge/machine-learning-lifecycle-and-validation]]
