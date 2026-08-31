---
title: "[STUDYING] 30. sLLM 구현 및 Fine Tunning_Day1_핵심 정리"
created: 2026-08-29
updated: 2026-09-01
type: blog-post
tags: ["blog", "technical-writing"]
category: "STUDYING"
published: 2026-08-28
source_url: https://ch010104.tistory.com/348
---
# [STUDYING] 30. sLLM 구현 및 Fine Tunning_Day1_핵심 정리

## 원문

https://ch010104.tistory.com/348

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

AI 서비스를 위한 LLM 서빙 파이프라인(Serving Pipeline)의 전체 구조를 다룸

처리 흐름: 요청 수신 → 전처리 → 모델 추론 → 후처리 → 응답 반환

## 원문 기반 개념 정리

### LLM 파이프라인 개요

AI 서비스를 위한 LLM 서빙 파이프라인(Serving Pipeline)의 전체 구조를 다룸

처리 흐름: 요청 수신 → 전처리 → 모델 추론 → 후처리 → 응답 반환

파이프라인을 외부/내부로 구분하는 이유는 이어지는 슬라이드에서 다룸

### 외부 파이프라인 vs 내부 파이프라인 - 왜 구분하는가

### 상용 LLM 내부망 구축의 한계

VPC·전용 인스턴스로 상용 LLM을 사내망에 배치해도, 모델의 학습 데이터 활용 정책은 벤더 정책에 의존함

계약상 "학습에 사용하지 않음"을 명시해도 기술적으로 완전히 감사·검증하기는 현실적으로 어려움

규제 산업(금융/의료/공공)은 이 불확실성 자체를 리스크로 간주해 완전 내부 격리를 요구하는 경우가 많음

### 내부 파이프라인 구성의 두 가지 목적

목적 1 · 데이터 주권 확보: 외부 전송이 원천적으로 불가능한 구조를 만들어, 계약이 아닌 아키텍처로 데이터 보안을 보증함

목적 2 · 도메인 버티컬 최적화: 특정 도메인 지식(법률/의료/사내 프로세스)을 연결해, 범용 LLM보다 좁지만 깊은 목적 성능을 확보함

범용 LLM은 넓지만 얕은 지식을 갖는 반면, 버티컬 sLLM은 좁지만 깊은 지식과 낮은 지연시간·비용을 함께 얻을 수 있음. 이 두 목적이 과정 전체 실습의 배경이 됨

### MLM vs CLM 이해

Masked Language Model(MLM) - 문맥 양방향 참조, 빈칸 채우기 방식 학습 (예: BERT 계열)

Causal Language Model(CLM) - 이전 토큰만 참조하는 단방향 순차 생성 학습 (예: GPT 계열)

Fine-Tuning 영역이 MLM보다 CLM을 주로 다루는 이유는 이어지는 슬라이드에서 다룸

### MLM vs CLM 구조 상세 비교

### 왜 Fine Tuning은 CLM 중심으로 이루어지는가

생성형 태스크의 다운스트림 다양성: 요약·대화·코드생성 등 서로 다른 태스크를 하나의 디코더 구조로 자연스럽게 대응 가능

Instruction-following 패러다임과의 정합성: "프롬프트 → 응답" 형태의 학습이 CLM의 다음 토큰 예측 구조와 직접적으로 일치

MLM 구조의 생성 한계: 양방향 마스킹 구조는 자유 생성에 부적합해 분류·추출 태스크에 국한되는 경향

산업 표준화: 최근 sLLM(Llama, Qwen, Gemma, Exaone 등)이 대부분 Decoder-only(CLM) 구조를 채택

상용 LLM인 ChatGPT, Gemini도 Decoder-only 계열임 (Claude는 내부 구조 비공개지만 Decoder-only 특성을 보유한다고 언급됨)

### 연구·산업 발전 동향 - BERT 시대에서 GPT 시대로

생성형 서비스 수요 증가, RLHF·Instruction Tuning 기법의 정립, Decoder-only 구조가 대규모 학습에 유리하다는 다수 연구 결과가 맞물리며 산업 전반이 CLM 중심으로 수렴함

### 상용 환경의 CLM Fine Tuning 기법 개요

사내 sLLM 파이프라인에서는 대규모 RLHF보다 Instruction Tuning + PEFT(LoRA) 조합이 비용·속도 면에서 실무적으로 가장 많이 사용됨

### LLM vs sLLM 비교

LLM 공통 기능 이해 - 토크나이저, 임베딩 알고리즘, 전처리/후처리 과정

sLLM 핵심 기능 도출 - 경량화 아키텍처, 양자화(Quantization), On-Device 추론

sLLM이 버티컬 도메인/내부 업무에 쓰이기 위해 갖춰야 할 특성은 이어지는 슬라이드에서 다룸

