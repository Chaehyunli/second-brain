---
title: "[모든 개발자를 위한 HTTP 웹 기본 지식] 7. HTTP 헤더 - 캐시와 조건부 요청"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "http", "inflearn"]
category: "INFLEARN"
published: 2026-03-31
source_url: https://ch010104.tistory.com/250
---

# [모든 개발자를 위한 HTTP 웹 기본 지식] 7. HTTP 헤더 - 캐시와 조건부 요청

## 원문

https://ch010104.tistory.com/250

## 노트 유형

`tutorial`

## 학습 목표 및 맥락

데이터가 변경되지 않아도 계속 네트워크를 통해 데이터를 다운로드해야 함

인터넷 네트워크는 느리고 비싸며, 브라우저 로딩 속도가 느려져 사용자 경험이 저하됨

## 원문 기반 학습 정리

### 1. 캐시 기본 동작

### 캐시가 없을 때

데이터가 변경되지 않아도 계속 네트워크를 통해 데이터를 다운로드해야 함

인터넷 네트워크는 느리고 비싸며, 브라우저 로딩 속도가 느려져 사용자 경험이 저하됨

### 캐시가 적용

첫 번째 요청: 서버가 응답 헤더에 cache-control: max-age=60을 포함하여 전송 (60초간 유효)

두 번째 요청: 브라우저 캐시를 확인하여 유효 시간 내라면 네트워크를 타지 않고 캐시에서 조회 (매우 빠름)

캐시 시간 초과: 유효 시간이 지나면 다시 서버를 통해 데이터를 조회하고 캐시를 갱신함 (네트워크 다운로드 발생)

다시 서버로부터 정보를 받아서 캐시에 데이터를 저장함

근데, 첫 번째 요청으로부터 받은 데이터와 세 번째 요청으로 받는 데이터가 같은데 또 다운받는건 비효율적?

### 2. 검증 헤더와 조건부 요청

### 캐시 시간 초과 후의 상황

서버에서 기존 데이터를 변경함

서버에서 기존 데이터를 변경하지 않음 (이 경우 데이터를 다시 받는 대신 캐시 재사용 가능)

### Last-Modified와 If-Modified-Since

검증 헤더: Last-Modified (데이터 최종 수정일)

조건부 요청: if-modified-since (캐시가 가진 최종 수정일을 서버에 전달)

결과:

데이터 미변경 시: 304 Not Modified 응답. HTTP Body 없이 헤더 정보(0.1M)만 전송하여 네트워크 부하 급감

데이터 변경 시: 200 OK 응답. 모든 데이터(Body 포함 1.1M) 전송

### ETag와 If-None-Match

ETag (Entity Tag): 캐시용 데이터에 고유한 버전 이름을 부여 (예: "v1.0", "aaaaa")

특징:

진짜 단순하게 ETag만 보내서 같으면 유지, 다르면 다시 받기

서버에서 캐시 제어 로직을 완전히 관리 (예: 배포 주기에 맞춰 갱신)

1초 미만 단위의 캐시 조정이 가능하며, 날짜 기반 로직의 한계를 극복

해시를 사용함ETag와 If-None-Match

ETag (Entity Tag): 캐시용 데이터에 고유한 버전 이름을 부여 (예: "v1.0", "aaaaa")

특징:

진짜 단순하게 ETag만 보내서 같으면 유지, 다르면 다시 받기

서버에서 캐시 제어 로직을 완전히 관리 (예: 배포 주기에 맞춰 갱신)

1초 미만 단위의 캐시 조정이 가능하며, 날짜 기반 로직의 한계를 극복

해시를 사용함

### 3. 캐시 제어 헤더

### Cache-Control (캐시 지시어)

얼마동안 캐시가 유효할건가?

max-age: 캐시 유효 시간 (초 단위)

no-cache: 데이터는 캐시해도 되지만, 항상 원(origin) 서버에 검증하고 사용

no-store: 데이터에 민감한 정보가 있으므로 저장 금지 (메모리 사용 후 즉시 삭제)

public: 응답이 public 캐시(프록시 서버)에 저장되어도 됨

private: 응답이 해당 사용자만을 위한 것이므로 private 캐시에 저장해야 함 (기본값)

s-maxage: 프록시 캐시에만 적용되는 max-age

### 하위 호환 및 기타

Pragma: no-cache (HTTP 1.0 하위 호환)

Expires: 캐시 만료일을 정확한 날짜로 지정 (현재는 Cache-Control: max-age 권장)

Age: 오리진 서버에서 응답 후 프록시 캐시 내에 머문 시간

### 4. 프록시 캐시

한국 클라이언트와 미국 원(origin) 서버 사이의 거리 문제를 해결하기 위해 한국 어딘가에 프록시 캐시 서버를 도입

private 캐시: 웹 브라우저 로컬 캐시

응답이 해당 사용자만을 위한 것임

public 캐시: 프록시 캐시 서버의 캐시 (여러 사용자가 공유)

### 5. 캐시 무효화

### 확실한 캐시 무효화 응답

민감한 정보가 포함된 페이지에 적용:

Cache-Control: no-cache, no-store, must-revalidate

Pragma: no-cache (HTTP 1.0 호환용)

### no-cache vs must-revalidate

no-cache: 원 서버에 접근할 수 없을 때, 캐시 서버 설정에 따라 과거의 데이터라도 반환할 수 있음 (Error or 200 OK)

must-revalidate: 원 서버에 접근할 수 없는 경우, 반드시 오류가 발생해야 함 (504 Gateway Timeout). 돈과 관련된 결과 등 매우 중요한 정보에 사용

캐시 만료 후에 상황

## 관련 글

- [[blog/INFLEARN/index|INFLEARN]]
- [[blog/INFLEARN/모든 개발자를 위한 HTTP 웹 기본 지식- 6. HTTP 일반 헤더|[모든 개발자를 위한 HTTP 웹 기본 지식] 6. HTTP 일반 헤더]]
- [[blog/INFLEARN/모든 개발자를 위한 HTTP 웹 기본 지식- 5. HTTP 상태코드 (HTTP Status Codes)|[모든 개발자를 위한 HTTP 웹 기본 지식] 5. HTTP 상태코드 (HTTP Status Codes)]]
- [[blog/INFLEARN/모든 개발자를 위한 HTTP 웹 기본 지식- 4. HTTP 메서드 활용 및 API 설계|[모든 개발자를 위한 HTTP 웹 기본 지식] 4. HTTP 메서드 활용 및 API 설계]]
