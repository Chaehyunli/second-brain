---
title: "[STUDYING] 5. Transformer: Self-Attention부터 생성 구조까지"
created: 2026-07-21
updated: 2026-07-21
type: blog-post
tags: ["blog", "technical-writing"]
category: "STUDYING"
published: 2026-07-21
source_url: https://ch010104.tistory.com/311
---
# [STUDYING] 5. Transformer: Self-Attention부터 생성 구조까지

## 원문

https://ch010104.tistory.com/311

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

Transformer는 RNN·CNN 없이 Attention을 중심으로 시퀀스를 처리하는 아키텍처다. 문장 전체의 토큰 관계를 병렬로 계산할 수 있어, 대규모 언어모델의 학습과 발전을 가능하게 한 핵심 구조가 되었다.

Self-Attention에서 각 입력 토큰은 선형변환을 거쳐 Query(Q), Key(K), Value(V)를 만든다. Query는 현재 토큰이 찾는 정보의 관점, Key는 다른 토큰이 제공하는 비교 기준, Value는 실제로 가져올 정보라고 이해할 수 있다.

## 원문 기반 개념 정리

Transformer는 RNN·CNN 없이 Attention을 중심으로 시퀀스를 처리하는 아키텍처다. 문장 전체의 토큰 관계를 병렬로 계산할 수 있어, 대규모 언어모델의 학습과 발전을 가능하게 한 핵심 구조가 되었다.

### Self-Attention의 질문: 지금 어떤 토큰을 참고해야 하는가

Self-Attention에서 각 입력 토큰은 선형변환을 거쳐 Query(Q), Key(K), Value(V)를 만든다. Query는 현재 토큰이 찾는 정보의 관점, Key는 다른 토큰이 제공하는 비교 기준, Value는 실제로 가져올 정보라고 이해할 수 있다.

예를 들어 “민지가 책을 읽었다”에서 읽었다를 해석할 때 모델은 민지가와 책을에 서로 다른 정도로 주목한다. 중요한 점은 사람이 문법 규칙을 직접 지정하지 않아도, 학습을 통해 어떤 관계가 유용한지 가중치로 찾는다는 것이다.

### Scaled Dot-Product Attention

Q와 K의 내적으로 토큰 사이의 관련도 점수를 계산한다. 점수가 크면 해당 Key를 가진 토큰을 더 참고할 가능성이 높다. 차원 dₖ가 커지면 내적 값이 너무 커져 Softmax가 지나치게 한 후보에 쏠리고 학습이 불안정해질 수 있으므로 √dₖ로 나눈다.

Softmax는 점수를 합이 1인 가중치로 바꾸고, 이 가중치로 Value를 합쳐 문맥이 반영된 새 벡터를 만든다. 즉 단어는 고립된 표현이 아니라, 현재 문장에서 필요한 다른 토큰 정보를 섞은 표현으로 바뀐다.

### Multi-Head Attention

한 종류의 관계만 보는 대신 여러 head가 서로 다른 투영 공간에서 Attention을 계산한다. 어떤 head가 주어-동사 관계에, 다른 head가 대명사-선행사 또는 의미적 유사성에 주목하도록 학습될 수 있다. 각 head 출력은 연결(concatenate)한 뒤 선형변환해 다음 층이 사용할 하나의 표현으로 통합한다.

다만 head에 사람이 미리 역할을 배정하는 것은 아니며, attention weight만으로 모델의 완전한 사고 과정을 설명할 수도 없다.

### Transformer 블록을 이루는 요소

Self-Attention 뒤에는 각 토큰에 독립적으로 적용되는 Feed-Forward Network가 있어 비선형적인 특징 변환을 수행한다. Residual Connection은 원래 입력을 더해 정보 손실과 기울기 소실을 줄이고, Layer Normalization은 값의 분포를 안정화해 깊은 네트워크 학습을 돕는다.

Attention은 토큰 순서 자체를 알지 못한다. 따라서 “개가 사람을 물었다”와 “사람이 개를 물었다”의 차이를 표현하려면 위치 정보를 입력 임베딩에 더하는 Positional Encoding이 필요하다.

### Encoder·Decoder와 Masking

Encoder는 입력 전체를 참고해 문맥적 표현을 만들며, 분류·검색·정보 추출에 강점이 있다. Decoder는 이전 토큰을 바탕으로 다음 토큰을 생성하며 GPT 계열 LLM의 기반이 된다. Encoder-Decoder 구조는 입력을 이해한 뒤 다른 출력 시퀀스를 생성하므로 번역·요약에 적합하다.

생성 모델은 미래 토큰을 미리 보면 안 된다. Causal Mask는 i번째 토큰이 i 이후 위치의 Key를 보지 못하게 막는다. 학습 중에는 정답 문장을 사용해 여러 위치의 손실을 병렬 계산할 수 있지만, 실제 생성에서는 이전에 나온 토큰만 사용해 한 단계씩 다음 토큰을 만든다.

### LLM으로 이어지는 의미와 한계

Transformer는 병렬 처리와 장거리 관계 학습을 가능하게 해 대규모 사전학습을 확장했다. 하지만 입력 길이가 길어질수록 Attention의 계산·메모리 비용도 커질 수 있다. 그래서 긴 문서 시스템에서는 관련 문서만 선별하는 RAG, 청킹, 대화 이력 요약, 구조화된 메모리 같은 Context Engineering이 함께 필요하다.

LLM의 출력은 확률적 생성이다. 따라서 검색·도구 호출·출력 형식 검증·사람 승인 같은 시스템 설계가 결합될 때 Transformer의 언어 능력이 실제 서비스에서 더 안전하게 활용될 수 있다.

## 관련 글

- [[blog/STUDYING/index|STUDYING]]