### 버티컬 도메인 sLLM이 갖춰야 할 특성

도메인 지식 반영도: 전문 용어·사내 프로세스·업무 맥락을 정확히 이해

추론 효율성: On-Device 또는 저비용 인프라에서도 충분히 빠른 응답

데이터 프라이버시: 민감 정보가 외부로 유출되지 않는 구조적 보장

최신성 유지 용이성: 낮은 재학습 비용으로 정책·지식 변경에 신속히 대응

안전한 출력 제어: 사내 정책·규정에 맞는 응답 범위 준수

### LLM vs sLLM 다차원 비교표

### Fine Tuning - sLLM 특성을 완성하는 핵심 다리

흐름: 기본 sLLM(경량·범용지식 얕음) → Fine-Tuning(도메인 데이터 주입) → 도메인 특화 sLLM(요구 특성 충족)

Fine-Tuning 없는 sLLM은 단지 '작은 모델'일 뿐, 실무에 쓸 수 있는 수준의 도메인 정확도를 보장하지 않음

Fine-Tuning을 통해 도메인 지식 주입, 응답 스타일 정렬, 사내 안전 정책 반영이 이루어져야 비로소 실무 적용이 가능해짐

앞서 정리한 sLLM의 요건(도메인 지식/프라이버시/최신성/안전성)은 Fine-Tuning을 통해 '완성'되는 특성임

### sLLM Use Case 실습

sLLM의 특징(경량성, 온디바이스, 데이터 보안성)을 활용한 Use Case 이해

상용 LLM을 쓰기 어려운 환경/사유는 이어지는 슬라이드에서 유형별로 정리

실제 구현 시나리오 중심으로 사내 문서 기반 sLLM Q&A 챗봇 사례를 다룸

### 상용 LLM 사용이 어려운 상황 유형

### 시나리오별 sLLM 활용 사례

### 구현 시나리오 상세 - 사내 문서 기반 sLLM Q&A 챗봇

1단계 · 문서 수집 및 청크 분할: 사내 규정·매뉴얼 문서를 의미 단위(청크)로 분할

2단계 · 임베딩 생성 및 벡터DB 저장: 임베딩 모델로 각 청크를 벡터화하여 벡터DB에 색인

3단계 · 질의 시 관련 문서 검색(RAG): 사용자 질의와 유사한 청크를 벡터DB에서 검색

4단계 · sLLM 추론 및 답변 생성: 검색된 문서를 컨텍스트로 제공해 sLLM이 최종 답변 생성

### Fine Tuning 전략

Fine Tuning 전략 이해 - Full Fine-Tuning과 PEFT의 차이

PEFT 주요 기법 - LoRA, Adapter, Prefix-Tuning, Prompt-Tuning

시나리오별 효과적인 기법과 예제 코드는 이어지는 슬라이드에서 다룸

### 시나리오별 적합 PEFT 기법 매핑

다음 두 슬라이드에서 LoRA와 Prompt Tuning의 실제 적용 코드를 PEFT 라이브러리 기준으로 살펴봄

### LoRA 적용 예제 코드 - 도메인 지식 주입

기존 모델 위에 LoRA Adapter를 붙인 후, 학습 시에 도메인 지식을 주입하는 구조

학습 데이터 흐름: 도메인 데이터 → Forward → Loss 계산 → Backpropagation → LoRA Weight 업데이트

```text
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model, TaskType

model = AutoModelForCausalLM.from_pretrained("internal-sllm-base")
tokenizer = AutoTokenizer.from_pretrained("internal-sllm-base")

lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=8,                  # rank: 낮을수록 경량, 높을수록 표현력 증가
    lora_alpha=16,         # 스케일링 계수
    lora_dropout=0.05,
    target_modules=["q_proj", "v_proj"],  # 어텐션 투영층에 적용
)
model = get_peft_model(model, lora_config)
model.print_trainable_parameters()
# 예: trainable params: 4.2M || all params: 1.3B || trainable%: 0.32%

SFTTrainer(
    model=model,
    train_dataset=domain_dataset, ...
)
```

r(rank)이 낮을수록 학습 파라미터가 적어 경량이지만 표현력은 낮아지고, 높을수록 반대의 트레이드오프가 발생함

target_modules로 어텐션의 q_proj, v_proj에만 어댑터를 적용해 전체 파라미터의 0.32%만 학습

### Prompt Tuning 예제 코드 - 극소 자원 환경

기본 모델 앞에 학습 가능한 virtual prompt embedding을 붙여, 도메인 지식이 모델 내부 가중치 전체가 아니라 입력 앞에 붙는 작은 Prompt Embedding 벡터에 학습됨

