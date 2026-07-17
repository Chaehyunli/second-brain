---
title: "[CLAUDE] Claude CLI MCP 서버 연결하기"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "AI", "Claude", "LLM", "mcp"]
category: "AI(MCP)"
published: 2026-03-08
source_url: https://ch010104.tistory.com/213
---

# [CLAUDE] Claude CLI MCP 서버 연결하기

## 원문

https://ch010104.tistory.com/213

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

현재 구성된 시스템은 문서 검색 + 코드 관리 + 인프라(DB/Redis) 제어 + 브라우저 시각화가 통합된 형태입니다.

서버 이름 역할 (Role) 활용 시나리오 (Spring Boot 기준)

## 원문 기반 개념 정리

### 1. 연결된 MCP 서버 목록 및 역할 (Role)

현재 구성된 시스템은 문서 검색 + 코드 관리 + 인프라(DB/Redis) 제어 + 브라우저 시각화가 통합된 형태입니다.

서버 이름 역할 (Role) 활용 시나리오 (Spring Boot 기준)

### 2. Claude Desktop vs Claude Code (CLI) 차이

두 환경은 설정 파일과 동작 방식이 완전히 분리되어 있습니다. 서로 영향을 주지 않으니 각각 관리해야 합니다.

Claude Desktop (앱): GUI 기반 비서. claude_desktop_config.json 사용. (전역 설정만 가능)

Claude Code (CLI): 터미널 기반 개발 에이전트. **프로젝트별(Local)**로 다른 설정을 가질 수 있어 개발에 훨씬 유리합니다.

### 3. 설정 파일 저장 위치 및 스코프 (Scope) 관리

Claude CLI의 설정은 .claude\\config.json 한 곳에서 관리되지만, 그 안에서 **전역(User)**과 **프로젝트(Project)**가 나뉩니다.

### 📂 저장 위치 및 구분

파일 경로: C:\\Users\\chaeh\\.claude\\config.json

전역(Global) 설정: mcpServers 섹션에 위치. 어떤 폴더에서든 사용 가능.

대상: context7, github, sequential-thinking, filesystem, browser

프로젝트(Project) 설정: projects 섹션 하위의 특정 경로(.../capstone-backend)에 위치. 해당 폴더에서만 활성화.

대상: supabase-db, upstash-redis

### 4. 핵심 연결 정보 및 확인 방법

### 🔌 DB 및 Redis 연결 (Supabase & Upstash)

Postgres: JDBC 형식이 아닌 표준 URI(postgresql://...)로 변환하여 연결됨.

Redis: 보안을 위해 TLS(Rediss) 프로토콜(rediss://...)을 사용하여 Upstash 클라우드에 연결됨.

### 🌐 브라우저 도구 (Playwright 대신 Puppeteer)

기존 server-playwright 패키지의 404 오류를 해결하기 위해 공식 패키지인 **@modelcontextprotocol/server-puppeteer*를 사용하여 browser라는 이름으로 전역 등록을 마쳤습니다.

### ✅ 현재 상태 확인 명령어

터미널에서 아래 명령어를 입력했을 때 모두 **✓ Connected**가 뜨면 완벽합니다.

```text
claude mcp list
```

### 5. Claude CLI(MCP) 서버 추가 명령어

터미널(PowerShell/CMD)을 열고 아래 명령어를 순서대로 입력하세요.

### 1. 전역 도구 설정 (Global/User Scope)

어떤 폴더에서든 Claude를 실행했을 때 항상 사용할 수 있는 공통 도구들입니다. 터미널 어디서든 입력하세요.

```text
# 1. 브라우저 시각화 (Puppeteer - Playwright 404 에러 해결 버전)
claude mcp add browser --scope user -- npx -y @modelcontextprotocol/server-puppeteer

# 2. 브라우저 엔진(Chrome) 필수 설치 (이게 없으면 browser가 작동 안 함)
npx puppeteer browsers install chrome

# 3. 최신 기술 문서 및 웹 검색 (Context7)
claude mcp add context7 --scope user -- npx -y @modelcontextprotocol/server-context7

# 4. GitHub 리포지토리 및 PR 관리
claude mcp add github --scope user -- npx -y @modelcontextprotocol/server-github

# 5. 복잡한 문제 해결을 위한 단계별 사고 도구
claude mcp add sequential-thinking --scope user -- npx -y @modelcontextprotocol/server-sequential-thinking

# 6. 로컬 파일 읽기/쓰기 및 수정 권한
claude mcp add filesystem --scope user -- npx -y @modelcontextprotocol/server-filesystem "C:\\Users\\chaeh\\Desktop\\capstone-backend"
```

(주의: filesystem 경로 부분은 실제 프로젝트 폴더 경로에 맞춰 수정하세요.)

### 2. 프로젝트 개별 도구 설정 (Project Scope)

특정 프로젝트의 DB나 캐시 정보는 보안상 해당 폴더 내에서만 활성화되도록 설정합니다. 반드시 프로젝트 폴더(capstone-backend)로 이동(cd) 후 입력하세요.

```text
# Supabase 등록
claude mcp add supabase-db -- npx @modelcontextprotocol/server-postgres "postgresql://postgres.mcimkbbulvutcfweeovq:ZNzW0loQqUIfCUrq@aws-1-ap-northeast-1.pooler.supabase.com:6543/postgres"

# Upstash Redis 등록
claude mcp add upstash-redis -- npx @modelcontextprotocol/server-redis "rediss://:AfxzAAIncDE5NDEyOTRmMmE3Nzc0M2UyYTA2NjRiNjZjNmE2NGZmOXAxNjQ2Mjc@moved-akita-64627.upstash.io:6379"
```

### 3단계: 설정 결과 확인

모든 명령어를 입력했다면, 아래 명령어로 모든 서버가 정상적으로 연결(✓ Connected)되었는지 확인합니다.

```text
claude mcp list
```

### 💡 요약 및 활용 팁

브라우저 확인(Browser): 이제 Claude에게 "내 로컬 서버(localhost:8080)에 접속해서 프론트엔드 UI가 기획서대로 잘 나왔는지 스크린샷 찍어서 분석해줘"라고 시킬 수 있습니다.

데이터 교차 검증: "supabase-db에서 유저 정보를 읽어온 다음, 실제 웹 화면(browser)에 그 데이터가 표 형식으로 잘 출력되고 있는지 확인해줘"라는 고난도 작업이 가능해집니다.

파일 수정(Filesystem): 화면이 이상하거나 로직이 틀렸다면 "filesystem 도구로 해당 컨트롤러 파일을 열어서 에러를 수정해줘"라고 명령하세요.

## 관련 글

- [[blog/AI(MCP)/index|AI(MCP)]]
- [[blog/AI(ML & DL)/딥러닝- Gradient 및 자동 미분(Autogradient)|[딥러닝] Gradient 및 자동 미분(Autogradient)]]
- [[blog/AI(ML & DL)/딥러닝- 오토인코더와 활용|[딥러닝] 오토인코더와 활용]]
- [[blog/CLAUD COMPUTERING/딥러닝- 텐서플로우의 GradientTape (자동 미분)|[딥러닝] 텐서플로우의 GradientTape (자동 미분)]]
