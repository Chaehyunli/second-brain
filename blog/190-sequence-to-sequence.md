---
title: "[딥러닝]Sequence to Sequence"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: [blog, technical-writing]
category: "AI(ML & DL)"
published: 2025-11-18
source_url: https://ch010104.tistory.com/190
archive_method: Tistory sitemap + HTML content extraction
---

# [딥러닝]Sequence to Sequence

> 원문: https://ch010104.tistory.com/190

## 본문

1. Sequence to Sequence (Seq2Seq)  정의: Sequence to Sequence (Seq2Seq) 학습은 이름 그대로 입력이 주어졌을 때 원하는 출력이 나오도록 하는 방법을 의미 구조: 입력 시퀀스(Input X)와 출력 시퀀스(Output Y)로 구성  입력 (N): $x_1$부터 $x_N$까지 N개의 입력이 있음 출력 (M): $y_1$부터 $y_M$까지 M개의 출력이 있음   특징 (N≠M): Seq2Seq의 핵심 특징은 입력 시퀀스의 길이(N)와 출력 시퀀스의 길이(M)가 반드시 같지 않아도 된다는 것  N to 1: 여러 개의 입력(N)이 하나의 출력(M=1)을 생성할 수 있음 N to M: 여러 개의 입력(N)이 여러 개의 출력(M>1)을 생성할 수 있음     2. Seq2Seq 학습의 다양한 예시 Seq2Seq 모델은 입력과 출력의 길이에 제약이 없기 때문에 다양한 분야에서 활용됩니다.  음성 인식 (Speech Recognition)  입력: 음성 신호 (Speech Signal) 출력: 텍스트 (Text)   동영상 프레임 라벨링 (Movie Frame Labeling)   입력: 비디오 프레임 (Video Frame) 출력: 장면 레이블 (Scene Labels)   형태소 분석 (POS Tagging)  입력: 텍스트 (Text) (예: "오늘 날씨 가 참 좋습니다") 출력: 품사 (POS) (예: "명사 명사 조사 부사 동사")   산술 계산 (Arithmetic Calculation)    입력: 수학적 표현 (Math Expression) (예: "342 + 21") 출력: 숫자 (Numbers) (예: "363")   기계 번역 (Machine Translation)  입력: 한국어 텍스트 (Korean Text) (예: "서울역 근처 스타벅스 로 가자") 출력: 영어 텍스트 (English Text) (예: "Let's go to Starbucks near Seoul station")   문장 완성 (Sentence Completion)  입력: 한국어 텍스트 (Korean Text) (예: "삼성동에서 스타") 출력: 완성된 텍스트 (예: "벅스 한번 보여줘")   위치 라벨링 (Location Labeling)  입력: GPS 시퀀스 (GPS Sequence) 출력: 위치 레이블 (Location Labels) (예: "집", "도로", "회사")     3. Seq2Seq 딥러닝 접근 방식    시퀀스 모델링 (Sequence Modeling): S2S를 딥러닝으로 접근하기 위해서는 시퀀스를 모델링 기억 (Memory)의 필요성:  단순히 입력을 독립적으로 예측하는 것이 아니라(P. 22) 30, Hidden Layer(은닉층)가 **'기억'**을 가지고 연관되어야 함 기억이란 '과거의 어떤 것이 현재에 영향을 미치는 것'을 의미 '행위의 이유'가 '행위'를 만들고, 그 '행위'가 다시 '다음 시간의 행위의 이유'가 되어 현재에 영향을 미치는 순환적 개념(기억)     4. 순환 신경망 (RNN)    RNN (Recurrent Neural Network): '순서가 있는 데이터(Sequential Data)' 처리에 특화된 신경망 구조: RNN이 Feed Forward Network와 달리, 은닉층(hidden state) 간의 연결을 통해 이전 시간의 정보(x_1)가 다음 시간의 출력(y_2, y_3...)에 영향을 미치는 것을 보여줍니다. RNN의 문제점:   역전파 시 동일한 가중치를 반복해서 곱하는 구조적 특징이 있음 그래디언트 소실 (Vanishing Gradient): 가중치가 1보다 작으면 그래디언트가 0에 가까워져 장기 기억을 잃음 그래디언트 폭주 (Exploding Gradient): 가중치가 1보다 크면 그래디언트가 무한대에 가까워져 학습이 불안정 RNN은 구조적으로 바로 전의 것에만 영향을 받기 쉬워 장기 의존성(Long-Dependency) 반영이 어려움     5. LSTM (Long Short-Term Memory)   목적: RNN의 짧은 기억력 문제를 해결하기 위해 등장 아이디어: 'Memory Cell'이라는 박스를 두어 기억을 관리 3가지 게이트 (Gates):  Input Gate (입력 게이트): 현재의 새로운 정보를 얼마나 '저장'할지 결정 Forget Gate (망각 게이트): 과거의 기억을 얼마나 '잊어버릴지' 결정 Output Gate (출력 게이트): 현재 메모리 셀의 기억 중 무엇을 '출력'할지 결정   구현: 각 게이트(Input, Forget, Output)가 '과거'와 '현재'의 정보를 모두 입력받아(네트워크로 설계되어) 다음 행동을 결정하는 구조       6. 인코딩(Encoding) 접근 방식    RNN의 기억: RNN Layer는 입력이 순차적으로 들어올 때, 최종 출력이 잘 나오도록 파라미터를 조정합니다. 47474747이는 곧, RNN Layer가 출력에 필요한 정보를 '기억'하게 됨을 의미 인코딩 과정: P. 33의 다이어그램은 이 과정을 시각화  "서울역", "근처", "스타벅스", "로", "가자" 라는 입력이 순서대로 RNN Layer에 들어감 각 단어가 입력될 때마다 RNN의 은닉 상태(다이어그램 안의 막대 그래프)가 업데이트되며 정보가 누적