학습 데이터 흐름: 도메인 데이터 → Virtual Prompt + 사용자 입력 생성 → Forward → Loss 계산 → Backpropagation → Virtual Prompt Embedding 업데이트

```text
from peft import PromptTuningConfig, PromptTuningInit, get_peft_model

prompt_config = PromptTuningConfig(
    task_type="CAUSAL_LM",
    prompt_tuning_init=PromptTuningInit.TEXT,
    num_virtual_tokens=20,   # 학습되는 가상 토큰 개수 (매우 적음)
    prompt_tuning_init_text="다음 사내 문서를 바탕으로 정확하게 답변하라:",
    tokenizer_name_or_path="internal-sllm-base",
)

model = get_peft_model(base_model, prompt_config)
model.print_trainable_parameters()
# 예: trainable params: 20K || all params: 1.3B || trainable%: 0.0015%
# On-Device 환경처럼 저장·연산 자원이 극도로 제한적일 때 적합
```

LoRA(0.32%) 대비 학습 파라미터 비율이 훨씬 낮음(0.0015%) → 극소 자원 환경에 적합하지만 표현력은 더 제한적

### 다음 주제 예고 - 0. 프로젝트 구조 이해

전체 디렉토리 구조 한눈에 보기

코드를 읽는 순서 (데이터 → 학습 → 평가 → 서비스)

Instruction SFT vs Context-based QA SFT

PEFT 기초 실습으로 이동

### 개선 전 vs 개선 후 성능·정확도 비교 (예시)

위 수치는 교육 목적의 예시 값이며, 실제 프로젝트에서는 검증 데이터셋 기준으로 자체 측정한 정확도를 사용해야 함

### PEFT 기초 실습

### 실습 시나리오 정의 - 사내 FAQ 챗봇 LoRA 튜닝

실습 진행 순서

1단계 · FAQ 데이터 준비: 질문-답변 쌍을 Instruction 형식(질문/답변)으로 정리

2단계 · 모델·LoRA 설정: 베이스 sLLM 로드 후 LoRA Config 적용

3단계 · 학습 실행: 소량의 데이터로 빠르게 학습 후 결과 확인

4단계 · 결과 검증: 학습 전/후 동일 질문에 대한 응답 품질 비교

### 사내 FAQ 챗봇 실습의 전체 로드맵

모델 성능 향상 → Qwen2.5 + LoRA FAQ Fine Tuning (Day1)

Context & Reasoning → Qwen2.5 + FAISS RAG FAQ 검색 답변 (Day1) → 맥락 압축, 요약 후 답변, 긴 입력 정리, Self-refine (Day2)

Inference Optimization → Qwen2.5 4bit Quantization 추론 테스트 (Day1)

### 0. 프로젝트 구조 이해

### sllm-main 전체 프로젝트 구조 (데모용 포함 전체)

```text
sllm-main/
├── requirements.txt
├── readme.md
├── dataset/
│   ├── source/        원천 문서                  [데모 · 전처리용, 수업 범위 아님]
│   ├── training/      학습·검증 데이터              [실습 제공]
│   └── evaluation/    평가 데이터                  [실습 제공]
├── scripts/
│   ├── build_sft_dataset.py         데이터 분리    [데모 · 실습 X]
│   ├── build_training_dataset.py    데이터 생성    [데모 · 실습 X]
│   ├── train_lora.py                           [실습 제공]
│   └── evaluate_model.py                       [실습 제공]
├── models/hr-qwen-lora/   학습 결과               [실습 제공 · 빈 폴더]
├── outputs/                                     [실습 제공 · 빈 폴더]
├── vector_db/, run.ipynb                        [데모 · 수업 범위 아님]
└── sllm_service/, frontend/, app.py             [데모 · 수업 범위 아님]
```

이번 실습은 원천 문서의 수집·전처리가 아니라, 준비된 학습 데이터를 이용해 SFT를 수행하고 Base Model 대비 Fine-tuned Model의 성능 변화를 확인하는 것이 목적임

원천 데이터와 데이터 생성 과정은 실습 범위에서 제외하고, SFT에 바로 사용할 수 있도록 전처리된 Train/Validation/Evaluation 데이터를 제공함

### 실습 배포본 구조 (sllm-student/)

```text
sllm-student/
├── requirements.txt
├── dataset/
│   ├── training/
│   │   ├── hr_sft_train.jsonl
│   │   └── hr_sft_validation.jsonl
│   └── evaluation/
│       └── hr_eval.jsonl
├── scripts/
│   ├── train_lora.py
│   └── evaluate_model.py
├── models/hr-qwen-lora/     (처음에는 빈 폴더)
└── outputs/                 (처음에는 빈 폴더)
```

