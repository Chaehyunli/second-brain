---
title: "[7/21] 참고 — Multi-Head Attention"
notion_page_id: "3a41d84b-f68e-81bc-a6e2-de8e8a59375c"
notion_url: "https://app.notion.com/p/3a41d84bf68e81bca6e2de8e8a59375c"
source_url: "https://www.blossominkyung.com/deeplearning/transformer-mha"
source_type: "external_reference"
content_sha256: "816a028b4c7a907878b0b81e15575f4952dc1e06e78cb59dd760da0ad29201e1"
synced_at: "2026-07-21T07:00:29Z"
source_title: "트랜스포머(Transformer) 파헤치기—2. Multi-Head Attention"
tags: [SKALA, Transformer, self-attention, multi-head-attention]
---

# [7/21] 참고 — Multi-Head Attention

## 원문
[트랜스포머(Transformer) 파헤치기—2. Multi-Head Attention](https://www.blossominkyung.com/deeplearning/transformer-mha)

## 이 참고 노트의 위치
Self-Attention은 한 토큰이 같은 시퀀스 안의 다른 토큰을 얼마나 참고할지 계산한다. Multi-Head Attention은 이 계산을 여러 투영 공간에서 병렬로 수행해 문법·의미·장거리 의존성처럼 서로 다른 관계를 함께 포착한다.

- 상위 Notion 페이지: [[notion/SKALA/index|SKALA 학습 노트]]
- Day1 Notion 원문: [LLM과 Transformer 아키텍처 — Day1 핵심 정리](https://app.notion.com/p/3a41d84bf68e8163bfa0d4f8af36e3d5)

## 1. Attention과 Self-Attention의 차이
일반 Attention은 현재 질의에 답하기 위해 입력 중 더 관련 있는 부분에 큰 가중치를 둔다. 기계번역의 decoder처럼, 한쪽 시퀀스의 상태가 다른 쪽 입력을 참조하는 형태가 대표적이다.

**Self-Attention**은 Q·K·V가 모두 같은 입력 시퀀스에서 만들어진다. 따라서 각 토큰은 문장 안의 다른 모든 토큰을 참고해 자신을 문맥화한다. 같은 표면 단어도 주변 단어가 다르면 다른 의미 표현을 가질 수 있다. 예를 들어 `tear`는 `paper`와의 관계에서는 ‘찢다’, `shed`와의 관계에서는 ‘눈물’이라는 단서를 얻는다.

## 2. Query, Key, Value의 역할
입력 `X`는 서로 다른 학습 가중치로 세 가지 표현으로 투영된다.

```python
Q = X @ W_Q  # 현재 토큰이 찾는 정보
K = X @ W_K  # 다른 토큰이 제공하는 검색용 특징
V = X @ W_V  # 실제로 전달·합산할 정보
```

| 표현 | 질문으로 이해하기 | 계산에서 하는 일 |
| --- | --- | --- |
| Query | “나는 무엇을 참고해야 하는가?” | Key와 비교해 관련성 점수 생성 |
| Key | “나는 어떤 조건으로 참조될 수 있는가?” | Query와의 매칭 대상 |
| Value | “참조되면 어떤 정보를 전달하는가?” | attention 가중합의 실제 내용 |

딕셔너리의 key-value 비유와 달리, attention은 정확히 같은 key만 찾지 않는다. Query와 Key의 **유사도 정도**에 비례해 여러 Value를 섞는다.

## 3. Scaled Dot-Product Attention의 계산 흐름

$$
Attention(Q,K,V)=softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

### ① Score: `QKᵀ`
`QKᵀ`의 `(i, j)` 성분은 i번째 Query 토큰이 j번째 Key 토큰을 얼마나 참고할지 나타내는 원시 점수다. 각 행은 하나의 토큰이 모든 토큰에 주는 관심 분포의 출발점이다.

### ② Scale: `√d_k`로 나누기
Key 차원 `d_k`가 커지면 내적의 크기와 분산도 커질 수 있다. 큰 점수를 그대로 Softmax에 넣으면 한 항목만 1에 가깝고 나머지가 0에 가까워져 gradient가 작아질 수 있다. `√d_k` 스케일링은 점수 범위를 완화해 학습을 안정화한다.

### ③ Softmax: 가중치로 정규화
각 Query 행에 Softmax를 적용하면 가중치는 0~1 사이가 되고 행 합은 1이다. 이 값은 확률처럼 해석할 수 있는 attention 비중이지만, 사람의 설명 가능한 인과적 중요도와 동일하다고 단정하면 안 된다.

### ④ Value 가중합
정규화한 attention weight와 V를 곱하면 각 토큰은 다른 토큰의 정보를 관련성 비율로 섞은 새 문맥 벡터를 얻는다.

```text
input X
→ Q, K, V 선형 투영
→ QKᵀ: 관련성 점수
→ / √d_k: 점수 안정화
→ softmax: attention weight
→ weight × V: 문맥화된 output
```

## 4. Multi-Head Attention: 한 가지 관계만 보지 않기
한 개의 attention head는 한 투영 공간에서만 토큰 관계를 본다. Multi-Head Attention은 `h`개의 head가 서로 다른 `W_Q^h`, `W_K^h`, `W_V^h`를 학습하게 한다.

$$
head_i = Attention(QW_i^Q, KW_i^K, VW_i^V)
$$

$$
MultiHead(Q,K,V) = Concat(head_1,\ldots,head_h)W^O
$$

각 head가 사람이 붙인 ‘문법 head’나 ‘의미 head’ 하나로 반드시 고정되는 것은 아니다. 다만 여러 투영 공간은 주어·동사 관계, 대명사 지시, 인접 어구, 장거리 의미 연결처럼 서로 다른 패턴을 병렬로 포착할 **표현 용량**을 제공한다.

## 5. Concat 뒤 출력 선형변환의 역할
여러 head의 출력은 이어 붙인 뒤 `W^O`를 거쳐 다시 `d_model` 공간으로 변환된다.

- head별로 분산된 특징을 통합한다.
- 다음 레이어가 사용할 일정한 차원으로 맞춘다.
- 서로 다른 관점의 정보를 학습 가능한 방식으로 재조합한다.

따라서 Multi-Head Attention은 단순히 같은 attention을 여러 번 복제하는 것이 아니라, **서로 다른 투영 → 관계 계산 → 정보 통합**의 구조다.

## 6. Transformer 블록 안에서의 연결
인코더 블록에서는 보통 다음 흐름으로 동작한다.

```text
X = token embedding + positional encoding
H = LayerNorm(X + MultiHeadAttention(X, X, X))
Y = LayerNorm(H + FeedForward(H))
```

- positional encoding이 어순 단서를 제공한다.
- multi-head attention이 토큰 사이 정보를 섞는다.
- residual connection이 원래 입력과 gradient 흐름을 보존한다.
- layer normalization이 학습 분포를 안정화한다.
- feed-forward network가 각 토큰 위치에 비선형 특징 변환을 적용한다.

Decoder의 masked self-attention은 미래 토큰을 보지 못하게 mask를 추가한다. 그래서 학습 중에는 병렬 계산하면서도, 생성 시에는 이전 토큰만 근거로 다음 토큰을 예측할 수 있다.

## 학습 점검
- [ ] 일반 Attention과 Self-Attention의 Q·K·V 출처 차이를 설명할 수 있다.
- [ ] Q·K의 내적이 왜 attention score가 되는지 설명할 수 있다.
- [ ] `√d_k` 스케일링이 Softmax·gradient 안정화와 연결되는 이유를 설명할 수 있다.
- [ ] Multi-Head Attention에서 concat 후 `W^O`가 필요한 이유를 설명할 수 있다.
- [ ] positional encoding과 multi-head attention이 Transformer 입력에서 어떻게 이어지는지 설명할 수 있다.

## 출처
- [원문 글](https://www.blossominkyung.com/deeplearning/transformer-mha)
- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
