---
title: "[STUDYING] 32. 데이터분석 및 AIOps_머신러닝 및 딥러닝 이해_A_핵심정리"
created: 2026-09-03
updated: 2026-09-03
type: blog-post
tags: ["blog", "technical-writing"]
category: "STUDYING"
published: 2026-09-02
source_url: https://ch010104.tistory.com/350
---
# [STUDYING] 32. 데이터분석 및 AIOps_머신러닝 및 딥러닝 이해_A_핵심정리

## 원문

https://ch010104.tistory.com/350

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

단순한 패턴 매칭 기반의 초기 대화형 프로그램(1966, Weizenbaum)

Rogerian Psychotherapy Style: 환자의 말을 되묻거나 감정을 반영하는 문장을 사용하는 상담 방식을 모방

## 원문 기반 개념 정리

### 1. AI 역사와 개념

### 1-1. AI 역사 연표

### 1-2. [참고] ELIZA

단순한 패턴 매칭 기반의 초기 대화형 프로그램(1966, Weizenbaum)

Rogerian Psychotherapy Style: 환자의 말을 되묻거나 감정을 반영하는 문장을 사용하는 상담 방식을 모방

ELIZA Effect: 사용자가 기계에 감정이나 지능이 있다고 착각하는 현상 → 기술의 과대평가로 이어짐

### 1-3. [참고] Deep Blue

IBM의 체스 전문 Expert System (Chess-playing Expert System)

정규 시간 규정(regular time controls) 하에서 현직 세계 챔피언(Kasparov)을 이긴 최초의 컴퓨터

### 1-4. [참고] ELIZA vs Deep Blue

두 시스템 모두 "AI의 초창기 방식"이라는 공통점이 있지만 작동 방식과 평가는 명확히 다름. 규칙 기반 문제에서는 인간을 능가할 수 있음을 증명한 최초 사례이나, 두 시스템 모두 규칙 기반이라 학습과 일반화는 하지 못함.

### 1-5. Game AI의 역사

1950~2000년대: Checkers AI → Chess AI(Deep Blue, 1997) → CNN(1989) → Backprop(1986) → MCTS Go 등으로 발전

2016년: DeepMind의 AlphaGo가 바둑에서 인간 최상위 기사에게 승리

2017년: AlphaGo가 StarCraft II API를 공개(8/9), OpenAI가 Dota2에서 세계 최정상급 프로게이머를 1v1로 격파(8/11)

### 1-6. AI / ML / DL / 생성형AI 관계 (NOPE!)

흔히 "AI = ChatGPT"라고 생각하기 쉽지만 실제로는 포함관계임

범위: 인공지능(AI) ⊃ 머신러닝(ML) ⊃ 딥러닝(DL) ⊃ 생성형AI ⊃ ChatGPT / Copilot 등

### 1-7. [참고] AI Evolution (Model to Intelligence)

ANI (Artificial Narrow Intelligence): 특정 업무(분야)에 특화된 알고리즘 기반의 학습된 모델

규칙 기반 Expert System / Machine Learning(SVM, XGBoost, Ensemble 등) / 딥러닝 기반 서비스(얼굴인식, 바둑AI 등) → Machine Learning & Deep Learning 영역

G.AI (Generative AI)

Single Modal: (텍스트) Large Language Models / (이미지) DALL-E, Stable Diffusion, Midjourney / (음성) Text-to-Speech, Voice Conversion

Multi Modal: GPT-4Vision, Flamingo, Kosmos-2 등 (텍스트+이미지+오디오+비디오 종합 이해 및 생성)

Actuation with Perception: 로봇 제어 AI(휴머노이드, 산업용 로봇), 자율주행/드론 (Perception-Action Loop, Embodied AI, Physical AI, Cognitive Robotics)

AGI (Artificial General Intelligence): 인간 수준의 광범위하고 유연한 학습 및 추론 능력 확보. AI의 미래적 목표로 아직 구체적으로 실현된 예는 없음. 더 나아가면 ASI(Artificial Super Intelligence) 가능성도 거론됨

### 2. Statistics vs ML, 모델 접근 방향

### 2-1. Statistics vs ML in ANI

분석 모델은 전문가 직관을 기반으로 가설을 확인하는 통계분석과, 데이터 관계를 학습하여 가설을 발견하는 머신러닝 기법을 함께 활용함.