RAG 및 서빙(sllm_service/, frontend/, app.py)은 실습 제외 대상(수업 범위 아님)

RAG·서빙 코드는 별도 과목 영역이라 제공하지 않으며, 필요 시 구축된 URL로 데모를 접속하여 설명할 수 있음

### 코드를 읽는 흐름

build_sft_dataset.py · build_training_dataset.py로 데이터를 만들고, train_lora.py로 학습한 뒤 evaluate_model.py로 검증하고, sllm_service로 서빙함

순서: ① 데이터 준비 → ② 학습(train_lora.py) → ③ 평가 → ④ 서비스 실행

### Instruction SFT vs Context-based QA SFT - 두 갈래

### PEFT 기초 실습 - HR 규정 안내 챗봇 실습

### 실습 시나리오 정의 - HR 규정 안내 챗봇 LoRA 튜닝

실습 진행 순서

1단계 · Context-based QA SFT 데이터 생성: hr_manual_v1.txt를 규정 Section별로 나눠 질문·정답 자동 생성

2단계 · Instruction SFT 데이터 분리: 검증된 Q&A를 train/validation/evaluation으로 분리

3단계 · LoRA/QLoRA 학습: 환경별(CUDA/MPS/CPU) 자동 분기로 hr-qwen-lora 학습

4단계 · 결과 평가: Base vs Fine-tuned 모델의 키워드·F1·Hallucination 점수 비교

### HR 규정 안내 챗봇 실습의 전체 로드맵

모델 성능 향상 → Qwen2.5 + LoRA/QLoRA HR 규정 Fine-Tuning (Day1)

Context & Reasoning → Qwen2.5 + BGE-M3 RAG 문서 검색 답변 (Day1) → 맥락 압축, 요약 후 답변, 긴 입력 정리, Self-refine (Day2)

Inference Optimization → Qwen2.5 4bit Quantization 추론 테스트 (Day1)

### 실습 코드 - Instruction SFT 데이터 검증·분리 (build_sft_dataset.py)

입력: dataset/training/hr_sft_all.jsonl (검수 완료 Q&A)

```python
import json, random

def validate_record(record, line_number):
    messages = record.get("messages")
    if not isinstance(messages, list) or len(messages) < 2:
        raise ValueError(f"{line_number}번째 줄: messages 필요")
    roles = [m.get("role") for m in messages]
    if "user" not in roles or "assistant" not in roles:
        raise ValueError(f"{line_number}번째 줄: user/assistant 없음")

def main():
    records = read_jsonl(INPUT_PATH)   # 형식 검증 포함
    random.seed(RANDOM_SEED)
    random.shuffle(records)

    total = len(records)
    eval_n = max(1, round(total * 0.1))
    val_n   = max(1, round(total * 0.1))

    write_jsonl(TRAIN_PATH,      records[eval_n + val_n:])
    write_jsonl(VALIDATION_PATH, records[eval_n:eval_n + val_n])
    write_jsonl(EVALUATION_PATH, records[:eval_n])
```

각 레코드가 user/assistant role을 모두 포함하는지 검증한 뒤, 전체 데이터의 10%씩을 evaluation/validation으로 떼어내고 나머지를 train으로 사용

### 실습 코드 - Context-based QA SFT 데이터 생성 #1 (문서 분리)

입력: dataset/source/hr_manual_v1.txt

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class ManualSection:
    section_id: str
    title: str
    content: str

# "Chapter 3","제3장","3.1 연차" 패턴을 규정 제목으로 인식
def is_heading(line: str) -> bool:
    return any(p.search(line.strip()) for p in HEADING_PATTERNS)

def split_manual_sections(text: str) -> list[ManualSection]:
    sections, title, lines = [], "", []
    def flush():
        content = normalize_content(lines)
        if is_valid_section(title, content):
            sid = f"section-{len(sections)+1:03d}"
            sections.append(ManualSection(sid, title.strip(), content))
    for line in text.splitlines():
        if is_heading(line):
            flush(); title = line.strip()
        else:
            ...
```

정규식 패턴으로 "Chapter 3", "제3장", "3.1 연차" 같은 줄을 규정 제목(heading)으로 인식해, 원문 매뉴얼을 ManualSection 단위로 분리

### 실습 코드 - Context-based QA SFT 데이터 생성 #2 (질문·정답 생성)

```python
# 같은 규정을 6가지 질문 표현으로 반복 학습
def create_train_questions(section):
    title = clean_section_title(section.title)
    return [
        f"{title}에 대한 규정을 설명해 주세요.",
        f"직원이 {title}과 관련해 반드시 알아야 할 사항은?",
        f"{title}을 실제 업무에 적용할 때 조건과 예외는?",
        f"{title} 규정의 핵심 기준과 예외를 정리해 주세요.",
    ]

