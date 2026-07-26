---
title: "[기타] BERT 개념 — 구조·사전 훈련·파인튜닝 정리"
created: 2026-07-26
updated: 2026-07-26
type: blog-post
tags: ["blog", "technical-writing"]
category: "기타"
published: 2026-07-26
source_url: https://ch010104.tistory.com/318
---
# [기타] BERT 개념 — 구조·사전 훈련·파인튜닝 정리

## 원문

https://ch010104.tistory.com/318

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

게시: 애뚱 · 2021-11-17 · 문돌이 존버/데이터 분석

이 노트는 원문을 그대로 복제하지 않고, 핵심 개념·도식·코드 흐름을 학습용으로 재구성했다. 원문은 "딥 러닝을 이용한 자연어 처리 입문"을 바탕으로 작성됐다고 밝힌다.

## 원문 기반 개념 정리

### 출처와 정리 범위

원문: 버트(BERT) 개념 간단히 이해하기

게시: 애뚱 · 2021-11-17 · 문돌이 존버/데이터 분석

확인일: 2026-07-26

이 노트는 원문을 그대로 복제하지 않고, 핵심 개념·도식·코드 흐름을 학습용으로 재구성했다. 원문은 "딥 러닝을 이용한 자연어 처리 입문"을 바탕으로 작성됐다고 밝힌다.

### 한눈에 보기

BERT는 Transformer 인코더만 여러 층 쌓아 대규모 비라벨 텍스트로 사전 훈련한 뒤, 목표 작업에 맞는 작은 출력층을 붙여 미세 조정하는 모델이다. 핵심은 각 토큰이 좌우 문맥을 함께 반영한 표현을 얻는다는 점이다.

### 1. 크기와 문맥형 표현

BERT-Base는 12개 인코더 층, hidden size 768, attention head 12개로 구성되며 약 110M 파라미터다. BERT-Large는 24개 층, hidden size 1024, head 16개로 약 340M 파라미터다.

입력 토큰 벡터는 각 인코더 층의 self-attention을 거치면서 같은 입력 안의 다른 토큰 정보를 반영한다. 따라서 [CLS]를 포함한 각 위치의 출력은 단순 단어 벡터가 아니라 문맥 의존 표현이다.

### 2. 입력은 세 임베딩의 합

### WordPiece

자주 쓰이는 단어는 그대로 두고, 어휘에 없는 단어는 더 작은 조각으로 나눈다. 예를 들어 embeddings가 어휘에 없으면 em, ##bed, ##ding, ##s처럼 분해할 수 있다. ##는 단어 중간에서 이어지는 조각이라는 표시다. 이 방식은 미등록 단어 문제를 완화한다.

### Position·Segment

BERT는 위치 정보를 학습 가능한 position embedding으로 더한다. 두 입력 구간을 쓸 때는 [SEP]로 경계를 표시하고 Segment 0/1 embedding을 더한다. 여기서 “두 문장”은 문법적 문장 두 개에만 한정되지 않으며, 질문과 본문처럼 두 텍스트 구간일 수도 있다.

### 3. 사전 훈련: MLM과 NSP

BERT의 원문 기준 사전 훈련은 두 목적을 함께 사용한다.

### Masked Language Modeling (MLM)

입력 토큰의 15%를 예측 대상으로 고른다.

그 대상 중 80%는 [MASK], 10%는 임의 단어, 10%는 원래 단어로 둔다.

모델은 선택된 위치의 원래 토큰만 예측하며, 이 변형 비율은 사전 훈련과 실제 사용 사이의 [MASK] 불일치를 줄이기 위한 장치다.

### Next Sentence Prediction (NSP)

두 텍스트 A/B가 실제로 이어지는 관계인지 이진 분류한다. 원문은 실제 연속 쌍과 무작위 조합 쌍을 50:50으로 제시하고, [CLS] 위치의 출력으로 IsNextSentence/NotNextSentence를 예측하는 흐름을 설명한다.

### 4. 파인튜닝: 출력층만 작업에 맞게 교체

사전 훈련된 BERT 위에 작은 task head를 붙여 레이블 데이터로 추가 훈련한다.

단일 텍스트 분류: [CLS] 출력으로 감성·뉴스 분류 등 문서 전체를 분류한다.

토큰 태깅: 각 토큰 위치의 출력으로 POS 태깅·개체명 인식(NER)을 수행한다.

텍스트 쌍 분류/회귀: [SEP]와 segment embedding으로 두 텍스트를 구분해 자연어 추론 등을 푼다.

질의응답: 질문과 본문을 함께 넣고 본문에서 답 span의 시작·끝 위치를 예측한다.

### 5. Attention mask

길이가 다른 입력을 배치로 맞추기 위해 padding을 넣을 때, attention mask는 실제 토큰과 padding을 구분한다. 원문 설명대로 일반적으로 실제 토큰 위치는 1, padding 위치는 0으로 두어 모델이 padding에 attention을 쓰지 않게 한다.

### 6. 최소 실습 흐름

원문은 TensorFlow와 Hugging Face의 TFBertForMaskedLM, AutoTokenizer, FillMaskPipeline으로 한국어 BERT 마스크 예측을 시연한다. 현재 환경에서는 라이브러리 버전 호환성을 먼저 확인해야 한다.

```text
from transformers import AutoTokenizer, FillMaskPipeline, TFBertForMaskedLM

model = TFBertForMaskedLM.from_pretrained("klue/bert-base", from_pt=True)
tokenizer = AutoTokenizer.from_pretrained("klue/bert-base")

inputs = tokenizer("치킨은 정말 맛있는 [MASK]다.", return_tensors="tf")
print(inputs["input_ids"])
print(inputs["token_type_ids"])
print(inputs["attention_mask"])

pipe = FillMaskPipeline(model=model, tokenizer=tokenizer)
pipe("치킨은 정말 맛있는 [MASK]다.")
```

### 학습 체크

[CLS] 출력이 문서 수준 분류에 자주 쓰이는 이유를 설명할 수 있는가?

WordPiece의 ## 표기가 무엇을 뜻하는가?

MLM에서 예측 손실을 계산하는 위치와 attention mask가 막는 위치는 어떻게 다른가?

단일 텍스트 분류·토큰 태깅·QA에서 각각 어느 출력 위치를 사용하는가?

### 원문·이미지 출처

글 전체: moondol-ai.tistory.com/463

삽입 도식 3개: 해당 원문 본문의 BERT-Base/Large 구조, contextual embedding, BERT·GPT-1·ELMo 비교 그림. 원문에 표시된 도식 출처는 "딥 러닝을 이용한 자연어 처리 입문"이다.

원문 저작권 표기는 저작자표시·비영리·변경금지이며, 본 노트는 출처를 연결한 요약과 필요한 도식 인용으로 한정한다.

## 관련 글

- [[blog/기타/index|기타]]
