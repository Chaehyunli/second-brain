---
title: "대규모 백엔드 인프라 아키텍처 및 배포 전략 - Ngnix, Load Balancer, 웹/앱"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: ["blog", "technical-writing", "load balancer", "ngnix", "배포"]
category: "기타"
published: 2026-06-12
source_url: https://ch010104.tistory.com/284
---

# 대규모 백엔드 인프라 아키텍처 및 배포 전략 - Ngnix, Load Balancer, 웹/앱

## 원문

https://ch010104.tistory.com/284

## 핵심 요약

- **1. 대규모 백엔드 인프라 아키텍처: 트래픽 분산과 동기화** — 초기 서비스는 단일 서버(Single Server)로 시작하지만, 트래픽 폭주 시 서버의 사양을 높이는 스케일 업(Scale-Up)에는 물리적/비용적 한계가 존재합니다.
- **1.1. 로드 밸런서 (Load Balancer)와 Nginx 심화** — 로드 밸런서는 하나의 공인 주소(Domain/IP)로 들어오는 수많은 사용자의 요청을 뒤에 대기 중인 여러 대의 백엔드 서버(K대)로 균등하게 분배해 주는 최전선 문지기이자 트래픽 지휘관입니다.
- **L4 vs L7 로드 밸런서** — L4 로드 밸런서 (네트워크/전송 계층): IP 주소와 포트(Port) 번호만 보고 트래픽을 분산합니다.
- **💡 Nginx 로드 밸런싱 및 헬스 체크 설정 (nginx.conf)** — Nginx를 리버스 프록시(Reverse Proxy) 및 로드 밸런서로 사용할 때, 단순히 트래픽만 나누는 것이 아니라 장애가 발생한 서버를 격리(Health Check)하고 가중치(Weight)를 부여할 수 있습니다.

## 관련 글

- [[blog/기타/index|기타]]
- [[blog/GCP/GCP- GCP로 프로젝트 배포하기 - ( 6 ) GCS 란- GCS 생성하기|[GCP] GCP로 프로젝트 배포하기 - ( 6 ) GCS 란?  GCS 생성하기]]
- [[blog/GCP/GCP- GCP로 프로젝트 배포하기 - ( 6 ) GCP VPC 생성하기 (89)|[GCP] GCP로 프로젝트 배포하기 - ( 6 ) GCP VPC 생성하기]]
- [[blog/GCP/GCP- GCP로 프로젝트 배포하기 - ( 6 ) GCP VPC 생성하기|[GCP] GCP로 프로젝트 배포하기 - ( 6 ) GCP VPC 생성하기]]