# 정답에 원문 규정(context)을 그대로 포함하는 것이 핵심
def build_structured_answer(section):
    conclusion = first_sentence(section.content)
    return f"""
결론: {conclusion}

적용 규정: {section.content}

위 규정만으로 판단하기 어려운 개별 상황은 추측하지 말고
인사팀 또는 담당 부서에 확인해야 합니다.
""".strip()
```

동일한 규정 Section에 대해 표현이 다른 질문을 여러 개 생성해 다양한 질의 방식에 대응하도록 학습시킴

정답은 결론과 원문 규정(context)을 함께 포함시켜, 근거 있는 응답을 하도록 구조화함

### 실습 코드 - Context-based QA SFT 데이터 생성 #3 (평가 키워드·안전장치)

```python
# 평가용 must_include 키워드: 회사 코드 > 숫자·기한 > 정책 용어 순
def extract_must_include_keywords(section, max_keywords):
    keywords = []
    keywords += extract_company_codes(section.content)   # AURORA, ORBIT ..
    keywords += extract_numeric_rules(section.content)   # "3영업일" 등
    keywords += [t for t in COMPANY_POLICY_TERMS if t in section.content]
    return list(dict.fromkeys(keywords))[:max_keywords]

# 규정에 없는 질문에는 "모른다"고 답하도록 안전 응답 학습
def unknown_policy_answer() -> str:
    return (
        "현재 제공된 규정에서는 해당 내용을 확인할 수 없습니다. "
        "임의로 추측하거나 단정하지 말고 인사팀 또는 담당 부서에 "
        "확인해야 합니다."
    )
```

평가 키워드는 회사 코드 → 숫자·기한 → 정책 용어 순으로 우선순위를 두어 추출

"개인 여행 경비를 전액 지원하나요?" 같이 규정에 없는 질문에는 안전 응답을 학습시켜, train/validation/evaluation 세트 전반에서 Hallucination(허위 확답)을 억제하도록 함

### 실습 코드 - LoRA/QLoRA 학습 환경 자동 분기 (train_lora.py #1)

```python
def detect_device_type() -> str:
    if torch.cuda.is_available():
        return "cuda"
    if torch.backends.mps.is_available():
        return "mps"
    return "cpu"

def create_training_profile(device_type):
    if device_type == "cuda":
        use_qlora = parse_bool_env("USE_QLORA", True)
        return TrainingProfile(
            training_mode="QLoRA 4bit NF4 CUDA" if use_qlora
                          else "FP16 LoRA CUDA",
            learning_rate=2e-4 if use_qlora else 1e-4,
        )
    if device_type == "mps":
        # Apple Silicon: 속도보다 학습 안정성 우선 -> FP32 LoRA
        return TrainingProfile(training_mode="FP32 LoRA Apple MPS")
    # CPU: FP32 LoRA, max_length 256으로 축소
    return TrainingProfile(training_mode="FP32 LoRA CPU")
```

### 실습 코드 - LoRA Config & SFTTrainer 설정 (train_lora.py #2)

```python
def create_lora_config(profile):
    return LoraConfig(
        r=profile.lora_rank,               # 기본 16
        lora_alpha=profile.lora_alpha,   # 기본 32
        lora_dropout=profile.lora_dropout,
        bias="none",
        task_type="CAUSAL_LM",
        target_modules=[
            "q_proj", "k_proj", "v_proj", "o_proj",
            "gate_proj", "up_proj", "down_proj",
        ],
    )

def create_sft_config(profile, output_dir):
    return SFTConfig(
        output_dir=str(output_dir),
        num_train_epochs=profile.epochs,
        learning_rate=profile.learning_rate,
        eval_strategy="epoch", save_strategy="epoch",
        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
        # conversational 데이터에서 assistant 응답만 loss 계산
        assistant_only_loss=True,
        packing=False,
    )
```

이번 실습의 LoRA는 앞선 예제 코드(q_proj/v_proj만 적용)보다 넓게 q/k/v/o_proj와 gate/up/down_proj까지 모두 target_modules에 포함

assistant_only_loss=True로 설정해 대화형 데이터에서 assistant 응답 부분에 대해서만 loss를 계산

### 실습 코드 - 학습 실행 및 저장 (train_lora.py #3)

```text
dataset = load_training_dataset(train_path, validation_path)
tokenizer = load_tokenizer()
model = load_model(profile)
lora_config = create_lora_config(profile)

trainer = SFTTrainer(
    model=model,
    args=create_sft_config(profile, output_dir),
    train_dataset=dataset["train"],
    eval_dataset=dataset["validation"],
    processing_class=tokenizer,
    peft_config=lora_config,
)

train_result = trainer.train()