Human Driven Approach (가설 확인 중심의 통계 분석): 전문가의 과거 경험과 직관을 기반으로 가설 수립 후 모델 설계. 정형데이터를 기반으로 주로 선형(Linear) 함수모형을 활용

Data Driven Approach (가설 발견 중심의 머신러닝): 데이터로부터 인지하지 못했던 새로운 데이터/데이터 간 관계를 발견. 정형+비정형데이터를 기반으로 비선형(Non-Linear) 함수모형 활용 (+AI, +Machine Learning, +Deep Learning)

핵심 메시지: 비교를 통한 우월함의 강조가 아닌, 발전의 방향과 영역의 확대

### 2-2. Statistics vs ML (방법론)

공통 분석 방법론 6단계:

### 2-3. Statistics vs ML (모델링)

### 2-4. 모델 접근 방향 - Classification vs Regression

### 2-5. [참고] Which algorithm is good?

두 집단을 나누는 경계(Classifier)는 데이터의 실제 분포(모양)에 따라 다르게 그려져야 함 (대각선 직선으로 나뉘는 경우 / 격자형으로 나뉘는 경우 / 원형으로 나뉘는 경우 등 데이터 형태별로 적합한 경계가 다름)

핵심 원칙: 모델 구조(model structure)와 데이터 형태(shape)의 적합성을 고려하는 것

동일한 데이터에 Decision Tree, Random Forest, Linear SVM, RBF SVM, AdaBoost, Regularization Regression 등을 적용하면 데이터 성격에 따라 정확도가 크게 달라짐 → 데이터 성격과 특징을 잘 반영하는 결과를 보이는 알고리즘을 선택하는 것이 핵심

### 2-6. 모델 성능 영향 요인

전체 분석 과정 중 모델링(알고리즘 적용) 이전 단계에 80~90%의 노력이 필요함

(데이터 준비~변수 탐색까지 합산 시 상당 부분을 차지하며, 모델 설계 단계까지 포함하면 전체 노력의 대부분이 모델링 이전 단계에 소요됨)

### 2-7. 당부 말씀

공모전이나 Kaggle에서는: 최대한 많은 변수를 넣어 XGBoost/Ensemble 등으로 최대의 성능을 획득하는 접근 방식이 적합함 (목적이 우수한 모델 성능이기 때문)

비즈니스에서는: 목적에 맞고 활용 가능한 데이터를 확인하고, 안정적인 모델 성능을 획득하는 것이 접근 방식임 (목적이 비즈니스 문제를 해결하는 것이기 때문)

핵심 문구: 비즈니스에서의 모델링은 성능 점수 싸움이 아니라 "현장의 문제 해결책 싸움"이다. 모델의 정확도보다 중요한 것은 현업이 그 결과를 이해하고, 수용하고, 활용할 수 있는가이다.

### 3. Machine Learning

### 3-1. 도입 - 머신러닝이 하는 일

"유튜브가 어떻게 나보다 더 내 취향을 잘 아는 걸까?", "자율주행차는 어떻게 장애물을 피해 갈까?", "배민은 왜 배고플 때마다 광고 팝업이 뜰까?" 와 같은 질문들의 공통점

사람이 일일이 알려주지 않아도 머신이 데이터 기반으로 상황을 파악하고 예측 결과를 알려줌. 점점 더 잘 하기 위해 성능(수치)로 확인하는 방법도 함께 사용

### 3-2. 용어의 이해

Arthur Samuel: "Machine Learning is the field of study that gives computers the ability to learn without being explicitly programmed" (컴퓨터에게 명시적으로 프로그래밍하는 것 없이 배울 수 있는 능력을 주는 학문 분야)

Tom M. Mitchell: "A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P if its performance at tasks in T, as measured by P, improves with experience E." (어떤 과업 T들에 대해 성과평가지표 P의 관점에서 경험 E로부터 배워서, P값이 향상된다면 학습을 할 수 있다고 말할 수 있다)

핵심 요소: 반복 시도 중 얻는 시행착오(E) / 모델링 전략(T, P)

### 3-3. Approach - 학습의 조건

Improve with Experience: 반복 시도 중 얻는 시행착오 → Multi-run, Data-driven

전제조건: Target(Label)이 사전에 확보되어 있어야 함

구조: Task → Experience → Performance → Learning (순환적으로 반복되며 성능이 향상됨)

### 3-4. Learning - Train / Validation / Test

하나의 모델을 만들고 Train-Valid-Test 성능을 비교하여 모델의 활용 여부를 확인함 (Single-Split Evaluation)

