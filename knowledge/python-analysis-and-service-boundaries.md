---
schema_version: 1
id: knowledge-python-analysis-and-service-boundaries
title: Python의 분석 실험과 서비스 통합 경계
type: knowledge-note
status: verified
created: 2026-08-08
updated: 2026-08-08
checked_at: 2026-08-08
tags: [knowledge, python, data-analysis, machine-learning, backend]
sources:
  - entities/lim-chae-hyun.md
  - entities/projects/masil.md
  - entities/projects/nosogong.md
  - entities/projects/searchive.md
  - notion/SKALA/8-6 데이터 분석을 위한 Python 이해_Day1/8-6 데이터 분석을 위한 Python 이해_Day1 핵심 정리.md
  - notion/SKALA/8-6 데이터 분석을 위한 Python 이해_Day1/8-6 데이터 분석을 위한 Python 이해_Day1 실습.md
  - notion/SKALA/8-7 데이터 분석을 위한 Python 이해_Day2/8-7 데이터 분석을 위한 Python 이해_Day2 핵심 정리.md
  - notion/SKALA/8-7 데이터 분석을 위한 Python 이해_Day2/8-7 데이터 분석을 위한 Python 이해_Day2 실습.md
---

# Python의 분석 실험과 서비스 통합 경계

## 다루는 범위
이 노트는 Python 언어 개요가 아니라, 학습·분석 실험과 FastAPI 기반 서비스 기능이 만나는 지점을 근거로 연결한다.

## 두 작업면: 탐색과 실행
Day1은 `uv` 기반 환경·의존성 잠금, 함수·예외 처리, 파일 I/O와 실행 구조를 다룬다. Day2는 Pandas/Polars/DuckDB, 시각화, 통계 검정, sklearn Pipeline·joblib, 스크립트 기반 자동화를 분석 작업의 흐름으로 제시한다. 탐색 노트북과 재사용 가능한 `.py` 모듈은 역할을 분리한다.

## 분석 결론을 서비스 주장으로 바꾸지 않는 경계
Day2 택시 실습은 9백만 행 규모에서 지표 분해, 효과크기, 그룹 재정의로 결론을 수정한 사례다. p-value만으로 실질적 의미를 확정하지 않고 Cohen's d와 그룹 정의를 함께 검토했다. 이 분석 절차는 제품 성능이나 사용자 효과를 자동으로 증명하지 않는다.

## 프로젝트에서 확인된 Python의 역할
[[entities/projects/nosogong]]은 규칙 기반 합성 데이터 10,000건으로 XGBoost를 학습하고 FastAPI API 흐름에 연결했으며, 합성 데이터 평가를 실제 사용자 일반화로 과장하지 않는다. [[entities/projects/searchive]]는 FastAPI와 임베딩·키워드 추출을 검색 품질·지연 문제에 연결했다. [[entities/projects/masil]]은 FastAPI AI 서비스가 SSE와 일정·예약 컨텍스트를 다루는 Java WebFlux 백엔드와 분리돼 있음을 기록한다.

## 재현성과 운영의 관계
환경 잠금, 검증된 Pipeline 저장, 스크립트 실행 순서, 로그·테스트는 탐색 결과를 재실행 가능한 작업으로 바꾼다. 그러나 Day2 실습의 저장된 모델은 재로딩 예측 검증이 아직 없다고 기록되어 있으며, Masil·Searchive의 end-to-end 운영 성능도 이 근거만으로 확정하지 않는다.

## 관련 지식과 한계
[[knowledge/machine-learning-lifecycle-and-validation]]은 모델 검증 수명주기를, [[knowledge/performance-investigation-and-measurement-boundaries]]는 Searchive의 측정 범위를, [[knowledge/request-response-and-server-events]]는 Masil의 SSE 통신 경계를 보완한다. [[entities/lim-chae-hyun]]의 역량 지도는 사례의 위치를 보여 주지만 각 구현의 세부 증거는 위 프로젝트 원본에서 확인한다.

## 출처
- [[entities/lim-chae-hyun]]
- [[entities/projects/masil]]
- [[entities/projects/nosogong]]
- [[entities/projects/searchive]]
- [[notion/SKALA/8-6 데이터 분석을 위한 Python 이해_Day1/8-6 데이터 분석을 위한 Python 이해_Day1 핵심 정리]]
- [[notion/SKALA/8-6 데이터 분석을 위한 Python 이해_Day1/8-6 데이터 분석을 위한 Python 이해_Day1 실습]]
- [[notion/SKALA/8-7 데이터 분석을 위한 Python 이해_Day2/8-7 데이터 분석을 위한 Python 이해_Day2 핵심 정리]]
- [[notion/SKALA/8-7 데이터 분석을 위한 Python 이해_Day2/8-7 데이터 분석을 위한 Python 이해_Day2 실습]]