# load_best_model_at_end에 의해 선택된
# Validation 기준 최적 Adapter를 저장
trainer.save_model(str(output_dir))
tokenizer.save_pretrained(str(output_dir))
# -> models/hr-qwen-lora/ 에 저장됨
```

load_best_model_at_end=True 설정 덕분에, 학습 종료 시 Validation 기준으로 가장 성능이 좋았던 시점의 Adapter가 자동으로 선택되어 저장됨

### 실습 코드 - 평가 스크립트 구조 (evaluate_model.py #1)

```text
base_model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
tuned_model = PeftModel.from_pretrained(
    base_model, str(ADAPTER_PATH), is_trainable=False,
)

for record in evaluation_records:
    question = record["question"]

    # Base 모델: 같은 PeftModel에서 Adapter를 잠시 끈다
    with tuned_model.disable_adapter():
        base_answer = generate_answer(
            tuned_model, tokenizer, question,
        )

    # Fine-tuned: Adapter를 다시 켠 동일 모델
    tuned_answer = generate_answer(
        tuned_model, tokenizer, question,
    )

    base_result = evaluate_answer(base_answer, record)
    tuned_result = evaluate_answer(tuned_answer, record)
```

별도의 두 모델을 로드하지 않고, 하나의 PeftModel에서 disable_adapter()로 어댑터를 껐다 켜며 Base 응답과 Fine-tuned 응답을 같은 모델 인스턴스로 비교

### 실습 코드 - 평가 지표 계산 (evaluate_model.py #2)

```python
# Keyword 반영률: must_include 중 실제 포함된 비율
def keyword_score(answer, must_include, must_not_include):
    included = [k for k in must_include if k in answer]
    score = len(included)/len(must_include) if must_include else None
    forbidden = [k for k in must_not_include if k in answer]
    if forbidden and score is not None:
        score = max(0.0, score - 0.5)
    return score

# Unknown Policy 질문에서 "모른다"고 안전하게 답했는지 확인
def hallucination_score(answer, category, must_not_include):
    if category != "unknown_policy":
        return {"applicable": False}
    safe = any(t in answer for t in UNKNOWN_SAFE_TERMS)
    risky = any(t in answer for t in UNKNOWN_RISKY_PATTERNS)
    score = 1.0 if safe and not risky else 0.5 if safe else 0.0
    return {"applicable": True, "score": score}
```

종합 점수 계산 방식

일반 질문: keyword*0.7 + F1*0.3

Unknown 질문: keyword*0.3 + F1*0.2 + safety*0.5

keyword_score는 반드시 포함되어야 할 키워드 비율에서, 포함되면 안 되는 키워드(forbidden)가 있으면 감점하는 구조

### 실습 코드 - 실행 순서 및 결과 확인

```text
# 1) 데이터셋 생성 (Context-based QA SFT)
python scripts/build_training_dataset.py

# 2) 데이터 분리·검증 (Instruction SFT 형식 확인)
python scripts/build_sft_dataset.py

# 3) LoRA/QLoRA 학습 실행
SFT_MAX_LENGTH=512 SFT_EPOCHS=3 \
SFT_LEARNING_RATE=1e-4 SFT_GRAD_ACCUM=8 \
python scripts/train_lora.py
# -> models/hr-qwen-lora/ 생성

# 4) 결과 평가
python scripts/evaluate_model.py
# -> outputs/evaluation_results.jsonl
# -> outputs/evaluation_summary.json

# 재학습 시
rm -rf models/hr-qwen-lora
```

데이터 생성 → 분리·검증 → 학습 → 평가 순으로 스크립트를 실행하며, 재학습이 필요하면 기존 어댑터 폴더를 삭제한 뒤 3번부터 다시 진행

### 1. 이 학생은 원래 어떤 사람인가? : 구조 이해

트랜스포머는 원래 번역을 위해 만들어졌고, 통역팀처럼 두 역할로 나뉘어 있었음

청취 담당(인코더): 원어민의 말을 처음부터 끝까지 다 듣고, 문장 전체의 맥락을 양방향으로 파악해 핵심 의미를 정리함 → BERT가 이 역할만 떼어낸 모델(encoder-only)

발화 담당(디코더): 정리된 의미를 받아서 다른 언어로 한 단어씩 순서대로 말을 만들어냄 → GPT·Qwen이 이 역할만 떼어낸 모델(decoder-only)

BERT는 문장을 깊이 "이해"하는 데 특화되어 분류·검색·개체명 인식에 쓰이고, Qwen 같은 decoder-only 모델은 답을 순차적으로 "생성"하는 데 특화되어 챗봇·SFT·RLHF·DPO의 대상이 됨

실습에서 다루는 모든 파인튜닝은 생성이 목적이므로 decoder-only(CLM) 모델을 사용함

```text
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("internal-sllm-base")
tokenizer = AutoTokenizer.from_pretrained("internal-sllm-base")

