---
title: "[AI AGENT] AI Agent 성능 평가"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "ai agent", "spring boot"]
category: "AI(MCP)"
published: 2026-06-03
source_url: https://ch010104.tistory.com/282
---

# [AI AGENT] AI Agent 성능 평가

## 원문

https://ch010104.tistory.com/282

## 핵심 요약

- **1. AI Agent 평가의 핵심 레이어 및 메트릭** — AI Agent의 평가는 크게 생성 단계(Generation Layer)와 행동 단계(Action Layer)의 두 가지 관점으로 접근합니다.
- **① 생성 단계 (Generation Layer) - RAG 기반 할루시네이션 검증** — Agent가 외부 데이터(DB, 문서, API)를 참조해 답변할 때, 할루시네이션을 잡아내기 위해 LLM-as-a-Judge(더 똑똑한 LLM을 판사로 쓰는 방식) 기법을 활용한 3대 메트릭을 주로 사용합니다.
- **② 행동 단계 (Action Layer) - Agent 특화 행동 평가** — Agent는 단순히 답변만 하는 게 아니라 행동($Action$)을 취하므로, 할루시네이션이 행동의 오류로 이어지는지 검증해야 합니다.
- **2. 평가를 자동화하는 파이프라인 구조** — Agent 성능 평가는 사람이 일일이 검사할 수 없기 때문에, 개발 단계(CI/CD)에서 '골든 데이터셋(Golden Dataset)'을 기반으로 자동 평가 파이프라인을 구축하여 성능 저하를 방지합니다.

## 관련 글

- [[blog/AI(MCP)/index|AI(MCP)]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 4. 검증1 - Validation|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 4. 검증1 - Validation]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 3. 메시지와 국제화|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 3. 메시지와 국제화]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 2. 타임리프 - 스프링 통합과 폼|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 2. 타임리프 - 스프링 통합과 폼]]
