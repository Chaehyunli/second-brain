---
title: "[GCP] GCP로 프로젝트 배포하기 - ( 6 ) GCP VPC 생성하기"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: [blog, technical-writing]
category: "GCP"
published: 2025-05-28
source_url: https://ch010104.tistory.com/89
archive_method: Tistory sitemap + HTML content extraction
---

# [GCP] GCP로 프로젝트 배포하기 - ( 6 ) GCP VPC 생성하기

> 원문: https://ch010104.tistory.com/89

## 본문

1. 방화벽(Firewall)이란?  방화벽은 네트워크 보안을 위한 장치로, **"어떤 트래픽이 내 서버로 들어올 수 있는지 / 나갈 수 있는지를 제어하는 규칙"**을 설정  GCP 방화벽 특징  GCP에서는 VPC 단위로 방화벽이 적용됨 기본적으로 모든 인바운드(수신) 트래픽은 차단되어 있음 아웃바운드(발신)는 기본 허용 VPC 네트워크 - 방화벽 - 방화벽 규칙 추가   2. GCP 방화벽의 주요 구성 요소     항목 설명   이름 규칙의 이름. 어떤 용도로 만들었는지 구분용   네트워크 해당 방화벽 규칙을 적용할 VPC   우선순위 숫자가 낮을수록 우선 적용됨 (기본: 1000)   트래픽 방향 인그레스(Ingress) = 외부 → 내부 / 이그레스(Egress) = 내부 → 외부   일치 시 작업 허용(Allow) 또는 거부(Deny)   소스 트래픽이 어디서 오는지 (IP 범위)   프로토콜 및 포트 허용할 포트번호 (예: TCP:22, TCP:8080 등)   대상 이 규칙이 적용될 VM 대상 (전부 or 특정 태그)        3. 내가 만든 방화벽 규칙 요약 1) SSH 접속 허용   이름: allow-ssh 포트: TCP:22 소스 IP: 0.0.0.0/0 설명: 모든 외부에서 VM에 SSH 접속 허용      필수 규칙. 이게 없으면 GCP VM에 SSH 접속 불가   2) Spring Boot API 포트 허용   이름: allow-8080 포트: TCP:8080 소스 IP: 0.0.0.0/0 설명: 프론트엔드 또는 외부에서 백엔드 API 접속 허용      리버스 프록시나 도메인 연동 전에 직접 포트 접근 가능하게 열어둔 상태     3) Cloud SQL (MySQL) 내부 접속 허용   이름: allow-mysql 포트: TCP:3306 소스 IP: 10.10.0.0/24 설명: 동일 VPC 내부에서만 DB 접속 허용      외부에서 DB 접근 못 하게 하고, 같은 서브넷 내 VM만 접근 가능하도록 제한함     4) Redis 내부 접속 허용   이름: allow-redis 포트: TCP:6379 소스 IP: 10.10.0.0/24 설명: VM이 내부 Redis에 연결할 수 있도록 허용      보안 강화를 위해 Redis도 외부 노출 없이 내부 통신만 허용     5. 방화벽 규칙 만들기 팁     상황 포트 소스 IP 설명   외부에서 SSH 접속 22 0.0.0.0/0 필수 (테스트 끝나면 IP 제한 권장)   React에서 Spring 호출 8080 0.0.0.0/0 초기 개발용   내부에서 Cloud SQL 접근 3306 10.10.0.0/24 배포 환경 필수   내부 Redis 접근 6379 10.10.0.0/24 배포 환경 필수
