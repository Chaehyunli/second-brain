---
title: "[GCP] GCP로 프로젝트 배포하기 - ( 2 ) GCP IAM 란?"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing"]
category: "GCP"
published: 2025-05-24
source_url: https://ch010104.tistory.com/80
---

# [GCP] GCP로 프로젝트 배포하기 - ( 2 ) GCP IAM 란?

## 원문

https://ch010104.tistory.com/80

## 노트 유형

`project`

## 배경·목표·적용 맥락

GCP IAM(Identity and Access Management) 서비스는 Google Cloud Platform에서 리소스에 대한 액세스를 제어하고 관리하는 서비스

IAM을 사용하면 사용자, 그룹, 서비스 계정 및 기타 엔터티에 대해 세밀한 권한을 설정 가능

## 구현·의사결정·결과

### GCP IAM 서비스 란?

GCP IAM(Identity and Access Management) 서비스는 Google Cloud Platform에서 리소스에 대한 액세스를 제어하고 관리하는 서비스

IAM을 사용하면 사용자, 그룹, 서비스 계정 및 기타 엔터티에 대해 세밀한 권한을 설정 가능

주요 기능

1) 역할 기반 액세스 제어 (RBAC)

사용자에게 특정 역할을 부여하여 필요한 권한만 부여 가능

역할은 사전 정의된 역할(기본 역할)과 사용자 정의 역할로 나뉨

2) 정책 관리

IAM 정책을 통해 리소스에 대한 액세스를 제어 가능

정책은 특정 리소스에 대해 어떤 사용자가 어떤 작업을 수행할 수 있는지 정의

3) 서비스 계정

애플리케이션이나 VM 인스턴스가 GCP 리소스에 액세스할 수 있도록 하는 특수한 계정

서비스 계정에 대한 키를 생성하여 애플리케이션에서 인증에 사용 가능

4) 조직 정책

조직 수준에서 정책을 설정하여 하위 리소스에 대한 일관된 액세스 제어를 적용 가능

5) 요약

GCP IAM 서비스는 GCP 리소스에 대한 액세스를 안전하고 효율적으로 관리할 수 있도록 도와주는 중요한 도구

이를 통해 조직 내에서 권한을 세밀하게 제어하고, 보안성을 높일 수 있음

## 관련 글

- [[blog/GCP/index|GCP]]
- [[blog/GCP/GCP- GCP로 프로젝트 배포하기 - ( 1 ) GCP 란|[GCP] GCP로 프로젝트 배포하기 - ( 1 ) GCP 란?]]
- [[blog/GCP/GCP- GCP로 프로젝트 배포하기 - ( 3 ) GCP Service 계정 & 키 생성|[GCP] GCP로 프로젝트 배포하기 - ( 3 ) GCP Service 계정 & 키 생성]]
- [[blog/GCP/GCP- GCP로 프로젝트 배포하기 - ( 4 ) I AM 에서 역할 생성하기|[GCP] GCP로 프로젝트 배포하기 - ( 4 ) I AM 에서 역할 생성하기]]