흐름: Data Set(All) → Train Set + Test Set으로 분리 → Train Set을 다시 Train Set + Validation Set으로 분리

Train Set → Vanilla Model 학습 → Training Results 확인

Validation Set → Validation Results 확인 → Hyperparameter tuning, model selection에 활용

Test Set → 최종 Test Results로 모델 성능 평가

Single-split evaluation: 머신러닝/딥러닝 모델을 평가할 때 데이터셋을 딱 한 번만 분할(Hold-out)하여 성능을 측정하는 가장 기본적이고 단순한 방식 → 데이터셋의 크기가 매우 큰 경우 사용(데이터가 많으면 한 번만 나눠도 데이터의 통계적 특성이 고르게 반영됨)

### 3-5. Machine Learning Type

Supervised Learning: Input/Output 데이터를 모두 제공, 답(Y)을 찾기 위한 학습(감독학습). 최적의 정확도를 보이는 모델로 미래 데이터를 예측(Predict ↔ Output 비교)

Unsupervised Learning: Input 데이터만 제공, 답(Y)을 알려주지 않거나 알지 못하는 상태에서 스스로 학습(자율학습). 예상 패턴/clustering과 비교하여 insight 도출

Semi-Supervised Learning: Unlabeled 분포를 Labeled보다 더 많이 고려. Unlabeled 데이터를 함께 활용한다는 점에서 Supervised와 차이가 있으나 Output은 동일. Labeled 데이터로만 학습한 모델보다 더 좋은 성능의 모델을 만들어낼 가능성이 있음

### 3-6. [참고] Semi-Supervised Learning

라벨링 작업에 어려움이 있거나 학습 데이터량이 부족한 경우, 지도학습과 비지도학습을 함께 적용하여 학습시키는 방법

배경: Labeled보다 Unlabeled Data를 확보하기 쉬움. Unlabeled를 학습에 사용하면 데이터의 분포를 더 자세히 고려할 수 있어, Labeled Data로만 학습한 모델보다 더 좋은 성능의 모델을 만들어낼 가능성이 있음 (Label별 데이터 개수가 동일하다는 가정 하에)

가정사항

Smoothness: 가깝지 않은 데이터라도 라벨이 같을 것이라는 기대 (예: X1과 X3이 가깝지 않더라도 X3의 라벨이 X1과 같을 것이라는 기대)

Low-Density: 라벨을 구분하는 Optimal Boundary 주변에는 데이터가 적을 것이라는 가정

### 4. ML Algorithm

### 4-1. Algorithm 개념

사전적 의미: 어떤 문제를 해결하기 위해 정해진 일련의 절차나 방법

Input/output이 있고

각 단계가 모호하지 않고 (Definiteness)

유한 번에 끝나며 (Finiteness)

실제로 수행 가능해야 함 (Effectiveness)

Machine Learning에서는

Learning Algorithm: 데이터로부터 학습하는 절차 자체

Model: 그 절차로 데이터에 돌려서 나온 결과물 (학습 규칙/파라미터)

흐름: Data → Algorithm → Model

### 4-2. ML Algorithm 분류 개요

### 4-3. CART 계열 발전 (Decision Tree → Boosting)

발전 순서: Decision Tree(ML BASE) → Random Forest → Gradient Boosting → XGBoost / LightGBM

데이터 기반 확장 정리

트리 하나: Decision Tree

트리 하나 → 트리 여러 개: Random Forest

트리를 하나씩 연결하여 오답을 줄이는 방향: Gradient Boosting

계산 속도, 정밀도까지 개선: XGBoost, LightGBM

비유적 표현: 조건 → 판단 → 결론에 이르는 과정. 사람이 정한 규칙이 아니라 데이터에서 조건과 판단을 자동 생성하여 결정함 (예: "날씨가 좋으면 나간다 → 비가 오면 나가지 않는다"를 데이터로부터 자동 학습)

### 4-4. Decision Tree

### 개념

나무 구조의 모형 기반으로 분류/예측하는 분석 방법 (의사결정나무, Decision Tree, DT, CART)

의사결정규칙을 도표화하여 관심대상 집단을 몇 개의 소집단으로 분류(Classification)하거나 예측(Prediction)하는 분석 방법

모델링 내용이 나무구조로 한눈에 파악되어 쉽게 이해하고 설명할 수 있음

분류 또는 예측하고자 하는 목표변수를 Target Variable이라고 함

