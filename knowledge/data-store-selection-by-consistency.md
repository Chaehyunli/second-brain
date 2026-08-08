---
schema_version: 1
id: knowledge-data-store-selection-by-consistency
title: 일관성과 작업 부하에 따른 데이터 저장소 선택
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-08
checked_at: 2026-08-08
tags: [knowledge, initial-curation]
sources:
  - notion/SKALA/7-27 스마트 데이터 이해 및 활용_Day1/7-27 스마트 데이터 이해 및 활용_Day1 핵심 정리.md
  - notion/SKALA/7-28 스마트 데이터 이해 및 활용_Day2/7-28 스마트 데이터 이해 및 활용_Day2 핵심 정리.md
  - notion/Information/2026-07-26 — Cloudflare 실전 가이드 — Workers·Pages·KV·D1·VPS·AWS·CI-CD.md
---

# 일관성과 작업 부하에 따른 데이터 저장소 선택

## 시작점: 어떤 작업을 보장해야 하는가
저장소 선택은 제품 이름보다 트랜잭션 일관성, 조회·집계 모양, 권한, 지연·복구 요구에서 시작한다.

## 역할을 나눈 지도
트랜잭션 원장, 파일·객체, 캐시·설정, 벡터 인덱스는 같은 값을 가질 수 있어도 진실 원천과 조회 목적이 다르다. Day1·Day2의 SQL·벡터/그래프·분석 학습과 Cloudflare의 KV·D1·Vectorize 역할은 이 분리를 보여 준다.

## 선택 매트릭스
즉시 일관성이 필요한 변경은 원장 역할의 저장소에서 확인한다. 반복 조회는 캐시를, 유사도 검색은 벡터 인덱스를 후보로 검토하되 원본 메타데이터와 권한 검증을 분리한다.

## 배치·운영과의 관계
저장 위치와 복제·네트워크·장애조치는 [[knowledge/resilient-deployment-and-data-infrastructure]]에서 다루는 운영 경계에 영향을 준다.

## 피해야 할 단정
캐시를 즉시 일관성이 필요한 진실 원천으로 보거나, 특정 제품의 consistency 보장을 설정·공식 문서 확인 없이 일반화하지 않는다.

## 근거
- [[notion/SKALA/7-27 스마트 데이터 이해 및 활용_Day1/7-27 스마트 데이터 이해 및 활용_Day1 핵심 정리]]
- [[notion/SKALA/7-28 스마트 데이터 이해 및 활용_Day2/7-28 스마트 데이터 이해 및 활용_Day2 핵심 정리]]
- [[notion/Information/2026-07-26 — Cloudflare 실전 가이드 — Workers·Pages·KV·D1·VPS·AWS·CI-CD]]
