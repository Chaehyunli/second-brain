---
title: "[CLAUDE] Claude CLI MCP 서버 연결하기"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "AI", "Claude", "LLM", "mcp"]
category: "AI(MCP)"
published: 2026-03-08
source_url: https://ch010104.tistory.com/213
---

# [CLAUDE] Claude CLI MCP 서버 연결하기

## 원문

https://ch010104.tistory.com/213

## 핵심 요약

- **1. 연결된 MCP 서버 목록 및 역할 (Role)** — 현재 구성된 시스템은 문서 검색 + 코드 관리 + 인프라(DB/Redis) 제어 + 브라우저 시각화가 통합된 형태입니다.
- **2. Claude Desktop vs Claude Code (CLI) 차이** — 두 환경은 설정 파일과 동작 방식이 완전히 분리되어 있습니다.
- **3. 설정 파일 저장 위치 및 스코프 (Scope) 관리** — Claude CLI의 설정은 .claude\\config.json 한 곳에서 관리되지만, 그 안에서 **전역(User)**과 **프로젝트(Project)**가 나뉩니다.
- **📂 저장 위치 및 구분** — 파일 경로: C:\\Users\\chaeh\\.claude\\config.json

## 관련 글

- [[blog/AI(MCP)/index|AI(MCP)]]
- [[blog/AI(ML & DL)/딥러닝- Gradient 및 자동 미분(Autogradient)|[딥러닝] Gradient 및 자동 미분(Autogradient)]]
- [[blog/AI(ML & DL)/딥러닝- 오토인코더와 활용|[딥러닝] 오토인코더와 활용]]
- [[blog/CLAUD COMPUTERING/딥러닝- 텐서플로우의 GradientTape (자동 미분)|[딥러닝] 텐서플로우의 GradientTape (자동 미분)]]