활용 분야: 마케팅, CRM, 시장조사, 광고조사, 의학연구, 품질관리 등 / 고객 신용점수, 캠페인 반응분석, 고객세분화, 자동차 잔가 예측 등

### 해석 가능한 것 vs 해석 불가능한 것 (고객세분화 사례)

해석 가능

분류 규칙(if-then)이 그대로 읽힘 (예: 남성 + 월소득 500만원 이상 → Target 92%)

변수 중요도와 상호작용이 확인됨 (Root가 가장 중요한 변수. 남성은 소득, 여성은 신용도로 갈리는 특징 등)

해석 불가능

세그먼트 규칙(표본 수)과 신뢰성은 모름 (세그먼트별 %는 비율일 뿐, 92%가 몇 명인지는 알 수 없음)

Target의 정의와 인과관계는 모름 (트리는 연관성만 확인 가능하며 "남성이라서"라는 인과관계는 확인할 수 없음)

### 분리 기준과 나무 형성 과정

분리 기준: 부모 마디에서 자식 마디로 형성될 때 필요한 변수와 값의 부분집합

연속형: 분리기준보다 작으면 왼쪽 자식마디, 크면 오른쪽 자식마디로 데이터 분리

범주형: 전체 범주를 2개의 부분집합으로 분리하는 방향으로 진행

불순도가 최저가 되는 방향으로 분리를 결정 (연속형은 분산 활용, 이산형은 카이제곱 통계량/지니지수/엔트로피지수 활용)

나무 성장(Growing): 각 마디에서 최적의 분리규칙을 찾아 나무를 성장시킴. 정지규칙을 만족하면 중단

가지치기(Pruning): 오분류율을 크게 할 위험이 높거나 부적절한 추론규칙을 가진 가지를 제거

### [참고] 불순도 최저 방향

의사결정나무는 불순도를 최소로 줄이는 방법으로 진행되며, 불순도를 측정하는 방안으로 지니 지수와 엔트로피 지수를 사용함

### [참고] Entropy 쉽게 이해하기

빨간색 공과 파란색 공이 50개씩 있을 때

각 바구니에 한 종류만 있으면(전부 빨간색) → 완전히 순수 → entropy 0

정확히 반반씩 있으면(빨강 50, 파랑 50) → 가장 많이 섞임 → entropy 최대

각 바구니에서 무작위로 하나를 뽑았을 때 무슨 색깔인지 알려면 질문이 평균 몇 번 필요한가?

전부 빨간색 → 물어볼 필요 없음 = 0번 → entropy 0

색깔 반반 → 한 번은 꼭 물어봐야 함 = 1번 → entropy 1(bit)

Entropy = 정답을 알아내는 데 드는 평균 질문 수(불확실성)

의사결정나무에서 Entropy의 역할: 분할 전보다 분할 후에 entropy가 얼마나 줄어드는가를 보고, 가장 많이 줄이는 분할을 선택함

### Feature Importance

계산 방식: 1번의 분할 기준 → entropy 감소량을 구하고, 특성별로 전부 합산 → Feature Importance

해석 시 주의: 트리 위쪽에 있다고 해서 단순히 "매우 중요하다"라고 해석하기보다는, (Entropy를 얼마나 줄였나) × (몇 명에게 적용되나)의 합으로 이해하는 것이 정확함

예: root에서 1번만 분할되어도 전체 샘플이 대상이면 가중치가 커짐. 하위 그룹에서만 분할되는 변수는 샘플 비율이 작아 기여도가 작아짐

### 장단점

### [참고] Overfitting

ML 알고리즘 적용 시 발생하지 않도록 반드시 고려해야 하는 핵심 포인트

사전적 의미: Overfitting = Fit too much, 너무 잘 맞추다. Train dataset의 노이즈나 특수한 패턴까지 학습하여 test dataset 또는 production에서 성능이 저하됨 (예: 모의고사 문제를 외워 100점을 받았으나 실전 수능에서는 50점을 받음)

Overfitting은 모델이 단순히 데이터를 외운 상태에 가까움. 복잡한 모델 구조(깊은 트리, 많은 파라미터)일수록 쉽게 발생하며, 학습 데이터가 적을 때, Feature 수가 많을 때, Noise가 다수 포함되어 있을 때도 발생 가능성이 있음

