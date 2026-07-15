---
title: "Prompt 설계 및 Context Engineering"
notion_page_id: "39e1d84b-f68e-8182-849c-ff358cde88a9"
content_sha256: "238b241538bd45fbdd9972cb69b8f379f71511126088a966d6ecaa31bf8d050a"
source_url: "https://app.notion.com/p/39e1d84bf68e8182849cff358cde88a9"
synced_at: "2026-07-15T05:42:58Z"
---

# Prompt 설계 및 Context Engineering

## 학습 목표

생성형 AI의 흐름과 한계를 이해하고 프롬프트 구조화에서 컨텍스트·하네스 설계로 확장한다. 핵심은 좋은 한 문장을 찾는 것이 아니라 역할·지시·근거·예시·도구·대화 이력을 설계하고 검증하는 것이다.

## 생성형 AI와 LLM의 한계

- 생성형 AI는 답변 AI에서 RAG, AI Agent로 확장되고 있다. 품질은 모델뿐 아니라 검색·도구·실행·검증을 포함한 워크플로우에 좌우된다.
- LLM은 다음 토큰을 확률적으로 생성하므로 최신성, 내부·전문 지식, hallucination 문제가 있다. 사실·출처·불확실성을 명시하고 외부 근거를 제공해야 한다.
- 토큰 수는 비용·컨텍스트 한도·출력 길이와 연결된다. `temperature`, `top_p`, 출력 길이, reasoning effort, verbosity는 과업 특성에 맞게 선택한다.

## RICE/LEGO 프롬프트 구조

- **Role:** 도메인·경력·관점을 가진 역할을 정한다.
- **Instruction:** 산출물과 판단 절차를 구체화한다.
- **Context:** 대상, 현재 상황, 입력, 근거, 경계를 제공한다.
- **Examples:** 원하는 품질·형식의 짧은 예시를 제공한다.
- 여기에 policy/rule, style, constraints, output format을 더해 재사용 가능한 구조를 만든다.

```markdown
# Role
당신은 [도메인·경력·관점]을 가진 전문가입니다.

# Instruction
[산출물]을 작성하세요. 반드시 [판단 절차/포함 항목]을 따르세요.

# Context
- 대상: ...
- 사실로 취급할 근거: ...
- 제외할 해석/경계: ...

# Examples
[원하는 품질·형식의 짧은 예시]
```

## 주요 기법

- **Zero/One/Few-shot:** 예시 수를 조절해 형식과 분류 기준을 유도한다.
- **Chain of Thought:** 복잡한 문제를 증상·후보 원인·증거·검증·대책으로 분해한다.
- **Step-back:** 바로 답하기 전에 근본 목적·제약·놓친 가정을 검토한다.
- **Self-consistency:** 여러 추론 경로의 합의도를 활용한다.
- **Devil’s Advocate/Pre-mortem:** 이미 부결·실패했다고 가정하고 강한 반론과 보완 근거를 찾는다.

## Context Engineering과 Harness Engineering

- Context Engineering은 LLM 추론에 넣을 최적 정보 집합을 큐레이션하고 유지하는 전략이다. system prompt, memory/history, 도구·외부 지식, few-shot·format이 구성 요소다.
- 긴 컨텍스트는 Context Rot과 비용 문제를 낳으므로 무엇을 어떤 순서와 형태로 넣고 버릴지 설계해야 한다.
- Harness Engineering은 도구 권한, 실패 처리, 로그, 품질 판정, 재발 방지를 규칙·코드·검증 구조로 강제한다.
- `AGENTS.md`, 문서, 템플릿, 도구, 산출물, 로그를 분리하고 progressive disclosure를 적용한다.

## 실무 체크리스트

1. 과업을 생성·검색·요약·추론으로 분해한다.
2. RICE/LEGO로 역할, 지시, 근거, 예시, 정책과 형식을 구조화한다.
3. 최신·내부 정보는 RAG·문서·도구 결과로 보강하고 불확실성을 분리한다.
4. 사실형 작업은 일관성·검증을, 발상형 작업은 다양성·후보 비교를 우선한다.
5. 에이전트에는 권한·실패 처리·로그·리뷰 기준을 갖춘 Harness를 둔다.
