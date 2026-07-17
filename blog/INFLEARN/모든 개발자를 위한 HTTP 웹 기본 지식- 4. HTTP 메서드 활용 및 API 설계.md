---
title: "[모든 개발자를 위한 HTTP 웹 기본 지식] 4. HTTP 메서드 활용 및 API 설계"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "http", "inflearn"]
category: "INFLEARN"
published: 2026-03-27
source_url: https://ch010104.tistory.com/244
---

# [모든 개발자를 위한 HTTP 웹 기본 지식] 4. HTTP 메서드 활용 및 API 설계

## 원문

https://ch010104.tistory.com/244

## 노트 유형

`tutorial`

## 학습 목표 및 맥락

쿼리 파라미터(Query Parameters): 주로 GET 메서드에서 사용하며, 검색어 입력이나 정렬 필터링 등에 활용됩니다.

메시지 바디(Message Body): POST, PUT, PATCH 메서드에서 사용하며, 회원 가입, 상품 주문, 리소스 등록 및 수정 시 활용됩니다.

## 원문 기반 학습 정리

### 1. 클라이언트에서 서버로 데이터 전송 방식

데이터를 전달하는 방식은 크게 두 가지 경로를 이용합니다.

쿼리 파라미터(Query Parameters): 주로 GET 메서드에서 사용하며, 검색어 입력이나 정렬 필터링 등에 활용됩니다.

메시지 바디(Message Body): POST, PUT, PATCH 메서드에서 사용하며, 회원 가입, 상품 주문, 리소스 등록 및 수정 시 활용됩니다.

### 데이터 전송의 4가지 상황

정적 데이터 조회: 이미지, 정적 텍스트 문서 조회 (쿼리 파라미터 미사용, 경로만으로 조회).

동적 데이터 조회: 검색, 게시판 목록 정렬 (쿼리 파라미터 사용).

HTML Form 전송: 회원 가입, 데이터 변경 (주로 POST 사용, 파일 업로드 시 multipart/form-data 사용).

HTTP API 전송: 서버 간 통신, 앱/웹 클라이언트(Ajax, React, Vue) 통신 (주로 JSON 사용).

### 2. HTML Form을 통한 데이터 전송

HTML Form 태그는 기본적으로 GET과 POST만 지원한다는 제약이 있습니다.

application/x-www-form-urlencoded: 기본 형식으로, 데이터를 key=value 형태로 전송하며 URL 인코딩 처리를 합니다.

multipart/form-data: 파일 업로드 및 바이너리 데이터 전송 시 사용하며, 여러 종류의 데이터를 함께 보낼 수 있습니다.

제약 사항 해결: PUT, DELETE 등을 사용하지 못하므로, 경로에 /new, /edit, /delete와 같은 컨트롤 URI를 사용하여 문제를 해결합니다.

### 3. HTTP API 데이터 전송

현대적인 웹 개발에서 가장 많이 사용되는 방식입니다.

특징: 서버 대 서버 통신, 앱 클라이언트, AJAX 통신 등에 사용됩니다.

Content-Type: application/json이 사실상 표준(Standard)으로 사용됩니다.

메서드 활용: POST, PUT, PATCH를 통해 메시지 바디로 데이터를 자유롭게 전송합니다.

### 4. HTTP API 설계 예시: 컬렉션 vs 스토어

### ① 컬렉션 (Collection) - POST 기반 등록

서버가 리소스를 관리하는 가장 보편적인 방식입니다.

주요 특징: * 클라이언트는 등록될 리소스의 URI를 모른 채 요청을 보냅니다.

서버가 리소스의 URI를 생성하고 관리합니다.

등록 시 요청 URI는 리소스가 모인 상위 경로인 '컬렉션'을 가리킵니다.

예시: /members (회원 관리 시스템)

상세 동작:

클라이언트 요청: POST /members (데이터는 메시지 바디에 포함)

서버 처리: 신규 ID(예: 100)를 생성하고 저장

서버 응답: 201 Created 상태 코드와 함께 헤더에 Location: /members/100을 담아 전달

정의: 컬렉션(Collection)이란 서버가 관리하는 리소스 디렉터리를 의미합니다.

### ② 스토어 (Store) - PUT 기반 등록

클라이언트가 주도권을 가지고 리소스를 등록하는 방식입니다.

주요 특징: * 클라이언트가 리소스의 URI를 이미 알고 직접 지정하여 요청을 보냅니다.

서버는 클라이언트가 지정한 경로에 데이터를 그대로 저장하거나 덮어씁니다.

주로 파일 관리 시스템 등에서 사용됩니다.

예시: /files (정적 컨텐츠 또는 파일 관리)

상세 동작:

클라이언트 요청: PUT /files/star.jpg (리소스 경로를 명확히 지정)

서버 처리: 해당 경로에 데이터를 저장

서버 응답: 성공 시 200 OK 또는 204 No Content 등을 반환

정의: 스토어(Store)란 클라이언트가 관리하는 자원 저장소를 의미합니다.

### 5. URI 설계 핵심 개념 요약

성공적인 API 설계를 위해 다음 4가지 개념을 구분해야 합니다.

개념 설명 예시

참고: 순수 HTML Form은 GET/POST만 지원하므로 컨트롤 URI를 적극 활용하고, 그 외의 API 설계에서는 리소스 중심의 설계와 적절한 HTTP 메서드(GET, POST, PUT, PATCH, DELETE) 선택이 중요합니다.

## 관련 글

- [[blog/INFLEARN/index|INFLEARN]]
- [[blog/INFLEARN/모든 개발자를 위한 HTTP 웹 기본 지식- 2. URI의 개념과 웹 브라우저의 요청 흐름|[모든 개발자를 위한 HTTP 웹 기본 지식] 2. URI의 개념과 웹 브라우저의 요청 흐름]]
- [[blog/INFLEARN/모든 개발자를 위한 HTTP 웹 기본 지식- 1. 인터넷 네트워크|[모든 개발자를 위한 HTTP 웹 기본 지식] 1. 인터넷 네트워크]]
- [[blog/INFLEARN/모든 개발자를 위한 HTTP 웹 기본 지식- 5. HTTP 상태코드 (HTTP Status Codes)|[모든 개발자를 위한 HTTP 웹 기본 지식] 5. HTTP 상태코드 (HTTP Status Codes)]]
