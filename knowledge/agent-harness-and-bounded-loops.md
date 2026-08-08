---
schema_version: 1
id: knowledge-agent-harness-and-bounded-loops
title: Agent Harness와 제한된 자율 루프
type: knowledge-note
status: verified
created: 2026-08-06
updated: 2026-08-08
checked_at: 2026-08-08
tags: [knowledge, initial-curation]
sources:
  - notion/SKALA/7-15 기타/7-15 Agent Harness 핵심 구조 — LangChain.md
  - notion/SKALA/7-15 기타/7-15 OpenCode로 보는 코딩 에이전트 내부 구조.md
  - notion/Information/2026-07-19 — 하네스 엔지니어링과 루프 엔지니어링 | 최근 핫이슈.md
---

# Agent Harness와 제한된 자율 루프

## 다루는 질문
모델이 도구를 사용해 여러 단계를 수행할 때, 무엇이 실행 범위와 실패 복구를 통제하는가?

## 하네스의 책임 경계
하네스는 모델 자체와 구분해 context, tool, filesystem state, 권한, sandbox, 로그·테스트를 조합한다. LangChain 구조와 OpenCode 내부 구조를 다룬 SKALA 기록은 도구 호출과 작업 상태가 단발성 답변 밖에 있다는 점을 보여 준다.

## 제한된 자율 루프
발견 → 실행 → 검증 → 기록 또는 복구의 루프에서, 각 단계는 다음 단계의 입력을 남긴다. 재시도 횟수·중단 조건·허용된 도구를 정하지 않으면 실패한 행동이 같은 상태를 반복해서 손상시킬 수 있다.

## 근거가 연결하는 관계
[[knowledge/context-engineering-and-tool-grounding]]은 하네스가 넣을 evidence·memory·tool 결과의 선택 기준을 다룬다. [[knowledge/llm-reliability-and-human-oversight]]는 고위험 행동에서 모델 출력과 실행 사이에 둘 승인·결정론적 검증 경계를 다룬다.

## 적용 전 확인
권한, 상태 저장 위치, 독립 검증 방법, 중단·복구 절차를 함께 명시한다. 아래 기준본은 제품별 내부 권한 모델이나 특정 구현의 보안성을 증명하지 않는다.

## 출처와 해석 범위
- [[notion/SKALA/7-15 기타/7-15 Agent Harness 핵심 구조 — LangChain]]
- [[notion/SKALA/7-15 기타/7-15 OpenCode로 보는 코딩 에이전트 내부 구조]]
- Information 원본은 파일명에 `|`가 있어 wiki link 대신 frontmatter `sources` 경로로 추적한다.