주의사항: ML 알고리즘은 성능을 올리기 위해 계속 학습하는 구조이므로 기본적으로 overfitting 위험을 내재함(예외적인 문제가 아니라 기본적으로 항상 발생 가능성 있음). 반드시 train - valid - test 성능을 비교하여 안정적인 성능인지 확인해야 함

### 4-5. Random Forest

#tree, #random

random subset: 데이터 변수를 무작위로 선택하여

random trees: 여러 개의 트리들을 임의적으로 생성하여, 각 트리들로부터 얻어질 결과가 평균 이상이 되면

feature selection: 최대의 정보가 반영되도록 정답을 잘 설명할 수 있는 변수를 선택하여

random forest: 생성된 트리들의 성능에 투표하여 모델을 정의함 (voting using bagging to build random forest)

### 4-6. Boosting (Gradient Boosted Tree Machines)

#tree, #week2strong

weak model: 같은 가중치를 가지는 여러 개의 성능이 낮은 모델을 생성하고

gradient: 낮은 성능을 높이기 위해 학습을 진행(가중치 업데이트), 샘플 데이터로 모델 성능을 fitting한 후 전체 학습데이터셋에 반영

boosting: 해당 과정을 반복하여 오차를 최소화시키는 모델을 생성

### XGBoost vs LightGBM

### CatBoost

범주형 데이터를 전처리 없이 직접 처리할 수 있는 Boosting 알고리즘

튜닝 난이도가 낮고 기본 설정만으로도 높은 성능을 보여 현장에서 선호됨

방식: Leaf-Wise + Ordered Boosting

기존 XGBoost/LightGBM: 이전 모델이 예측에 실패한 부분을 다음 모델이 더 잘 맞추도록 보완하며 반복 → 라벨을 너무 많이 참조하면서 학습하여 "정답을 외우는" 과적합 위험 증가 (data leakage 위험)

CatBoost: 학습데이터 내 정답을 미리 다 보는 것이 아니라, 학습에 사용된 데이터만 기반으로 다음 트리를 학습시켜 과적합 방지 (같은 train 안에서 지금까지 풀어본 문제만 보고 다음 문제를 풀도록 하는 방식)

### 4-7. Support Vector Machine (SVM)

#kernel, #margin

데이터를 2개 그룹으로 구분할 수 있는 선형 분류를 먼저 하고

maximum margin: 그룹 간 분류를 좀 더 정확하게 하기 위해 그룹간 경계가 가장 큰 선형식을 찾음

kernel: 선형으로 분류할 수 없는 경우 feature space를 변형하여 그룹간 경계가 가장 큰 선형식을 찾음

soft margin: 반복 수행하여 경계는 크고, 분류 오류는 작은 것들로 모델을 정의함

용어 유래: 독일어 "Kern"에서 유래 → core, essence (사상/주체의 핵심, 중심). 수학적으로는 두 개체 사이의 관계나 핵심적인 부분을 나타내는 함수

### 모델 복잡도 파라미터

gamma: 두 샘플 사이의 거리에 얼마나 민감하게 반응할지를 결정하는 하이퍼파라미터로, 경계의 복잡도를 조절함. 값이 커질수록 거리에 민감하게 반응하여 과적합 가능성이 높아짐

C (Cost): 오차에 얼마나 벌점을 부과할지 결정하는 파라미터(오분류를 얼마나 허용할 것인가). Gamma와 함께 조절하여 모델을 최적화함

값이 큰 경우: 오분류를 최대한 줄이려는 방향으로 학습. Margin이 상대적으로 좁아질수록 모델이 데이터에 더 민감해져 과적합(overfitting) 위험이 높아짐

값이 작은 경우: Margin을 더 넓게 잡아 오분류에 대한 벌점을 낮게 부여("Training set에서 일부는 틀려도 괜찮다"는 방향). 값이 많이 작을수록 과소적합(underfitting) 가능성이 있음

### 4-8. Regularization

#regular, #performance

사전적 의미: 규칙이나 표준에 맞춰 정돈하다 (Regular(규칙, 기준, 일반) + -ization(과정 또는 결과))

통계에서의 회귀분석을 통해 유효변수를 찾더라도, 높은 상관관계를 가진 변수로 인해 설명력이 낮아질 수밖에 없음

목적: 모델이 너무 복잡해지는 것을 방지하고 데이터의 노이즈를 과도하게 학습하지 않도록 하여, 모델이 일반화된 성능을 확보하고 예측력(설명력)이 높은 모델을 정의하는 것

