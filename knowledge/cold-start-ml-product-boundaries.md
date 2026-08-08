---
schema_version: 1
id: knowledge-cold-start-ml-product-boundaries
title: 콜드스타트 ML의 제품 통합 경계
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-06
checked_at: 2026-08-06
tags: [knowledge, initial-curation]
sources:
  - entities/projects/nosogong.md
  - raw/sources/nosogong-detail-2026-03-08.md
  - knowledge/machine-learning-lifecycle-and-validation.md
---

# 콜드스타트 ML의 제품 통합 경계

## 핵심
초기 데이터가 부족할 때 규칙 기반 합성 데이터는 제품 흐름을 검증하는 출발점이 될 수 있지만, 실제 사용자 예측 성능을 증명하지는 않는다.

## 연결된 근거
- [[entities/projects/nosogong.md]]
- [[raw/sources/nosogong-detail-2026-03-08.md]]
- [[knowledge/machine-learning-lifecycle-and-validation.md]]

## 적용 기준
Nosogong의 규칙 유래 10,000건·XGBoost·서버 검증과 ML 검증 수명주기를 연결한다.

## 주의점 또는 한계
합성 데이터 R²/RMSE를 실사용 일반화 성능으로 표현하지 않으며, 실제 데이터 수집·재학습 전환 기준이 필요하다.
