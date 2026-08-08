---
schema_version: 1
id: knowledge-resilient-deployment-and-data-infrastructure
title: 복원력 있는 배포·데이터 인프라
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-08
checked_at: 2026-08-08
tags: [knowledge, initial-curation]
sources:
  - blog/SPRING BOOT/Spring Boot- 11. Cluster DB.md
  - blog/GCP/GCP- GCP로 프로젝트 배포하기 - ( 5 ) GCP VPC 란.md
  - notion/Information/2026-07-26 — Cloudflare 실전 가이드 — Workers·Pages·KV·D1·VPS·AWS·CI-CD.md
---

# 복원력 있는 배포·데이터 인프라

## 장애를 전제로 묻는 것
시작 순서, 네트워크 노출, DB 복제·풀링, 헬스체크, 복구 절차는 서로 다른 운영 책임이다.

## 배포 토폴로지와 책임 분리
컨테이너 의존 선언만으로 서비스 준비가 보장되지는 않는다. edge·VPS·DB 계층을 나누고, VPC의 서브넷·방화벽·라우팅으로 노출 경계를 정한다.

## 데이터 계층
DB 복제·읽기 분산·프록시·connection pool은 가용성과 부하를 다루지만 쓰기 일관성·장애조치 조건까지 검증해야 한다.

## 운영 절차
시작 순서와 헬스체크, 관측 신호, 장애조치와 복구를 함께 문서화한다. 배포 변경의 preview·production·rollback 흐름은 [[knowledge/git-flow-ci-cd-and-secret-boundaries]]와 연결된다.

## 관리형 서비스의 경계
관리형 기능·제한·가격·SLO는 시점에 따라 달라진다. 이 기록은 특정 서비스가 현재 요구를 충족한다는 증명이 아니며 공식 문서와 운영 설정 확인이 필요하다.

## 근거
- [[blog/SPRING BOOT/Spring Boot- 11. Cluster DB]]
- [[blog/GCP/GCP- GCP로 프로젝트 배포하기 - ( 5 ) GCP VPC 란]]
- [[notion/Information/2026-07-26 — Cloudflare 실전 가이드 — Workers·Pages·KV·D1·VPS·AWS·CI-CD]]
