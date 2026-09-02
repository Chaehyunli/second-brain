---
title: "[9/2] 데이터분석 및 AIOps_머신러닝 및 딥러닝 이해_C_핵심정리"
notion_page_id: "3cf1d84b-f68e-8060-84b2-e8900d9609b2"
source_url: "https://app.notion.com/p/3cf1d84bf68e806084b2e8900d9609b2"
synced_at: "2026-09-02T15:07:57+00:00"
content_sha256: "293b61d7895a4d46485d4807155e277ebe3a00f206c5656e94c7209ac78d7d2a"
---

# [9/2] 데이터분석 및 AIOps_머신러닝 및 딥러닝 이해_C_핵심정리

[[notion/SKALA/index|SKALA 학습 노트]]
> 원문: [Notion 페이지](https://app.notion.com/p/3cf1d84bf68e806084b2e8900d9609b2)
>
> 원문의 임시 서명 이미지 URL은 보존하지 않았으며, 안정적으로 확인 가능한 텍스트·코드·표를 유지했다.

### 개요. 딥러닝 네트워크가 다루는 문제 유형
기존에는 아래 4가지 큰 갈래로 딥러닝 네트워크의 역할을 구분해 왔음
| 구분 | 이미지 분류 | 자연어 처리 & 시계열 예측 | 데이터 생성 | 제어/최적화 |
| --- | --- | --- | --- | --- |
| 성격 | Architecture | Architecture | Model | Algorithm |
| 키워드 | 이미지 처리, Convolution Layer, Pooling Layer | 시퀀스 데이터, 시간 의존성 | 생성자/판별자, 생성 모델, 경쟁적 학습 | Agent, Reward, Policy, Environment |
| 핵심 설명 | 이미지·영상의 공간적 정보를 추출하는데 특화된 구조. Convolution Layer로 입력 데이터의 패턴을 학습 | 과거의 상태를 현재 상태에 반영하여 시간적 패턴을 학습하는 네트워크 구조 | 2개의 신경망이 경쟁적으로 학습. 생성자는 실제에 가깝게 데이터 생성, 판별자는 그 데이터를 구분 | 에이전트가 환경과 상호작용하며 보상을 통해 최적의 행동을 학습. 보상 피드백을 통해 의사결정 학습 |
#### Deep Learning, Expansion (전체 지형도)
AI Model-based Network를 정형/NLP/Vision/Speech 등 데이터 유형별로 나누고, 각 유형 안에서 다시 `기본` 아키텍처와 `확장` 아키텍처로 세분화한 지도임

| 데이터 유형 | 기본 Architecture | 확장 Architecture | AI Task (기본→확장) |
| --- | --- | --- | --- |
| 정형 | CNN, RNN/LSTM | TabNet, TCN 등 | 분류 → 시계열 예측 → 군집 |
| NLP | RNN, LSTM | Attention, Transformer, BERT, GPT | 텍스트 분류 → 단어 예측 → 문장 요약 → 번역 → 문장 생성(LLM) |
| Vision | CNN | AlexNet, ResNet, DenseNet, EfficientNet, GAN, StarGAN/StyleGAN | 이미지 분류 → 이미지 생성 → Text2Image / Image2Text |
| Actuation(제어) | DQN, Policy, A2C | PPO, SAC, Multi Agent PPO | 최적화 → 자율주행 → Physical AI |
학습 방식 축으로 보면 Supervised(Transfer/Few-Shot 포함), Semi-Supervised(Self-Supervised 포함), Unsupervised, Reinforcement Learning(Meta, Active 포함)으로도 나뉨
#### DL Architecture Expansion History (연표)
Computer Vision과 NLP 계열이 각각 별도로 발전해 온 흐름을 정리한 표. 이 표는 강의 전체에서 섹션이 바뀔 때마다 반복적으로 다시 제시되며 지금까지의 진행 상황을 상기시키는 용도로 쓰임
| 연도 | CV Architecture | 기여 |
| --- | --- | --- |
| 1990 | CNN | 이미지 처리에 강점, 합성곱 필터로 이미지 특징 자동 추출하는 방법론 제시 |
| 1998 | LeNet-5 | 초기 CNN 중 하나, MNIST를 위해 설계되어 현대 CNN의 기초를 다짐 |
| 2012 | AlexNet | GPU 기반 ReLU·Dropout 사용한 대형 CNN, ImageNet에서 혁신적 성과 & 딥러닝 대중화 |
| 2014 | VGGNet | 작은 필터(3\*3)로 아키텍처 단순화, 객체 인식 성능 향상 |
| 2014 | GoogleNet(Inception) | Inception 모듈 도입, 계산 자원 효율화하며 높은 정확도 유지 |
| 2015 | ResNet | Residual Learning으로 최대 152층까지 깊은 네트워크 구성, 기울기 소실 문제 해결 |
| 2017 | DenseNet | 각 층을 모든 다른 층과 연결, 파라미터 수를 줄이면서 정확도 향상 |
| 2017 | YOLO | 이미지 내 객체를 빠르고 효율적으로 실시간 탐지 |
| 2018 | EfficientNet | 네트워크 깊이·폭·해상도를 균형있게 조정, 적은 파라미터로 성능 극대화 |
| 2021 | ViT(Vision Transformer) | Transformer를 이미지 분류에 적용한 첫 사례, 전통적 CNN 성능을 능가(2\~5%) |
| 연도 | NLP Architecture | 기여 |
| --- | --- | --- |
| 1985 | RNN | 시퀀스 데이터를 처리할 수 있는 첫 신경망, 순차적 데이터 처리에 탁월 |
| 1997 | LSTM | RNN의 기울기 소실 문제 해결, 언어/음성 시퀀스에서 뛰어난 성능 |
| 2014 | Word2Vec | 단어 임베딩 혁신, 단어의 의미 관계를 연속 벡터로 학습 |
| 2015 | Seq2Seq | 인코더-디코더 확장, 기계번역 및 순차 데이터 작업 성능 향상 |
| 2017 | Transformer | Self-Attention 도입으로 RNN/LSTM 대체, 병렬 처리로 뛰어난 성능 |
| 2018 | BERT | Transformer 디코더 구조를 양방향으로 확장, Pre-training·Transfer Learning |
| 2019 | GPT-2 | Transformer 디코더 구조를 단방향으로 확장, 문맥에 맞는 텍스트 생성 |
| 2020 | GPT-3 | 1750억개 파라미터의 대형 Transformer, 미세조정 없이 다양한 NLP Task 수행 |
| 2021 | DALL-E | 텍스트 설명으로 이미지 생성, Cross-Modal/Multi-Modal |
| 2021 | CLIP | 이미지-텍스트 쌍을 학습, 비전 작업에서 Zero-Shot 학습 가능 |
| 2023 | GPT-4 | GPT-3 후속, 향상된 문맥 이해와 자연스러운 텍스트 생성 |
#### 핵심 용어 정리
- `Architecture` : 신경망의 구조적 설계 방식. Layer 구성, 층 간 연결 방식, 데이터 흐름 등을 정의
- `Algorithm` : 문제를 해결하기 위한 절차나 계산 방법. 딥러닝에서는 학습 방법, 최적화 절차, 데이터 처리 방법(Gradient Descent, Backpropagation, Optimizer 등)을 지칭
- `Model` : 데이터를 입력 받아 예측·분류 등의 작업을 수행하는 학습된 결과물. 학습이 완료된 후 목적에 맞는 작업을 수행
---
### 1A. 귀납적 편향의 설계 - 데이터의 구조를 코드에 새기다
이번 파트는 MLP의 한계와, 그 한계를 이미지 데이터에 맞게 보완한 CNN(공간적 지역성과 가중치 공유)을 다룸
#### 1. MLP의 특징이자 한계
MLP(Multi-Layer Perceptron)는 뉴런들이 층으로 쌓여 있고, 한 층의 모든 뉴런이 다음 층의 모든 뉴런과 빠짐없이 연결된 구조(fully-connected)임. Input은 1차원 벡터이며, 속성들이 서로 독립적일 때(tabular 데이터) 유의미함
이미지 데이터를 MLP에 그대로 적용하면 다음 세 가지 문제가 발생함
| 문제 | 내용 | 필요한 성질 |
| --- | --- | --- |
| 공간 구조 소실 | 1차원 벡터로 펼쳐지면 공간 구조가 사라짐. `28*28`이 `784`가 되면 어떤 픽셀이 어떤 픽셀 옆에 있었는지 정보가 사라짐 | 격자 유지(가까운 픽셀 관계 확인) |
| 파라미터 폭발 | Fully-connected 구조에서 입력 784, Hidden 1000개면 연결만 약 78만개. 학습 자체가 무거워짐 | 파라미터 절약 |
| 위치 의존 | 입력 i번째 자리가 특정 가중치에 묶여, 입력 위치마다 별도 가중치를 학습함. 학습 과정에서 위치가 바뀌면 처음부터 다시 배워야 함 | 위치 무관 재사용(배운 패턴을 어디서나 적용) |
이렇게 데이터를 다루는데 필요한 새로운 성질을 구조 자체에 미리 반영하는 것을 `귀납적 편향`이라고 부름. 합리적으로 예측하고 일반화하기 위해 사전에 부여하는 추가적인 가정이나 제약 조건을 의미함
MNIST(Modified National Institute of Standards and Technology database, 손글씨 숫자 이미지셋)를 예시로 CNN Architecture가 어떻게 이미지를 분류하는지 살펴봄. `28x28` 흑백 이미지를 Convolution(padding=1, kernel=3x3, stride=1) + ReLU → Max pooling(kernel=2x2, stride=2)을 두 차례 거쳐 `32x28x28 → 32x14x14 → 64x14x14 → 64x7x7`로 줄인 뒤 Flatten하여 `3136` 차원을 `128`차원으로, 다시 `10`개 클래스(0\~9)로 분류함. 컬러 이미지(자동차 등)에서도 동일하게 (CONV-CONV-POOL) 블록을 여러 번 반복한 뒤 FC Layer에서 최종 클래스(car/truck/airplane/ship/horse)를 분류함
#### 2. Convolution, 용어의 이해

- `[프랑스어]` 두 개의 것이 합쳐져서 하나가 되는 것(합성적)
- `[수학/IT]` 두 함수에 대한 수학적 연산. 하나의 함수가 다른 함수에 작용하는 필터 역할을 담당(특히 신호 처리에서). Low-pass Filter, High-pass Filter처럼 입력 신호에 필터를 곱성곱하여 원하는 성분만 걸러내는데 쓰임
- `[DL]` 작은 필터(돋보기)가 이미지의 한 부분과 뒤섞이며 새로운 특징(이미지)을 만들어 냄
간단한 예시로 5x5 이미지 행렬과 3x3 필터를 합성곱하면 하나의 출력 값(예: `4`)이 나오는데, 이는 이미지의 국소 영역과 필터가 대응 위치별로 곱해진 뒤 모두 더해진 값임
#### 3. Convolution Layer
3차원 이미지 정보에서 이미지 특징(Feature Map)을 뽑아내는 계층으로, Input 이미지와 Filter 간의 연산으로 이루어짐. Input(3D) 이미지 위에서 Filter(Kernel)를 이동시키며 각 위치마다 계산값을 뽑아내는 구조임
`Output(5,5)`, `Kernel(3,3)`, `Input(5,5)`, `Padding(1)`, `Stride(1)`처럼 각 요소의 크기를 정의해 출력 Feature Map의 크기가 어떻게 결정되는지 구조적으로 표현함
#### 3-(1). Kernel
- `Kernel = Filter`
- 합성곱 연산을 수행하는 작은 창으로, 이미지 위를 움직이며 합성곱 연산을 수행해 특징을 뽑아내는 역할
RGB 3채널 이미지의 경우 채널별 커널이 각각 존재하며, 각 채널의 합성곱 결과(예: `308`, `-498`, `164`)를 모두 더하고 편향(bias)을 더해 최종 출력 Feature map의 한 값을 만들어 냄
#### 3-(2). Filter (합성곱/필터 연산)

- 합성곱 연산은 Input map에 Filter window 크기만큼 적용하여 연산
- 연산은 Window 크기를 유지하면서 Stride만큼 움직이며 반복 수행
`Filter(3,3)`을 `stride=1`로 적용할 때, 각 Step마다 겹치는 영역의 원소끼리 곱한 뒤 모두 더해서(예: `1*2+2*0+3*1+0*0+1*1+2*2+3*1+0*0+1*2=15`) 출력 Feature map의 값을 하나씩 채워나가는 방식으로 진행됨
#### 3-(3). Padding
- `[영어사전]` (폭신하게 만들거나 형태를 잡기 위해 안에 대는) 속, 충전재
- 합성곱 연산 후 변형되는 Output size를 보정하기 위해 Input 데이터에 특정값(주로 0)을 채우는 것

`4x4` 입력에 `Zero-padding 1`을 적용하면 `6x6`이 되고, 여기에 `Filter(3,3)`을 `stride=1`로 적용하면 다시 `4x4` 크기의 Output Feature Map이 나옴. 예를 들어 좌상단 `(1,1)` 위치의 합성곱 결과는 `0*2+0*0+0*1+0*0+1*1+2*2+0*1+0*0+1*2=7`처럼 계산됨
#### 4. Pooling Layer

- 대표값을 추출하여 작은 이미지를 생성
- 사진을 축소하면서도 좋은 특징을 획득할 수 있는 방법이며, 대표적으로 학습 파라미터가 없는 Max-pooling을 사용
`4*4` 입력을 `Pooling(2*2)`로 처리하면 `2*2` 크기로 줄어들며, 각 `2*2` 영역에서 가장 큰 값 하나만 대표값으로 남기는 방식(Max pooling)임
#### 5. Flatten Layer
- `Flatten Layer`, `FC Layer`, `Fully-Connected Layer`, `Affine Layer`는 모두 같은 것을 가리킴
- 분석한 이미지 데이터를 라벨 분류하기 위해 1차원으로 바꿔주는 역할
| 구성 요소 | 역할 |
| --- | --- |
| Flatten Layer(Fully-Connected Layer) | N차원 데이터를 1차원으로 바꿈 |
| Dense Layer | Activation Function 적용 |
| Dense Layer(마지막) | Softmax 적용(Classification), 뉴런 개수는 라벨 개수와 동일 |
#### 6. Softmax Function
- `Softmax`, `Argmax`, `Argument Max`는 모두 "Max 값을 가짐을 증명한다"는 의미를 가짐
- CNN Architecture를 통해 어떤 클래스가 Max로 분류되었는지, Max값의 위치가 몇 번째인지 증명하는 역할

FC Layer의 출력값(logit, 예: `-0.1, 3.8, 1.1, -0.3`)을 Softmax 함수 `P(y=i) = e^zi / Σ e^zj`에 통과시키면 합이 1이 되는 확률값(예: `0.02, 0.91, 0.06, 0.01`)으로 변환됨. 모델의 출력값을 확률로 계산하고 가장 큰 값의 클래스로 예측하며, Fully Connected Layer의 뉴런 개수만큼 모두에게 영향을 미침
#### 정리하면 (CNN 파이프라인 요약)
이미지 특징을 뽑아내고(Conv), 중요한 것만 추려내고(Pooling), 펼쳐서(FC), 최종 분류(Dense)하는 구조로 요약됨

- Convolution Layer : 3차원 이미지 정보에서 이미지 특징(feature map)을 뽑아내는 계층. 이미지와 필터 간의 연산, 원본 이미지 위치 반영
	- 합성곱 연산(필터 연산) : Input feature map에서 filter window 만큼 적용하여 연산. 연산은 window 크기만큼 유지하면서 stride sliding을 반복 수행
	- Padding : 합성곱 연산 결과 변형되는 output size를 보정. Input feature map에 특정값(주로 0)이 채워짐
- Pooling Layer : Convolution Layer의 합성곱 연산 결과에서 추가적으로 공간을 줄이는 연산. Max-pooling 주로 사용됨, 학습 Parameter 없음
→ Convolution을 할 때, 이 이미지에서 어떠한 특징을 뽑을지에 따라서 서로 다른 필터(하지만 크기는 같은)를 적용해서 여러 층으로 계층을 쌓음
#### \[참고\] Simple CNN 적용 예시
전체 파이프라인은 Feature Extraction(Convolution+ReLU, Pooling을 여러 번 반복해 Feature Maps 생성)과 Classification(Flatten Layer → Fully Connected Layer → Softmax Activation Function → Probabilistic Distribution)의 두 단계로 나뉨
- 일반 이미지 예시: Input(동물 사진) → Feature Extraction → Flatten/FC → Output(Horse/Zebra/Dog 중 확률 분포)
- 의료 영상 예시: Input(MRI/CT 스캔) → Feature Extraction → Flatten/FC → Output(tumor 0.95, infection 0.03, normal 0.02)
#### \[참고\] Vision Task의 종류(Classification)
같은 이미지라도 어떤 작업(Task)을 수행하느냐에 따라 요구되는 출력이 다름
| Task | 정의 |
| --- | --- |
| Classification | 이미지 전체가 어떤 클래스(예: dog)인지 식별하는 작업 |
| Localization | 클래스 라벨과 함께 객체 위치를 나타내는 bounding box도 함께 구함 |
| Detection | 이미지 내 여러 객체들의 Localization을 함께 수행 |
| Segmentation | 클래스 라벨과 함께 객체의 외곽선(윤곽)까지 구분 |
### 1B. 귀납적 편향의 설계 - 순차성과 시간적 의존성 (RNN, LSTM)
#### 1. Recurrent, 매일 같은 방식으로 어제 다음 오늘을, 쌓인 기억으로 쓰는 일기
일기 쓰기에 비유하면 RNN에 필요한 성질을 직관적으로 이해할 수 있음
| 일기 쓰기 | RNN에 필요한 것 |
| --- | --- |
| 매일 같은 방식으로 일기쓰기(5줄이든 5장이든 쓰는 법은 같음) | 가변 길이 처리(길이가 달라도 같은 규칙으로 처리) |
| 어제 다음에 오늘 읽기 쓰기(순서대로 써 내려감) | 순서 보존(먼저 온 것을 반영, 사건의 순서대로 반영) |
| 어제까지 쌓인 감정의 영향(오늘 글이 영향 받음) | 과거 맥락 기억(이전 내용(요약)을 기반으로 현재와 합침) |
#### 1. Recurrent, 용어의 이해
- `Recurrent` \[영어사전\] 되풀이되는, 반복되는, 재발하는, 회귀하는 / 일기에서 매일 반복되는 습관
- `Recurrent Neural Network` : 시퀀스(Sequence) 데이터 처리에 특화된 인공 신경망
	- 시퀀스 데이터란 음성, 텍스트 또는 시간에 따라 측정되는 값으로, 데이터가 순차적으로 생성되며 데이터들 간의 순서나 관계가 중요하다는 특징을 가짐
	- 이를 효과적으로 고려하기 위해 이전 시점의 정보를 내부에 저장하는 일종의 기억 장치를 가짐
	- 문장의 의미는 이전 단어들(기억 상태)에 따라 결정되는데, RNN은 앞 내용을 기억하여 뒷 내용을 예측하는 구조임
#### 2. RNN
- `RNN` : 메모리를 저장하는 네트워크
- `Cell, Memory Cell` : Hidden Layer에서 Activation Function을 통해 결과를 내보내는 역할(내부 연산 단위). 이전의 값을 기억하려고 하는 일종의 메모리 역할을 수행하는 노드로, 각 시점에서 바로 이전 시점 출력값을 자신의 입력으로 사용함(동일한 Cell을 시간 축을 따라 복사해서 펼쳐 놓은 것처럼 구성)
- `Hidden State` : 여태까지 들어온(과거의) Input 정보를 저장. 이를 가지고 다음 단어를 예측(결과값, 결과 상태값)
#### 2. RNN - Hidden State (Key Point)
현재 시점(`h_t`)은 이전 시점(`h_t-1`)을 받아서 현재값(`X_t`)과 함께 다음 상태로 넘김. 이를 통해 과거의 정보가 현재로 전달됨
```javascript
Y_t = W_hy * h_t + b_y
h_t = tanh(W_hh' * h_t-1 + W_xh' * X_t + b_h)
```
- `Y_t` : 현재 상태에서 최종 출력을 만듦
- `h_t` : 이전 상태와 현재 입력을 결합해 새로운 상태를 만듦
- `W_xh'` : 입력데이터 X를 셀에 보내는데 사용되는 가중치
- `W_hh'` : 이전 시점 셀의 Hidden State값을 현재 시점 셀로 보내는데 사용되는 가중치
- `W_hy` : 현재 시점 셀의 Hidden State값을 출력 데이터 Y로 보내는데 사용되는 가중치
하나의 층 안의 모든 시점에서 동일한 가중치 값(`W_hh'`)이 공유됨(단, Hidden Layer가 2개 이상인 경우 Layer 간에는 서로 다른 가중치를 가짐). 이를 통해 학습에 필요한 가중치 수를 줄이고, 흐름에 따른 연관성을 고려하여 예측할 수 있음
#### \[참고\] RNN, 쉽게 이해하기 (가중치 공유의 이점)
`T=10, Hidden size=128, Input size=64`일 때를 예로 들면
- 공유하지 않는다면 : 시점마다 별도의 가중치가 필요하여 `10 * (128*128 + 64*128) = 246,000`개
- 공유한다면 : 시점 수와 무관하게 1세트만 존재하여 `64*128 + 128*128 = 24,600`개
시퀀스가 아무리 길어져도 파라미터 수는 고정된다는 것이 핵심 장점임
#### 2-(1). RNN, 다양한 구성
RNN은 입력과 출력의 길이에 대해 자유로운 구조로 다양하게 설계할 수 있고, 연속 데이터의 특징을 고려하여 Link의 방향도 단방향 또는 양방향으로 활용할 수 있음
| 구조 | 설명 |
| --- | --- |
| One-To-One | Hidden Layer가 1개인 구조 |
| One-To-Many | 하나의 입력에 대해 여러 개의 출력을 내보내는 구조 |
| Many-To-One | 여러 개의 입력에 대해 단 한 개의 출력을 내보내는 구조 |
| Many-To-Many | 여러 개의 입력에 대해 여러 개의 출력을 내보내는 구조 |
이 외에도 Cell을 층으로 여러 겹 쌓은 Deep RNN, 과거와 미래 방향을 모두 참조하는 Bidirectional RNN 등으로 확장할 수 있음
#### 2-(2). RNN Architecture
시퀀스 데이터의 순서를 고려하여 데이터들 간의 순서나 관계 특징을 Hidden State에 저장하고, 여태까지 들어온(과거의) Input 정보로 다음 단어를 예측함. Hidden State를 오래 유지해야 할 경우 Gradient Vanishing/Exploding 문제가 발생하여 이후 LSTM, GRU 등으로 아키텍처가 개선됨
```javascript
O_t = W_hy * h_t + b_y
h_t = tanh(W_hh' * h_t-1 + W_xh' * X_t + b_h)
```
각 시점(`X_1, X_2, X_3, ...`)마다 tanh 셀을 거쳐 Hidden State(`h_1, h_2, h_3`)가 이어지고, 각 시점의 출력(`O_1, O_2, O_3`)이 Softmax를 거쳐 손실(Loss)을 계산함. 정방향으로 값을 계산하는 것을 Forward Propagation, 시간의 역방향으로 오차를 전달하는 것을 Backward Propagation(BPTT, Backward Propagation Through Time)이라 부름
#### 2-(3). Softmax in RNN
- RNN은 시퀀스 데이터의 특징을 저장하고, 이를 기반으로 미래를 예측
- 시계열 데이터인 경우 Softmax 없이 예측값을 그대로 Output Layer로 전달
- 텍스트 데이터인 경우 학습한 N개의 단어 중 하나를 예측하므로 Softmax를 사용(→ Classification)
예를 들어 "나는 자전거를 ___" 다음에 올 단어를 예측할 때, Softmax Layer를 거쳐 각 후보 단어("산다", "부산다", "고친다", "탄다", "보낸다")별 확률을 산출하고 실제 정답과 Cross-Entropy Function으로 Loss를 계산함
#### 2-(4). RNN with tanh
`Tanh` 함수는 `tanh(x) = (e^x - e^-x)/(e^x + e^-x)`로 정의되며, 출력 범위가 `(-1, 1)`로 제한됨. Sigmoid와 유사하지만 출력값이 0 중심으로 분포되어 Gradient vanishing 문제가 덜 발생하며, RNN/LSTM에서 많이 활용됨(출력값이 양수와 음수로 나뉘는 문제에 사용)
`h_t = tanh(W_hh' * h_t-1 + W_xh' * X_t + b)`이고 `W_hh'=0.3, W_xh'=0.01, b=0.1`일 때, 입력값의 트렌드에 따라 `h_t`가 어떻게 수렴하는지 세 가지 케이스로 확인함
| 케이스 | 입력(X1,X2,X3) | h1 | h2 | h3 |
| --- | --- | --- | --- | --- |
| 1 (계속 증가) | 200, 300, 400 | 0.97 | 0.998 | 0.9997 |
| 2 (증가 후 감소) | 200, 50, 130 | 0.97 | 0.712 | 0.924 |
| 3 (증가 후 큰 폭 감소) | 200, -130, 50 | 0.97 | -0.721 | 0.366 |
값이 계속 증가하는 추세면 `h_t`가 1에 가깝게 포화되고, 큰 음수 입력이 들어오면 `h_t`가 급격히 음수로 꺾이는 등 tanh가 입력값의 트렌드 변화를 어떻게 반영하는지 보여줌
#### 3. LSTM, 비유적 설명(일기 쓰기)
- `RNN = 매일 쓰는 일기` : 하루하루의 감정이나 사건들은 다음 날의 글에 조금씩 영향을 미치지만, 시간이 오래 지나면 과거의 내용이 희미해지거나 잊혀짐(→ 기울기 소실 문제). 오래된 기억은 잘 보존되지 않아 중요한 사건도 사라질 수 있다는 한계가 있음
- `LSTM = 일기 + 중요 메모 노트` : 중요한 사건을 따로 기록하는 메모장을 가진 일기에 비유됨. 매일 일기를 쓸 때 오래된 메모 중 불필요한 것은 지우고(`forget gate`), 오늘 일 중 중요한 내용을 메모장에 추가하고(`input gate`), 메모장 속 오래된 중요한 내용을 참고하여 오늘 일기를 작성함(`output gate`)
#### 3. LSTM, Long Short-Term Memory
이전 상태를 유지하는 Cell State와, 해당 정보를 조절하는 Gate를 활용하여 과거 정보를 선택적으로 기억하고 활용할 수 있도록 설계됨. RNN은 과거로 거슬러 갈수록 정보가 사라지거나 무시되기 쉽지만, LSTM은 Gate를 활용해 Cell State가 장기 기억을 유지할 수 있도록 설계되어 Long-term dependency 문제를 해결함(다만 여전히 매우 긴 시퀀스에서는 한계가 있어 이후 Attention 등장의 배경이 됨)
```javascript
i = σ(W [h_t-1, x_t])       (input gate)
f = σ(W [h_t-1, x_t])       (forget gate)
o = σ(W [h_t-1, x_t])       (output gate)
g = tanh(W [h_t-1, x_t])    (후보 값)

c_t = f ⊙ c_t-1 + i ⊙ g
h_t = o ⊙ tanh(c_t)
```
- `c_t` : 과거 기억 중 일부(`f`)를 유지하고 새로운 입력(`g`)을 반영(`i`)한 값
- `h_t` : 현재 기억(`c_t`)에서 필요한 정보(`o`)를 꺼내서 출력한 값
- `[Remind]` Cell State는 장기 기억을 저장하는 공간, Hidden State는 특정 시점의 출력을 나타내는 상태
#### \[참고\] LSTM Gates 상세
| Gate | 역할 | 수식 |
| --- | --- | --- |
| Forget Gate | 이전 기억 중 버릴 것을 선택(Decide what information we're going to throw away from the cell state) | `f_t = σ(W_f · [h_t-1, x_t] + b_f)` |
| Input Gate | 새로운 정보를 저장할지 선택(Decide what new information we're going to store in the cell state) | `i_t = σ(W_i · [h_t-1, x_t] + b_i)`, 후보값 `C̃_t = tanh(W_c · [h_t-1, x_t] + b_C)` |
| Update(Cell State) | 얼마나 업데이트할지 반영하여 Cell State 갱신 | `C_t = f_t * C_t-1 + i_t * C̃_t` |
| Output Gate | 업데이트된 상태를 기반으로 출력 | `o_t = σ(W_o · [h_t-1, x_t] + b_o)`, `h_t = o_t * tanh(C_t)` |
#### 정리하면 (RNN 요약)
현재 입력 뿐만 아니라 이전 시점의 상태(Hidden State)를 기억하여 시간에 따른 데이터 흐름과 패턴을 학습하는 신경망임. Cell(Memory Cell)은 Hidden Layer에서 Activation Function을 통해 결과를 내보내는 내부 연산 단위이며, 각 시점의 출력값을 다음 시점의 입력으로 사용함. 하나의 층 안 모든 시점에서 동일한 가중치를 공유하여 학습에 필요한 가중치 수를 줄이면서 흐름에 따른 연관성을 고려해 예측할 수 있음
#### 정리하면 (RNN vs LSTM)
RNN은 짧은 기억력, LSTM은 긴 기억력으로 과거 정보를 더 잘 활용하도록 설계된 신경망임
| 구분 | RNN | LSTM |
| --- | --- | --- |
| 기억 능력 | 과거 정보를 짧게 기억 | RNN보다 과거 정보를 길게 기억 가능 |
| 구조 | 현재 상태와 입력값을 받아 Hidden State를 통해 출력, tanh 함수로 단순 계산 | Cell State(기억 저장소, 장기 상태)와 Hidden State(현재 상태)를 함께 사용. Cell State와 Gate를 활용하여 상태를 출력하며 Forget/Input/Output Gate로 정보를 조절 |
| 한계점 | 어느 정도 과거를 기억하지만 긴 시퀀스 학습이 어려움(Vanishing Gradient), 시간 순서 의존으로 연산 속도가 느림(병렬처리 한계) | 계산량이 많고 긴 시퀀스에서 목적을 달성하기 어려움, 시간 순서 의존으로 연산 속도가 느림(병렬처리 한계), 계산량이 많아 RNN보다 학습 시간이 길어짐 |
| 설명 | 순간순간 정보를 이어가는 방식 | 순간순간 정보를 이어가는 방식에 더해, 중요한 정보를 따로 저장하는 기억 저장소(Cell)를 통해 과거의 중요한 정보를 오래 활용할 수 있도록 함 |
#### 정리하면 (RNN의 귀납적 편향)
순서가 의미를 만들고, 현재는 과거에 의존하며, 규칙은 시점과 무관하다는 세 가지 성질을 구조에 반영함
| 필요한 성질 | RNN이 하는 일 | 귀납적 편향 |
| --- | --- | --- |
| 가변 길이 처리(길이가 달라도 같은 규칙) | 가중치 공유(같은 셀을 매 시점 재사용) | 규칙은 시점 무관, 언제든 같게 처리 → 파라미터 절약 + 가변 길이를 동시에 해결 |
| 순서 보존(사건 순서대로 반영) | 순차 처리(t=1,2,3...순서대로) | 순서가 의미를 바꿈, 배열이 곧 정보(예: "사람이 사과를 먹었다" ≠ "사과가 사람을 먹었다") |
| 과거 맥락 기억(이전 내용(요약) 기반) | 은닉 상태 전달(요약정보를 다음에 전달) | 현재는 과거에 의존, 과거를 알아야 현재를 이해함(예: "그것이 뜻하는 바는..") |
#### 정리하면 (LSTM의 귀납적 편향)
RNN의 골격을 그대로 두고, 무엇을 얼마나 오래 기억하고 무엇을 잊을지를 데이터가 스스로 정하게 하는 장치를 더한 아키텍처임
| RNN 약점 | LSTM이 하는 일 | 귀납적 편향 |
| --- | --- | --- |
| 먼 과거가 흐릿해짐(장기 의존성 손실) | Cell State(정보 고속도로)를 두어 중요한 것은 살아남게 함 | Hidden State와 별개로 고속도로 같은 경로(Cell State)를 두어 정보가 멀리까지 살아남도록 함 |
| 취사선택 불가(모두 똑같이 기억) | Gate로 취사선택(Input/Forget/Output 조절) | 각 Gate가 이번 정보를 얼마나 받아들일지, 과거를 얼마나 잊을지, 무엇을 내보낼지를 학습하여 조절 |
| 규칙을 사람이 정하지 못함 | Gate를 데이터로 학습(Forget/Update 학습) | Gate는 고정 규칙이 아니라 학습되는 값으로, 문제에 맞는 기억 전략을 스스로 익힘 |
### 2. 표현 학습이라는 다른 길 - 정답 없이 배우다
#### 1. 지도 학습의 한계
Supervised는 입력마다 "정답"이 있어야 학습이 가능함. Label에는 다음과 같은 한계점이 있음
- 비용 : 사람이 일일이 라벨링해야 하고, 전문가는 더 비싼 비용이 필요
- 애매한 문제 : 무엇이 "정답"인지 명확하게 정의하기 힘든 경우가 많음
- 레이블 이외 정보 손실 : 레이블로 구분되지 못한 데이터는 버려짐
그래서 필요한 발상은 "정답 없이, 데이터에서 스스로 학습하자"는 것이며, 입력 자신을 정답으로 삼는 `Unsupervised`, `Self-Supervised` 방식이 대두됨
#### 2. Auto-Encoder
- `Auto` : 자동으로
- `Encoder` : 데이터를 압축(특징만 남김)
- `Decoder` : 압축된 데이터를 원래대로 복원
데이터를 자동으로 압축했다가 다시 복원하는 신경망이며, 데이터를 압축하고 복원하는 과정을 스스로 학습하는 신경망임
#### 2-(1). AE 필요성 (차원의 저주)
- 데이터는 기본적으로 벡터로 표현되는데, 비정형 데이터는 더 많은 숫자로 표현됨(예: `28*28` 흑백 이미지 = `784`개 숫자)
- 딥러닝 네트워크에 적용하려면 차원이 필요하지만, 차원이 커지면 데이터 크기가 커지고 더 많은 데이터가 요구됨
- `차원의 저주` : 차원이 증가하면서 학습데이터 수가 차원수보다 적어져서 성능이 저하되는 현상으로 이어질 수 있음
기존 알고리즘 중에는 차원을 축소하여 분석하는 `PCA`(주성분 분석)가 있으나, PCA는 대체적으로 선형 관계에 적합하여 분산이 가장 큰 방향으로 데이터를 선형적으로 압축함. 비선형 데이터에서도 잘 압축하는 방법이 필요했고, 그 답이 Auto-Encoder임
- 입력 → 압축(Encoder) → 복원(Decoder) → 출력
- 입력과 출력이 최대한 같아지도록 학습
- 이 과정에서 중간에 중요한 특징만 남게 되는 압축을 학습시키는 것이 핵심
#### 2-(2). AE Architecture
Original input(예: 숫자 6 이미지) → Encoder → Latent Space Bottleneck → Decoder → Reconstructed input(복원된 6, 다소 흐릿함)
- `Encoder` : 데이터를 점점 줄여서 압축함 → 중요한 특징만 남김
- `Latent Space` : 가장 압축된 형태 = 가장 작은 차원으로 특징을 표현
- `Decoder` : 압축된 정보를 바탕으로 다시 원본처럼 복원
중요한 특징만 남기고 불필요한 정보를 줄이는 구조임
#### 2-(2). AE Architecture - 확장(Classification)
Auto-Encoder는 단순한 압축 도구가 아니라, "데이터의 특징"에 집중한 네트워크임. "압축된 특징이 결국 중요한 정보"라는 관점에서, Latent Space의 결과를 Classification(분류기)로도 보낼 수 있음. 압축을 통해 특징을 잘 뽑아냈다면, 해당 특징으로 Classification 문제도 잘 해결할 수 있다는 아이디어임
#### 3. Seq2Seq
AE는 입력을 그대로 복원하는 반면, Seq2Seq는 입력을 다른 시퀀스로 변환하는 네트워크임
- 입력 : 시간에 따라 변하는 시계열 데이터, 문장(자연어) 등
- 출력 : 입력과 길이가 다를 수도 있는 새로운 시퀀스(순서가 있는 데이터)
- 주로 기계 번역, 텍스트 요약, 챗봇(초기 버전) 등에 활용
인코더(Encoder)가 입력 문장(예: "je suis étudiant")을 LSTM으로 순차 처리한 뒤, 마지막 Hidden State 하나(Context Vector, Latent Space)에 입력 전체를 압축하고, 디코더(Decoder)가 이 Context Vector를 받아 출력 문장(예: "I am a student")을 순차적으로 생성함. 다만 Encoder의 마지막 Hidden State 하나에 입력 전체를 압축하기 때문에, 고정 길이 병목으로 인한 정보 손실이 발생한다는 한계가 있음
---
### 중간 정리 - Part-C. DL Architecture(1990\~2015)
지금까지 다룬 CNN, RNN, Auto-Encoder를 한 차례 되짚는 구간으로, 앞서 정리한 CNN 파이프라인(Conv-Pooling-FC-Dense), RNN(Cell/Hidden State/가중치 공유), AE(Encoder-Latent Space-Decoder) 요약 내용이 동일하게 다시 한 번 제시됨. 이후 DL Architecture Expansion History 표(연표)도 섹션이 바뀌기 전에 한 번 더 제시되며 지금까지의 진행 상황을 환기시킴
### 3. CNN의 진화 - 더 깊게, 더 안정적으로
이번 파트는 AlexNet(딥러닝 부흥과 GPU 학습)과 ResNet(residual connection과 깊이의 한계 돌파)을 다룸
#### ImageNet Challenge
ILSVRC(ImageNet Large Scale Visual Recognition Challenge)에서 CNN 계열 모델들이 해마다 층을 깊게 쌓으며 Top-5 오류율을 인간 수준(약 5.1%) 근처까지 낮춰온 과정을 보여주는 그래프임
- AlexNet : 8개 층, CNN 최초 우승
- VGG : 19개 층
- GoogLeNet : 22개 층
	- 대전제는 "레이어를 추가할수록 성능이 오른다"는 것이었으나, 실제로 레이어를 계속 추가하니 오히려 성능이 감소하는 현상이 나타남
	- 이는 Gradient Vanishing 때문이 아니며, Batch Norm·ReLU 등으로도 해결되지 않는 `Degradation`(깊이의 저주, 퇴화) 문제였음
- ResNet : 152개 층
	- "깊이 쌓으면 성능이 오른다"는 대전제를 증명해 낸 모델
	- Deep Neural Network(DNN) 시대의 서막을 열었고, 현대 DNN 모델들의 표준이 됨
#### 1. AlexNet (ILSVRC 2012)
AlexNet 주요 특징:
- 대형 CNN 구조 : 5개의 Conv Layer, 3개의 FC Layer로 구성된, 당시 기준 매우 깊은 대형 CNN 구조
- ReLU 도입 : 비선형성을 강화하고 학습속도를 향상시켰으며, 기울기 소실 문제 해결에 탁월한 성능을 보임
- Dropout : 학습 과정에서 임의로 일부 뉴런을 비활성화시켜 특정 뉴런에 지나치게 의존하지 않도록 하여 Overfitting을 해결
- GPU 사용 : 대규모 데이터셋을 빠르게 학습하기 위해 사용
- Data Augmentation, Normalization : 데이터 증강 기법으로 더 많은 학습 데이터를 생성하고, `LRN`(Local Response Normalization)이라는 정규화 기법을 적용해 CNN이 더 잘 학습되도록 처리
이를 통해 딥러닝이 이미지 처리와 인식 문제에서 탁월한 성능을 발휘할 수 있음을 증명함
#### 2. ResNet - 잔차의 재해석
`잔차`라는 개념이 통계 회귀분석, Vanilla CNN, ResNet에서 각각 어떻게 다르게 해석되는지 비교하면 ResNet의 아이디어가 더 명확해짐
| 구분 | 통계 회귀분석 | Vanilla CNN | ResNet |
| --- | --- | --- | --- |
| 잔차 | 실제값 - 예측값(모델 전체 출력 vs 정답) | 실제값 - 예측값(모델 전체 출력 vs 정답) | 출력 - 입력(블록 출력 vs 블록 입력) |
| 학습 대상 | 회귀 계수 | 목표 출력 `H(x)` | 변화량 `F(x) = H(x) - x` |
| 잔차 역할 | 줄여야 할 오차(결과) | 줄여야 할 오차(결과) | 학습하는 목표(변화량) |
| 잔차 = 0일 때 | 모델이 데이터를 완벽히 설명 = 학습 성공 | 출력이 정답과 일치 = 학습 성공 | 그 층이 아무것도 안 함 = 학습 성공과 무관 |
| 핵심 장치 | 최소제곱법 | Conv Layer 쌓기 | Skip Connection(입력을 출력에 더함) |
Vanilla CNN은 `INPUT x → CONV → CONV → OUTPUT H(x)`처럼 출력을 통째로 학습하지만, ResNet은 어떤 층이 굳이 바꿀 것이 없을 때(불필요할 때) 네트워크가 `F(x) → 0`을 선택할 수 있게 하여, 깊은 망에서도 학습이 안정적으로 이루어지도록 함
#### 2. ResNet - Residual Block
Residual Block은 지름길(Skip Connection)을 통해 각 블록의 입력 흐름을 보존하고, 필요한 변화량만 더해가며 정보를 점진적으로 정제하는 딥 네트워크임
- 성능 향상을 위해 신경망 깊이를 늘리면 학습 오차마저 커지는 현상이 있음 - 깊어지면 성능이 나빠짐(degradation)
- Residual Block은 각 블록의 입력을 그대로 넘겨주는 방식으로 이 문제를 해결
- 특정 블록이 유용한 변환을 학습하지 못하더라도 입력이 보존되어 최소한 성능이 나빠지지 않도록 안전장치를 마련
- 필요한 것만 정교하게 학습하겠다는 목적 : 입력은 skip으로 보존되므로, 각 블록은 바꿀 부분(`F(x)`)만 학습하면 됨
```javascript
x → [weight layer] → relu → [weight layer] → F(x)
F(x) + x (identity, Skip Connection)  → relu
```
#### \[참고\] Residual Block, 쉽게 이해하기 (원고 편집 비유)
- `Plain block` : 각 단계마다 원고를 백지에 다시 옮겨 씀. 안 고칠 부분까지 전부 다시 작성해야 해서 옮기는 과정에서 손실이 발생할 수 있음
- `Residual block` : 원본 위에 수정사항만 표시함. 고칠 것이 없으면 추가 작업이 없고, 그 단계에 들어온 원고가 그대로 남음
- 편집자는 무엇을 고쳐야 할지 미리 아는 것이 아니며, 최종 원고에 대한 평가가 역방향으로 전달되면서 각자 무엇을 고칠지가 정해짐
#### 2. ResNet 주요 특징 정리
CNN 기반으로 Residual Block을 제안하여, 층이 깊어지더라도 과적합이나 기울기 소실 문제를 해결함
- Residual Block : 레이어를 깊게 쌓으면 성능이 좋아질 수 있지만 기울기 소실 문제가 발생함. 각 층의 출력을 다음 층으로 직접 전달하는 Skip Connection을 추가해 문제를 해결(기존 정보 유지 + 더 필요한 것만 추가)
- 네트워크 안정성 : 100층 이상의 매우 깊은 네트워크도 학습 가능(최대 152층까지 설계). 깊은 네트워크지만 상대적으로 적은 파라미터로 높은 성능을 발휘하며, Residual Learning으로 깊은 네트워크에서도 안정적으로 학습 가능
- 다양한 변형 : `ResNet-18, ResNet-34, ResNet-50, ResNet-101, ResNet-152` 등. 더 깊은 모델은 더 복잡한 데이터셋을 처리하는데 유용하며, Computer Vision 외에도 NLP, Speech Recognition 등 다양한 딥러닝 응용 분야에서 활용됨
딥러닝에서의 네트워크 깊이 한계를 극복하며, Computer Vision의 표준 아키텍처로 자리매김함
### 4. Attention 등장 - 순차 처리의 병목을 넘다
이번 파트는 Transformer(self-attention과 병렬화, 그리고 O(n\^2) 비용)와 BERT(양방향 사전학습과 전이학습)를 다룸
#### 1. Transformer
중요한 것에 집중하는 방식으로, 문장을 더 정확하고 빠르게 이해할 수 있음
- 자연어 처리에서 RNN이나 LSTM을 대체한 BERT, GPT의 근간이 되는 기본 아키텍처
- Self-Attention 메커니즘을 도입하여 긴 문맥을 효율적으로 처리, NLP Task 성능을 크게 향상
| 개념 | 설명 |
| --- | --- |
| Attention | 입력 시퀀스(문장)의 각 요소(단어)가 다른 요소들과 얼마나 관련 있는지, 어느 부분에 집중할지 결정하는 매커니즘. 기계번역 시 목적어 단어를 번역할 때, 원문에서 관련된 단어들에 집중하여 더 정확하게 번역 |
| Self-Attention | 입력된 문장 내에서 각 단어가 다른 모든 단어와 얼마나 관련이 있는지 계산하는 것. RNN/LSTM이 순차적으로 처리하는 것과 달리, Self-Attention은 문장 내 모든 단어를 동시에(병렬로) 보고 처리 |
Attention 메커니즘을 잘 사용하기 위해 만든 구조가 바로 Transformer임
#### \[참고\] Attention, 쉽게 이해하기
| 구분 | 설명 |
| --- | --- |
| 데이터 특징 | 기존 RNN, LSTM의 한계 : 문장이 길면 앞의 내용이 잘 전달되지 않음(장기 의존성 문제). 착안 포인트 : 모든 단어를 다 참고하되, 중요한 단어에 더 집중하면 되지 않을까 |
| Attention | 문장을 읽고 마지막에 정리하는 것이 아니라, 읽으면서 중요한 단어에 형광펜으로 구분하듯 처리. 중요한 단어는 크게, 덜 중요한 단어는 작게 봄. 각 단어에 얼마나 집중할지 가중치를 구해서 중요한 단어일수록 크게 반영(예: "고양이가 창문에서 햇살을 받으며 잔다") |
| Self-Attention | 문장 안에서 각 단어들이 서로 얼마나 중요한지 보는 것. 각 단어가 문장 속 다른 단어들과 서로 영향을 주는 관계를 파악(예: 위 문장에서 '고양이'와 '잔다'의 관계가 강해 큰 가중치를 가짐) |
| Multi-Head Attention | 중요한 관계가 하나만 있는 것은 아니므로, 여러 개의 관계를 보기 위해 Head(하나의 시선)를 여러 개 둠. 문장 내에서 Head를 여러 개 달아 각 Head가 서로 다른 관계에 집중하게 함(데이터를 여러 관점에서 보는 것) |
| Masked Multi-Head Attention | 미래 단어는 절대 보면 안 되고, 현재 시점까지만 보고 판단해야 함. `Mask`는 가림막으로, 현재 단어가 미래 단어에 가중치를 주지 못하도록 처리(미래 단어를 보면 부정 행위). Multi-Head와 결합해 각 Head가 미래를 가린 상태에서 다른 관계를 분석(예: Head1은 "잔다→고양이가", Head2는 "햇살→창문"처럼 반대 방향은 마스크로 차단) |
#### \[참고\] QKV, 쉽게 이해하기
Attention은 각 단어가 다른 단어와 "얼마나 관련있는지"를 계산해 가중치를 매기는 것인데, 이를 숫자로 계산하기 위해 Query, Key, Value 세 가지 값을 사용함
- `Query` : 질문 - "나와 관련있는 단어가 누구지?"라고 묻는 역할. 현재 단어가 다른 단어들과 얼마나 연관이 있는지를 묻는 값(예: "잔다"가 Query라면 "누가 자는지" 관련된 단어를 찾으려는 질문)
- `Key` : 단서 - 각 단어가 "나는 이런 단어야"라고 스스로 소개하는 역할(예: '고양이가'의 Key는 "나는 주어야, 잠을 잘 수 있는 대상이야". 문법 분석이 아니라 학습된 특징 표현임)
- `Value` : 정보 - 그 단어가 실제로 담고 있는 의미/정보 그 자체(예: '고양이가'의 Value는 '잔다'에게 골라졌을 때 넘겨줄 "주어=고양이"라는 내용)
계산 흐름은 다음과 같음
1. Query와 Key를 비교하여 얼마나 관련있는지 점수(유사도)를 계산 (예: "잔다"기준 고양이가=90, 햇살을=15, 창문에서=10)
2. 그 점수를 가중치로 변환 (예: 고양이가 0.55, 창문에서 0.05, 햇살을 0.05, 받으며 0.10, 잔다 0.25)
3. Value를 곱해서 합산 → `0.55*(고양이가 value) + 0.05*(창문에서 value) + ... `처럼 계산되어, '고양이가'의 정보가 가장 많이 반영된 '잔다'의 표현이 만들어짐. 이렇게 '잔다'는 "고양이가 잔다"라는 문맥을 품은 단어가 됨
#### 2-(1). Scaled Dot-Product Attention
`Transformer > Attention > Scaled Dot-Product Attention`은 점수를 매겨서 집중하는 방식임
- `Attention` : 중요한 단어에 집중
- `Dot-Product` : 얼마나 비슷한 방향을 보고 있는가(Product는 단순 곱셈, Dot-Product는 두 벡터의 원소별 곱을 모두 더한 값). 계산된 값이 크면 두 단어 간의 관계가 강함을 뜻하므로 더 집중함
- `Scaled` : 벡터 차원이 커지면 dot-product 값도 커져 softmax가 제대로 작동하지 않게 되는데, 이를 해결하기 위해 스케일링을 추가함
- `Query` : 현재 단어가 다른 단어들과 얼마나 연관이 있는지를 묻는 값(질문)
- `Key` : 각각의 다른 단어들이 어떤 의미를 가지고 있는지 나타내는 값(단서)
- `Value` : 해당 단어의 실제 의미를 담은 값(정보)
- `Linear` : 각 Head의 결과를 합쳐서(Concat) 최종 결과를 만들어 냄
- `Multi-Head` : 여러 헤드가 동시에 작동하여 문장의 의미를 더 풍부하고 정확하게 이해할 수 있도록 함. 각각 다른 QKV 쌍을 통해 여러 질문을 던지고 그 결과를 모두 모아 집중해야 하는 단어를 정확히 찾아냄
```javascript
MultiHead(Q, K, V) = Concat(head_1, ..., head_h) * W^O
head_i = Attention(Q*W_i^Q, K*W_i^K, V*W_i^V)
```
#### 3. Transformer Architecture (구성요소)
| 구성요소 | 역할 |
| --- | --- |
| Encoder | 문장을 이해하는 부분. 입력 문장을 이해해서 중요한 정보를 추출 |
| ㄴ Multi-Headed Self-Attention | 문장 안에서 단어들끼리 관계를 따져서 중요한 단어에 집중 |
| ㄴ Feed-Forward | 그 결과를 다듬는 과정. 입력 벡터 → 더 큰 차원으로 확장 → ReLU → 축소 |
| States | 집중할 각 단어를 벡터 공간에서 잘 반영될 수 있도록 처리. AE의 Latent Space처럼 요약 압축 파일 역할을 하며, 단어별 요약 모음집 성격을 가짐(입력 길이에 따라 유동적이며, AE는 고정 크기인 것과 차이가 있음) |
| Decoder | 문장을 만들어내는 부분. 정보를 활용하여 출력 문장을 생성 |
| ㄴ Masked Multi-Headed Self-Attention | 문장을 만들어낼 때 앞부분만 보고 다음 단어를 예측 |
| ㄴ Multi-Headed Cross-Attention | 인코더가 뽑아놓은 문장 정보(Key, Value : 단서, 정보)와 현재 상태를 연결해 참고. 현재 문장만 보면 안 되므로 인코더 정보를 참고(요약본을 보고 힌트를 얻는 과정) |
| ㄴ Feed-Forward | 최종적으로 가공. 생성 문장을 다듬는 과정 |
#### 3. Transformer Architecture (BERT/GPT, Positional Encoding)
Transformer의 Encoder만 사용하면 텍스트 이해(BERT), Decoder만 사용하면 텍스트 생성(GPT)에 해당함
`※ Positional Encoding`
- 아키텍처 : RNN/LSTM처럼 순차적으로 처리하지 않고, 모든 단어를 동시에(병렬로) 처리함
- 상황 : 단어가 숫자로 바뀌어 들어가지만, 순서를 알 수 없게 됨
- 해결 : 각 단어에 위치정보(인코딩 벡터)를 더해서 문장의 순서 정보를 함께 반영(예: "고양이가 창문에 앉았다" → \[고양이+위치1, 창문에+위치2, 앉았다+위치3\])
#### 4. BERT
`BERT`, Bidirectional Encoder Representations from Transformers
- Transformer의 Encoder 부분을 기반으로 양방향 학습
- 입력 문장의 앞뒤 문맥을 모두 고려하여 단어를 이해하는데 중점
왜 BERT는 Transformer의 Encoder를 사용하는가
- 인코더 역할 : 텍스트를 입력받아 의미를 분석하고 이해함. 문장의 각 단어가 어떻게 서로 연결되어 있고 해석되어야 하는지 학습하며, 단어가 어떻게 관련되는지를 깊이 이해하는데 중점을 둠
- 인코더 기반 BERT가 주는 효과 : 양방향 문맥 이해(Bidirectional Context Understanding, 문장의 앞뒤 모든 단어를 고려하여 문맥 파악), Masked Language Model(문장의 일부 단어를 마스킹하고 그 단어를 맞추는 방식으로 학습)
- BERT가 Decoder를 사용하지 않는 이유 : 디코더는 학습한 내용을 토대로 텍스트 생성에 사용되는데, BERT는 생성이 아니라 문장 이해에 중점을 두므로 텍스트 생성 과정이 포함되지 않아 디코더 기능이 불필요함
NLP 분야에서 표준 모델로 자리매김함(문맥 이해의 혁신적 접근과 활용)
#### 5. BERT Architecture
문맥을 학습시키는 단계로 두 가지 목적함수를 사용함
- `NSP`(Next Sentence Prediction, 문장 수준 문맥) : `[CLS]`를 입력으로 "B가 A의 실제 다음 문장인가"를 이진 분류. 토큰 수준 문맥을 넘어 문장 간 연결 관계를 `[CLS]`에 축적시키려는 목적
- `Masked LM`(토큰 수준 문맥) : 입력 토큰의 약 15%를 가린 뒤, 그 자리의 최종 벡터로 원래 단어를 예측. 정답 토큰이 입력에서 제거되어 자기 자신을 컨닝하는 문제가 생기지 않아 양방향 학습을 가능하게 한 핵심 장치
- `T_N` : N번째 토큰의 최종 은닉 벡터 = 문맥이 반영된 해당 단어의 의미
- `C` : `[CLS]`의 최종 은닉 벡터 = 시퀀스 전체 요약 표현 → 문장 단위 작업(분류, 문장쌍 관계 판단)에 사용
- 각 층의 Self-Attention에서 모든 토큰이 모든 토큰을 동시에 참조함(양방향 Self-Attention)
- 층을 거칠수록 표현이 갱신됨 : 표층적 어휘 정보 → 구문 → 의미/지시 관계 순으로 문맥이 누적됨
- 같은 단어라도 주변 토큰에 따라 다른 벡터가 나옴 = `Contextual Embedding`
- 아직 문맥이 반영되지 않은 정적 입력(`E`)은 토큰 임베딩 + 세그먼트 임베딩(A/B 구분) + 위치 임베딩으로 구성됨
- 문장 두 개를 한 시퀀스로 묶어서 입력함. `[CLS]`는 모든 시퀀스의 첫 토큰으로 그 자체로는 의미가 없는 빈 슬롯이며, `[SEP]`는 문장을 구분하는 특수 토큰으로 경계는 표시하되 Attention은 경계를 넘어 흐르게 함(문장 간 문맥까지 학습 대상이 됨)
정리하면 Transformer의 Encoder를 계승하여, 정적 입력(`E`) → 양방향 Self-Attention 누적 → 문맥 반영 출력(`T, C`)의 흐름을 가지며, 이를 가능하게 한 목적함수가 Masked LM(단어 수준) + NSP(문장 수준)임
#### \[참고\] Masked LM, 쉽게 이해하기
오른쪽 문맥을 쓰지 않으면 풀 수 없는 문제를, 정답 누출 없이 풀 수 있게 만든 목적함수임
왜 오른쪽 문맥이 필요한가
- "그는 \[MASK\]을 열고 우유를 꺼냈다" vs "그는 \[MASK\]을 열고 여권을 꺼냈다"
- 순방향 LM은 두 문장을 구분할 수 없어 같은 확률 분포를 낼 수밖에 없음 (참고 : 한국어는 서술어가 뒤에 있어 오른쪽 문맥 의존도가 더 큼)
왜 "가리는" 절차가 필요한가
| 양방향 + 일반 LM | Masked LM |
| --- | --- |
| "그는 냉장고를 열고 우유를 꺼냈다"에서 냉장고를 예측하는데, 입력에 냉장고가 그대로 보임 → 손실이 0에 수렴하여 학습되는 것이 없음 | "그는 \[MASK\]를 열고 우유를 꺼냈다"에서 정답이 입력에서 제거됨 → 주변 문맥으로만 복원해야 함 |
#### 6. BERT 주요 특징
- `Pre-training Model` : 대량의 데이터로 언어의 규칙과 의미를 학습한 사전 모델
- `Finetuning` : 사전 학습된 BERT를 특정한 작업에 맞게 추가 학습
- `Transfer Learning` : BERT의 학습된 언어 지식을 바탕으로 새로운 작업에 적용하며, 필요 시 Finetuning을 진행
| 단계 | 설명 |
| --- | --- |
| Pre-training | 기본적인 언어 패턴을 학습하는 단계로, 많은 데이터를 사용해 일반적인 언어의 규칙과 의미를 학습 |
| Fine-Tuning | 사전 학습된 모델을 특정 작업(질문에 답하기, 문장 분류 등)에 맞게 아키텍처를 변형하거나 추가 학습 데이터로 학습(가중치 업데이트를 통한 모델 최적화) |
`※ Pretraining Details`
- Data : Wikipedia, BookCorpus
- 64 TPU chips for 4 days
- BERT-base : 12 Layer, 768 Hidden, 12 Head
- BERT-large : 24 Layer, 1024 Hidden, 16 Head
#### \[참고\] BERT's Transfer Learning (방사선 보고서 분류 사례)
BERT 기반 전이학습을 통해 방사선 보고서의 문장을 해부학 클래스별로 분류한 연구(Transfer Learning of Radiology Text Classification)
- 구조화되지 않은 텍스트, 매우 적은 해부학 카테고리에서도 의미있는 성능을 확인함
- Methods : 900개 보고서에서 추출한 6,272개 문장을 신체 부위별로 수작업 라벨링하고, BERT 기반 분류를 BiLSTM 및 빈도 기반(count-based) 방법과 비교
- Results : BERT 기반 접근법이 가장 높은 macro-averaged AUPRC(0.88)와 AUC(0.97)를 달성했으며, 레이블된 학습 데이터가 적은 소수 클래스에서도 대부분의 해부학 클래스에서 baseline을 능가함
### 5. 규모와 비용의 시대 - 더 크게, 더 효율적으로
이번 파트는 Beyond Transformer, MoE(조건부 연산으로 푸는 규모 확장), Kimi Linear(KDA & MLA 하이브리드)를 다룸
#### 1. Beyond Transformer
Transformer가 뛰어나지만 비용, 메모리 등의 구조적 한계가 있어 이를 해결하기 위한 새로운 아키텍처들이 제안됨. 크게 두 갈래로 발전함
`Efficient-oriented Track` : Attention 구조 자체를 대체하여 장문 처리와 계산 효율을 근본적으로 개선하는 전략 (Linear Recurrent Models)
| 시기 | 모델 | 특징 |
| --- | --- | --- |
| 2021-11 | S4 | RNN 재설계 가능. Transformer 병목 일부 해결하나 성능은 불안정 |
| 2023-06 | HyenaDNA | Long Conv + Gating으로 Attention 대체 가능성 탐색. 성능·처리속도 등 여전히 한계 |
| 2023-07 | RetNet | Multi-scale Retention Block을 통해 Attention 대체. Transformer와 유사한 성능, 안정성 유지 |
| 2023-12 | Mamba | 긴 문맥 대응을 위해 SSM 도입. 하드웨어 효율까지 고려한 설계 |
| 2024-06 | DeltaNet | Delta update rule로 긴 문맥 유지 및 학습 안정성 개선 |
| 2024-12 | Gated DeltaNet | Delta update rule + Gating + 하드웨어 효율. Mamba 대비 안정적 학습 및 긴 문맥 성능 확보 |
| 2025-11 | Kimi Linear | Hybrid(Kimi delta + full attention) architecture. Transformer 대체가 가능한 수준까지 도달 |
`Scaling-oriented Track` : 모델 파라미터를 늘리되 실제 계산량은 최소화하는 확장 전략 (Mixture of Experts)
| 시기 | 모델 | 특징 |
| --- | --- | --- |
| 2017-01 | Sparsely-Gated MoE Layer | MoE 구조를 딥러닝 맥락에서 정립. Sparse Gating 개념 도입 |
| 2020-06 | GShard | Conditional Computation + MoE. 분산 학습 프레임워크 확립 |
| 2021-01 | Switch Transformer | 기존 MoE보다 단순한 라우팅 구조로 효율 개선. 1조 파라미터급 모델 가능성 확인 |
| 2021-12 | GLaM | MoE 기반 대형 언어모델 설계. 계산량·에너지 효율 획기적 개선 |
`※ LLM adapting MoE` : (2023-12) Mistral 8\*7B(오픈소스 MoE 상용화 시작점), (2024-01) DeepSeekMoE(MoE 구조적 완성도 및 실적 적용 확산), (2025-09) Qwen3-Next(Hybrid Attention + MoE)
#### 2. Transformer가 풀지 못한 한계
토큰이 늘어날수록 계산량뿐 아니라 메모리 사용량까지 함께 증가하는 구조라는 것이 핵심 한계임. 매번 새로운 단어를 하나 말할 때마다, 지금까지 했던 모든 말을 다시 참고하면서 다음 말을 정하는 방식이기 때문임
- `Multi-Headed Self-Attention` : 각 토큰이 모든 다른 토큰과 상호작용함. 입력 길이가 n개일 때 각 토큰이 n개의 key-value(KV) 조합을 참조해야 하므로 계산량이 대략 `O(n^2)`이 됨. KV cache는 입력 길이에 따라 누적되므로, 긴 문장을 처리할수록 메모리 사용량이 선형적으로 증가함
- `Multi-Headed Cross-Attention` : Decoding에서 KV cache 누적이 점차 커짐. 추론(inference) 단계에서 실시간 응답이나 긴 문맥 처리 능력이 떨어져 병목 현상이 발생함. Long-context model이나 Agent 설계 시 Transformer 기반 LLM은 구조적으로 효율성의 한계를 가짐
#### \[참고\] Transformer 계산량, 쉽게 이해하기 (회의 비유)
회의에서 모두가 대화해야 하는 상황에 비유하면, n명이 모인 회의에서 각자가 발언하기 전에 "다른 모든 사람의 의견"을 참조해야 함
- 사람이 2명이면 참고 관계 4가지(`2*2`)
- 사람이 10명이면 참고 관계 100가지(`10*10`)
- 사람이 100명이면 참고 관계 10,000가지(`100*100`)
Self-Attention은 문장 안의 토큰 하나하나가 "나머지 모든 토큰과 얼마나 관련 있는지"를 모두 비교해야 하므로, 토큰 수가 n개이면 비교해야 할 쌍이 `n*n = n^2`이 됨
- `KV cache`(메모리) : 토큰 하나가 들어올 때마다 그 토큰의 정보(K, V) 한 줄을 노트에 적어두는 것과 같아서, 토큰이 늘어난 만큼만 노트가 길어지는 선형(`n`) 증가
- 계산량 : 새로운 토큰이 하나 들어올 때마다, 지금까지 노트에 적힌 모든 줄을 다시 훑어봐야 해서 계산량은 `O(n^2)` 형태로 늘어남
#### 3. 왜 RNN을 다시 보는가
RNN의 고정 비용이 다시 매력적으로 느껴지지만, 그 대신 정확도를 희생한 대가임을 알아야 함
| 구분 | TRANSFORMER | RNN |
| --- | --- | --- |
| 철학 | 정확도를 위해 비용을 부담함(설계 철학의 직접적 결과) | 비용을 줄이기 위해 정확도를 일부 버림(압축이라는 설계 선택의 직접적 결과) |
| 과거 처리 방식 | 전부 원본 KV로 보존(무압축) | 단일 고정 상태로 압축 |
| 토큰당 생성 비용 | `O(L)`  • 매번 전체 재참조 | `O(1)`  • 고정 상태만 참조 |
| 메모리 | 길이에 비례해 누적 | 고정(길이 무관) |
| 조회 정확도(recall) | 최대 - 원본 그대로 꺼냄 | 손상 - 덮어써서 복원 불가 |
| 치르는 대가 | 비용, 메모리를 전부 떠안음 | 정보 손실을 그대로 떠안음 |
정확도(recall↑)와 효율(비용↓) 사이에는 Trade-off 관계가 있으며, 최근 흐름은 "RNN으로 돌아가자"는 것이 아니라 RNN의 효율이라는 장점만 떼어내면서, 과거에 치렀던 단점은 없이 가져오려는 노력임
#### \[참고\] 회의록 작성으로 쉽게 이해하기
POV : 긴 회의를 듣고 회의록 한 부를 완성하는 일에 비유함
1. 순차의 벽을 깨다(RNN → SSM) : RNN은 1번 발언을 듣고 회의록을 작성해야 그 다음 2번 발언으로 넘어갈 수 있어(순차), 회의가 길수록 오래 걸림. SSM은 회의록 전체 녹취록이 확보된 상태에서, 발언 N개를 순차적으로 보지 않고 한꺼번에 묶어 회의록을 작성함(병렬)
2. 나누어서 빠르게(Chunk-wise) : 2시간 회의록을 혼자 담당하면 느리므로, 회의를 10분 단위(chunk)로 쪼개 여러명이 동시에 맡아 각자 정리한 뒤 마지막에 이어 붙임(chunk 내부는 순차, chunk 간은 병렬)
3. 바뀐 것만 반영(DeltaNet) : 새로운 발언이 나올 때마다 회의록을 처음부터 다시 작성하지 않고, 기존 회의록은 유지하되 달라진 부분만 내용을 업데이트함(State 유지, 새로운 입력으로 생긴 변화분(delta)만 State에 갱신). Transformer 방식(전체를 매번 다시 참고)을 따르지 않는다는 점이 핵심임
#### 4. Linear Recurrent Models
계산 비용을 선형시간(`O(n)`)으로 만들고, 병렬 학습이 가능하도록 발전해온 현재 RNN 계열을 정리함
`(0) RNN-Style 유지 vs (1) SSM(State-Space Model, 상태공간모델)`
| 구분 | RNN의 Hidden State | SSM의 Hidden State |
| --- | --- | --- |
| 순서 | 1번→2번→...→N번을 반드시 차례대로(하나씩) | 과거 의존은 유지하되 전체를 펼쳐 한꺼번에 계산(병렬) |
| 결과 | 길어질수록 느리고, 오래된 정보가 덮어써져 희미해짐 | 길어져도 빠르게(병렬 학습), 비용은 선형 |
둘 다 과거 정보를 고정 크기의 Hidden State에 압축하여 다음 스텝으로 전달하지만, 바뀐 것은 그것을 갱신하는 방식(순차 → 선형 병렬)임
`(2) Chunk-wise 병렬화 & GPU-friendly 구조 (대표 예 : RetNet)`
회의록을 Chunk A(발언1+2+3), Chunk B(발언4+5+6)처럼 나누어, 학습 관점에서는 Chunk 내부를 병렬로 계산하고 Chunk 간에는 순차적으로 이어붙임(회의록 = 시작 + A → B). 추론 관점에서는 길어져도 GPU가 구간별로 나눠 빠르게 처리할 수 있음
`(3) Linear-time Attention (대표 예 : DeltaNet)`
```javascript
h_t = h_t-1 + Δ
```
Delta(`Δ`)는 새 입력값과 기존 기억의 예측값의 차이이며, 새로운 입력을 만날 때마다 그 오차만큼만 State를 Update함. 회의록에 비유하면 `회의록0=빈 회의록(시작)`, `회의록1=회의록0+Δ1`, `회의록2=회의록1+Δ2`처럼 이전 회의록에 변화분만 누적해서 더해가는 방식임
#### \[참고\] DeltaNet
- `Delta Rule` : 노트를 매번 다시 쓰는 것이 아니라 필요한 부분만 수정
- 문장이 길어져도 빠르고, GPU 친화적이며, 선형 시간으로 문맥 정보를 반영
- RNN처럼 State를 유지하면서 Attention처럼 정보를 반영하는 방식
`h_t = h_t-1 + Δ` (이전 기억에 변화분만 더하는 연산이며, Δ는 변화량을 뽑아내는 역할을 함)
#### 5. MoE, Mixture of Experts
모든 계산을 처리하지 않고 필요한 전문가만 선택해 확장성과 효율을 얻는 구조임
| 구분 | Sparsely-Gated MoE Layer | Switch Transformer |
| --- | --- | --- |
| 목적 | MoE 개념 최초 제안 - 여러 전문가 중 일부만 사용하자 | 실전에 사용하기 좋게 단순화한 모델 - 더 빨리, 더 크게 확장하자 |
| 비유 | 학생을 보고 2명의 선생님을 배정해 반반 나누어 가르침 | 학생마다 딱 1명의 담당 선생님만 배정해 고민 없이 빠르게 배치 |
| 전문가 선택 방식 | 토큰마다 Top-2 Experts 선택. Expert간 교차 통신을 고려해야 함(특정 토큰을 적절한 전문가에게 보내는 비용) | Top-1 Expert 선택(단일 라우팅). 통신 부담이 극감하여 훈련 효율 향상 |
| 장점 | 전체 모델이 아닌 일부 전문가만 사용해 계산 자원 절감 가능, 전문가들이 서로 다른 패턴을 학습해 표현력 향상 | 통신 비용이 대폭 줄어 1조 파라미터 모델까지 확장 가능, 단순한 라우팅 구조로 학습 안정성 확보(구현·운영 용이) |
| 단점 | 토큰마다 연산량이 여전히 큼, Expert간 교차 라우팅(통신 비용)이 발생해 대규모 시스템에서는 비효율적 | 부적절한 라우팅 발생 시 특정 전문가에 부하(imbalanced routing), 라우터 품질이 모델 전체 성능에 영향(게이트 학습이 중요) |
#### 6. Kimi Linear
KDA(Kimi Delta Attention)로 속도와 메모리를 잡고, MLA(Multi-head Latent Attention)로 전체 맥락을 보강하는 구조임
`KDA, Kimi Delta Attention` (DeltaNet 계열 확장)
- `h_t = α · h_t-1 + Δ` (변화분 Δ만 계산하되, `α`로 얼마나 지울지도 함께 조절)
- 회의록 비유 : `회의록t = α·회의록t-1 + Δt`. 과거를 모두 남기고 변화분만 더하는 기존 방식과 달리, 무한정 길어지지 않도록 낡은 것은 흐려지고 중요한 것은 진하게, 그리고 빠르게 유지함
`MLA, Multi-head Latent Attention` (Multi-Head Attention 대비)
- 기존 Multi-Head Attention(Transformer)은 토큰마다 `[K,V]`를 각 Head 개수만큼 그대로 보관(발언마다 원본을 통째로 보관 → KV cache 부담)
- MLA는 여러 `[K,V]`를 압축하여 하나의 요약본으로 보관(발언마다 요약본 1개만 보관 → 핵심만 반영된 요약본, 다시 확인할 때는 원본을 복원/참조)
- Trade-off : 메모리 공간은 줄지만(↓) 복원 부담은 늘어남(↑)
#### 6. Kimi Linear - 하이브리드 구조
KDA로 속도와 메모리를, MLA로 맥락을, MoE로 확장을 담당하는 하이브리드 아키텍처임. 순수 선형도 순수 어텐션도 아닌 하이브리드 구조로, 빠른 방식(KDA)을 주력으로 쓰고 전체를 보는 방식(MLA)을 섞어 장점을 결합함. 긴 문맥에서도 속도와 메모리는 선형 수준으로 가볍게, 품질은 Full Attention급으로 유지하는 것이 목표임
- `KDA, 효율 담당` : 전체 토큰을 다시 보지 않으므로 빠르고 메모리가 적음. Norm/Linear는 State에 반영, KDA는 얼마나 남기고 얼만큼 버릴지 최종 결정, Conv/L2는 불필요한 세부 정보를 제거해 핵심만 남김, Linear는 새로운 정보가 들어왔을 때 얼마나 변화시킬지 계산
- `MLA, 맥락 담당` : 느리지만 전체 관계를 놓치지 않으므로, KDA만으로 약해지는 장거리 맥락을 보강
- `MoE, 확장 담당` : Feed-Forward 대신 MoE로 대체하여, 각 토큰을 독립적으로 가공해 전문가에게 전달(파라미터는 증가하지만 연산량은 그대로 유지). `Shared`(공통 기반 처리, 항상 작동)와 `Routed`(토큰별 전문 처리)로 구성되어 `MoE = Shared(고정) + Routed(선택)`
실험을 통해 확인한 속도·메모리·정확도의 균형 비율은 `KDA : MLA = 3 : 1`로, `KDA-KDA-KDA-MLA` 순서로 블록을 배치함
#### \[참고\] Kimi Linear (아키텍처 평가와 시사점)
아키텍처 평가
- GPT-o1, DeepSeek R1과 같이 추론 능력을 끌어올리기 위해 강화학습을 통한 모델 추가학습 흐름이 있음
- Kimi Linear는 강화학습 방식보다 더 빠르게, 더 높은 정확도를 제시함
- AI Agent가 수십만 토큰에 이르는 복잡한 작업을 실시간에 가깝게 처리할 수 있는 가능성을 확인함
- 모델 패러다임 변화 가능성 : 큰 모델이 상위 전략을 수립하고, 하위 여러 모델이 세부 작업을 처리하는 구조(Supervisor 형태)로 갈 수 있음
시사점
- 가장 큰 모델이 아니라, 가장 효율적인 모델이 승부를 가를 수 있음
- 현존하는 LLM은 대부분 초거대 단일 모델이지만, 문샷AI는 정교하게 설계된 하이브리드 구조와 연산 효율성을 무기로 전혀 다른 방향으로 경쟁하고 있음
- AI Agent가 복잡한 작업을 수행하고, 수십만 토큰이 실시간으로 오가며 협력하는 시대가 오고 있음
관련하여 중국의 오픈 모델 '키미 K3'가 프런티어 AI 진입, 토큰 경제 대전환을 이끌고 있다는 언론 보도와, 중국의 무료 AI 모델(K1) 출시가 트럼프 정부의 대응 방향에도 영향을 주고 있다는 보도, Artificial Analysis 인텔리전스 지수를 통한 여러 모델 간 비교 등이 참고 자료로 함께 제시됨
---
### 마무리 - Part-C. DL Architecture(2017\~Current)
Transformer 이후의 흐름(Efficient-oriented Track의 Linear Recurrent Models와 Scaling-oriented Track의 MoE, 그리고 이를 결합한 Kimi Linear까지)을 다시 한 번 정리하며 강의를 마무리함. DL Architecture Expansion History 표(CV/NLP 연표)와 Beyond Transformer 표가 마지막에 한 번 더 반복 제시되며 전체 흐름을 되짚음
