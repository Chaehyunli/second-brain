---
title: 노소공
created: 2026-07-10
updated: 2026-07-10
type: entity
tags:
  [
    project,
    backend,
    python,
    fastapi,
    machine-learning,
    data-engineering,
    database,
    architecture,
  ]
sources: [raw/sources/employment-zip-2026-07-10.md]
confidence: high
---

# 노소공 — Interactive pet growth service

## Overview

2025-03~2025-10 진행한 인터랙티브 펫 육성 팀 프로젝트. FastAPI 기반 백엔드와 XGBoost 감정 변화 예측 모델링을 담당했다.

## Key decisions and implementation

- 사용자·펫·재화·보상 도메인의 ERD와 FastAPI API를 설계·구현했다.
- Pygame 코드를 React 런타임에 그대로 이식할 수 없다는 호환성 문제를 조기에 식별했다. 코드는 설계도로만 활용하고, 프런트엔드가 웹 환경에 맞게 재구현하도록 협업 방향을 전환했다.
- 클라이언트 미니게임 결과 조작 가능성을 고려해 서버 검증 후 보상을 지급하는 처리 흐름을 설계했다.
- 실제 플레이 로그가 없는 콜드 스타트 상황에서 행동·선호도·방치일·현재 감정 상태를 반영한 규칙 기반 생성 함수로 10,000건의 합성 데이터를 만들었다.
- 범주형 전처리 후 XGBoost Regressor를 학습해 테스트셋 R² 0.9964, RMSE 0.22를 기록했고 서버 기능에 연동했다.

## Portfolio role

[[entities/lim-chae-hyun]]이 ML을 단순 모델 학습이 아니라 서비스 요구·데이터 생성·API 통합까지 연결했음을 보여준다. [[concepts/backend-portfolio-narrative]]에서는 콜드 스타트 해결과 런타임 호환성 판단을 핵심 사례로 다룬다.
