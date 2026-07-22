---
title: "[STUDYING] 6 - 1. LLM과 Transformer 아키텍처_Day2 - 핵심 정리"
created: 2026-07-22
updated: 2026-07-22
type: blog-post
tags: ["blog", "technical-writing", "LLM", "Studying", "Transformer"]
category: "STUDYING"
published: 2026-07-22
source_url: https://ch010104.tistory.com/312
---
# [STUDYING] 6 - 1. LLM과 Transformer 아키텍처_Day2 - 핵심 정리

## 원문

https://ch010104.tistory.com/312

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

전 세계 지식 근로자의 75%가 생성형AI를 업무 현장에 활용 중임(31.5개국 3.1만명 설문)

기존 1.0 버전이 개발자 옆에서 코딩을 도와주는 AI 기반 에디터(IDE) 형태였다면, 2.0은 여러 AI 에이전트에게 역할을 분담하고 병렬로 업무를 지시하는 독립형 명령/관리 플랫폼으로 완전히 개편

## 원문 기반 개념 정리

생성형 AI가 업무 자동화를 더 빠르게 앞당기는 추세임

전 세계 지식 근로자의 75%가 생성형AI를 업무 현장에 활용 중임(31.5개국 3.1만명 설문)

### AI 활용 능력이 곧 경쟁력이 되는 시대

### 시대별 경쟁력의 원천 비교

기존 1.0 버전이 개발자 옆에서 코딩을 도와주는 AI 기반 에디터(IDE) 형태였다면, 2.0은 여러 AI 에이전트에게 역할을 분담하고 병렬로 업무를 지시하는 독립형 명령/관리 플랫폼으로 완전히 개편

→ 기존 1.0과 다르게, 코드창이 없고, AI 에이전트들을 관리하는 것임

→ 앞으로 개발자의 경쟁력은 ‘코드를 얼마나 빨리 치느냐’가 아니라, ‘문제를 얼마나 잘 정의하고 AI를 활용해 시스템을 설계 하느냐’에 있음

이러한 흐름 속에서, Foward Deplyed Engineer라는 새로운 융합형 인재가 요구됨

→ 문제를 푸는 사람보다 문제를 정의하는 사람이 필요함

### 현대 LLM 모델 특징

LLM은 딥러닝 기반의 범용 모델로, 하나의 모델이 다양한 Task를 처리할 수 있다는 점이 핵심임. 현대 LLM을 특징짓는 네 가지 요소는 아래와 같음.

특징 핵심 내용 유의점

### LLM Leafer Board

https://www.vellum.ai/llm-leaderboard

### Market Leaders 비교 — Gemini · Claude · Grok · LLaMA

주요 LLM 4종을 개발 주체·포지셔닝·강점 관점에서 대비한 세그먼트임. 각 모델이 어떤 방향으로 차별화를 시도하는지가 핵심임.

### 모델별 한눈 비교

### RLHF — 사람의 선호(취향)를 담아보자 (Reinforcement Learning from Human Feedback)

RLHF는 사람의 선호(Feedback)를 이용해 LLM이 더 도움이 되고, 더 안전하며, 사람의 의도에 맞게 답변하도록 학습시키는 기법임.

### 왜 필요한가

대규모 사전학습(Pretraining)만 거친 LLM은 지식은 뛰어나지만, 사람이 원하는 방식으로 답하지는 못함. 그 이유는 학습 목표 자체가 "사람이 좋아하는 답"이 아니기 때문임.

다음 단어를 잘 예측하도록 학습되었을 뿐, 사람이 좋아하는 답변을 배우지는 않음.

그 결과 무례하거나 질문 의도를 빗나간 답을 하기도 함.

구체적 증상: 공격적인 답변, 장황한 답변, 사람 취향과 다른 답변 등.

### 핵심 전환

"정답을 맞히는 모델"에서 "친근한 표현을 담아 사람을 만족시키는 모델"로 진화할 필요가 생김.

즉 RLHF의 목적은 지식의 양을 늘리는 것이 아니라, 답변의 방식·태도를 사람 선호에 맞추는 데 있음.

### 장점 (Benefit)

일반적으로 지시 이해력이 향상되고, 응답의 정중함·일관성이 생겨 "사람 같은 답변"에 가까워짐.

ChatGPT를 포함한 생성형 AI 서비스의 대화 품질은 상당 부분 RLHF에 의해 유도됨. 즉 우리가 체감하는 "말 잘 통하는 느낌"의 상당수가 RLHF의 결과물임.

### 한계 (Limitation)

Reward Hacking: 모델이 내용의 옳고 그름보다 "보상(점수)을 잘 받는 응답(말투)"만 학습하는 문제.

그 결과 무난하고 안전한 답변만 내놓는 경향이 학습되어 응답의 다양성이 감소함.

사람마다 선호가 다름: 보상 기준이 사람 선호에 의존하기 때문에 편향이 끼어듦.

Reward Model 학습 과정에서 사람에 의한 편향이 발생함.

