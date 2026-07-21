---
title: "[7/21] LLM과 Transformer 아키텍처 — Day1 핵심 정리"
notion_page_id: 3a41d84b-f68e-8163-bfa0-d4f8af36e3d5
source: https://app.notion.com/p/3a41d84bf68e8163bfa0d4f8af36e3d5
source_url: https://app.notion.com/p/3a41d84bf68e8163bfa0d4f8af36e3d5
synced_at: 2026-07-21T15:09:09Z
content_sha256: b1d1aa9636a818c7c23569377d823c337fd4c1854de48958105b274fb69e374a
---

# [7/21] LLM과 Transformer 아키텍처 — Day1 핵심 정리

[[notion/SKALA/index|SKALA 학습 노트]]

- 원문: [Notion 페이지](https://app.notion.com/p/3a41d84bf68e8163bfa0d4f8af36e3d5)
- 범위: Software 1.0·2.0·3.0, LLM과 NLP 표현, 임베딩·언어모델, Transformer와 Self-Attention의 수학적 구성, 인코더·디코더의 동작을 순서대로 다룬다.

## 1. Software 1.0에서 Software 3.0으로 (슬라이드 3–14)

### Software 1.0과 2.0

- **Software 1.0**은 사람이 Python·C++·JavaScript·CSS 등으로 규칙과 예외를 명시하고, `Programmer-readable code → Interpreter/Compiler → Machine Program` 흐름으로 실행 프로그램을 만든다. 로직을 사람이 직접 통제하므로 검증 가능성과 재현성이 중요한 영역에서 강점이 있다.
- **Software 2.0**은 사람이 개별 규칙 대신 데이터셋, 신경망 구조, 손실함수, 학습 절차를 제공하고 최적화기가 가중치를 찾는 방식이다. `Data + NN architecture → Optimizer/Compiler → Statistically-based Machine Program`으로 표현된다. 따라서 성능 개선 시 코드뿐 아니라 데이터 품질·라벨·목적함수가 실제 문제를 반영하는지 점검해야 한다.
- 2.0은 이미지 분류·추천·번역·음성 인식·이상탐지처럼 규칙을 모두 쓰기 어려운 문제에 적합하지만, 과업마다 데이터·정답·평가 기준·학습·배포를 다시 준비하는 **task-specific AI**라는 한계가 있다.

### Foundation Model과 Software 3.0

Transformer의 등장(2017년 *Attention Is All You Need*) → Foundation Model의 대규모 사전학습 → LLM 대중화라는 흐름에서, 하나의 모델이 Fine-tuning·Prompting으로 여러 과업에 적응하는 범용 모델로 전환한다.

**Software 3.0**에서는 자연어 지시와 데이터를 AI agent에 제공해 프로그램 또는 통계적 프로그램을 생성한다. 개발자의 역할은 코드를 전부 작성하는 일에서 목표·역할·제약을 명세하는 일로 확장된다. 단, 자연어는 모호하므로 목표와 제약을 명확히 적고 결과를 검증해야 한다. 1.0·2.0·3.0은 완전한 대체 관계가 아니라 문제 특성에 맞게 함께 쓰인다.

### LLM의 역할·한계·증강지능

원문은 LLM을 추론 엔진, 지식 인터페이스, 자연어 컴파일러, 에이전트의 두뇌 역할을 하는 새로운 실행 환경으로 설명한다. 다만 제품 설계에는 다음 네 한계를 포함해야 한다.

1. **Black Box**: 수십억 파라미터가 답을 만든 과정을 설명하거나 오류 원인을 추적하기 어렵다.
2. **Bias**: 웹 학습데이터의 문화적·시대적·사실적 편향이 남으며, 프롬프트만으로 근본 제거되지 않아 조용히 실패할 수 있다.
3. **Hallucination**: LLM은 정답 검색기가 아니라 다음 토큰의 그럴듯함을 예측하므로 가짜 출처·수치·코드를 자연스럽게 만들 수 있다.
4. **Non-deterministic**: 같은 입력도 결과가 달라질 수 있어 일반 프로그램과 같은 일관성을 전제하면 안 된다.

따라서 결정론적 업무는 기존 코드로, 판단·추론·생성은 LLM으로 맡기고 검증·데이터 품질·사람의 감독을 결합한다. 증강지능은 AI를 인간 대체가 아니라 지식·판단·의사결정을 확장하는 co-pilot으로 본다. 예시로 리테일 AI는 유동인구·구매이력·판매데이터에서 레이아웃을 제안하지만 최종 진열·판매 판단은 담당자가 한다.

## 2. LLM과 NLP 표현의 발전 (슬라이드 18–42)

LLM은 방대한 텍스트를 학습해 언어를 이해·생성·처리하는 시스템이며, 하나의 사전학습 모델로 번역·요약·질의응답 같은 과업을 폭넓게 수행한다. 자연어가 중요한 프로그래밍 매개가 되었지만 자연어 지시는 실행 명세와 같지 않으므로 반복 확인이 필요하다.

### 빈도 기반 표현

- **One-hot**: 어휘 사전의 해당 위치만 1, 나머지는 0인 벡터다. 예를 들어 사전에서 `아주`가 3번이면 `[0, 0, 1, 0, 0]`이다.
- **BoW**: 단어 순서를 버리고 빈도를 합친다. `아주 아주 위험 합니다`는 `[0, 0, 2, 1, 1]`처럼 표현된다.
- **N-gram**: 연속한 n개 단어로 국소 순서를 보존한다. `I am studying bigram model`의 bi-gram은 `{I am, am studying, studying bigram, bigram model}`이다. n이 커지면 조합과 메모리가 폭발한다.
- **TF-IDF**: 문서 안 빈도(TF)와 전체 문서에서의 희귀도(IDF)를 곱해, 해당 문서에는 자주 나오지만 전체에는 드문 단어에 큰 가중치를 준다.

이 방식은 주제분류·검색에 유용하지만 순서·긴 문맥·의미 관계를 충분히 표현하지 못하고 어휘가 커지면 희소 고차원 문제가 생긴다. WordNet 같은 시소러스는 Synset·상위어·하위어·부분 관계를 그래프로 제공하지만 구축 비용과 신조어·실제 문맥 반영에 한계가 있다.

### 분포가설, 임베딩, 언어모델

**분포가설**은 비슷한 문맥에서 쓰이는 단어는 의미도 비슷하다는 관점이다. Word Embedding은 단어를 밀집 벡터로 바꿔 의미가 가까운 단어가 벡터 공간에서도 가까워지게 한다.

- **Word2Vec**은 주변 단어로 중심 단어를 예측하는 CBOW 또는 중심 단어로 주변을 예측하는 Skip-gram으로 임베딩을 학습한다. 예문 `you say goodbye and i say hello.`에서 `goodbye`와 주변 단어의 관계를 입력·정답 쌍으로 만들며, 은닉층 가중치가 의미 벡터가 된다.
- `king - man + woman ≈ queen` 같은 관계는 벡터 공간의 규칙성을 보이지만 항상 정확하지 않고 데이터 편향·빈도의 영향을 받는다.
- **Language Model**은 단어열의 그럴듯함에 확률을 부여하고, 앞 문맥을 보고 다음 단어 후보의 확률을 추정한다. RNN은 이전 은닉상태를 전달하지만 긴 문장에서 vanishing gradient와 장기 의존성 문제가 있다.
- LSTM은 gate로 정보 흐름을 더 세밀하게 제어하고, GRU는 이를 경량화한다. Seq2Seq는 encoder의 context vector를 decoder에 넘기지만 긴 입력을 하나의 벡터로 압축하면 정보가 소실된다. Attention은 출력 시점마다 encoder의 전체 hidden state를 참고하고 단어별 중요도를 점수화해 이 문제를 완화한다.
- **Contextual embedding**은 `bank`처럼 동일한 단어도 금융기관/강둑이라는 주변 문맥에 따라 다른 벡터가 되게 한다.

전이학습은 사전학습 모델이 이미 구조화한 중간 표현을 유사 과업에 쓰는 방법이다. 원문은 GPT-3 학습데이터를 약 500B token, GPT-2 1.5B→GPT-3 175B 파라미터로 제시하며, 스케일링이 성능 향상과 함께 자원·비용 문제도 낳는다고 설명한다.

## 3. 벡터·유사도·행렬 연산 (슬라이드 44–55)

- **유클리드 거리**는 차이의 제곱합에 제곱근을 취한 직선 거리로, 절대 크기가 의미 있는 공간에서는 직관적이지만 고차원 임베딩의 크기 차이에 민감하다.
- **코사인 유사도**는 두 벡터 내적을 각 길이로 나누어 방향의 각도를 비교한다. 1은 같은 방향, 0은 직교, -1은 반대 방향이다. 문서 길이보다 방향이 중요한 텍스트 임베딩에 자주 사용한다. 표현 모델·차원·척도에 따라 검색 이웃이 달라질 수 있다.
- **내적**은 대응 원소의 곱을 더해 스칼라를 만들며, Attention에서 Query와 Key의 관련성 점수에 쓰인다. 행렬곱은 왼쪽 행과 오른쪽 열의 내적을 원소로 계산하며 신경망 선형층·Attention 투영을 배치 단위로 수행한다.
- **선형변환**은 행렬로 벡터를 다른 표현 공간에 매핑한다. 같은 입력에서 Q·K·V처럼 역할이 다른 표현을 만들 때 사용한다. 원문 예시에서 `(1×K)` 입력은 `(K×768)` 가중치로 `(1×768)`, 또는 `(K×1536)` 가중치로 `(1×1536)` 벡터가 된다.
- **Softmax**는 실수 점수를 합이 1인 확률분포로 바꾼다. 큰 점수의 비중을 키우지만 점수 규모에 민감하므로 Attention의 `√d_k` 스케일링과 연결된다.

## 4. Transformer와 Self-Attention (슬라이드 57–65)

Transformer는 RNN/CNN 없이 Self-Attention으로 시퀀스를 처리하자는 2017년 제안이다. RNN 계열의 순차 처리·장기 의존성 문제와 CNN의 먼 토큰 관계 처리 문제를 피하면서 병렬 학습을 가능하게 했다. 원문은 WMT 2014 English–German에서 BLEU 28.4, English–French에서 BLEU 41.8이라는 당시 SOTA 성과와 더 낮은 학습비용을 제시한다.

### 인코더·디코더와 Q/K/V

Transformer는 인코더-디코더 구조다. 인코더는 입력을 여러 self-attention과 feed-forward 층으로 벡터화하고, 디코더는 인코딩 표현과 masked self-attention으로 목표 문장을 생성한다.

Self-Attention은 입력을 각각 Q(Query), K(Key), V(Value)로 선형변환한다.

- **Q**: 어떤 정보를 참고할지 묻는 표현
- **K**: 다른 Q가 참고할 수 있도록 자신을 나타내는 표현
- **V**: 실제로 전달·가중합할 정보

점수행렬은 `QKᵀ`이다. `(i, j)` 원소는 i번째 토큰이 j번째 토큰을 얼마나 주목하는지의 원점수이며, 확률이 아니므로 스케일링과 Softmax가 뒤따른다. 예시에서 `study`의 Q가 `I, study, AI, hard`의 K와 내적해 관련성을 만들고, 그 비율로 V를 섞어 문맥화된 표현을 만든다.

### Scaled Dot-Product Attention

Q·K 차원 `d_k`가 커지면 내적 분산이 커져 Softmax가 포화되고 gradient가 작아질 수 있다. 이를 막기 위해 `√d_k`로 나눈 뒤 Softmax를 적용한다.

`Attention(Q, K, V) = Softmax(QKᵀ / √d_k)V`

이 식의 출력은 각 토큰이 다른 토큰의 V를 가중합한 문맥 벡터다. 행렬 연산이므로 병렬 처리할 수 있다.

## 5. Multi-Head Attention과 인코더 블록 (슬라이드 66–72)

**Multi-Head Attention**은 여러 head가 서로 다른 투영 공간에서 토큰 관계를 학습하게 한다. 각 head의 결과를 concatenate한 뒤 다시 선형변환해 여러 관점의 특징을 통합하고 다음 층이 쓸 차원으로 맞춘다. head별 가중치는 학습되는 값이므로 사전에 “이 head는 문법, 저 head는 의미”라고 고정할 수는 없다.

인코더 블록은 attention 결과에 원래 입력을 더하는 **residual connection**과 **LayerNorm**을 사용한다.

`Output = LayerNorm(Input + MultiHeadAttention(Input))`

잔차 연결은 원래 정보를 보존하고 gradient 소실을 줄이며, LayerNorm은 토큰 벡터의 분포를 정규화해 학습을 안정화한다. 이어지는 Feed-Forward Network는 각 토큰 위치에 독립적인 비선형 변환(ReLU 등)을 적용한다. 토큰 간 상호작용은 Attention이, 위치별 특징 변환은 FFN이 담당한다.

Self-Attention은 토큰을 병렬로 보기 때문에 순서를 자체적으로 알 수 없다. 그래서 입력 임베딩에 **Positional Encoding**을 더한다. 원문은 학습 가능한 position embedding 또는 삼각함수 기반 인코딩을 언급하며, 단순 위치 숫자는 의미 벡터를 덮을 수 있으므로 적절하지 않다고 설명한다. 이것이 `나는 밥을 먹었다`와 `밥이 나를 먹었다`처럼 순서가 바뀐 문장을 구별할 수 있게 하는 보완책이다.

디코더의 **Masked Self-Attention**은 현재 위치가 미래 토큰의 Key를 보지 못하게 점수를 차단한다. 학습 때는 정답 시퀀스로 병렬 손실을 계산할 수 있지만, 추론 때는 이전에 생성한 토큰만 사용해 한 단계씩 다음 토큰을 생성한다. 즉 미래 정답을 미리 참조하지 못하게 하는 mask가 생성형 언어모델의 인과성을 보장한다.

## 학습 점검

1. Software 2.0의 task-specific 한계를 Foundation Model은 사전학습·Prompting·Fine-tuning으로 어떻게 바꾸는가?
2. BoW/TF-IDF의 순서·의미 한계를 Word2Vec과 contextual embedding은 각각 어떻게 보완하는가?
3. `QKᵀ` 점수에 왜 `√d_k`로 나누고 Softmax를 적용하는가?
4. Self-Attention이 순서를 모르는 문제를 Positional Encoding과 causal mask는 각각 어떻게 해결하는가?

## 공개 게시물

- [[blog/STUDYING/STUDYING- 5. Transformer- Self-Attention부터 생성 구조까지|공개 블로그 글]]