print(model.config.model_type)           # 예: qwen2 (decoder-only, CLM)
print(model.config.is_encoder_decoder)   # False → 생성 전문가 구조
```

model_type과 is_encoder_decoder 값으로 해당 모델이 decoder-only 생성 전문가 구조인지 코드로 확인 가능

### 2. 어떻게 가르칠 것인가? : 학습 도구(PEFT)

공장의 핵심 기계(원본 가중치)를 통째로 뜯어고치는 대신, 그 옆에 작은 우회 보정 장치를 다는 방법 → PEFT(Parameter-Efficient Fine-Tuning)

LoRA(Low-Rank Adaptation): 핵심 기계 옆에 병렬로 다는 우회 보정 장치. 원본은 그대로 두고 작은 보정값만 학습하며, 나중에 원본과 합칠 수도 있어 속도 손해가 거의 없음

Adapter: 각 작업 라인 중간에 직렬로 끼워 넣는 작은 보정 스테이션

Prefix-Tuning: 모든 라인의 작업반장에게 참고 메모를 하나씩 쥐여주는 방식

Prompt-Tuning: 공장 정문에 오늘의 작업 지시서만 붙여두는, 가장 가벼운 방식

실무에서는 이 중 LoRA(및 QLoRA)가 사실상 표준으로 가장 널리 쓰임

```text
from peft import LoraConfig, get_peft_model, TaskType

lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=8,                                   # 보정 장치의 손잡이 개수
    lora_alpha=16,                          # 보정값을 반영하는 증폭 다이얼
    lora_dropout=0.05,                      # 과적합 방지용 안전장치
    target_modules=["q_proj", "v_proj"],   # 보정 장치를 설치할 위치
)

model = get_peft_model(model, lora_config)
model.print_trainable_parameters()
# 예: trainable params: 4.2M || all params: 1.3B || trainable%: 0.32%
```

r은 보정 장치의 손잡이 개수(랭크), lora_alpha는 보정값을 반영하는 증폭 정도, target_modules는 보정 장치를 설치할 위치를 의미함

### 3. 무엇을 가르칠 것인가? : 학습 목적

도구(2장)를 정했다면, 이제 그 도구로 정확히 무엇을 가르칠지 구분해야 함

SFT(Supervised Fine-Tuning, 지도 미세조정): 모범답안집을 주고 따라 쓰게 하는 글쓰기 과외와 같음. (질문, 정답) 쌍으로 "이렇게 답하라"는 형식·태도를 가르침

CPT(Continued Pre-training, 지속 사전학습): 라벨 없는 대량의 도메인 원문을 계속 읽혀서 지식 자체를 두껍게 새겨 넣는 단계. 새로운 방대한 사실 정보를 주입하려면 SFT보다 이 단계가 필요함

RLHF/DPO(Reinforcement Learning from Human Feedback / Direct Preference Optimization): 여러 답변 중 어떤 게 더 나은지 가려내는 단계

RLHF는 채점 로봇(보상 모델)을 따로 만들어 실시간 코칭을 받는 방식

DPO는 채점 로봇 없이 "이 글이 저 글보다 낫다"는 비교 예시(기출문제집)를 직접 학습하는 더 단순한 방식

```text
from trl import SFTTrainer

trainer = SFTTrainer(
    model=model,
    train_dataset=domain_dataset,   # (질문, 정답) 형태의 사내 데이터
    tokenizer=tokenizer,
)
trainer.train()
```

```text
from trl import DPOTrainer

dpo_trainer = DPOTrainer(
    model=model,
    ref_model=None,                     # 비워두면 원본을 참조 모델로 자동 사용
    train_dataset=preference_dataset,   # (prompt, chosen, rejected) 비교 쌍
)
dpo_trainer.train()
```

### 실무 예시 - 지식 증류(Knowledge Distillation)를 SFT와 잇는 시나리오

지식 증류는 단독으로 끝나는 기법이 아니라, 부족한 도메인 데이터를 채워서 앞의 SFT 단계로 이어주는 전 단계임

진행 순서: ① 데이터 부족 확인 → ② 교사 모델에게 시드 예시 제공 → ③ 유사 형식의 질문·답변 대량 생성 → ④ 품질 검수 → ⑤ 실제+합성 데이터를 합쳐 SFT·LoRA 학습

```text
# ② + ③ 교사 모델에게 소량의 실제 예시를 주고 합성 데이터 생성 요청
seed_examples = real_domain_dataset[:5]         # 실제 사내 데이터 일부를 예시로 사용