"어떤 사람/문화의 선호가 기준이 되어야 하는가?"라는 근본적 질문이 남음.

비용 문제: 사람이 직접 라벨링(Human Labeling)해야 하므로 비용이 많이 발생함.

### Scaling Law

### 개념 (Concept)

Scaling Law는 모델 크기(Parameter), 학습 데이터(Data), 연산량(Compute)을 늘리면 LLM의 성능이 예측 가능한 방식으로 향상된다는 경험적 법칙임.

핵심은 세 요소 중 하나만 키우는 게 아니라, Parameter·Data·Compute 세 요소의 균형에 의해 성능이 결정된다는 점임.

### Scaling의 3요소

(1) 모델의 크기 — 파라미터의 수

(2) 학습 데이터의 양 — 학습 토큰 수

(3) 연산량 — 학습에 투입되는 Compute

### 그래프 해석 (GPT-3 논문 Figure 1.2)

단순 과제(단어에서 무작위 기호 제거)에서 모델 크기별 in-context learning 성능을 비교한 그림임.

가로축: 문맥에 주어진 예시 수(Number of Examples in Context, K) / 세로축: 정확도(Accuracy %).

세 곡선은 모델 크기: 175B / 13B / 1.3B Params. 위로 갈수록 큰 모델임.

Zero-shot → One-shot → Few-shot으로 예시가 늘수록 정확도가 오르며, 큰 모델일수록 곡선이 더 가파르게 상승함.

즉 큰 모델일수록 문맥 정보(in-context information)를 더 효율적으로 활용함을 보여줌. 실선은 자연어 프롬프트가 있는 경우, 점선은 없는 경우(No Prompt)로, 큰 모델일수록 그 격차도 잘 활용함.

X축이 커질 수록, Y축이 지수형태로 줄어듬

때문에, AI 개발의 방향성이 바뀜

과거 : 더 좋은 모델 구조를 만들자 → 알고르짐 경쟁

Scaling Law : 더 크게 학습시키자 → 인프라 경쟁 → 더 많은 GPU를 사용!!

### Chinchilla's Scaling Law — 무조건 크게 만들면 될까?

앞서 본 "규모를 키우면 성능이 오른다"는 흐름에 대한 반론·보정 격 슬라이드임. 무작정 모델만 키우는 것이 최선이 아니라, 규모 안에서도 균형이 중요하다는 것을 보여줌.

### Chinchilla의 발견

2022년 Google DeepMind가 발표한 LLM임.

"큰 모델 + 적은 데이터"보다 "적절한 모델 크기 + 충분한 데이터"가 더 나은 성능을 보임을 관찰함.

즉 Scaling에도 최적 비율이 존재하며, 모델·데이터·연산량을 균형 있게 확장하는 것이 더 중요함.

### GPT-3 vs Chinchilla 비교

핵심 대비: Chinchilla는 파라미터가 GPT-3의 절반 이하지만, 학습 토큰은 약 4~5배 많음. 그 결과 더 작은 모델이 오히려 더 나은 성능을 냄.

### DeepSeek, Game-Changer? — 성능 대비 가격 관점

DeepSeek-V3가 왜 화제가 되었는지를 "성능 vs 가격" 산점도로 보여줌. 핵심 질문은 같은 성능을 훨씬 싼값에 낼 수 있는가임.

### 그래프 축 읽기

가로축(X): 언어모델 API 사용 시 입력 토큰 100만 개당 가격. 로그 스케일이라 오른쪽으로 갈수록 비용이 지수적으로 커짐. 왼쪽일수록 저렴함.

세로축(Y): MMLU Redux ZeroEval 점수. 언어모델의 지식·문제 해결 능력을 평가하는 지표로, 위로 갈수록 성능이 높음.

따라서 "왼쪽 위(싸고 성능 높음)"에 위치할수록 가성비가 좋은 모델이며, 그래프의 파란 영역이 성능/가격 최적 구간(performance/price ratio optimum range)임.

### DeepSeek-V3의 위치

DeepSeek-V3(빨간 별)는 그래프 왼쪽 상단, 즉 저가 구간에 있으면서도 성능 점수는 약 89 수준으로 최상위권에 위치함.

비교 대상: Claude 3.5 Sonnet, GPT-4o 등 최상위 성능 모델들은 성능은 비슷하지만 가격이 오른쪽(고가)에 몰려 있음.

반대로 GPT-4o-mini, DeepSeek-V2.5 등은 저가지만 성능(약 82)이 상대적으로 낮음.

결과적으로 DeepSeek-V3는 최상위급 성능을 최저가 구간에서 달성해, 최적 구간에 홀로 근접해 있는 형태임.

### DeepSeek-R1을 구성하는 세 축

Chain of Thought (사고 과정 노출): 추론 과정을 단계적으로 설명하게 함.

Explain Reasoning — 왜 그렇게 답했는지 근거를 드러냄.

Correct Mistakes — 중간 과정에서 스스로 오류를 교정함.

Reinforcement Learning (강화학습): 시행착오를 통해 행동을 개선함.

Experimentation — 다양한 시도를 함.

