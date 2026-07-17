---
title: "[기계학습] ML(Machine Learning) 이란?"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "AI", "CS"]
category: "AI(ML & DL)"
published: 2025-03-10
source_url: https://ch010104.tistory.com/10
---

# [기계학습] ML(Machine Learning) 이란?

## 원문

https://ch010104.tistory.com/10

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

**머신러닝(ML)**은 컴퓨터가 명시적으로 프로그래밍되지 않고도 데이터를 기반으로 학습하고 스스로 패턴을 찾는 인공지능(AI) 기술!

“A computer program is said to learn from experience E with respect to some task T and some performance measure P, if its performance on T, as measured by P, improves with experience E.” – Tom Mitchell, 1997

## 원문 기반 개념 정리

### 📌 ML(Machine Learning) 란?

**머신러닝(ML)**은 컴퓨터가 명시적으로 프로그래밍되지 않고도 데이터를 기반으로 학습하고 스스로 패턴을 찾는 인공지능(AI) 기술!

“A computer program is said to learn from experience E with respect to some task T and some performance measure P, if its performance on T, as measured by P, improves with experience E.” – Tom Mitchell, 1997

experience E로부터 task T를 수행하기 위해 필요한 것들을 학습하는 것! task T에 대한 수행 능력 지표(task T를 얼마나 잘하나) performance measure P를 통해 해당 모델을 평가!!

-> task T에 대한 지표 P가 경험 E를 통해 향상 가능하다는 전제가 필요

예시) Spam Filter Example

어떤 한 메일이 주어졌을 때, 그 이메일이 스팸인지 아닌지 판단하는 것을 spam filter라고 함. 주어진 다양한 스팸, 비스팸 메일들(학습 자료 experience E)을 training set이라 칭함. 이러한 training set을 통해 학습을 함. -> 이렇게 훈련된 것을 model이라 함. 이후에 새로운 메일이 주어졌을 때, 스팸인지 아닌지 판단! task t: 메일 중에 스팸 메일을 골라내는 것 experience e: 주어진 많은 스팸, 비스팸 메일의 training set performance measure p: 올바르게 판단된 메일의 비율(정확도)

### 1. ML을 왜 사용할까? ( 전통적인 학습 알고리즘 VS ML 개념)

1) 전통적인 학습 알고리즘

(1) 개념

사람이 직접 정의한 규칙과 조건문(If-Else)으로 설계됨

입력값에 따라 미리 정의된 절차를 수행

예제: 정렬 알고리즘(퀵 정렬, 머지 정렬), 암호화 알고리즘(AES, RSA)

스팸 메일의 특징을 분석 (예: "무료", "당첨" 등의 단어가 포함됨)

탐지 로직 구현 (특정 단어가 포함되었는지 확인하는 규칙 기반 알고리즘 작성)

성능 평가 (스팸 필터가 원하는 만큼 잘 작동하는지 확인 후, 부족하면 1~2단계를 반복)

복잡한 문제에 대한 규칙 설계의 어려움

문제의 복잡도가 증가할수록 사람이 직접 설계해야 하는 규칙도 복잡해짐

규칙이 지속적으로 변경되어야 함

스팸 메일 발송자가 기존의 규칙을 회피하는 새로운 형태의 메일을 보내면 탐지 불가

(예: "4U"가 포함된 이메일이 차단된 것을 인지한 후 "U로 시작하는" 메일을 보내기 시작함)

새로운 유형의 스팸에 대한 대응이 느림

새로운 유형의 메일을 걸러내려면 사람이 추가적인 규칙을 설계해야 하며, 이 과정이 반복되어야 함

전통적인 스팸 필터를 만들기 위해서는 다음과 같은 단계를 거친다.

2) ML(Machine Learning)

머신러닝을 활용하면 위와 같은 반복적인 규칙 설계 없이, 모델이 데이터를 학습하여 자동으로 패턴을 찾아낼 수 있다. 머신러닝 기반 스팸 필터는 다음과 같이 동작한다.

대량의 이메일 데이터를 수집하고, 스팸과 정상 메일로 라벨링

머신러닝 모델이 스팸과 정상 메일의 특징을 자동으로 학습

새로운 이메일이 들어오면 학습된 모델이 자동으로 스팸 여부를 판단

시간이 지남에 따라 새로운 데이터를 학습하며 모델이 지속적으로 개선됨

-> 기존의 전통적인 학습 알고리즘은 Rules와 Data를 통해 학습시키지만, ML은 Data와 Answers의 training set을 통해 스스로 Rules를 학습하도록 함

