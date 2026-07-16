---
title: "Agent Harness 핵심 구조 — LangChain"
notion_page_id: "39e1d84b-f68e-815b-b26e-ecece209da8d"
notion_url: "https://app.notion.com/p/39e1d84bf68e815bb26eecece209da8d"
source_url: "https://www.langchain.com/blog/the-anatomy-of-an-agent-harness"
type: "manual-learning-note"
---

# [7/15] Agent Harness 핵심 구조 — LangChain

## 연결
- 상위 개념: [[7-15 Prompt 설계 및 Context Engineering]]
- 관점 확장: [[7-15 AI 에이전틱 패턴의 진화 — Prompt·Context·Harness]]
- 구현 사례: [[7-15 OpenCode로 보는 코딩 에이전트 내부 구조]]

## 원문
[The Anatomy of an Agent Harness](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness)

## 핵심
- **에이전트 = 모델 + 하네스**: 모델 밖의 도구, 상태, 실행·제약·피드백 로직이 실제 작업 가능한 에이전트를 만든다.
- 파일시스템은 세션 밖 상태와 중간 산출물을 보존하고, Git은 변경 추적·복구·실험 분기를 가능하게 한다.
- 범용 실행 도구(Bash·코드), 격리된 sandbox, 테스트·로그·브라우저 같은 검증 수단이 반복 개선 루프를 뒷받침한다.
