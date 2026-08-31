---
title: "[8/31] sLLM 구현 및 Fine Tunning_Day2_핵심 정리"
notion_page_id: "3cc1d84b-f68e-8095-844a-f4a63b6085bf"
source_url: "https://app.notion.com/p/3cc1d84bf68e8095844af4a63b6085bf"
synced_at: "2026-09-01T00:07:33+09:00"
content_sha256: "80975ad04f85526d634f3698b600adc2ce34962a7c4762ee5e298604f4920a42"
---

# [8/31] sLLM 구현 및 Fine Tunning_Day2_핵심 정리

[[notion/SKALA/index|SKALA 학습 노트]]
[[notion/SKALA/8-28 sLLM 구현 및 Fine Tunning_Day1/8-28 sLLM 구현 및 Fine Tunning_Day1_핵심 정리|sLLM Day1 핵심 정리]]

> 원문: [Notion 페이지](https://app.notion.com/p/3cc1d84bf68e8095844af4a63b6085bf)
>
> 원문의 임시 서명 이미지 URL은 보존하지 않았으며, 안정적으로 확인 가능한 텍스트·코드·표를 유지했다.

### 1. 핵심 용어 핵심 정리
- **CLM (Causal Language Modeling):** **"다음 단어 맞추기"**
	- 앞 문맥을 보고 다음에 올 단어를 예측하는 사전 학습 방식입니다. GPT, Llama, Qwen 등 생성형 LLM/SLLM의 기반이 됩니다.
- **MLM (Masked Language Modeling):** **"빈칸 채우기"**
	- 문장 중간의 빈칸(\[MASK\])을 맞추는 학습 방식입니다. BERT 등이 대표적이며, RAG에서 문서 검색 시 쓰이는 임베딩 모델 제작에 주로 사용됩니다.
- **Pre-training (사전 학습):** **"초·중·고 의무 교육"**
	- 수조 개의 인터넷 문장 데이터를 CLM 방식으로 읽혀 언어의 구조와 세상의 일반 지식을 습득시키는 단계입니다.
- **Fine-tuning (파인튜닝):** **"대학/직업 전문 교육"**
	- 이미 사전 학습된 모델을 가져와 특정 목적이나 분야(의료, 사내 업무 등)에 맞게 가중치를 추가 학습시키는 과정입니다.
- **SFT (Supervised Fine-Tuning):** **"Q&A 족보 학습 (지도 파인튜닝)"**
	- `[질문 - 정답]` 형태의 데이터를 제공하여, AI가 지시를 이해하고 대화 형태로 정답을 출력하도록 길들이는 파인튜닝의 대표적인 목적/단계입니다.
- **PEFT (Parameter-Efficient Fine-Tuning):** **"가성비 학습 방식"**
	- 모델 전체 가중치를 다 수정하지 않고 일부 파라미터만 학습시켜 GPU 메모리와 비용을 획기적으로 아끼는 기술의 총칭입니다.
- **LoRA (Low-Rank Adaptation):** **"PEFT의 대표 기법"**
	- 기존 가중치 옆에 작고 효율적인 저랭크(Low-Rank) 행렬 레이어를 병렬로 추가해 변환량만 학습시키는 가장 대중적인 PEFT 구현 방식입니다.
- **RAG (Retrieval-Augmented Generation):** **"오픈북 테스트 (검색 증강 생성)"**
	- 모델 내부를 학습시키는 것이 아니라, 외부에 사내 보안 문서 DB를 두고 질문이 들어왔을 때 관련 문서를 '검색해서 첨부'해 답하게 만드는 외부 시스템입니다.
### 2. SLLM 폐쇄망 구축 전체 프로세스 (처음부터 끝까지)
```plain text
[1단계] 오픈소스 Instruct 모델 수급 (CLM + SFT 완료 상태)
    ↓
[2단계] 사내 데이터베이스 기반 내부망 RAG 구축
    ↓
[3단계] 성능 한계 보완을 위한 SFT + LoRA 파인튜닝 (도메인 특화)
    ↓
[4단계] 서비스 상용화를 위한 추론 최적화 (양자화 등)
```
#### **1단계: 오픈소스 Base / Instruct 모델 선택**
- 허깅페이스 등에서 이미 **CLM 사전 학습과 기본 SFT가 끝난 오픈소스 SLLM**(`Qwen-7B-Instruct`, `Llama-3-8B-Instruct` 등)을 사내 서버로 다운로드합니다.
- 이미 기본적인 한국어/영어 대화 및 일반 지식 파악 능력이 탑재되어 있습니다.
#### **2단계: 보안 강화를 위한 내부망 RAG 우선 구축**
- 사내 보안 문서(PDF, DB 등)를 벡터화(Embedding)하여 사내 서버에 구축합니다. (이때 검색기 역할로 MLM 기반 임베딩 모델 활용)
- SLLM이 사용자의 질문을 받으면 사내 DB에서 관련 정보를 검색해 와서 답변하도록 **오픈북 시스템**을 먼저 만듭니다.
#### **3단계: SFT + LoRA를 활용한 도메인 파인튜닝 (필요시)**
- RAG를 붙였음에도 **사내 전문 용어를 잘 못 알아듣거나, 사내 보고서 서식을 지키지 못하는 문제**가 발생할 때 진행합니다.
- 사내 전용 `[업무 질문 - 양식에 맞춘 정답]` 데이터셋을 작성합니다.
- GPU 비용을 절감하기 위해 **PEFT 기법인 LoRA를 적용하여 SFT를 실행**합니다.
#### **4단계: 추론 최적화 (Inference Optimization) 및 서비스 배포**
- 완성된 SLLM을 실제 사내 직원들이 쓸 수 있도록 응답 속도를 높이고 GPU 비용을 줄입니다.
- **양자화(Quantization, FP16 \$\\rightarrow\$ INT4/INT8)** 적용 및 **vLLM** 같은 고성능 추론 엔진을 붙여 폐쇄망 서비스를 가동합니다.
---
### sLLM 및 PEFT 트렌드 (1/4)
- sLLM 및 PEFT와 관련된 학계·업계·현장의 최신 동향을 다룬다.
- Day1이 "왜 sLLM을 선택하는가(What)"였다면, Day2는 "현장에서 어떻게 구현하는가(How)"를 다룬다.
- 파라미터 학습 기법과 맥락 압축 기법이 각각 어떻게 발전해왔는지는 다음 슬라이드에서 살펴본다.
---
### 연구 동향 - 성능·효율 향상의 3가지 축 (2/4)
sLLM의 성능과 효율은 서로 다른 3가지 축에서 동시에 발전해왔다.
#### 축 1 · 모델 성능 향상 (파라미터 튜닝/학습)
- Adapter (2019): 레이어 사이에 소형 모듈 삽입
- LoRA (2021): 저랭크 행렬로 가중치 변화량만 학습
- QLoRA (2023): 4비트 양자화 + LoRA 결합
- DoRA (2024): 크기·방향 분해로 표현력 개선
#### 축 2 · Context & Reasoning (추론 및 컨텍스트 처리)
- Retrieval 기반 압축: 관련 문서만 선별해 길이 축소
- Prompt Compression (LLMLingua 계열)
- 요약 기반 컨텍스트 압축
- Long-Context 모델 자체 확장 (예: 128K 토큰급)
#### 축 3 · 추론 효율화 (Inference Optimization)
- Quantization: 가중치 정밀도 축소(INT8/INT4)
- MoE: 필요한 Expert만 선택적으로 연산
- Speculative Decoding: Draft 모델로 생성 가속
- KV Cache 최적화: 반복 연산 재사용·경량화
---
### 핵심 통찰 - 기법 선택이 성능을 좌우한다 (3/4)
- 동일한 Open Weight sLLM을 선택하고 동일하게 추가 학습·Fine-Tuning을 적용하더라도, 결과 성능은 팀마다 크게 달라진다.
- 차이를 만드는 것은 모델 자체가 아니라 다음 세 가지에 대한 방법론이다.
	- 어떤 파라미터를 얼마나 학습시키는지
	- 맥락을 어떻게 이해시키는지(Context & Reasoning)
	- 얼마나 효율적으로 추론하는지(Inference Optimization)
- 즉, sLLM 구축의 성패는 모델 선택보다 학습·압축 기법의 설계 역량에 달려 있다.
- 이 통찰이 Day2 전체를 관통하는 전제이며, 이후 모든 내용은 "무엇을 쓸까"가 아니라 "어떻게 다룰까"에 초점을 둔다.
---
### Day2 실전 흐름 미리보기 (4/4)
`기법 선택가이드` → `시나리오 도출` → `서비스 설계` → `서비스 구현` → `PEFT 응용실습`
- RAG와 Fine-Tuning의 경계를 먼저 명확히 하고(선택가이드), 이를 결합한 상용 수준 시나리오를 설계한다(시나리오 도출).
- Qwen2.5-1.5B + BGE-M3를 기준으로 서비스 아키텍처를 설계·구현하며, 이 과정에서 필요한 맥락압축/파라미터 학습 코드 모듈을 직접 다룬다.
- 마지막 PEFT 응용실습에서 전체 파이프라인을 조립하고 배포까지 진행한다.
---
### sLLM 목적별 PEFT기법 선택 가이드 (1/5)
- 목적(도메인 특화 지식 주입, 극소 파라미터 사용, 추론 능력 강화)별로 PEFT 기법을 선택하는 기준을 다룬다.
- 도메인 지식 주입은 RAG/벡터DB 파이프라인과는 명확히 구분되는 작업이다 - 다음 슬라이드에서 비교표로 정리한다.
- 동일 목적(내부보안/도메인버티컬)이라도 선택한 모델 특성에 따라 필요한 후처리 수준이 달라진다.
---
### 도메인 지식 주입의 두 갈래 - RAG/벡터DB vs Fine Tuning (2/5)
| 구분 | RAG / 벡터DB 파이프라인 | Fine-Tuning (파라미터 학습) |
| --- | --- | --- |
| 지식 저장 위치 | 외부 벡터DB (런타임에 검색) | 모델 파라미터 내부 (학습 시 내재화) |
| 지식 최신성 반영 | 문서만 갱신하면 즉시 반영 | 재학습해야 반영 (비용·시간 소요) |
| 작동 방식 | 검색된 근거 문서를 컨텍스트로 제공 | 모델 자체의 이해·응답 능력이 향상 |
| 목적 | 사실 검색, 근거 제시, 최신 정보 반영 | 정확성·성능 자체의 근본적 향상 |
| 한계 | 검색 품질에 성능이 좌우됨 | 재학습 비용, 과적합 위험 |
| 관계 | 상호 배타적이지 않음 | RAG + Fine-Tuned 모델 결합 가능 |
---
### 목적별 파이프라인·임베딩·기법 선택 가이드 (3/5)
| 목적 | 파이프라인 특성 | 임베딩 선택 | 적합 PEFT 기법 |
| --- | --- | --- | --- |
| 내부 보안 (문서 유출 방지) | 완전 내부 RAG 파이프라인 | 다국어 임베딩 (BGE-M3) | Prompt/Prefix Tuning |
| 도메인 버티컬 (전문지식 심화) | Fine-Tuning 중심 파이프라인 | 도메인 특화 임베딩 | LoRA / QLoRA |
| 두 목적 결합 (내부+전문화) | RAG + Fine-Tuned 모델 결합 | 다국어+도메인 하이브리드 | LoRA + Prompt Tuning 병행 |
---
### 목적별 sLLM·임베딩 선택 다양성 (4/5)
| 목적/환경 | sLLM 선택 예시 | 임베딩 선택 예시 |
| --- | --- | --- |
| 다국어 범용 (한국어 포함) | Qwen2.5-1.5B-Instruct (3B\~7B 확장 가능) | BGE-M3 (Dense·Sparse·Multi-Vector) |
| 한국어 특화 강화 | EXAONE 3.5 2.4B (LG AI Research, 한/영 균형 vocab) | BGE-M3 또는 한국어 특화 임베딩 |
| On-Device 극경량 | Qwen2.5-0.5B/1.5B급 경량 모델 | 경량 Dense 임베딩 위주 |
이번 과정은 Qwen2.5-1.5B + BGE-M3 조합을 기준으로 진행한다. 학습 파라미터를 3B\~7B로 올려도 동일한 코드 구조를 그대로 활용할 수 있도록 설계된 조합이다.
---
### 실전 시행착오별 노하우 (5/5)
- RAG만으로 해결하려다 실패하는 경우: 근거 문서가 없는 질문(추론·판단이 필요한 질문)에는 RAG가 근본적으로 취약하다.
- Fine Tuning만으로 해결하려다 실패하는 경우: 최신 정보나 자주 바뀌는 규정은 재학습 주기가 못 따라간다.
- 임베딩 모델과 sLLM의 언어 커버리지 불일치: 임베딩은 다국어인데 sLLM이 한국어에 약하면 검색은 잘 되어도 답변 품질이 떨어진다.
- 처음부터 완벽한 파이프라인을 설계하려 하지 말고, 작은 시나리오로 시작해 RAG/Fine-Tuning 비중을 점진적으로 조정하는 것이 현장에서 검증된 접근이다.
---
### PEFT 시나리오 도출 (1/4)
- sLLM 목적별 PEFT 시나리오를 도출하고, 시나리오 간 차이점을 이해한다.
- 맥락 압축과 파라미터 Fine-Tuning을 결합하면 기존과는 다른 레벨의 상용 sLLM을 구축할 수 있다.
- 이 결합 구조와 시나리오 도출 프레임워크는 다음 슬라이드에서 다룬다.
---
### 새로운 레벨의 sLLM 상용 구축 - 맥락압축 + 파인튜닝 결합 (2/4)
#### 기존 방식 (RAG 기반 확장)
- RAG(벡터DB 검색)만 적용: 근거 문서를 그대로 컨텍스트에 삽입하고, 모델 자체는 변경하지 않음
#### 새로운 레벨 (LLM 연구 확장)
- 맥락 정보를 압축해 효율적으로 제시
- 파라미터 Fine-Tuning으로 모델 자체의 이해도를 함께 끌어올림
동일한 Open Weight sLLM이라도, 맥락을 어떻게 압축해 제시하고 파라미터를 어떻게 학습시키느냐에 따라 결과 수준이 완전히 달라진다. 이것이 "상용 수준"과 "데모 수준"을 가르는 지점이다.
---
### 시나리오 도출 프레임워크 (3/4)
1. 목적 정의: 내부 보안 / 도메인 버티컬 / 두 목적 결합 중 무엇을 우선할지 명확히 함
2. 데이터 확보: 도메인 문서(RAG용)와 학습 데이터(Fine-Tuning용)를 구분해 수집
3. 기법 선택 (압축·파인튜닝 비중 결정): 맥락압축 위주로 갈지, 파라미터 학습 비중을 높일지 목적에 맞게 배분
4. 검증 기준 설정: 정확도·응답속도·비용 등 무엇을 기준으로 성공을 판단할지 사전 정의
---
### 실전 시나리오 예시 - Qwen2.5-1.5B 기준 도메인 버티컬 구축 (4/4)
| 항목 | 내용 |
| --- | --- |
| 목적 | 사내 계약서 검토 보조 sLLM 구축 (법무 도메인 버티컬) |
| 데이터 | 계약서 조항 요약 데이터 + 계약 유형별 위험조항 판례 요약 |
| 기법 배분 | 맥락압축(긴 계약서 요약 후 제시) 60% + LoRA Fine-Tuning(법무 용어·판단기준 주입) 40% |
| 검증 기준 | 위험조항 탐지 정확도, 응답 근거 제시 여부, 평균 응답 지연시간 |
---
### sLLM 서비스 설계 (1/4)
- sLLM 서비스 파이프라인과 임베딩 알고리즘의 연결 구조, 벡터DB 선정 및 설계를 다룬다.
- 실습 기준 모델: Qwen2.5-1.5B-Instruct + BGE-M3 임베딩 - 아키텍처는 다음 슬라이드에서 상세히 다룬다.
- 한국어 환경에 특화된 대안 모델(EXAONE 3.5)도 함께 소개한다.
---
### 서비스 파이프라인 아키텍처 - Qwen2.5-1.5B + BGE-M3 (2/4)
`사용자 질의` → `BGE-M3 임베딩` → `벡터DB 검색` → `맥락 압축` → `Qwen2.5-1.5B (LoRA 적용)` → `응답`
- 질의를 BGE-M3로 임베딩한 뒤 벡터DB에서 관련 문서를 검색한다(Dense+Sparse 하이브리드 가능).
- 검색된 문서는 그대로 넣지 않고 맥락 압축을 거쳐 핵심만 추려 Qwen2.5-1.5B에 전달한다.
- Qwen2.5-1.5B는 LoRA로 도메인 지식이 주입된 상태로 최종 응답을 생성한다.
- 이 구조는 RAG(검색)와 Fine-Tuning(파라미터 학습)이 함께 작동하는 결합형 파이프라인이다.
---
### 한국어 특화 대안 모델 - EXAONE 3.5 (3/4)
| 비교 항목 | Qwen2.5-1.5B-Instruct | EXAONE 3.5 (2.4B\~) |
| --- | --- | --- |
| 개발사 | Alibaba (Qwen Team) | LG AI Research |
| 파라미터 규모 | 1.5B (3B\~7B 확장 가능) | 2.4B / 7.8B / 32B |
| 언어 구성 | 29개 이상 언어 (다국어 범용) | 한국어·영어 약 50:50 균형 Vocabulary |
| 강점 | 폭넓은 다국어 지원, 활발한 생태계 | 한국어 실사용 벤치마크에서 동급 대비 우수 |
| 컨텍스트 길이 | 최대 128K (통상 32K) | 최대 32K |
한국어 응답 비중이 특히 높은 서비스라면 EXAONE 3.5를, 다국어 확장성과 생태계 크기를 우선한다면 Qwen2.5 계열을 검토한다.
---
### 벡터DB 선정 기준 (4/4)
- 완전 내부 운용 필요 여부: 사내 인프라에 직접 설치 가능한 오픈소스 벡터DB인지 확인
- 하이브리드 검색 지원 여부: BGE-M3의 Dense+Sparse 결과를 함께 활용할 수 있는지
- 메타데이터 필터링 성능: 부서/문서유형 등 조건별 검색이 얼마나 유연한지
- 운영 복잡도: 소규모 PoC 단계에서는 가벼운 임베디드형, 상용 확장 단계에서는 분산 클러스터형 검토
---
### sLLM 서비스 구현 (1/5)
- sLLM 서비스 파이프라인 구현, 벡터DB 연동, 기본 성능 튜닝을 다룬다.
- 상용 LLM은 벤더가 이미 상당한 후처리(정확성·안전성 강화)를 적용해 제공하지만, sLLM은 이를 사용자가 직접 구현해야 한다.
- 이를 위해 필요한 Fine-Tuning 카테고리와 실무에서 자주 쓰이는 코드 모듈은 다음 슬라이드에서 다룬다.
---
### Fine-Tuning이 필요한 카테고리 정리 (2/5)
| 카테고리 | 상용 LLM은 이미 처리한 부분 | sLLM에서 직접 다뤄야 할 기법 |
| --- | --- | --- |
| 정확성 향상 | 도메인 용어·사실 관계 오류 감소 | LoRA / QLoRA (파라미터 학습) |
| 맥락 활용 효율 | 긴 문서를 이해하고 핵심만 반영 | Prompt Compression / 요약 압축 |
| 응답 스타일 정렬 | 사내 톤·형식에 맞는 응답 생성 | Instruction Tuning |
| 안전성/정책 준수 | 금지 주제 회피, 민감정보 마스킹 | 규칙 기반 후처리 + 소규모 Fine-Tuning |
---
### 맥락 정보 압축 기법 코드 모듈 (3/5)
Qwen2.5-1.5B를 로드하고 텍스트를 생성하는 공통 코드 구조다. GPU(CUDA) 환경과 CPU(Mac/Windows) 환경을 분기 처리한다.
```python
# pip install -U torch transformers accelerate pypdf python-docx
import os
import torch
from pypdf import PdfReader
from docx import Document
from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM

# 1. Qwen2.5-1.5B 로드
MODEL_NAME = "Qwen/Qwen2.5-1.5B"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# GPU(CUDA) 환경
# model = AutoModelForCausalLM.from_pretrained(
#     MODEL_NAME,
#     torch_dtype=torch.float16,
#     device_map="auto",
# )

# CPU 환경 (Mac / Windows 공통)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float32,
)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token
model.config.pad_token_id = tokenizer.pad_token_id
```
이어서 공통 생성 함수를 정의한다. 실제 `compress_context()`, RAG 검색, FastAPI 엔드포인트로 이어지는 전체 구현은 "PEFT 응용 실습"에서 `sllm_service` 패키지의 실제 코드로 다룬다.
```python
# 2. 공통 생성 함수
def generate_text(prompt, max_new_tokens=512):
    inputs = tokenizer(
        prompt, return_tensors="pt",
        truncation=True, max_length=2048,
    )
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False, use_cache=True,
            pad_token_id=tokenizer.pad_token_id,
            eos_token_id=tokenizer.eos_token_id,
        )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
```
---
### Context & Reasoning 추가 예제 - Long-Context 처리 (YaRN)
검색 없이 문서 전체를 그대로 입력에 넣는 Long-Context 방식으로, RAG/Context Compression과는 다른 트레이드오프를 가진다.
```python
# pip install -U torch transformers accelerate
from transformers import AutoConfig, AutoTokenizer, AutoModelForCausalLM

# Long Context 확장 설정 (YaRN)
MODEL_NAME = "Qwen/Qwen2.5-1.5B-Instruct"
config = AutoConfig.from_pretrained(MODEL_NAME)

# 기본 32K context를 약 4배 확장하는 예시
# 실제 안정성은 모델/transformers 버전에 따라 달라질 수 있음
config.rope_scaling = {
    "rope_type": "yarn",
    "factor": 4.0,
    "original_max_position_embeddings": 32768,
}

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME, config=config, torch_dtype=torch.float32,
)
```
---
### 파라미터 학습 기법(QLoRA) 코드 모듈 (4/5)
QLoRA 전체 학습 코드는 이미 Day1 실습(`scripts/train_lora.py`)에서 다뤘다. CUDA 환경에서 `USE_QLORA=True`(기본값)이면 자동으로 아래 4bit NF4 양자화 로딩으로 분기한다.
```python
from transformers import BitsAndBytesConfig
from peft import prepare_model_for_kbit_training

quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    quantization_config=quantization_config,
    device_map="auto",
)
model = prepare_model_for_kbit_training(model)

# 이후 LoRA Config·SFTTrainer 적용은 train_lora.py #2,#3과 동일
```
---
### SOTA 패턴 & 연구 동향 정리표 (5/5)
| 기법 | 핵심 아이디어 | 현장 적용 상황 |
| --- | --- | --- |
| QLoRA | 4비트 양자화 + LoRA | 메모리 제약 환경에서 대형 모델 파인튜닝 |
| DoRA | 가중치 크기·방향 분리 학습 | LoRA보다 높은 표현력이 필요한 경우 |
| Prompt Compression | 중요도 기반 토큰 제거 | 긴 문서를 짧은 컨텍스트로 압축 |
| Instruction Tuning | 지시-응답 쌍 학습 | 응답 스타일·형식을 사내 기준에 정렬 |
---
### 추론 효율화 (Inference Optimization) (1/6)
- LLM 자체의 연산·구조를 최적화해 추론 속도와 서빙 비용을 개선하는 작업이다.
- 파라미터 튜닝(모델 성능 향상)이나 Context & Reasoning(맥락 처리)과는 다른 층위로, "어떻게 더 빠르고 싸게 실행하는가"의 문제다.
- 대표 기법: Quantization, MoE(Mixture of Experts), Speculative Decoding, KV Cache 최적화
---
### 성능·효율 최적화의 3가지 축 - 전체 프레임워크 (2/6)
| 기준 축 | 핵심 질문 | 대표 기법 |
| --- | --- | --- |
| ① 모델 성능 향상 (파라미터 튜닝/학습) | 정확성을 어떻게 높이는가? | LoRA, QLoRA, DoRA |
| ② Context & Reasoning (추론 및 컨텍스트 처리) | 맥락을 어떻게 이해시키는가? | Prompt Compression, RAG, Long-Context |
| ③ 추론 효율화 (Inference Optimization) | 어떻게 더 성능을 높이고 자원 비용 절감을 할 수 있는가? | Quantization, MoE, Speculative Decoding, KV Cache |
세 축은 서로 배타적이지 않고 함께 적용된다. 실전에서는 LoRA(①) + 맥락압축(②) + Quantization(③)을 동시에 조합하는 경우가 많다.
---
### Quantization - 모델 경량화 (3/6)
- 가중치·활성값의 정밀도를 FP16/FP32에서 INT8/INT4 등으로 낮춰 메모리 사용량과 연산량을 줄이는 기법이다.
- PTQ(Post-Training Quantization): 학습 후 양자화하며, 적용이 간단하지만 정확도 손실이 있을 수 있다.
- QAT(Quantization-Aware Training): 학습 과정에 양자화를 반영해 정확도 손실을 최소화한다.
| 정밀도 | 메모리 사용량 | 추론 속도 | 정확도 영향 |
| --- | --- | --- | --- |
| FP16 | 기준(100%) | 기준(1x) | 정확도 손실 없음 |
| INT8 | 약 50% | 약 1.5\~2x | 경미한 손실 |
| INT4 (예: GPTQ, AWQ) | 약 25% | 약 2\~3x | 미세 조정 없이는 손실 발생 가능 |
---
### MoE (Mixture of Experts) - 선택적 연산 구조 (4/6)
입력마다 전체 파라미터가 아닌 일부 Expert만 활성화하는 구조다.
`입력 토큰` → `Router(게이팅)` → 일부 Expert만 선택되어 연산
- Router가 입력 특성에 맞는 소수의 Expert만 선택해 연산한다 - 전체 파라미터는 크지만 실제 활성화되는 파라미터는 일부다.
- 대형 모델 수준의 표현력을 유지하면서도 추론 시 연산량은 훨씬 적게 유지할 수 있다.
- 최근 open-weight LLM/sLLM 계열에서 MoE 구조 채택이 늘어나는 추세다.
---
### Speculative Decoding - 추론 속도 가속 (5/6)
`Draft 모델이 여러 토큰 예측` → `Target 모델이 한 번에 검증` → `일치 토큰 일괄 채택` → `불일치 지점부터 재생성`
- 작고 빠른 Draft 모델이 다음 여러 토큰을 미리 순차적으로 예측한다(저비용 추론).
- 크고 정확한 Target 모델(예: Qwen2.5-1.5B)이 이 후보들을 한 번의 순전파로 병렬 검증한다.
- 검증을 통과한 토큰은 그대로 채택해 여러 토큰을 한 번에 생성한 효과를 얻는다 - 최종 출력 품질은 Target 모델 기준으로 유지된다.
- 불일치가 발생한 지점부터는 Target 모델이 다시 생성해 정확성을 보장한다.
---
### KV Cache 최적화 - 메모리 효율적 추론 (6/6)
- Transformer는 매 토큰 생성 시 이전 토큰들의 Key/Value를 다시 계산하지 않도록 캐시(KV Cache)에 저장해 재사용한다.
- 하지만 시퀀스가 길어질수록 캐시 크기가 선형으로 증가해 메모리 병목이 발생한다.
| 기법 | 핵심 아이디어 | 적합한 상황 |
| --- | --- | --- |
| PagedAttention | 캐시를 페이지 단위로 관리해 메모리 단편화 최소화 | 긴 대화/다중 요청 동시 처리 서빙 |
| Multi-Query Attention (MQA) | 여러 Query가 Key/Value 공유, 캐시 크기 축소 | 메모리 제약이 큰 On-Device 환경 |
| Grouped-Query Attention (GQA) | MQA와 기존 방식의 절충 - 그룹 단위 KV 공유 | Qwen2.5 등 최근 sLLM에서 채택 |
---
### PEFT 응용 실습 (1/4)
#### STEP 1 · 서비스 구현 및 PEFT 적용
- Qwen2.5-1.5B-Instruct + BGE-M3 기반 서비스 파이프라인 구현
- 목적에 맞는 PEFT 기법(LoRA 등) 적용
- 적용 전/후 응답 품질 비교
#### STEP 2 · sLLM 서빙 배포
- 튜닝된 모델을 서빙 환경에 배포
- 기본 성능(지연시간/처리량) 점검
- 실서비스 관점의 체크리스트 점검
---
### 실습 시나리오 최종 정의 (2/4)
| 항목 | 내용 |
| --- | --- |
| 목표 | Qwen2.5-1.5B-Instruct + BGE-M3 + hr-qwen-lora로 HR 문서 기반 Q&A 서비스 완성 |
| 기법 구성 | sllm_service 패키지: RAG 검색 + Context Compression + LoRA 자동 로딩 통합 |
| 배포 목표 | FastAPI로 서빙하며, Day1에서 학습한 hr-qwen-lora가 자동으로 연결되는지 확인 |
#### 실습 진행 순서
1. Day1 결과물 연결: `scripts`로 만든 `hr-qwen-lora` Adapter를 `sllm_service`가 자동 감지
2. 파이프라인 조립: `config.py` → `runtime.py` → `routers/services` 흐름을 실제 코드로 확인
3. 실행 및 테스트: `uvicorn`으로 서비스 실행 후 Swagger에서 통합 질의 테스트
---
### 실습 코드 - 파이프라인 조립 (3/4)
RAG는 문서를 찾고, Context Compression은 찾은 문서를 줄이고, LoRA/QLoRA 모델은 도메인에 맞는 방식으로 답변한다.
`사용자 질문` → `RAG 검색(선택)` → `Context Compression` → `Long Context` → `LoRA/QLoRA 적용 Qwen2.5-1.5B` → `Inference Optimization(4bit Quantization)` → `최종 답변 생성` → `FastAPI 서빙`
| 코드 단계 | 관련 기술 | 설명 |
| --- | --- | --- |
| bge_m3.encode() | Retrieval Embedding | 질문을 벡터로 변환 |
| vector_[db.search](http://db.search)() | RAG / Vector Search | 관련 문서 검색 (선택 기능) |
| compress_context() | Context Compression | 검색 결과 또는 원문을 LLM 처리 쉬운 맥락으로 압축 |
| Long Context | Long Context | 긴 문서 압축 없이 그대로 입력 |
| LoRA / QLoRA | Parameter Tuning | 도메인 특화 성능 향상 |
| 4bit Quantization (GPU 필요) | Inference Optimization | GPU 메모리 절감 및 추론 효율 향상 |
| qwen_model.generate() | LLM Generation | 최종 자연어 생성 |
| FastAPI Endpoint | Serving System | 외부 서비스 제공 |
---
### 실습 코드 - 파이프라인 조립 (Skeleton #1)
```python
# LLM Application Pipeline Skeleton
def answer_query(
    user_query: str,
    mode: str = "compression",   # long_context | compression
    use_rag: bool = False,
) -> str:
    # 1. Retrieval Embedding (선택)
    retrieved_docs = None
    if use_rag:
        q_emb = bge_m3.encode(
            user_query, normalize_embeddings=True,
        )
        # 2. Vector Search (선택)
        retrieved_docs = vector_db.search(
            q_emb,
            top_k=5,
        )
    # 3. Context Engineering
    if mode == "compression":
        context = compress_context(
            docs=retrieved_docs, model=qwen_model, max_tokens=500,
        )
    elif mode == "long_context":
        context = build_long_context(
            docs=retrieved_docs,
        )
    else:
        raise ValueError("Unknown Context Mode")
```
---
### sllm_service 패키지 내부 구조
```javascript
sllm_service/
├── app.py                     FastAPI 생성 + Router 조립
├── config.py                  모델명·경로·환경변수 설정
├── runtime.py                 모델·임베딩 로딩, LoRA 자동 연결
├── state.py                   문서/벡터 인덱스 메모리 상태
├── schemas.py                 요청 데이터 형식(Pydantic)
│
├── services/                  비즈니스 로직
│   ├── generation_service.py  Prompt 구성·생성
│   ├── document_service.py    문서 Chunk·Embedding
│   ├── rag_service.py         Top-K 검색
│   └── vector_service.py      벡터 인덱스 추상화
│
└── routers/                   HTTP API 경로
    ├── system_router.py       Health Check
    ├── document_router.py     업로드·Chunk 조회
    ├── rag_router.py          RAG·압축·Long Context
    └── inference_router.py    추론 최적화·통합 Pipeline
```
---
### 실습 코드 - [app.py](http://app.py) (FastAPI 앱 조립)
```python
# sllm_service/app.py
from fastapi import FastAPI
from sllm_service.config import settings
from sllm_service.routers.document_router import router as document_router
from sllm_service.routers.inference_router import router as inference_router
from sllm_service.routers.rag_router import router as rag_router
from sllm_service.routers.system_router import router as system_router

def create_app() -> FastAPI:
    application = FastAPI(
        title=settings.app_title,
        version=settings.app_version,
    )
    application.include_router(system_router)
    application.include_router(document_router)
    application.include_router(rag_router)
    application.include_router(inference_router)
    return application

app = create_app()

# 실행: python -m uvicorn sllm_service.app:app --port 8080
```
---
### 실습 코드 - [config.py](http://config.py) #1 (기본 설정)
```python
# sllm_service/config.py
@dataclass(frozen=True)
class Settings:
    app_title: str = os.getenv("APP_TITLE", "sLLM-service")
    app_version: str = os.getenv("APP_VERSION", "1.3.0")

    model_name: str = os.getenv(
        "MODEL_NAME", "Qwen/Qwen2.5-1.5B-Instruct",
    )
    embedding_model_name: str = os.getenv(
        "EMBEDDING_MODEL_NAME", "BAAI/bge-m3",
    )

    max_input_tokens: int = parse_int_env("MAX_INPUT_TOKENS", 8192)
    chunk_size: int = parse_int_env("CHUNK_SIZE", 1000)

    # CUDA에서만 bitsandbytes 4bit NF4 적용, MPS/CPU는 자동 분기
    use_4bit: bool = parse_bool_env("USE_4BIT", default=True)

    # Qwen·BGE-M3를 모두 MPS에 올리면 메모리 부담이 커서
    # 임베딩 모델은 기본적으로 CPU 사용
    embedding_device: str = os.getenv("EMBEDDING_DEVICE", "cpu")
```
---
### 실습 코드 - [config.py](http://config.py) #2 (LoRA 선택 정책)
```python
# auto: Adapter 있으면 LoRA, 없으면 Base
# base: Adapter 있어도 Base 강제 사용  /  lora: Adapter 필수
model_variant: ModelVariant = parse_model_variant_env(
    "MODEL_VARIANT", default="auto",
)

# 기본 경로: models/hr-qwen-lora/ (Day1 학습 결과)
lora_adapter_path: Path = parse_path_env(
    "LORA_ADAPTER_PATH",
    default=PROJECT_ROOT / "models" / "hr-qwen-lora",
)

lora_adapter_name: str = os.getenv(
    "LORA_ADAPTER_NAME", "hr-assistant",
)

# False 권장: Base + PEFT Adapter 형태 유지 (병합 X)
merge_lora_adapter: bool = parse_bool_env(
    "MERGE_LORA_ADAPTER", default=False,
)

# True면 Adapter가 불완전할 때 서버 기동을 실패시킴
# 초급 실습에서는 False 권장 (자동으로 Base로 대체)
strict_lora_loading: bool = parse_bool_env(
    "STRICT_LORA_LOADING", default=False)
```
---
### 실습 코드 - [runtime.py](http://runtime.py) #1 (환경별 Base 모델 로딩)
```python
# sllm_service/runtime.py
def load_base_qwen_model(has_cuda, has_mps):
    if has_cuda and settings.use_4bit:
        quantization_config = BitsAndBytesConfig(
            load_in_4bit=True, bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.float16,
        )
        model = AutoModelForCausalLM.from_pretrained(
            settings.model_name,
            quantization_config=quantization_config, device_map="auto",
        )
        return model, model.device, "4bit NF4 CUDA"
    if has_cuda:
        model = AutoModelForCausalLM.from_pretrained(
            settings.model_name, dtype=torch.float16,
        ).to("cuda:0")
        return model, torch.device("cuda:0"), "FP16 CUDA"
    if has_mps:
        model = AutoModelForCausalLM.from_pretrained(
            settings.model_name, dtype=torch.float16,
        ).to("mps")
        return model, torch.device("mps"), "FP16 Apple MPS"
    # CUDA/MPS 모두 없으면 CPU FP32
    model = AutoModelForCausalLM.from_pretrained(
        settings.model_name, dtype=torch.float32,).to("cpu")
    return model, torch.device("cpu"), "FP32 CPU"
```
---
### 실습 코드 - [runtime.py](http://runtime.py) #2 (LoRA 자동 감지·연결)
```python
# 정상 Adapter 조건: adapter_config.json +
# adapter_model.safetensors(또는 .bin) 존재
def inspect_lora_adapter(adapter_path):
    if not adapter_path.is_dir():
        return False, "Adapter directory not found"
    config_ok = (adapter_path / "adapter_config.json").is_file()
    weight_ok = any(
        (adapter_path / name).is_file()
        for name in ("adapter_model.safetensors", "adapter_model.bin")
    )
    return (config_ok and weight_ok), None

def decide_lora_usage(adapter_path):
    available, _ = inspect_lora_adapter(adapter_path)
    if settings.model_variant == "base":
        return False, available
    if settings.model_variant == "lora":
        if not available:
            raise FileNotFoundError("정상 LoRA Adapter가 필요합니다.")
        return True, True
    # auto: Day1에서 hr-qwen-lora를 학습해 두면 자동으로 감지되어
    # Fine-tuned 모델이 응답한다. 없으면 Base 모델로 대체된다.
    return available, available
```
---
### 실습 코드 - [schemas.py](http://schemas.py) & [state.py](http://state.py)
```python
# sllm_service/schemas.py
class QueryRequest(BaseModel):
    document_id: str
    question: str
    top_k: int = Field(5, ge=1, le=20)
    max_new_tokens: int = Field(256, ge=32, le=1024)

class PipelineRequest(BaseModel):
    document_id: str
    question: str
    mode: Literal["rag","compression","long_context"] = "compression"
    use_rag: bool = True
    top_k: int = Field(5, ge=1, le=20)
    max_new_tokens: int = Field(256, ge=32, le=1024)

# sllm_service/state.py
# 업로드한 문서와 벡터 인덱스를 저장하는 런타임 상태
documents: dict[str, dict] = {}
vector_indexes: dict[str, object] = {}
# Mac: NumPy 인덱스 / Colab·Linux: FAISS 인덱스 - 타입에 의존하지 않음
```
---
### 실습 코드 - services / routers 역할 정리
```python
# services/  (비즈니스 로직)
generation_service.py   Prompt 구성 + Qwen 텍스트 생성
document_service.py     문서 읽기·Chunk 분할·Embedding 등록
rag_service.py          질문 Embedding + Top-K Chunk 검색
vector_service.py       Mac NumPy / Colab FAISS 검색 추상화

# routers/  (HTTP API)
system_router.py        루트 API + Health Check
document_router.py      샘플 로드·파일 업로드·Chunk 조회
rag_router.py           RAG · Compression · Long Context API
inference_router.py     추론 최적화 테스트 + 통합 Pipeline

# app.py는 이 4개 router를 include_router()로 조립만 하고,
# 실제 로직은 모두 services/ 아래에 있다.
```
---
### 실습 코드 - 실행 및 통합 테스트
```bash
# 1) 서비스 실행
python -m uvicorn sllm_service.app:app --host 127.0.0.1 --port 8080

# 2) Swagger UI 접속
http://127.0.0.1:8080/docs

# 3) 통합 Pipeline 테스트
POST /pipeline
{
  "document_id": "샘플 로드 후 받은 id",
  "question": "연차 신청은 어떻게 하나요?",
  "mode": "compression",
  "use_rag": true
}

# MODEL_VARIANT=auto 이면 models/hr-qwen-lora/가 있을 때
# Day1에서 학습한 Fine-tuned 모델이 자동으로 응답한다.
```
---
### 배포 체크리스트 (4/4)
- LoRA 적용 전/후 동일 질문 세트에 대한 응답을 비교해 개선을 확인했는가?
- 맥락 압축이 지나쳐 핵심 정보가 유실되지 않는지 샘플 검증을 거쳤는가?
- 평균 응답 지연시간이 서비스 요구 수준(예, 3초 이내)을 충족하는가?
- 예외 상황(검색 결과 없음, 토큰 초과 등)에 대한 처리 로직이 준비되었는가?
---
### Day 2 마무리 - 과정의 철학
sLLM은 도메인 기반 버티컬 지식 주입에 특화된 AI 서비스다.
동일한 LLM 기술이라도 파라미터를 어떻게 학습시키고(모델 성능 향상), 맥락을 어떻게 이해시키며(Context & Reasoning), 얼마나 효율적으로 실행하느냐(추론 효율화)에 따라 성능은 천차만별이다.
이 세 축을 함께 설계하는 작업이 곧 사용자에게 특화된 정확성과 성능을 갖춘 핵심 sLLM으로 거듭나게 하는 과정이다.
#### 그래서 이 성능을 지속적으로 유지하려면
`매번 사람이 직접 감시` → `Agentic AI가 자동 감지·대응` → `AIOps 체계로 연결`
사람이 매번 감시·재학습을 판단할 수는 없기 때문에, 향후 Agentic AI가 성능 저하를 스스로 감지하고 대응하며 AIOps 체계로 자연스럽게 연결된다. AIOps는 별도 과목에서 학습한다.
