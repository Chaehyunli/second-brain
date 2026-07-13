---
title: "[딥러닝] 딥러닝 - MINST 손글씨 인식"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing"]
category: "AI(ML & DL)"
published: 2025-09-23
source_url: https://ch010104.tistory.com/139
---

# [딥러닝] 딥러닝 - MINST 손글씨 인식

## 원문

https://ch010104.tistory.com/139

## 핵심 요약

- **1단계: 데이터 준비하기 - MNIST란 ?** — - MNIST는 사람들이 직접 쓴 0부터 9까지의 손글씨 숫자 이미지 데이터셋 28×28 픽셀 크기의 흑백 이미지
- **2단계: 신경망 모델 만들기** — - Keras의 Sequential 모델은 각 레이어(layer)를 레고 블록처럼 순차적으로 쌓아 만드는 간단하고 직관적인 방법
- **3단계: 모델 컴파일하기 (학습 과정 설정)** — - 모델이 어떻게 학습할지를 정하는 '컴파일' 단계가 필요
- **4단계: 데이터 전처리** — - 모델에 데이터를 입력하기 전에, 모델이 이해할 수 있는 형태로 가공하는 과정이 필요

## 관련 글

- [[blog/AI(ML & DL)/index|AI(ML & DL)]]
- [[blog/AI(ML & DL)/딥러닝- 퍼셉트론(Perceptron)과 경사 하강법(Gradient Descent)|[딥러닝] 퍼셉트론(Perceptron)과 경사 하강법(Gradient Descent)]]
- [[blog/AI(ML & DL)/딥러닝- 머신러닝- 학습(Learning)과 모델(Model)|[딥러닝] 머신러닝: 학습(Learning)과 모델(Model)]]
- [[blog/AI(ML & DL)/딥러닝- 인공지능의 동향|[딥러닝] 인공지능의 동향]]
