---
title: "[Spring Boot] 3. 로컬 파일 업로드 권한 문제 → supabase"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "java", "spring boot"]
category: "SPRING BOOT"
published: 2026-03-03
source_url: https://ch010104.tistory.com/197
---

# [Spring Boot] 3. 로컬 파일 업로드 권한 문제 → supabase

## 원문

https://ch010104.tistory.com/197

## 노트 유형

`troubleshooting`

## 문제·재현 맥락

Spring Boot 서버에서 userUpload/DOC 경로에 파일을 저장하려 시도.

에러 발생: java.nio.file.AccessDeniedException: /Users/userUpload

## 원인·해결 근거

### 1. 발단: 로컬 환경의 한계와 권한 에러

### 상황

Spring Boot 서버에서 userUpload/DOC 경로에 파일을 저장하려 시도.

에러 발생: java.nio.file.AccessDeniedException: /Users/userUpload

원인: 서버 프로세스가 Mac/Linux의 루트 권한 구역(/Users/)에 폴더를 생성할 권한이 없음.

### 결과 (빈 껍데기 현상)

DB(장부): "파일이 저장되었다"고 데이터는 기록됨 (성공).

Storage(창고): 실제 하드디스크에는 파일이 저장되지 않음 (실패).

팀원 공유 불가: 내 컴퓨터에 설령 저장되더라도, 다른 팀원의 컴퓨터에는 해당 파일이 없으므로 다운로드가 불가능함.

### 2. 해결책의 진화: 로컬에서 클라우드로

이 문제를 해결하려면 "누구의 컴퓨터도 아닌, 모두가 접근 가능한 공용 창고"가 필요합니다. 여기서 Supabase가 등장합니다.

### Supabase란?

정의: 오픈소스 기반의 서비스형 백엔드(BaaS).

무료 여부: 넉넉한 프리티어 제공 (DB 500MB, 스토리지 1GB).

가용성: 24시간 클라우드에서 가동되는 공용 서버.

### 3. 상세 흐름: Supabase를 이용한 아키텍처 재구축

이제 시스템이 어떻게 바뀌어야 하는지 단계별 흐름입니다.

### STEP 1: 중앙 집중형 데이터베이스 (PostgreSQL)

이전: 각자 로컬 DB를 쓰거나 수동으로 동기화.

변경: Supabase의 Managed PostgreSQL 사용.

효과: 팀원 A가 관리자 페이지에서 데이터를 입력하면, 팀원 B의 화면에도 즉시 나타남. 24시간 켜져 있으므로 내 컴퓨터를 꺼도 팀원은 작업 가능.

### STEP 2: 오브젝트 스토리지 (S3 Storage)

이전: /Users/userUpload 같은 로컬 물리 경로 사용.

변경: Supabase 내장 Storage (S3 호환) 사용.

효과: 1. 파일이 질문자님의 하드디스크가 아닌 Supabase 클라우드 서버에 저장됨.

서버가 폴더를 생성할 권한을 걱정할 필요가 없음 (API로 전송하므로).

모든 팀원이 같은 클라우드 경로에서 파일을 다운로드함.

### STEP 3: 보안 다운로드 (Presigned URL)

문제: 클라우드에 올리면 아무나 내 파일을 다 가져가면 어떡하지?

해결: Presigned URL(서명된 URL) 방식 도입.

파일은 **비공개(Private)**로 설정.

사용자가 다운로드 요청 시, Spring Boot 서버가 로그인 여부와 권한을 체크.

권한이 있다면 S3(Supabase)에게 "5분짜리 임시 통행증(URL)"을 발행해달라고 요청.

사용자는 그 임시 링크로만 안전하게 다운로드.

### 4. 최종 비교 정리

항목 기존 방식 (Local) 개선 방식 (Supabase)

## 관련 글

- [[blog/SPRING BOOT/index|SPRING BOOT]]
- [[blog/SPRING BOOT/Spring Boot- 2. Flyway 마이그래이션 규칙|[Spring Boot] 2. Flyway 마이그래이션 규칙]]
- [[blog/SPRING BOOT/Spring Boot- 1. Spring Boot의 FeignClient 설정(python 포함)|[Spring Boot] 1. Spring Boot의 FeignClient 설정(python 포함)]]
- [[blog/SPRING BOOT/Spring Boot- 5. mock 테스트 코드 작성|[Spring Boot] 5. mock 테스트 코드 작성]]
