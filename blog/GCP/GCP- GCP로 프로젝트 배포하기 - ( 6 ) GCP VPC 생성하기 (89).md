---
title: "[GCP] GCP로 프로젝트 배포하기 - ( 6 ) GCP VPC 생성하기"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "GCP", "배포"]
category: "GCP"
published: 2025-05-28
source_url: https://ch010104.tistory.com/89
---

# [GCP] GCP로 프로젝트 배포하기 - ( 6 ) GCP VPC 생성하기

## 원문

https://ch010104.tistory.com/89

## 노트 유형

`project`

## 배경·목표·적용 맥락

방화벽은 네트워크 보안을 위한 장치로, **"어떤 트래픽이 내 서버로 들어올 수 있는지 / 나갈 수 있는지를 제어하는 규칙"**을 설정

리버스 프록시나 도메인 연동 전에 직접 포트 접근 가능하게 열어둔 상태

## 구현·의사결정·결과

### 1. 방화벽(Firewall)이란?

방화벽은 네트워크 보안을 위한 장치로, **"어떤 트래픽이 내 서버로 들어올 수 있는지 / 나갈 수 있는지를 제어하는 규칙"**을 설정

GCP 방화벽 특징

GCP에서는 VPC 단위로 방화벽이 적용됨

기본적으로 모든 인바운드(수신) 트래픽은 차단되어 있음

아웃바운드(발신)는 기본 허용

VPC 네트워크 - 방화벽 - 방화벽 규칙 추가

### 2. GCP 방화벽의 주요 구성 요소

### 3. 내가 만든 방화벽 규칙 요약

1) SSH 접속 허용

```text
이름: allow-ssh
포트: TCP:22
소스 IP: 0.0.0.0/0
설명: 모든 외부에서 VM에 SSH 접속 허용
```

필수 규칙. 이게 없으면 GCP VM에 SSH 접속 불가

2) Spring Boot API 포트 허용

```text
이름: allow-8080
포트: TCP:8080
소스 IP: 0.0.0.0/0
설명: 프론트엔드 또는 외부에서 백엔드 API 접속 허용
```

리버스 프록시나 도메인 연동 전에 직접 포트 접근 가능하게 열어둔 상태

3) Cloud SQL (MySQL) 내부 접속 허용

```text
이름: allow-mysql
포트: TCP:3306
소스 IP: 10.10.0.0/24
설명: 동일 VPC 내부에서만 DB 접속 허용
```

외부에서 DB 접근 못 하게 하고, 같은 서브넷 내 VM만 접근 가능하도록 제한함

4) Redis 내부 접속 허용

```text
이름: allow-redis
포트: TCP:6379
소스 IP: 10.10.0.0/24
설명: VM이 내부 Redis에 연결할 수 있도록 허용
```

보안 강화를 위해 Redis도 외부 노출 없이 내부 통신만 허용

### 5. 방화벽 규칙 만들기 팁

## 관련 글

- [[blog/GCP/index|GCP]]
- [[blog/GCP/GCP- GCP로 프로젝트 배포하기 - ( 6 ) GCP VPC 생성하기|[GCP] GCP로 프로젝트 배포하기 - ( 6 ) GCP VPC 생성하기]]
- [[blog/GCP/GCP- GCP로 프로젝트 배포하기 - ( 6 ) GCS 란- GCS 생성하기|[GCP] GCP로 프로젝트 배포하기 - ( 6 ) GCS 란?  GCS 생성하기]]
- [[blog/GCP/GCP- GCP로 프로젝트 배포하기 - ( 5 ) GCP VPC 란|[GCP] GCP로 프로젝트 배포하기 - ( 5 ) GCP VPC 란?]]
