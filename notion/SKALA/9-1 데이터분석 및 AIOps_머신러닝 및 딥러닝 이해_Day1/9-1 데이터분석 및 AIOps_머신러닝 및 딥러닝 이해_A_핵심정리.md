---
title: "[9/1] 데이터분석 및 AIOps_머신러닝 및 딥러닝 이해_A_핵심정리"
notion_page_id: "3cd1d84b-f68e-8076-ae29-f29e03321679"
source_url: "https://app.notion.com/p/3cd1d84bf68e8076ae29f29e03321679"
synced_at: "2026-09-01T15:10:20+00:00"
content_sha256: "557cc41682fc71cc3d6bd480573d2c25255e242d935ea63594c576bb8d180118"
---

# [9/1] 데이터분석 및 AIOps_머신러닝 및 딥러닝 이해_A_핵심정리

[[notion/SKALA/index|SKALA 학습 노트]]
> 원문: [Notion 페이지](https://app.notion.com/p/3cd1d84bf68e8076ae29f29e03321679)
>
> 원문의 임시 서명 이미지 URL은 보존하지 않았으며, 안정적으로 확인 가능한 텍스트·코드·표를 유지했다.

### 1. AI 역사와 개념
#### 1-1. AI 역사 연표
| 년도 | 사건 | 개요 | 기여 내용 |
| --- | --- | --- | --- |
| 1956 | Dartmouth Conference | "인공지능(Artificial Intelligence)"이라는 용어를 처음 사용한 회의 | AI 연구의 공식 시작점 / 지능을 기계로 구현할 수 있다는 새로운 연구 영역 제시 |
| 1966\~73 | 1차 AI 겨울 | 초기 언어처리 시스템(ELIZA 등)이 기대에 못 미쳐 연구 지원이 급감 | 과도한 기대와 현실 간의 격차 / 연구 자금과 관심이 급격히 낮아진 대표 사례 |
| 1980 | 전문가 시스템 부상 | 규칙기반 Expert System(XCON)이 기업 문제 해결에 활용 | AI의 실무 문제 해결 적용 가능성 확산 / 상업적 가능성 첫 인정 |
| 1987\~93 | 2차 AI 겨울 | 전문가 시스템의 유지비용과 한계로 다시 투자 축소 | 지식기반 시스템의 확장성 문제 확인 / 데이터 기반 접근의 필요성 부각 |
| 1997 | Deep Blue vs Kasparov | IBM의 체스 AI, Deep Blue가 인간 세계 챔피언을 이김 | 기호 기반 AI가 특정 규칙 기반 문제에서는 인간을 능가할 수 있음을 입증 |
| 2012 | 딥러닝의 부활 - AlexNet | 이미지넷 대회에서 CNN 기반 AlexNet의 혁신적 성과 | 딥러닝이 기존 방식보다 압도적으로 우수함을 입증 / GPU 기반 학습 확산 |
| 2016 | 알파고 vs 이세돌 | DeepMind의 알파고가 바둑에서 이세돌에게 승리 | 딥러닝 기법의 성공적 융합 사례(강화학습, 딥러닝, 몬테카를로 트리 탐색) |
| 2018 | BERT 등장 | Google이 문맥 이해 중심의 NLP 모델 BERT 발표 | Transformer 기반 양방향 사전학습 모델 / NLP 문맥 처리 능력 대폭 향상 |
| 2022 | ChatGPT 공개 | OpenAI가 일반 사용자 대상 대화형 LLM 서비스 출시 | LLM이 일반 사용자에게 개방 / 생성형AI와 대화형 시스템의 대중화 시작 |
| 2023\~현재 | Multimodal(2023) / RAG(2024) / AI Agent(2025) | 다양한 유형의 데이터를 입력으로 처리하고 LLM을 목적지향 에이전트로 활용 | 단순 생성에서 벗어나 사용자 의도(Context) 이해 → 실행까지 확장 |
#### 1-2. \[참고\] ELIZA
- 단순한 패턴 매칭 기반의 초기 대화형 프로그램(1966, Weizenbaum)
- Rogerian Psychotherapy Style: 환자의 말을 되묻거나 감정을 반영하는 문장을 사용하는 상담 방식을 모방
- `ELIZA Effect`: 사용자가 기계에 감정이나 지능이 있다고 착각하는 현상 → 기술의 과대평가로 이어짐
#### 1-3. \[참고\] Deep Blue
- IBM의 체스 전문 Expert System (Chess-playing Expert System)
- 정규 시간 규정(regular time controls) 하에서 현직 세계 챔피언(Kasparov)을 이긴 최초의 컴퓨터
#### 1-4. \[참고\] ELIZA vs Deep Blue
| 구분 | ELIZA | Deep Blue |
| --- | --- | --- |
| 개요 | 초기 언어 처리 시스템 / 과도한 기대와 현실의 격차를 보여준 사례 | 기호 기반 AI / 특정 규칙 기반 문제에서 인간을 능가할 수 있음을 입증 |
| 사용 목적 | 심리상담 시뮬레이터(대화 모사) | 체스 플레이(전략 게임) |
| 작동 방식 | Pattern matching | Rule-Based + Search |
| 지식/전략 사용 | 사전 정의된 문장 패턴 | 인간 전문가의 체스 규칙 + 수백만 수의 시뮬레이션 |
| 지능 여부 | 지능처럼 보이지만 전혀 관련 없음 | 고도의 계산, 처리 속도가 핵심 |
| 한계 | 의미 이해 불가, 단순 키워드 반응 | 일반화 어려움, 체스 이외에는 활용 제한 |
두 시스템 모두 "AI의 초창기 방식"이라는 공통점이 있지만 작동 방식과 평가는 명확히 다름. 규칙 기반 문제에서는 인간을 능가할 수 있음을 증명한 최초 사례이나, 두 시스템 모두 규칙 기반이라 `학습과 일반화`는 하지 못함.
#### 1-5. Game AI의 역사
- 1950\~2000년대: Checkers AI → Chess AI(Deep Blue, 1997) → CNN(1989) → Backprop(1986) → MCTS Go 등으로 발전
- 2016년: DeepMind의 AlphaGo가 바둑에서 인간 최상위 기사에게 승리
- 2017년: AlphaGo가 StarCraft II API를 공개(8/9), OpenAI가 Dota2에서 세계 최정상급 프로게이머를 1v1로 격파(8/11)
#### 1-6. AI / ML / DL / 생성형AI 관계 (NOPE!)
- 흔히 "AI = ChatGPT"라고 생각하기 쉽지만 실제로는 포함관계임
- 범위: 인공지능(AI) ⊃ 머신러닝(ML) ⊃ 딥러닝(DL) ⊃ 생성형AI ⊃ ChatGPT / Copilot 등
#### 1-7. \[참고\] AI Evolution (Model to Intelligence)
![]()
- `ANI` (Artificial Narrow Intelligence): 특정 업무(분야)에 특화된 알고리즘 기반의 학습된 모델
	- 규칙 기반 Expert System / Machine Learning(SVM, XGBoost, Ensemble 등) / 딥러닝 기반 서비스(얼굴인식, 바둑AI 등) → Machine Learning & Deep Learning 영역
- `G.AI` (Generative AI)
	- Single Modal: (텍스트) Large Language Models / (이미지) DALL-E, Stable Diffusion, Midjourney / (음성) Text-to-Speech, Voice Conversion
	- Multi Modal: GPT-4Vision, Flamingo, Kosmos-2 등 (텍스트+이미지+오디오+비디오 종합 이해 및 생성)
	- Actuation with Perception: 로봇 제어 AI(휴머노이드, 산업용 로봇), 자율주행/드론 (Perception-Action Loop, Embodied AI, Physical AI, Cognitive Robotics)
- `AGI` (Artificial General Intelligence): 인간 수준의 광범위하고 유연한 학습 및 추론 능력 확보. AI의 미래적 목표로 아직 구체적으로 실현된 예는 없음. 더 나아가면 `ASI`(Artificial Super Intelligence) 가능성도 거론됨
---
### 2. Statistics vs ML, 모델 접근 방향
#### 2-1. Statistics vs ML in ANI
분석 모델은 전문가 직관을 기반으로 가설을 확인하는 통계분석과, 데이터 관계를 학습하여 가설을 발견하는 머신러닝 기법을 함께 활용함.
- `Human Driven Approach` (가설 확인 중심의 통계 분석): 전문가의 과거 경험과 직관을 기반으로 가설 수립 후 모델 설계. 정형데이터를 기반으로 주로 선형(Linear) 함수모형을 활용
- `Data Driven Approach` (가설 발견 중심의 머신러닝): 데이터로부터 인지하지 못했던 새로운 데이터/데이터 간 관계를 발견. 정형+비정형데이터를 기반으로 비선형(Non-Linear) 함수모형 활용 (+AI, +Machine Learning, +Deep Learning)
- 핵심 메시지: 비교를 통한 우월함의 강조가 아닌, 발전의 방향과 영역의 확대
#### 2-2. Statistics vs ML (방법론)
공통 분석 방법론 6단계: 
![]()
| 구분 | Data | EDA | Modeling | Output |
| --- | --- | --- | --- | --- |
| 통계 기반 | Sample Data | EDA | Linear Regression 또는 Logistic Regression (회귀분석: Linear, 분류분석: Logistic → 거의 정해진 분류 기법) | Result |
| ML 기반 | Data | EDA → Feature Extraction & Selection | 여러 모델(A, B...) Training/Predict 반복 → Accuracy/Error 비교 → Strong Model 도출 | Result |
#### 2-3. Statistics vs ML (모델링)
| 구분 | Statistic Modeling | Machine Learning |
| --- | --- | --- |
| 철학 | 정해진 분포와 가정에 부합하는 신뢰도 높은 모델(모델의 복잡성보다 단순성의 정확도를 중시) | 규칙 기반이 아닌 데이터에서 학습할 수 있는 알고리즘 활용 |
| 가정 | 선형 방정식 형태로 변수 간 관계를 공식화. 데이터 피팅 전에 모델 곡선의 모양을 가정해야 함. 변수는 해석 가능한 수준으로 반영 | 학습 데이터 기반으로 패턴을 학습, 기본적인 관계를 가정할 필요 없음 |
| 데이터 분할 | Train:Test = 7:3, Train 데이터에서 전체 정확도와 개별 변수 수준의 진단 수행 | Train:Test = 7:3, Train을 다시 Train:Validation = 50:20으로 분리 → Validation으로 Hyperparameter 조정 및 성능 검증 |
| 진단 | P-value 등 다양한 매개변수 진단 필요 | 통계적 진단 테스트를 수행하지 않음 |
#### 2-4. 모델 접근 방향 - Classification vs Regression
| 구분 | Classification | Regression |
| --- | --- | --- |
| 목적 | 독립변수(X)로 답(Y)을 구분하기 위한 경계 찾기 (`Decision Boundary`) | 독립변수(X)를 통해 답(Y)과 가장 유사하도록 예측 (`Best Fit Line`) |
| 결과값 | Discrete(이산형, 불연속) - Class Labels | Continuous(연속형) - Number |
| 모델평가 | 분류 정확도 - `Accuracy` | 예측 정확도 - `Sum of Squared Error (r²)` |
![]()
#### 2-5. \[참고\] Which algorithm is good?
![]()
- 두 집단을 나누는 경계(Classifier)는 데이터의 실제 분포(모양)에 따라 다르게 그려져야 함 (대각선 직선으로 나뉘는 경우 / 격자형으로 나뉘는 경우 / 원형으로 나뉘는 경우 등 데이터 형태별로 적합한 경계가 다름)
- 핵심 원칙: `모델 구조(model structure)와 데이터 형태(shape)의 적합성`을 고려하는 것
- 동일한 데이터에 Decision Tree, Random Forest, Linear SVM, RBF SVM, AdaBoost, Regularization Regression 등을 적용하면 데이터 성격에 따라 정확도가 크게 달라짐 → 데이터 성격과 특징을 잘 반영하는 결과를 보이는 알고리즘을 선택하는 것이 핵심
#### 2-6. 모델 성능 영향 요인
전체 분석 과정 중 모델링(알고리즘 적용) 이전 단계에 `80~90%의 노력`이 필요함
![]()
(데이터 준비\~변수 탐색까지 합산 시 상당 부분을 차지하며, 모델 설계 단계까지 포함하면 전체 노력의 대부분이 모델링 이전 단계에 소요됨)
#### 2-7. 당부 말씀
- 공모전이나 Kaggle에서는: 최대한 많은 변수를 넣어 XGBoost/Ensemble 등으로 최대의 성능을 획득하는 접근 방식이 적합함 (목적이 우수한 모델 성능이기 때문)
- 비즈니스에서는: 목적에 맞고 활용 가능한 데이터를 확인하고, 안정적인 모델 성능을 획득하는 것이 접근 방식임 (목적이 비즈니스 문제를 해결하는 것이기 때문)
- 핵심 문구: 비즈니스에서의 모델링은 성능 점수 싸움이 아니라 "현장의 문제 해결책 싸움"이다. 모델의 정확도보다 중요한 것은 현업이 그 결과를 이해하고, 수용하고, 활용할 수 있는가이다.
---
### 3. Machine Learning
#### 3-1. 도입 - 머신러닝이 하는 일
- "유튜브가 어떻게 나보다 더 내 취향을 잘 아는 걸까?", "자율주행차는 어떻게 장애물을 피해 갈까?", "배민은 왜 배고플 때마다 광고 팝업이 뜰까?" 와 같은 질문들의 공통점
- 사람이 일일이 알려주지 않아도 머신이 데이터 기반으로 상황을 파악하고 예측 결과를 알려줌. 점점 더 잘 하기 위해 성능(수치)로 확인하는 방법도 함께 사용
#### 3-2. 용어의 이해
- Arthur Samuel: "Machine Learning is the field of study that gives computers the ability to learn without being explicitly programmed" (컴퓨터에게 명시적으로 프로그래밍하는 것 없이 배울 수 있는 능력을 주는 학문 분야)
- Tom M. Mitchell: "A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P if its performance at tasks in T, as measured by P, improves with experience E." (어떤 과업 T들에 대해 성과평가지표 P의 관점에서 경험 E로부터 배워서, P값이 향상된다면 학습을 할 수 있다고 말할 수 있다)
	- 핵심 요소: 반복 시도 중 얻는 시행착오(E) / 모델링 전략(T, P)
#### 3-3. Approach - 학습의 조건
![]()
- `Improve with Experience`: 반복 시도 중 얻는 시행착오 → Multi-run, Data-driven
- 전제조건: Target(Label)이 사전에 확보되어 있어야 함
- 구조: Task → Experience → Performance → Learning (순환적으로 반복되며 성능이 향상됨)
#### 3-4. Learning - Train / Validation / Test
![]()
- 하나의 모델을 만들고 Train-Valid-Test 성능을 비교하여 모델의 활용 여부를 확인함 (`Single-Split Evaluation`)
- 흐름: Data Set(All) → Train Set + Test Set으로 분리 → Train Set을 다시 Train Set + Validation Set으로 분리
- Train Set → Vanilla Model 학습 → Training Results 확인
- Validation Set → Validation Results 확인 → Hyperparameter tuning, model selection에 활용
- Test Set → 최종 Test Results로 모델 성능 평가
- Single-split evaluation: <br>머신러닝/딥러닝 모델을 평가할 때 데이터셋을 딱 한 번만 분할(Hold-out)하여 성능을 측정하는 가장 기본적이고 단순한 방식<br>→ 데이터셋의 크기가 매우 큰 경우 사용(데이터가 많으면 한 번만 나눠도 데이터의 통계적 특성이 고르게 반영됨)
#### 3-5. Machine Learning Type
![]()
- Supervised Learning: Input/Output 데이터를 모두 제공, 답(Y)을 찾기 위한 학습(감독학습). 최적의 정확도를 보이는 모델로 미래 데이터를 예측(Predict ↔ Output 비교)
- Unsupervised Learning: Input 데이터만 제공, 답(Y)을 알려주지 않거나 알지 못하는 상태에서 스스로 학습(자율학습). 예상 패턴/clustering과 비교하여 insight 도출
- Semi-Supervised Learning: Unlabeled 분포를 Labeled보다 더 많이 고려. Unlabeled 데이터를 함께 활용한다는 점에서 Supervised와 차이가 있으나 Output은 동일. Labeled 데이터로만 학습한 모델보다 더 좋은 성능의 모델을 만들어낼 가능성이 있음
#### 3-6. \[참고\] Semi-Supervised Learning
라벨링 작업에 어려움이 있거나 학습 데이터량이 부족한 경우, 지도학습과 비지도학습을 함께 적용하여 학습시키는 방법
![]()
- 배경: Labeled보다 Unlabeled Data를 확보하기 쉬움. Unlabeled를 학습에 사용하면 데이터의 분포를 더 자세히 고려할 수 있어, Labeled Data로만 학습한 모델보다 더 좋은 성능의 모델을 만들어낼 가능성이 있음 (Label별 데이터 개수가 동일하다는 가정 하에)
- 가정사항
	- `Smoothness`: 가깝지 않은 데이터라도 라벨이 같을 것이라는 기대 (예: X1과 X3이 가깝지 않더라도 X3의 라벨이 X1과 같을 것이라는 기대)
	- `Low-Density`: 라벨을 구분하는 Optimal Boundary 주변에는 데이터가 적을 것이라는 가정
---
### 4. ML Algorithm
#### 4-1. Algorithm 개념
- 사전적 의미: 어떤 문제를 해결하기 위해 정해진 일련의 절차나 방법
	- Input/output이 있고
	- 각 단계가 모호하지 않고 (Definiteness)
	- 유한 번에 끝나며 (Finiteness)
	- 실제로 수행 가능해야 함 (Effectiveness)
- Machine Learning에서는
	- `Learning Algorithm`: 데이터로부터 학습하는 절차 자체
	- `Model`: 그 절차로 데이터에 돌려서 나온 결과물 (학습 규칙/파라미터)
- 흐름: Data → Algorithm → Model
#### 4-2. ML Algorithm 분류 개요
| 계열 | 대표 알고리즘 | 핵심 특징 |
| --- | --- | --- |
| Tree (CART) | Decision Tree | Decision Rule, 트리 형태로 Rule 구분 |
| Random | Random Forest | Data random subset, Making random trees, Building random forest |
| Boosting (Weak to Strong) | XGBoost / LightGBM | 오분류 데이터에 가중치 부여, 여러 weak model 생성 후 성능이 향상 안 될 때까지 반복(boosting) / LightGBM은 XGBoost의 연산방식 개선(병렬처리, Leaf-Wise) |
| Kernel (Maximum Margin) | SVM | 그룹간 경계가 가장 크도록 구분, 비선형 데이터에서는 커널로 구분 |
| Regularization | LASSO / Ridge | LASSO는 예측력 높은 모델을 정의하며 회귀계수를 조정, Ridge는 변수 선별 없이 모두 반영하고 낮은 회귀계수는 0에 가깝게 처리 |
#### 4-3. CART 계열 발전 (Decision Tree → Boosting)
- 발전 순서: Decision Tree(ML BASE) → Random Forest → Gradient Boosting → XGBoost / LightGBM
- 데이터 기반 확장 정리
	- 트리 하나: Decision Tree
	- 트리 하나 → 트리 여러 개: Random Forest
	- 트리를 하나씩 연결하여 오답을 줄이는 방향: Gradient Boosting
	- 계산 속도, 정밀도까지 개선: XGBoost, LightGBM
- 비유적 표현: 조건 → 판단 → 결론에 이르는 과정. 사람이 정한 규칙이 아니라 데이터에서 조건과 판단을 자동 생성하여 결정함 (예: "날씨가 좋으면 나간다 → 비가 오면 나가지 않는다"를 데이터로부터 자동 학습)
#### 4-4. Decision Tree
#### 개념
![]()
- 나무 구조의 모형 기반으로 분류/예측하는 분석 방법 (`의사결정나무`, Decision Tree, DT, CART)
- 의사결정규칙을 도표화하여 관심대상 집단을 몇 개의 소집단으로 분류(Classification)하거나 예측(Prediction)하는 분석 방법
- 모델링 내용이 나무구조로 한눈에 파악되어 쉽게 이해하고 설명할 수 있음
- 분류 또는 예측하고자 하는 목표변수를 `Target Variable`이라고 함
- 활용 분야: 마케팅, CRM, 시장조사, 광고조사, 의학연구, 품질관리 등 / 고객 신용점수, 캠페인 반응분석, 고객세분화, 자동차 잔가 예측 등
#### 해석 가능한 것 vs 해석 불가능한 것 (고객세분화 사례)
![]()
- 해석 가능
	- 분류 규칙(if-then)이 그대로 읽힘 (예: 남성 + 월소득 500만원 이상 → Target 92%)
	- 변수 중요도와 상호작용이 확인됨 (Root가 가장 중요한 변수. 남성은 소득, 여성은 신용도로 갈리는 특징 등)
- 해석 불가능
	- 세그먼트 규칙(표본 수)과 신뢰성은 모름 (세그먼트별 %는 비율일 뿐, 92%가 몇 명인지는 알 수 없음)
	- Target의 정의와 인과관계는 모름 (트리는 연관성만 확인 가능하며 "남성이라서"라는 인과관계는 확인할 수 없음)
#### 분리 기준과 나무 형성 과정
- 분리 기준: 부모 마디에서 자식 마디로 형성될 때 필요한 변수와 값의 부분집합
	- 연속형: 분리기준보다 작으면 왼쪽 자식마디, 크면 오른쪽 자식마디로 데이터 분리
	- 범주형: 전체 범주를 2개의 부분집합으로 분리하는 방향으로 진행
- `불순도가 최저`가 되는 방향으로 분리를 결정 (연속형은 분산 활용, 이산형은 카이제곱 통계량/지니지수/엔트로피지수 활용)
- 나무 성장(Growing): 각 마디에서 최적의 분리규칙을 찾아 나무를 성장시킴. 정지규칙을 만족하면 중단
- 가지치기(Pruning): 오분류율을 크게 할 위험이 높거나 부적절한 추론규칙을 가진 가지를 제거
#### \[참고\] 불순도 최저 방향
의사결정나무는 불순도를 최소로 줄이는 방법으로 진행되며, 불순도를 측정하는 방안으로 지니 지수와 엔트로피 지수를 사용함
![]()
#### \[참고\] Entropy 쉽게 이해하기
- 빨간색 공과 파란색 공이 50개씩 있을 때
	- 각 바구니에 한 종류만 있으면(전부 빨간색) → 완전히 순수 → entropy 0
	- 정확히 반반씩 있으면(빨강 50, 파랑 50) → 가장 많이 섞임 → entropy 최대
- 각 바구니에서 무작위로 하나를 뽑았을 때 무슨 색깔인지 알려면 질문이 평균 몇 번 필요한가?
	- 전부 빨간색 → 물어볼 필요 없음 = 0번 → entropy 0
	- 색깔 반반 → 한 번은 꼭 물어봐야 함 = 1번 → entropy 1(bit)
- Entropy = 정답을 알아내는 데 드는 평균 질문 수(불확실성)
- 의사결정나무에서 Entropy의 역할: 분할 전보다 분할 후에 entropy가 얼마나 줄어드는가를 보고, 가장 많이 줄이는 분할을 선택함
#### Feature Importance
- 계산 방식: 1번의 분할 기준 → entropy 감소량을 구하고, 특성별로 전부 합산 → Feature Importance
- 해석 시 주의: 트리 위쪽에 있다고 해서 단순히 "매우 중요하다"라고 해석하기보다는, `(Entropy를 얼마나 줄였나) × (몇 명에게 적용되나)의 합`으로 이해하는 것이 정확함
	- 예: root에서 1번만 분할되어도 전체 샘플이 대상이면 가중치가 커짐. 하위 그룹에서만 분할되는 변수는 샘플 비율이 작아 기여도가 작아짐
#### 장단점
| 구분 | 내용 |
| --- | --- |
| 장점 - 직관성 | 모델 시각화가 가능하고 비전문가도 이해하기 쉬움. 규칙기반으로 분류/예측을 수행하고 결과 해석이 간단함 |
| 장점 - 전처리 부담 | 범주형/연속형 데이터를 모두 처리 가능. 표준화나 정규화가 필요하지 않음. 이상치, 결측치에 덜 민감함 |
| 장점 - 변수 중요도 | 분할 기준으로 사용된 특성을 기반으로 가장 중요한 변수를 쉽게 파악 가능(Feature Importance) |
| 장점 - 데이터셋 | 비교적 작은 데이터셋에서도 잘 동작하며 빠르게 학습 가능 |
| 단점 - 과적합 | 나무가 깊게 성장할수록 훈련 데이터에 과적합될 가능성이 높음 (가지치기, 최대 깊이 제한으로 방지) |
| 단점 - 불안정성 | 데이터에 민감하여 작은 변화에도 별도의 트리를 생성할 수 있음 (앙상블 기법 - RandomForest, Bagging - 으로 극복) |
| 단점 - 일반화 성능 | 나무의 깊이에 따라 일반화 성능이 낮아질 수 있음. 단일 트리는 변수 간 상호작용을 반영하는 데 한계가 있음 |
| 단점 - 데이터셋 영향 | 큰 데이터셋에서는 분할 기준을 찾는 계산량이 많아질 수 있고, 클래스 불균형 데이터에서는 잘못된 분류 결과를 낼 가능성이 있음 |
#### \[참고\] Overfitting
ML 알고리즘 적용 시 발생하지 않도록 반드시 고려해야 하는 핵심 포인트
- 사전적 의미: `Overfitting` = Fit too much, 너무 잘 맞추다. Train dataset의 노이즈나 특수한 패턴까지 학습하여 test dataset 또는 production에서 성능이 저하됨 (예: 모의고사 문제를 외워 100점을 받았으나 실전 수능에서는 50점을 받음)
| 구분 | 정상적인 학습 | Overfitting |
| --- | --- | --- |
| 학습 대상 | 데이터의 본질적 패턴 | 데이터의 노이즈나 특수 상황까지 반영 |
| 모델 복잡도 | 적절 (규칙적 구조) | 과도 (지나치게 복잡) |
| 검증 성능 | 안정적 유지 | 전반적으로 낮거나 안정적으로 유지되지 못함 |
- Overfitting은 모델이 단순히 데이터를 외운 상태에 가까움. 복잡한 모델 구조(깊은 트리, 많은 파라미터)일수록 쉽게 발생하며, 학습 데이터가 적을 때, Feature 수가 많을 때, Noise가 다수 포함되어 있을 때도 발생 가능성이 있음
- 주의사항: ML 알고리즘은 성능을 올리기 위해 계속 학습하는 구조이므로 기본적으로 overfitting 위험을 내재함(예외적인 문제가 아니라 기본적으로 항상 발생 가능성 있음). 반드시 train - valid - test 성능을 비교하여 안정적인 성능인지 확인해야 함
#### 4-5. Random Forest
`#tree, #random`
- `random subset`: 데이터 변수를 무작위로 선택하여
- `random trees`: 여러 개의 트리들을 임의적으로 생성하여, 각 트리들로부터 얻어질 결과가 평균 이상이 되면
- `feature selection`: 최대의 정보가 반영되도록 정답을 잘 설명할 수 있는 변수를 선택하여
- `random forest`: 생성된 트리들의 성능에 투표하여 모델을 정의함 (voting using bagging to build random forest)
#### 4-6. Boosting (Gradient Boosted Tree Machines)
`#tree, #week2strong`
- `weak model`: 같은 가중치를 가지는 여러 개의 성능이 낮은 모델을 생성하고
- `gradient`: 낮은 성능을 높이기 위해 학습을 진행(가중치 업데이트), 샘플 데이터로 모델 성능을 fitting한 후 전체 학습데이터셋에 반영
- `boosting`: 해당 과정을 반복하여 오차를 최소화시키는 모델을 생성
#### XGBoost vs LightGBM
![]()
#### CatBoost
![]()
- 범주형 데이터를 전처리 없이 직접 처리할 수 있는 Boosting 알고리즘
- 튜닝 난이도가 낮고 기본 설정만으로도 높은 성능을 보여 현장에서 선호됨
- 방식: `Leaf-Wise + Ordered Boosting`
	- 기존 XGBoost/LightGBM: 이전 모델이 예측에 실패한 부분을 다음 모델이 더 잘 맞추도록 보완하며 반복 → 라벨을 너무 많이 참조하면서 학습하여 "정답을 외우는" 과적합 위험 증가 (data leakage 위험)
	- CatBoost: 학습데이터 내 정답을 미리 다 보는 것이 아니라, 학습에 사용된 데이터만 기반으로 다음 트리를 학습시켜 과적합 방지 (같은 train 안에서 지금까지 풀어본 문제만 보고 다음 문제를 풀도록 하는 방식)
#### 4-7. Support Vector Machine (SVM)
`#kernel, #margin`
- 데이터를 2개 그룹으로 구분할 수 있는 선형 분류를 먼저 하고
- `maximum margin`: 그룹 간 분류를 좀 더 정확하게 하기 위해 그룹간 경계가 가장 큰 선형식을 찾음
- `kernel`: 선형으로 분류할 수 없는 경우 feature space를 변형하여 그룹간 경계가 가장 큰 선형식을 찾음
- `soft margin`: 반복 수행하여 경계는 크고, 분류 오류는 작은 것들로 모델을 정의함
- 용어 유래: 독일어 "Kern"에서 유래 → core, essence (사상/주체의 핵심, 중심). 수학적으로는 두 개체 사이의 관계나 핵심적인 부분을 나타내는 함수
#### 모델 복잡도 파라미터
- `gamma`: 두 샘플 사이의 거리에 얼마나 민감하게 반응할지를 결정하는 하이퍼파라미터로, 경계의 복잡도를 조절함. 값이 커질수록 거리에 민감하게 반응하여 과적합 가능성이 높아짐
- `C (Cost)`: 오차에 얼마나 벌점을 부과할지 결정하는 파라미터(오분류를 얼마나 허용할 것인가). Gamma와 함께 조절하여 모델을 최적화함
	- 값이 큰 경우: 오분류를 최대한 줄이려는 방향으로 학습. Margin이 상대적으로 좁아질수록 모델이 데이터에 더 민감해져 과적합(overfitting) 위험이 높아짐
	- 값이 작은 경우: Margin을 더 넓게 잡아 오분류에 대한 벌점을 낮게 부여("Training set에서 일부는 틀려도 괜찮다"는 방향). 값이 많이 작을수록 과소적합(underfitting) 가능성이 있음
#### 4-8. Regularization
`#regular, #performance`
- 사전적 의미: 규칙이나 표준에 맞춰 정돈하다 (Regular(규칙, 기준, 일반) + -ization(과정 또는 결과))
- 통계에서의 회귀분석을 통해 유효변수를 찾더라도, 높은 상관관계를 가진 변수로 인해 설명력이 낮아질 수밖에 없음
- 목적: 모델이 너무 복잡해지는 것을 방지하고 데이터의 노이즈를 과도하게 학습하지 않도록 하여, 모델이 일반화된 성능을 확보하고 예측력(설명력)이 높은 모델을 정의하는 것
- 설명력을 향상시키는 회귀계수를 선별하는 과정을 반복하여 예측력이 높은 모델을 채택함
#### LASSO vs Ridge
| 구분 | LASSO (Least Absolute Shrinkage and Selection Operator) | Ridge (mountain crest, 능선/산등성이) |
| --- | --- | --- |
| 규제 방식 | L1 규제 적용: 회귀계수의 절대값에 패널티 부여 | L2 규제 적용: 회귀계수의 제곱합에 패널티 부여 |
| 효과 | 낮은 회귀계수를 강제로 0으로 처리하여 변수 선택 효과 발생. 모델이 단순해지면 중요한 변수만 남음 | 회귀계수를 표준화 처리(center/scale)하고 낮은 회귀계수는 0에 가깝게 처리(shrinkage)하여 다중공선성 문제 완화 |
| 변수 처리 | 변수 선별 또는 제거 발생 | 변수 선별 또는 제거 없이 모든 변수를 반영 |
| 파라미터 시작값 | alpha 값을 조정(사용자 정의 가능), 보통 0.1에서 시작해 조심스럽게 | 보통 1.0 정도부터 시작해 안정적으로 |
| 적합한 상황 | 변수 선택 및 모델 단순화가 필요할 때 | 다중공선성 문제가 우려되거나 모든 변수를 활용하고 싶을 때 |
| 비유 | 유사한 의미를 가지는 단어를 모두 없애 버리고 "사랑한다"라는 단어만 채택하여 모델 해석력이 상승되는 효과 | 관계가 없는 데이터는 모두 없애버리고 유사한 의미는 최대한 반영하여 "사랑한다", "사모한다"를 함께 선택 (모델 복잡도가 상대적으로 있음) |
---
### 5. 오늘의 퀴즈 (복습용 자가 점검)
아래 각 문항은 상황에 맞는 1순위 알고리즘을 고르는 문제. 먼저 스스로 풀어본 뒤 토글을 열어 정답과 이유를 확인.
#### Q1. 설명 가능성이 최우선인 상황
대출 심사 모델의 거절 사유를 규제 담당자와 비전공 임원에게 한 장의 그림으로 설명해야 함. 정확도보다 설명 가능성이 우선.
보기: (A) Decision Tree (B) Random Forest (C) XGBoost (D) SVM
<details>
<summary>정답 및 해설</summary>
	정답 (A) Decision Tree. 트리 구조가 그대로 시각화되어 if-then 규칙을 비전공자도 읽을 수 있음. 나머지는 앙상블/커널 구조라 해석이 상대적으로 어려움.
</details>
#### Q2. 빠르게 안정적인 기준 성능을 잡고 싶은 상황
새로운 분류 문제에서 튜닝에 시간을 많이 쓰지 않고 빠르게 안정적인 기준 성능을 잡고 싶음. 과적합도 함께 줄이고 싶음.
보기: (A) Decision Tree (B) Random Forest (C) SVM (D) LASSO
<details>
<summary>정답 및 해설</summary>
	정답 (B) Random Forest. 여러 트리의 투표(bagging)로 단일 Decision Tree보다 과적합에 강하고, 기본 설정만으로도 준수한 기준 성능을 얻기 쉬움.
</details>
#### Q3. 대회에서 마지막 한 방울까지 정확도를 짜내야 하는 상황
정형 데이터로 진행되는 예측 대회에 참가. 튜닝 노력을 들여 마지막 한 방울의 정확도까지 짜내야 함.
보기: (A) Decision Tree (B) Random Forest (C) SVM (D) XGBoost
<details>
<summary>정답 및 해설</summary>
	정답 (D) XGBoost. Gradient Boosting 계열은 세밀한 하이퍼파라미터 튜닝을 통해 정형 데이터에서 최고 수준의 예측 성능을 뽑아낼 수 있어 대회에서 널리 쓰임.
</details>
#### Q4. 수천만 행, 학습 속도와 메모리 효율이 중요한 상황
수천만 행 규모의 정형 데이터, 학습 속도와 메모리 효율이 매우 중요. 성능 정확도도 중요하여 부스팅 계열을 쓰기로 정함.
보기: (A) AdaBoost (B) XGBoost (C) LightGBM (D) CatBoost
<details>
<summary>정답 및 해설</summary>
	정답 (C) LightGBM. Leaf-Wise 분할과 연산 최적화로 XGBoost보다 대용량 데이터에서 학습 속도와 메모리 효율이 뛰어남.
</details>
#### Q5. 고유값 많은 범주형 변수가 다수인 상황
고유값이 많은 범주형 변수가 다수인 데이터. 인코딩 전처리에 손을 많이 대고 싶지 않음.
보기: (A) Random Forest (B) XGBoost (C) CatBoost (D) Ridge
<details>
<summary>정답 및 해설</summary>
	정답 (C) CatBoost. 범주형 데이터를 원-핫 인코딩 등 별도 전처리 없이 직접 처리할 수 있도록 설계된 Boosting 알고리즘.
</details>
#### Q6. 표본은 적고 변수는 매우 많은 고차원 상황
표본은 수백 개인데 변수는 수천 개인 데이터셋(예: 유전자 발현, 텍스트 등). EDA를 통해 비선형 경계가 필요함을 확인.
보기: (A) Decision Tree (B) Random Forest (C) LightGBM (D) SVM
<details>
<summary>정답 및 해설</summary>
	정답 (D) SVM. 고차원·소표본 상황에서 강점을 가지며, 커널 트릭으로 비선형 경계를 효과적으로 학습할 수 있음.
</details>
#### Q7. 변수는 많지만 대체로 선형이고 해석 가능한 모델이 필요한 상황
변수가 수백 개인데 대체로 선형 관계를 가짐을 확인. 진짜 중요한 변수만 남긴 간결하고 해석 가능한 모델이 필요.
보기: (A) LASSO (B) Ridge (C) SVM (D) LightGBM
<details>
<summary>정답 및 해설</summary>
	정답 (A) LASSO. L1 규제로 불필요한 변수의 회귀계수를 0으로 만들어 변수 선택 효과를 내므로, 중요 변수만 남긴 해석 가능한 모델을 만들기에 적합함.
</details>
---