설명력을 향상시키는 회귀계수를 선별하는 과정을 반복하여 예측력이 높은 모델을 채택함

### LASSO vs Ridge

### 5. 오늘의 퀴즈 (복습용 자가 점검)

아래 각 문항은 상황에 맞는 1순위 알고리즘을 고르는 문제. 먼저 스스로 풀어본 뒤 토글을 열어 정답과 이유를 확인.

### Q1. 설명 가능성이 최우선인 상황

대출 심사 모델의 거절 사유를 규제 담당자와 비전공 임원에게 한 장의 그림으로 설명해야 함. 정확도보다 설명 가능성이 우선.

보기: (A) Decision Tree (B) Random Forest (C) XGBoost (D) SVM

정답 및 해설

정답 (A) Decision Tree. 트리 구조가 그대로 시각화되어 if-then 규칙을 비전공자도 읽을 수 있음. 나머지는 앙상블/커널 구조라 해석이 상대적으로 어려움.

### Q2. 빠르게 안정적인 기준 성능을 잡고 싶은 상황

새로운 분류 문제에서 튜닝에 시간을 많이 쓰지 않고 빠르게 안정적인 기준 성능을 잡고 싶음. 과적합도 함께 줄이고 싶음.

보기: (A) Decision Tree (B) Random Forest (C) SVM (D) LASSO

정답 및 해설

정답 (B) Random Forest. 여러 트리의 투표(bagging)로 단일 Decision Tree보다 과적합에 강하고, 기본 설정만으로도 준수한 기준 성능을 얻기 쉬움.

### Q3. 대회에서 마지막 한 방울까지 정확도를 짜내야 하는 상황

정형 데이터로 진행되는 예측 대회에 참가. 튜닝 노력을 들여 마지막 한 방울의 정확도까지 짜내야 함.

보기: (A) Decision Tree (B) Random Forest (C) SVM (D) XGBoost

정답 및 해설

정답 (D) XGBoost. Gradient Boosting 계열은 세밀한 하이퍼파라미터 튜닝을 통해 정형 데이터에서 최고 수준의 예측 성능을 뽑아낼 수 있어 대회에서 널리 쓰임.

### Q4. 수천만 행, 학습 속도와 메모리 효율이 중요한 상황

수천만 행 규모의 정형 데이터, 학습 속도와 메모리 효율이 매우 중요. 성능 정확도도 중요하여 부스팅 계열을 쓰기로 정함.

보기: (A) AdaBoost (B) XGBoost (C) LightGBM (D) CatBoost

정답 및 해설

정답 (C) LightGBM. Leaf-Wise 분할과 연산 최적화로 XGBoost보다 대용량 데이터에서 학습 속도와 메모리 효율이 뛰어남.

### Q5. 고유값 많은 범주형 변수가 다수인 상황

고유값이 많은 범주형 변수가 다수인 데이터. 인코딩 전처리에 손을 많이 대고 싶지 않음.

보기: (A) Random Forest (B) XGBoost (C) CatBoost (D) Ridge

정답 및 해설

정답 (C) CatBoost. 범주형 데이터를 원-핫 인코딩 등 별도 전처리 없이 직접 처리할 수 있도록 설계된 Boosting 알고리즘.

### Q6. 표본은 적고 변수는 매우 많은 고차원 상황

표본은 수백 개인데 변수는 수천 개인 데이터셋(예: 유전자 발현, 텍스트 등). EDA를 통해 비선형 경계가 필요함을 확인.

보기: (A) Decision Tree (B) Random Forest (C) LightGBM (D) SVM

정답 및 해설

정답 (D) SVM. 고차원·소표본 상황에서 강점을 가지며, 커널 트릭으로 비선형 경계를 효과적으로 학습할 수 있음.

### Q7. 변수는 많지만 대체로 선형이고 해석 가능한 모델이 필요한 상황

변수가 수백 개인데 대체로 선형 관계를 가짐을 확인. 진짜 중요한 변수만 남긴 간결하고 해석 가능한 모델이 필요.

보기: (A) LASSO (B) Ridge (C) SVM (D) LightGBM

정답 및 해설

정답 (A) LASSO. L1 규제로 불필요한 변수의 회귀계수를 0으로 만들어 변수 선택 효과를 내므로, 중요 변수만 남긴 해석 가능한 모델을 만들기에 적합함.

## 관련 글

- [[blog/STUDYING/index|STUDYING]]
