---
title: "[GCP] GCP로 프로젝트 배포하기 - ( 1 ) GCP 란?"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "GCP"]
category: "GCP"
published: 2025-05-24
source_url: https://ch010104.tistory.com/79
---

# [GCP] GCP로 프로젝트 배포하기 - ( 1 ) GCP 란?

## 원문

https://ch010104.tistory.com/79

## 노트 유형

`project`

## 배경·목표·적용 맥락

GCP는 Google Cloud Platform의 약자로, 구글에서 제공하는 클라우드 컴퓨팅 서비스

GCP는 다양한 클라우드 서비스(예: 컴퓨팅, 스토리지, 데이터베이스, 머신러닝 등)를 제공하여 사용자가 애플리케이션을 개발, 배포 및 운영할 수 있도록 지원

## 구현·의사결정·결과

### 1. GCP 란?

GCP는 Google Cloud Platform의 약자로, 구글에서 제공하는 클라우드 컴퓨팅 서비스

GCP는 다양한 클라우드 서비스(예: 컴퓨팅, 스토리지, 데이터베이스, 머신러닝 등)를 제공하여 사용자가 애플리케이션을 개발, 배포 및 운영할 수 있도록 지원

GCP를 사용하면 인프라를 직접 관리할 필요 없이 구글의 글로벌 인프라를 활용하여 확장 가능하고 안정적인 애플리케이션을 구축 가능

### 2. 주요 클라우드 플랫폼의 비교

1) GCP (Google Cloud Platform)

장점

Google의 강력한 데이터 분석 및 머신러닝 도구 제공 (BigQuery, TensorFlow 등)

Kubernetes의 창시자로서 강력한 컨테이너 관리 서비스 (GKE)

뛰어난 네트워크 성능 및 글로벌 네트워크 인프라

단점

AWS와 Azure에 비해 서비스 범위가 좁음

일부 지역에서의 지원 및 서비스 가용성 제한

2) AWS (Amazon Web Services)

장점

가장 오래되고 성숙한 클라우드 플랫폼으로서 다양한 서비스 제공

글로벌 인프라 및 데이터 센터의 광범위한 분포

다양한 컴퓨팅, 스토리지, 데이터베이스 옵션

단점

복잡한 가격 구조

일부 서비스의 경우 초기 설정 및 관리가 복잡할 수 있음

3) Azure (Microsoft Azure)

장점

Microsoft 제품과의 높은 호환성 (Windows Server, Active Directory, SQL Server 등)

하이브리드 클라우드 솔루션 제공

강력한 개발자 도구 및 DevOps 지원 (Visual Studio, GitHub 통합 등)

단점

일부 서비스의 경우 성숙도가 AWS에 비해 낮음

복잡한 가격 구조

### 3. 요약

GCP는 데이터 분석 및 머신러닝에 강점을 가지고 있으며, 네트워크 성능이 뛰어남

AWS는 가장 다양한 서비스와 글로벌 인프라를 제공하며, 성숙한 클라우드 플랫폼

Azure는 Microsoft 제품과의 높은 호환성과 하이브리드 클라우드 솔루션에 강점을 가지고 있음

## 관련 글

- [[blog/GCP/index|GCP]]
- [[blog/GCP/GCP- GCP로 프로젝트 배포하기 - ( 3 ) GCP Service 계정 & 키 생성|[GCP] GCP로 프로젝트 배포하기 - ( 3 ) GCP Service 계정 & 키 생성]]
- [[blog/GCP/GCP- GCP로 프로젝트 배포하기 - ( 4 ) I AM 에서 역할 생성하기|[GCP] GCP로 프로젝트 배포하기 - ( 4 ) I AM 에서 역할 생성하기]]
- [[blog/GCP/GCP- GCP로 프로젝트 배포하기 - ( 5 ) GCP VPC 란|[GCP] GCP로 프로젝트 배포하기 - ( 5 ) GCP VPC 란?]]
