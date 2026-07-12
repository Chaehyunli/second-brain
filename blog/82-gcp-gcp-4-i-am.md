---
title: "[GCP] GCP로 프로젝트 배포하기 - ( 4 ) I AM 에서 역할 생성하기"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: [blog, technical-writing]
category: "GCP"
published: 2025-05-24
source_url: https://ch010104.tistory.com/82
archive_method: Tistory sitemap + HTML content extraction
---

# [GCP] GCP로 프로젝트 배포하기 - ( 4 ) I AM 에서 역할 생성하기

> 원문: https://ch010104.tistory.com/82

## 본문

특정 사용자만 특정 리소스에 접근 하도록 설정하기 특정 사용자만 특정 리소스에 접근 하도록 설정하는 방법이다     1. I AM에 메뉴에 접근   2. 역할을 클릭 후 상단에 + 역할 만들기를 클릭하여 새로운 역할을 생성   3. 역할 이름을 입력하고, 설명이 필요하면 설명을 입력   4. ID 및 역할 실행 상태는 구성에 따라서 다르게 설정 (OR 태그 이용 가능)     5. + 권한 추가를 클릭하여 추가할 권한을 선택 후 추가 버튼을 클릭하여 추가    내가 만든 역할을 이후에 서비스 계정에 부여 가능 - 위의 예시에서는 VM 접근 권한 이라는 역할에 여러 권한을 부여해서 만듬