장점 1. 기존의 방법에 비해, 간결한 코드로 더 빠르고 쉽게 유지가 가능하고 더 정확함 2. 기존 방식의 복잡한 문제에서는 좋은 방법이 아님 -> ML이 해결책을 찾을 가능성이 있음 3. 새로운 패턴에 대해 기존의 방식보다 적응하기가 더 쉬움 4. 훈련된 ML 모델을 분석하여 사람이 생각하지 못했던 특징을 찾아낼 수도 있음

### 2. ML vs 전통적인 알고리즘 비교

1) 머신러닝이 유리한 경우

데이터의 패턴이 명확하지 않고 복잡한 경우

입력 데이터가 변화할 가능성이 높은 경우

사람이 직접 규칙을 설계하기 어려운 경우(예: 자연어 처리, 음성 인식)

2) 전통적 알고리즘이 유리한 경우

문제 해결 방식이 명확하게 정의될 수 있는 경우(예: 정렬, 탐색)

고정된 규칙으로 처리해야 하는 경우(예: 암호화, 데이터 압축)

높은 신뢰성과 정확성이 요구되는 경우(예: 금융 시스템의 트랜잭션 처리)

### 3. 다양한 ML 적용 사례

(1) 이미지 및 영상 처리

제품 이미지 분석: CNNs, Transformers 활용

의료 영상 분석(종양 탐지 등): 시맨틱 이미지 분할 기법 사용

(2) 자연어 처리(NLP)

뉴스 기사 자동 분류, 부적절한 댓글 탐지: RNNs, CNNs, Transformers 활용

긴 문서 요약 및 챗봇 개발

(3) 회귀 분석

회사의 미래 수익 예측: 선형 회귀, 랜덤 포레스트 회귀 등 사용

주식 가격 예측, 날씨 예측: RNNs, CNNs 활용

(4) 기타 응용

음성 인식: Voice Assistant 개발

신용카드 부정 사용 탐지: 이상 탐지 기법(Gaussian Mixture Models, Autoencoders) 적용

추천 시스템: K-means, DBSCAN 등 활용

강화 학습(Reinforcement Learning): AlphaGo와 같은 AI 기반 게임 구현

### 4. 생성형 AI(Generative AI)

(1) 개요

Generative AI는 텍스트, 이미지, 음악 등 새로운 콘텐츠를 생성하는 AI 분야이다.

주요 기술: 신경망(Neural Networks), GANs(Generative Adversarial Networks), VAEs(Variational Autoencoders) 1. 신경망(Neural Networks): - Deep Learning 모델을 기반으로 학습 2. GANs(Generative Adversarial Networks): - 두 개의 신경망, 즉 **생성자(Generator)**와 **판별자(Discriminator)**가 서로 경쟁하면서 데이터를 생성하는 모델 **생성자(Generator)**: 진짜와 가장 가까운 가짜를 만들어 내는 것이 목표 **판별자(Discriminator)**: 가짜를 판별해 내는 것이 목표 - ex) 1. 가짜 인물 이미지 생성 (예: 딥페이크) 2. 스타일 변환 (예: 사진을 그림 스타일로 변환) 3. 데이터 증강 (예: 의료 영상 생성) 3. VAEs(Variational Autoencoders): - 데이터의 중요한 특징을 압축하고, 이를 바탕으로 새로운 데이터를 생성하는 모델 - ex) 1. 이미지 생성 및 편집 (예: 손글씨 생성, 얼굴 합성) 2. 데이터 차원 축소 및 특징 학습 3. 노이즈 제거 (예: 흐릿한 사진 복원)

(2) 주요 응용

텍스트 생성: GPT-4, Google Bard 활용

이미지 및 비디오 생성: GANs 기반 생성 도구(DeepArt, RunwayML 등)

음악 생성: OpenAI Jukebox, AIVA 활용

AI 기반 프로그래밍 도우미: GitHub Copilot

## 관련 글

- [[blog/AI(ML & DL)/index|AI(ML & DL)]]
- [[blog/AI(ML & DL)/기계학습- ML(Machine Learning) 시스템의 종류|[기계학습] ML(Machine Learning) 시스템의 종류]]
- [[blog/AI(ML & DL)/기계학습- ML(Machine Learning)의 주요 과제(데이터, 알고리즘 문제)|[기계학습] ML(Machine Learning)의 주요 과제(데이터, 알고리즘 문제)]]
- [[blog/AI(ML & DL)/기계학습- Python NumPy란-- ( 1 )|[기계학습] Python NumPy란?? ( 1 )]]
