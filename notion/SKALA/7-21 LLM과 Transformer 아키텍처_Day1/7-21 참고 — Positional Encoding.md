---
title: "[7/21] 참고 — Positional Encoding"
notion_page_id: "3a41d84b-f68e-81b1-b8f0-eb3100f0d53a"
notion_url: "https://app.notion.com/p/3a41d84bf68e81b1b8f0eb3100f0d53a"
source_url: "https://www.blossominkyung.com/deeplearning/transfomer-positional-encoding"
source_type: "external_reference"
content_sha256: "4ee9b49ef8243ad8b999331cfccaddfb1a36f2053fae3a1b79d94b63cf04c317"
synced_at: "2026-07-21T07:00:29Z"
source_title: "트랜스포머(Transformer) 파헤치기—1. Positional Encoding"
tags: [SKALA, Transformer, positional-encoding, attention]
---

# [7/21] 참고 — Positional Encoding

## 원문
[트랜스포머(Transformer) 파헤치기—1. Positional Encoding](https://www.blossominkyung.com/deeplearning/transfomer-positional-encoding)

## 이 참고 노트의 위치
Transformer는 토큰을 병렬로 처리한다. Positional Encoding은 이 병렬 처리의 장점은 유지하면서 **어순·거리·상대 위치**를 모델 입력에 전달하는 장치다. Day1의 Transformer 인코더 및 Self-Attention 설명을 읽은 뒤 연결해 복습한다.

- 상위 Notion 페이지: [[notion/SKALA/index|SKALA 학습 노트]]
- Day1 Notion 원문: [LLM과 Transformer 아키텍처 — Day1 핵심 정리](https://app.notion.com/p/3a41d84bf68e8163bfa0d4f8af36e3d5)

## 1. Input Embedding: 토큰을 계산 가능한 벡터로 바꾸기
문장은 토큰으로 나뉘고, 각 토큰은 vocabulary의 ID를 얻는다. 임베딩 레이어는 이 ID를 `d_model` 차원의 밀집 벡터로 바꾼다.

```text
"This is my car"
→ token IDs
→ embedding lookup
→ token embeddings X ∈ R^(sequence_length × d_model)
```

임베딩의 각 차원은 학습을 통해 단어의 사용 맥락·특징을 담는다. 의미적으로 비슷한 사용 맥락을 가진 단어는 벡터 공간에서 가까워질 수 있다. 그러나 임베딩만으로는 해당 토큰이 문장의 몇 번째 위치에 있는지 알 수 없다.

## 2. Transformer의 병렬 처리와 순서 정보 문제
RNN/LSTM은 이전 시점의 hidden state를 다음 시점으로 넘기므로 입력 순서가 구조에 들어간다. 반면 Transformer의 self-attention은 모든 토큰 쌍을 한꺼번에 계산한다. 이는 GPU 병렬 처리에 유리하지만, 입력 행을 바꾸어도 attention 연산 자체는 위치를 모른다.

어순은 의미를 바꾼다. 부정어의 위치가 달라지면 “입학할 수 있었다”와 “입학하지 못했다”처럼 문장 전체의 뜻이 바뀐다. 따라서 병렬 입력에 위치 정보를 별도로 주입해야 한다.

## 3. 위치 표현이 충족해야 할 조건
1. **일관성**: 같은 위치는 시퀀스 길이나 다른 입력과 무관하게 같은 식별값을 가져야 한다.
2. **크기 제어**: 위치 벡터가 단어 의미 임베딩보다 과도하게 커져 의미를 덮어서는 안 된다.
3. **구분 가능성**: 서로 다른 위치가 구분되어야 하며, 가까운 위치 사이의 관계도 학습할 수 있어야 한다.

단순한 정수 `1, 2, 3, ...`은 시퀀스가 길수록 값이 커진다. 반대로 0~1 정규화는 같은 절대 위치라도 전체 길이에 따라 값이 달라진다. 둘 다 위 조건을 동시에 만족하지 못한다.

## 4. Sinusoidal Positional Encoding
원 논문은 각 위치 `pos`와 벡터 차원 `i`에 서로 다른 주기의 사인·코사인 함수를 사용한다.

$$
PE_{(pos,2i)} = \sin\left(\frac{pos}{10000^{2i/d_{model}}}\right)
$$

$$
PE_{(pos,2i+1)} = \cos\left(\frac{pos}{10000^{2i/d_{model}}}\right)
$$

### 왜 사인·코사인인가
- 출력 범위가 -1~1이어서 위치 값이 무한히 커지지 않는다.
- 차원마다 다른 주기를 사용하므로 하나의 스칼라 성분이 우연히 같아도 전체 위치 벡터는 구분될 가능성이 높다.
- 사인·코사인을 번갈아 사용해 위상 차이를 활용한다.
- 고정식이므로 학습 때 보지 못한 더 긴 길이에도 위치 표현을 계산할 수 있다. 다만 일반화 성능은 모델·길이·학습 조건에 따라 별도로 검증해야 한다.

현대 Transformer 계열은 원 논문의 고정식 외에도 학습형 absolute positional embedding, relative position bias, RoPE 같은 위치 표현을 사용한다. 핵심 문제는 같지만 위치를 주입하는 방식은 모델마다 다르다.

## 5. Embedding + Position: 왜 concatenate가 아니라 덧셈인가
기본 Transformer는 토큰 임베딩과 위치 벡터의 차원을 같게 두고 더한다.

```python
x = token_embedding(token_ids)      # [batch, seq_len, d_model]
pos = positional_encoding(seq_len)  # [seq_len, d_model]
x = x + pos
```

덧셈은 입력 차원을 유지하므로 이후 선형층·attention의 파라미터 수와 연산량을 늘리지 않는다. 모델은 같은 표현 공간에서 의미와 위치를 함께 해석한다. 연결(concatenate)은 두 정보를 분리해 보존할 수 있지만 차원이 늘어 메모리·파라미터·런타임 비용이 증가한다.

## 6. Self-Attention과의 연결
위치 정보가 더해진 `X`는 Q·K·V를 만들기 위한 입력이 된다.

```text
X = token embedding + positional encoding
Q = XW_Q, K = XW_K, V = XW_V
→ attention score와 weighted value 계산
```

따라서 같은 단어라도 문장 위치와 주변 토큰에 따라 다른 attention 관계를 형성할 수 있다. Positional Encoding은 attention의 가중치 자체가 아니라, attention이 문맥을 계산할 때 사용할 **위치 단서가 포함된 입력 표현**이다.

## 학습 점검
- [ ] Transformer가 순서를 구조적으로 자동 인식하지 못하는 이유를 설명할 수 있다.
- [ ] 단순 증가 정수·0~1 정규화 위치값의 한계를 설명할 수 있다.
- [ ] Sinusoidal encoding에서 차원별 주기가 다른 이유를 설명할 수 있다.
- [ ] 위치 정보가 Q/K/V 생성 이전에 더해지는 흐름을 설명할 수 있다.

## 출처
- [원문 글](https://www.blossominkyung.com/deeplearning/transfomer-positional-encoding)
- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