Behavior Update — 그 결과로 응답 방식을 갱신함.

Distillation (증류): 큰 모델의 능력을 작은 모델로 압축·전달함.

Compress Model — 모델을 경량화함.

Improve Accessibility — 누구나 쓰기 쉽게 접근성을 높임.

### 개념 (Concept)

큰 모델(Teacher)이 Reasoning을 거쳐 답변을 생성하면, 작은 모델(Student)은 그 정답뿐 아니라 추론(사고) 과정까지 함께 학습함.

즉 정답만 학습하는 것을 넘어, "생각하는 방법"까지 학습하는 것이 핵심임.

따라서 Distillation은 단순히 모델을 압축하는 것이 아니라, Teacher 모델의 능력을 Student 모델에게 전달하는 과정으로 이해해야 함.

### 작동 흐름 (Workflow)

(1) DeepSeek-R1 같은 거대 모델(Teacher)이 대량의 추론 데이터(Synthetic Reasoning Data)를 생성함.

(2) 그 데이터를 이용해 Llama 등 기존 오픈 모델을 다시 학습(Fine-tuning)시켜 Distilled 모델을 만듦.

정리하면 거대 모델 → 추론 데이터 생성 → 오픈 모델 재학습 → 경량 Distilled 모델의 순서임.

### Distillation — Hard Label vs Soft Label

Distillation에서 Student 모델이 무엇을 학습하는지를 라벨의 형태로 설명하는 슬라이드임. 핵심은 Soft Label이 왜 지식 전달에 유리한가임.

### Hard Label vs Soft Label 비교

핵심 차이: Hard Label은 "정답 하나만 1, 나머지는 0"이라 정답 외 정보가 없음. Soft Label은 "고양이 0.7, 개 0.2"처럼 클래스 간 유사성(고양이와 개가 비슷하다는 정보)까지 담고 있어 정보량이 훨씬 많음.

### Knowledge Distillation에서 Soft Label의 역할

일반화 성능 향상: Soft Label은 Teacher Model의 학습 경험(클래스 간 유사성 정보)을 담고 있어, Student Model이 Hard Label로만 배울 때보다 더 일반화된 성능을 가질 수 있음.

Student 모델의 학습 안정화: Soft Label 값의 특성 덕분에 더 촘촘하게 학습이 진행되어 과적합을 줄이는 데 효과적임.

추론 속도 향상: 안정적으로 학습된 Student Model은 실시간 대응이 필요한 환경에서도 빠르게 응답할 수 있음.

### MoE (Mixture of Experts) — 필요한 전문가만 활성화한다

MoE는 모든 파라미터를 매번 쓰는 대신, 입력마다 필요한 일부 전문가(Expert)만 골라 활성화하는 구조임. 앞서 DeepSeek R1이 "총 671B 중 활성 37B"였던 것이 바로 이 방식임.

### Dense Transformer vs MoE 비교

### MoE 작동 흐름

Router (Gating Network): 입력 질문을 보고 어떤 Expert를 쓸지 결정하는 라우터임. MoE의 핵심 부품임.

Expert 선택: 전체 Expert(1 ~ N) 중 라우터가 고른 소수(예: Expert 2, Expert N-1)만 활성화됨.

Combine (Weighted Sum): 선택된 Expert들의 출력을 가중합해 하나의 결과로 합침.

Output: 합쳐진 결과를 최종 출력으로 내보냄.

### MoE (Mixture of Experts) — Router와 Expert

### Router 작동 흐름 (Router Workflow)

입력 토큰이 들어오면 Router는 각 Expert에 대한 점수(Score)를 계산함 → Softmax로 각 Expert의 선택 확률을 산출함 → 확률이 높은 상위 몇 개(Top n)만 활성화함.

Router 자체도 작은 신경망(Linear Layer)이며, 학습 대상임. 즉 "어떤 입력을 어떤 Expert에 보낼지"도 학습을 통해 좋아짐.

### 관련 수식 풀이

Score = x·Wr : 입력 토큰 x에 라우터 가중치 Wr을 곱해 각 Expert에 대한 점수(적합도)를 구함.

Pi = e^(si) / Σj e^(sj) : 점수 si에 Softmax를 적용해 Expert i가 선택될 확률 Pi로 변환함. 분모는 전체 Expert 점수의 합이라, 모든 확률의 합이 1이 되도록 정규화하는 역할임.

정리하면 점수 계산(Score) → 확률화(Softmax) → 상위 n개 선택의 순서임.

### Expert의 전문화 원리

처음에는 모든 Expert가 동일함(차이 없음).

학습이 진행되면 Router가 비슷한 입력 토큰을 계속 같은 Expert에게 보냄 → 그 Expert는 해당 분야를 반복 학습하며 점점 그 영역의 "전문가"가 됨.

즉 Expert의 전문성은 사전에 지정된 것이 아니라, 라우팅과 학습이 반복되며 자연스럽게 형성되는 결과물임.

## 관련 글

- [[blog/STUDYING/index|STUDYING]]