synthetic_data = []
for _ in range(200):
    prompt = build_generation_prompt(seed_examples)   # 예시 형식 프롬프트 구성
    response = teacher_model.generate(prompt)         # 대형 교사 모델 호출
    synthetic_data.append(parse_qa_pair(response))    # (질문, 답변) 쌍으로 파싱

# ④ 품질 검수 (형식·사실관계 등 필터링)
clean_data = [d for d in synthetic_data if quality_check(d)]

# ⑤ 실제 데이터 + 합성 데이터를 합쳐 SFT 학습 (앞서 본 흐름 그대로 재사용)
domain_dataset = real_domain_dataset + clean_data
trainer = SFTTrainer(
    model=model,
    train_dataset=domain_dataset,
    tokenizer=tokenizer,
)
trainer.train()
```

teacher_model(교사 모델)은 특정 상용 LLM을 가리키는 고유명사가 아니라 "학생 모델보다 더 크고 뛰어난 모델"이라는 역할을 가리키는 이름임 — GPT-4·Claude 같은 상용 API가 맡을 수도, 회사가 이미 가진 더 큰 자체 모델이 맡을 수도 있음

가이드가 상용 범용 LLM을 예로 든 이유는 지식 증류의 정의여서가 아니라, 사내에 마땅한 대형 모델이 없을 때 데이터를 가장 빠르게 채울 수 있는 흔한 선택지이기 때문임

지식 증류 구도: 학생(학습시키려는 작은 sLLM) ↔ 교사(더 크고 뛰어난 어떤 모델이든). 교사에게 시드 예시를 보여주고 대량의 (질문, 답변) 쌍을 생성시킨 뒤, 그 결과물을 학생 모델이 SFT로 학습함

교사 모델도 모르는 지식(회사만의 고유 규정 등)은 증류로 주입할 수 없음

상용 API를 교사로 쓸 경우 이용 약관상 그 출력으로 경쟁 모델을 학습시키는 것이 제한될 수 있어 사전 확인이 필요함

### 4. 학습은 내부적으로 어떻게 일어나는가? : 원리

완성된 제품(모델 출력)을 검사해서 오차를 확인한 뒤, 그 오차가 왜 생겼는지 거꾸로 추적하며 보정 장치의 손잡이를 얼마나 돌려야 할지 계산하는 과정 → 역전파(Backpropagation)

순서: ① Forward(데이터가 모델을 통과해 예측 생성) → ② Loss 계산(예측과 정답을 비교해 오차 산출) → ③ Backward(오차를 거슬러 올라가며 조정 방향 계산) → ④ Optimizer Step(보정 장치(LoRA)만 실제로 업데이트)

이 순서(forward→backward)는 모든 신경망에 공통된 절차이며 RNN만의 특징이 아님

RNN에 고유한 것은 시퀀스의 시간축까지 함께 거슬러 올라가는 BPTT(Backpropagation Through Time)라는 변형이고, Transformer는 시간축 순환 구조가 없어 일반적인 역전파만으로 충분함

```text
outputs = model(**batch)   # ① Forward
loss = outputs.loss        # ② 오차 계산
loss.backward()            # ③ Backpropagation
optimizer.step()           # ④ 파라미터(LoRA만) 업데이트
optimizer.zero_grad()      # 다음 스텝을 위해 기울기 초기화
```

### 5. 자원이 부족할 땐 어떻게 하는가? : 최적화

LoRA에서는 원본 핵심 기계(가중치)를 고해상도 설계도(16비트) 그대로 창고에 보관함 → 모델이 커질수록 창고 공간(GPU 메모리)을 많이 차지

QLoRA(Quantized Low-Rank Adaptation, 양자화된 저순위 적응): 이 설계도를 4비트짜리 초압축 요약본으로 창고에 보관하고, 계산이 필요한 순간에만 잠깐 펼쳐서 쓴 뒤 다시 압축해둠. 학습 대상(LoRA 보정 장치)은 완전히 동일하며, 원본을 얼마나 압축해서 보관하느냐만 다름

장점: 메모리 사용량이 극적으로 줄어 훨씬 큰 모델을 훨씬 저사양 GPU에서도 파인튜닝할 수 있음

트레이드오프: 압축·해제 과정에서 계산 속도가 약간 느려지고, 아주 미세한 정보 손실이 생길 수 있음

```text
from transformers import AutoModelForCausalLM, BitsAndBytesConfig

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype="bfloat16",
)

model = AutoModelForCausalLM.from_pretrained(
    "internal-sllm-base",
    quantization_config=bnb_config,   # 창고를 4비트로 압축
)

model = get_peft_model(model, lora_config)   # 이후 LoRA는 2장과 동일하게 적용
```

## 관련 글

- [[blog/STUDYING/index|STUDYING]]
