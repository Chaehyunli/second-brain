---
title: "[7/22] LLM과 Transformer 아키텍처_Day2 - 핵심 정리"
notion_page_id: 3a51d84b-f68e-802d-af8a-e2ecb7363c56
source: https://app.notion.com/p/3a51d84bf68e802daf8ae2ecb7363c56
source_url: https://app.notion.com/p/3a51d84bf68e802daf8ae2ecb7363c56
synced_at: 2026-07-22T15:06:42Z
content_sha256: c2b53c5fca988fa9faa3f8fb435738b570fd00ca81bfcbbdfd2392a8cfb18a48
---

# [7/22] LLM과 Transformer 아키텍처_Day2 - 핵심 정리

[[notion/SKALA/index|SKALA 학습 노트]]

- 원문: [Notion 페이지](https://app.notion.com/p/3a51d84bf68e802daf8ae2ecb7363c56)
- 범위: AI 활용 역량의 맥락에서 현대 LLM의 특징, RLHF, Scaling Law와 Chinchilla, DeepSeek의 성능·가격 관점, 추론 증류, MoE의 Router·Expert 흐름을 순서대로 정리한다.
- 이미지 슬라이드는 원문에 있었으나, 만료형 서명 URL은 보관하지 않았다. 아래 내용은 원문 본문에서 직접 확인한 텍스트·표·수식에 한정한다.

## 1. AI 활용 능력이 경쟁력이 되는 맥락

원문은 생성형 AI가 업무 자동화를 앞당기고 있으며, 31.5개국 3.1만 명 설문에서 전 세계 지식근로자의 75%가 생성형 AI를 현장 업무에 활용한다고 제시한다.

| 구분 | 과거 — 검색의 시대 | 현재 — AI의 시대 |
| --- | --- | --- |
| 핵심 능력 | 정보를 찾아내는 **검색능력** | AI를 도구로 활용하는 **AI 활용능력** |
| 시대 성격 | 정보 희소성: *아는 것이 힘* | 정보 범람: *활용하는 것이 힘* |
| 경쟁력 연결 | 검색능력이 곧바로 경쟁력 | 활용능력이 여러 단계를 거쳐 성과로 증폭 |

원문은 기존 1.0이 개발자 옆에서 코딩을 돕는 AI 기반 에디터(IDE)였다면, 2.0은 여러 AI 에이전트에 역할을 나누고 병렬 업무를 지시하는 독립형 명령·관리 플랫폼으로 바뀌었다고 설명한다. 따라서 경쟁력의 초점은 코드를 빠르게 치는 일보다 문제를 정의하고 AI를 써서 시스템을 설계하는 능력으로 옮겨가며, 이 흐름에서 *Forward Deployed Engineer* 같은 융합형 인재가 요구된다는 것이 원문의 주장이다.

## 2. 현대 LLM의 네 특징

LLM은 딥러닝 기반 범용 모델로, 하나의 모델이 여러 task를 수행할 수 있다는 점이 핵심이다.

| 특징 | 원문의 핵심 내용 | 학습상 유의점 |
| --- | --- | --- |
| 매개변수 규모 | 매우 많은 파라미터를 가지며 GPT-3는 약 **1,750억 개** 수준 | 복잡한 언어 패턴 학습·추론의 전제가 되는 규모 |
| 사전 학습 | 대량 텍스트로 문법·의미·문맥을 학습 | 사전학습(범용) 뒤 Fine-tuning(특화)의 2단계 구조 |
| NLP 작업 | 생성·번역·요약·감정분석·질의응답 등 수행 | 정해진 작업을 넘어 자연스러운 텍스트 생성에 강점 |
| Transformer | 문맥 이해와 병렬 데이터 처리가 가능한 아키텍처 | 대규모 LLM을 가능하게 한 기술적 기반 |

원문은 LLM Leaderboard로 `https://www.vellum.ai/llm-leaderboard`를 제시한다. 이는 해당 시점의 비교 자료 링크이며, 본 노트는 링크 내부의 현황을 자동으로 검증·분석하지 않는다.

### Market Leaders: Gemini · Claude · Grok · LLaMA

| 구분 | Gemini 3.x | Claude | Grok 4 | LLaMA 4 |
| --- | --- | --- | --- | --- |
| 개발 주체 | Google | Anthropic | xAI | Meta |
| 한 줄 포지셔닝 | 모든 사람에게 유용한 AI | 문제 해결사를 위한 코드 생성 강자 | 인류에 안전·유익한 AI | 개방형 생태계의 오픈소스 |
| 원문상 강점 | 멀티모달, Google Workspace 연동 | 코드 생성·개발 보조, 긴 문서·대화 | 수학·논리·과학 추론, DeepSearch | weights 공개, 파인튜닝 가능한 다양한 크기 |
| 대표 활용 | 문서 요약·초안·기획 | 리서치·보고서·긴 기획서의 사고 파트너 | 최신 정보 반영 답변 | 연구·개발 커뮤니티와 자체 파인튜닝 |

원문은 Google Brain과 DeepMind의 합병(2023), Bard·Duet 통합 뒤 Gemini 런칭(2024.02), Gemini 2.5(2025.03), Claude Opus 4.5(2025.11.24), Grok 4/Grok 4 Heavy(2025.07.09), LLaMA 4(2025.04) 등의 이력을 표로 제시한다. 이는 원문에 기재된 비교 시점의 정보이며, 최신 제품 사실로 일반화하지 않는다.

## 3. RLHF: 사람의 선호를 학습 목표에 반영하기

**RLHF (Reinforcement Learning from Human Feedback)** 는 사람의 feedback을 이용해 LLM이 더 도움되고, 안전하며, 사람의 의도에 맞게 답하도록 학습시키는 기법이다.

사전학습만 거친 모델은 다음 단어를 잘 예측하도록 최적화됐을 뿐 사람이 선호하는 답을 목표로 삼지는 않는다. 그래서 질문 의도에서 벗어나거나 공격적·장황한 답, 취향에 맞지 않는 답을 낼 수 있다. RLHF의 전환점은 지식량을 늘리는 것보다 답변의 **방식과 태도**를 사람 선호에 맞추는 데 있다.

### 장점과 한계

- 장점: 지시 이해, 정중함, 응답 일관성이 좋아져 사람이 체감하는 대화 품질을 높일 수 있다. 원문은 ChatGPT를 포함한 생성형 AI의 “말이 잘 통하는 느낌” 상당 부분이 RLHF에 의해 유도된다고 설명한다.
- **Reward Hacking**: 내용의 옳고 그름보다 점수를 잘 받을 말투만 익히면 무난하고 안전한 답만 내며 다양성이 줄 수 있다.
- 선호의 편향: 보상 기준이 사람 선호에 의존하므로 Reward Model 학습에 사람·문화의 편향이 들어갈 수 있다.
- 비용: Human Labeling이 필요하므로 비용이 크다.

## 4. Scaling Law와 Chinchilla의 보정

**Scaling Law**는 파라미터(Parameter), 학습 데이터(Data), 연산량(Compute)을 늘리면 LLM 성능이 예측 가능한 방식으로 좋아진다는 경험 법칙이다. 원문의 핵심은 하나만 키우는 것이 아니라 세 요소의 **균형**이 성능을 좌우한다는 점이다.

GPT-3 논문 Figure 1.2의 원문 해석은 다음과 같다.

- 과제는 단어에서 무작위 기호를 제거하는 단순 과제다.
- 가로축은 문맥 예시 수 `K`, 세로축은 정확도다.
- 곡선은 175B·13B·1.3B 모델이며, 큰 모델일수록 위에 위치한다.
- Zero-shot → One-shot → Few-shot으로 예시가 늘면 정확도가 오르고, 큰 모델일수록 문맥 정보를 더 효율적으로 쓴다.
- 실선은 자연어 프롬프트가 있는 경우, 점선은 없는 경우다.

원문은 이 흐름이 “더 좋은 알고리즘 구조” 경쟁에서 “더 크게 학습시키기 위한 인프라·GPU” 경쟁으로 방향을 바꾸었다고 요약한다.

### Chinchilla: 큰 모델만이 답은 아니다

| 항목 | GPT-3 | Chinchilla |
| --- | --- | --- |
| 파라미터 | 175B | 70B |
| 학습 토큰 | 약 300B | 약 1.4T |
| 모델 크기 | 큼 | 더 작음 |
| 데이터 | 부족 | 충분 |
| 원문상 성능 비교 | 상대적으로 열위 | 더 우수 |

원문은 Chinchilla를 2022년 Google DeepMind가 발표한 LLM으로 소개하며, “큰 모델 + 적은 데이터”보다 “적절한 모델 크기 + 충분한 데이터”가 나을 수 있음을 보였다고 설명한다. Chinchilla의 파라미터는 GPT-3의 절반 이하이지만 학습 토큰은 약 4~5배 많다는 대비가 핵심이다.

## 5. DeepSeek: 성능 대비 가격과 추론 증류

원문 그래프는 X축을 입력 토큰 100만 개당 API 가격(로그 스케일), Y축을 MMLU Redux ZeroEval로 설명한다. 따라서 왼쪽 위일수록 저렴하면서 성능이 높은 지점이다. 원문상 DeepSeek-V3는 약 89의 성능 점수와 저가 구간이라는 위치로 제시되며, Claude 3.5 Sonnet·GPT-4o와 같은 고성능 모델은 더 고가 구간에, GPT-4o-mini·DeepSeek-V2.5는 저가이지만 약 82 수준으로 대비된다.

원문은 DeepSeek-R1을 다음 세 축으로 묶는다.

1. **Chain of Thought**: 추론 과정을 단계적으로 드러내고, 중간 오류를 교정한다.
2. **Reinforcement Learning**: 다양한 시도와 결과를 통해 응답 행동을 갱신한다.
3. **Distillation**: 큰 모델의 능력을 더 작은 모델로 압축·전달해 접근성을 높인다.

### Knowledge Distillation과 라벨

Teacher가 reasoning을 거쳐 답을 만들면 Student는 정답뿐 아니라 그 추론 과정까지 학습한다. 원문 흐름은 다음과 같다.

`거대 Teacher 모델 → Synthetic Reasoning Data 생성 → Llama 등 오픈 모델 Fine-tuning → 경량 Distilled 모델`

| 구분 | Hard Label | Soft Label |
| --- | --- | --- |
| 정의 | one-hot 형식의 확정 레이블 | 모델이 예측한 확률분포 |
| 예시 | 고양이=1, 개=0 | 고양이=0.7, 개=0.2, 여우=0.1 |
| 정보량 | 정답만 있어 낮음 | 클래스 간 유사성까지 담아 높음 |

Soft Label은 Teacher의 클래스 간 유사성 정보를 전달하므로 Student의 일반화와 학습 안정화에 도움이 될 수 있다. 다만 이는 원문의 설명이며, 어떤 데이터·모델에도 자동으로 같은 효과를 보장한다는 뜻은 아니다.

## 6. MoE: 필요한 Expert만 활성화하는 구조

**MoE (Mixture of Experts)** 는 모든 파라미터를 매번 쓰는 대신 입력마다 필요한 일부 Expert만 골라 활성화하는 구조다. 원문은 DeepSeek-R1의 “총 671B 중 활성 37B”를 예로 든다.

| 구분 | Dense Transformer | MoE |
| --- | --- | --- |
| 처리 | 모든 뉴런·파라미터 사용 | 토큰마다 소수 Expert만 선택 |
| 활성화 | 항상 모두 활성 | 대부분 비활성, 일부만 활성 |
| 연산량 | 모든 항목을 계산하므로 큼 | 필요한 부분만 계산해 절감 가능 |
| 흐름 | Question → Transformer Layer → Output | Question → Router → 선택 Expert → Combine → Output |

### Router의 수식과 흐름

1. **Score 계산**: `Score = x·Wr` — 입력 토큰 `x`와 Router 가중치 `Wr`로 각 Expert 적합도를 만든다.
2. **확률화**: `Pi = e^(si) / Σj e^(sj)` — Softmax로 Expert `i`가 선택될 확률을 만든다. 전체 확률 합은 1이다.
3. **Top-n 선택**: 확률이 높은 일부 Expert만 활성화한다.
4. **결합**: 선택 Expert의 출력을 weighted sum으로 합쳐 Output으로 낸다.

Router는 작은 선형층이며 학습 대상이다. 처음에는 Expert가 동일하지만, Router가 유사 입력을 같은 Expert로 반복 전송하면서 해당 Expert가 그 영역에 특화된다. 즉 Expert의 전문성은 미리 지정되는 것이 아니라 라우팅과 학습의 반복 속에서 형성된다.

## 핵심 연결

- Day1의 Transformer·Self-Attention 기초는 [[notion/SKALA/7-21 LLM과 Transformer 아키텍처_Day1/7-21 LLM과 Transformer 아키텍처 — Day1 핵심 정리]]에서 확인할 수 있다.
- 원문에서 제시한 제품 비교·그래프의 수치와 해석은 작성 시점의 수업 자료 내용이다. 최신 벤치마크나 제품 사양을 판단할 때는 별도 원본 검증이 필요하다.
