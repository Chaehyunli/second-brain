---
title: "[AI AGENT] AI Agent 성능 평가"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "ai agent", "spring boot"]
category: "AI(MCP)"
published: 2026-06-03
source_url: https://ch010104.tistory.com/282
---

# [AI AGENT] AI Agent 성능 평가

## 원문

https://ch010104.tistory.com/282

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

AI Agent의 평가는 크게 생성 단계(Generation Layer)와 행동 단계(Action Layer)의 두 가지 관점으로 접근합니다.

Agent가 외부 데이터(DB, 문서, API)를 참조해 답변할 때, 할루시네이션을 잡아내기 위해 LLM-as-a-Judge(더 똑똑한 LLM을 판사로 쓰는 방식) 기법을 활용한 3대 메트릭을 주로 사용합니다.

## 원문 기반 개념 정리

### 1. AI Agent 평가의 핵심 레이어 및 메트릭

AI Agent의 평가는 크게 생성 단계(Generation Layer)와 행동 단계(Action Layer)의 두 가지 관점으로 접근합니다.

### ① 생성 단계 (Generation Layer) - RAG 기반 할루시네이션 검증

Agent가 외부 데이터(DB, 문서, API)를 참조해 답변할 때, 할루시네이션을 잡아내기 위해 LLM-as-a-Judge(더 똑똑한 LLM을 판사로 쓰는 방식) 기법을 활용한 3대 메트릭을 주로 사용합니다.

충실성 (Faithfulness / Groundedness)

개념: Agent가 내놓은 답변이 참조한 컨텍스트(문서나 API 결과)에 실제로 기반하고 있는가?

측정법: 답변의 문장들을 개별적 사실(Statements) 단위로 쪼갠 뒤, 판사 LLM에게 *"이 문장이 컨텍스트로부터 유출 가능한가?"*를 물어 예/아니오로 판별한 뒤 비율을 점수화합니다. 컨텍스트에 없는 내용을 지어냈다면(할루시네이션) 이 점수가 낮아집니다.

답변 부합성 (Answer Relevance)

개념: Agent가 질문의 의도에 맞는 답변을 했는가? (엉뚱한 삼천포로 빠지지 않았는가?)

측정법: Agent의 답변을 바탕으로 판사 LLM에게 역으로 질문을 역생성하게 만든 뒤, 그렇게 만들어진 역생성 질문이 최초 유저의 질문과 의미론적으로 얼마나 유사한지 비교하여 측정합니다.

컨텍스트 정밀도 (Context Precision)

개념: Agent가 필요한 정보를 정확하게 잘 검색(Retrieval)해 왔는가?

측정법: 검색된 정보 조각들 중 진짜 답변에 도움을 준 유용한 정보가 상위에 랭크되어 있는지를 판사 LLM이 평가합니다.

### ② 행동 단계 (Action Layer) - Agent 특화 행동 평가

Agent는 단순히 답변만 하는 게 아니라 행동($Action$)을 취하므로, 할루시네이션이 행동의 오류로 이어지는지 검증해야 합니다.

도구 호출 정확도 (Tool Call Correctness)

개념: Agent가 엉뚱한 API를 호출하거나, 존재하지 않는 인자($Argument$)를 지어내서 채워 넣지 않는지(이것도 일종의 행동 수준 할루시네이션입니다) 검증합니다.

태스크 완수율 (Task Completion Rate)

개념: 여러 차례의 턴(Turn)을 거친 뒤 최종 목적지에 올바르게 잘 도달했는가?

궤적 및 비용 효율성 (Trajectory & Step Efficiency)

개념: 목표를 달성하기 위해 무한 루프에 빠지거나 쓸데없이 20~30턴씩 돌지 않고, 최적의 단계(예: 3~5턴 이내)로 해결했는지 측정합니다.

### 2. 평가를 자동화하는 파이프라인 구조

Agent 성능 평가는 사람이 일일이 검사할 수 없기 때문에, 개발 단계(CI/CD)에서 '골든 데이터셋(Golden Dataset)'을 기반으로 자동 평가 파이프라인을 구축하여 성능 저하를 방지합니다.

```text
[테스트 입력 (User Query)]
       │
       ▼
 ┌───────────┐      [도구/DB 조회]      ┌────────────────┐
 │ AI Agent  │ ──────────────────────> │ Context / Tool │
 └───────────┘                         └────────────────┘
       │                                       │
       ├───────────────────────────────────────┘
       ▼ (중간 과정 Trace 및 최종 결과 산출)
 ┌──────────────────────────────────────────────────────┐
 │               LLM-as-a-Judge 평가                    │
 │  - Faithfulness (컨텍스트 기반 유추 여부)            │
 │  - Tool Accuracy (올바른 인자 사용 여부)             │
 └──────────────────────────────────────────────────────┘
       │
       ▼
 [Pass / Fail 결과 리포트 및 대시보드 시각화]
```

골든 데이터셋 구축: 질문, 가이드라인(원하는 컨텍스트), 그리고 이상적인 정답 예시를 모아둔 100~200개의 평가 데이터셋을 만듭니다.

테스트 실행: 코드가 수정될 때마다 Agent에게 이 질문들을 대량으로 던져 일제히 테스트를 수동/자동으로 기동합니다.

트레이싱(Tracing): Agent가 어떤 생각을 하고 어떤 도구를 썼는지 내부 실행 흐름의 모든 과정을 추적 기록합니다.

판사 LLM 검사: 판사 LLM(주로 GPT-4o나 Claude 3.5 Sonnet 같은 고성능 모델)이 정교한 프롬프트 수식을 기반으로 점수(0.0 ~ 1.0)를 산출해 리포트를 발행합니다.

### 3. 실무에서 사용하는 3대 테스트 전략

외부 날씨 API, 예약 시스템 등 실시간 데이터에 의존하는 AI Agent를 평가하기 위해 활용하는 전략들의 특성 비교입니다.

### 4. 현업에서 주로 쓰는 에이전트 평가 툴 (Frameworks)

현재 AI 엔지니어들이 에이전틱 시스템의 할루시네이션과 에러를 예방하기 위해 사용하는 대표적인 도구들입니다.

### ① DeepEval & RAGAS (코드 기반 자동화 평가)

RAGAS (RAG Assessment):

초점: RAG 파이프라인 및 문서 활용 퀄리티 평가에 특화.

장점: 학술적이고 정교한 수식 기반 메트릭 제공. 데이터프레임 단위의 실험에 최적화.

DeepEval:

초점: LLM 애플리케이션 및 AI 에이전트 종합 테스트 프레임워크.

장점: pytest 스타일 인터페이스 제공, 에이전트용 행동 평가 메트릭 지원. CI/CD 자동화 구축에 압도적으로 편리함.

### ② Promptfoo (프롬프트 A/B 테스트 및 보안 진단)

초점: 대규모 프롬프트 비교 실험 및 취약점 진단(Red-teaming).

장점: 수많은 프롬프트 후보군과 모델 버전별 결과를 격자형(Matrix) UI 리포트로 한눈에 비교할 수 있어 최적의 프롬프트 튜닝에 특화.

### ③ LangSmith & Langfuse (실행 과정 로깅 및 추적)

초점: Agent가 백그라운드에서 실행된 중간 궤적(Trace)을 시각적으로 투명하게 모니터링하는 플랫폼.

장점: "에이전트가 왜 이 시점에 이런 환각을 유발했는지", "API 호출 속도가 왜 이렇게 느려졌는지" 타임라인 별로 병목 구간을 상세히 파고들 수 있어 운영 환경 필수 도입 도구로 평가받음.

### 5. DeepEval 기반의 실제 평가 코드 구현

DeepEval을 활용하여 전략 3(Mocking)과 전략 1(Tool 검증) 및 전략 2(할루시네이션 검증)를 통합 적용한 실제 파이썬 구현체 예시입니다.

```python
import os
import unittest
from unittest.mock import patch

# 1. DeepEval 모듈 임포트
from deepeval import evaluate
from deepeval.test_case import LLMTestCase
from deepeval.metrics import HallucinationMetric, ToolCorrectnessMetric

# OpenAI API 키가 환경변수로 등록되어 있어야 판사 LLM이 평가를 수행할 수 있습니다.
# os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

# ==========================================
# [Target AI System] 대상 에이전트 코드 (시뮬레이션)
# ==========================================
class WeatherAgent:
    """사용자 질문에 따라 날씨 API를 호출하고 응답을 재가공하는 단순 에이전트"""
    def __init__(self, api_client):
        self.api_client = api_client

    def run(self, user_query: str) -> dict:
        # 실제 환경에서는 LLM이 Tool Calling을 판정하지만,
        # 여기서는 LLM이 get_weather API를 호출하기로 결심하고 인자를 추출한 상황을 가정합니다.

        # 1. Tool Call Argument 추출 (예시: 서울, 내일)
        location = "Seoul"
        date = "tomorrow"

        # 2. 외부 API 호출 (우리는 테스트 환경에서 이 client를 Mocking할 것입니다)
        api_response = self.api_client.get_weather(location=location, date=date)

        # 3. API 결과를 종합하여 최종 답변 작성 (할루시네이션 시뮬레이션을 위해 일부 오류를 포함함)
        # 실제 API 결과에는 최고기온이 25도라고 되어있으나, 32도라고 답변을 왜곡함 (환각)
        actual_output = f"내일 서울 날씨는 매우 덥겠으며, 최고 기온은 32도까지 치솟을 예정입니다."

        return {
            "actual_output": actual_output,
            "tool_called": "get_weather",
            "tool_arguments": {"location": location, "date": date},
            "retrieved_context": [str(api_response)]  # 평가를 위해 로깅된 컨텍스트
        }

# ==========================================
# [Test Suite] DeepEval + Mocking 기반 평가
# ==========================================
class TestWeatherAgent(unittest.TestCase):

    @patch('unittest.mock.MagicMock') # 외부 API 호출 클라이언트를 격리하기 위한 Mock 선언
    def test_weather_agent_evaluation(self, mock_api_client):
        # 1. Mocking 응답 설정 (전략 3: 고정된 Mock 데이터 제공)
        # 외부 날씨가 실제로 몇 도이든 관계없이 API는 고정 값을 리턴합니다.
        mock_api_client.get_weather.return_value = {
            "status": "success",
            "temp": 25,
            "condition": "mildly cloudy",
            "warning": "none"
        }

        # 2. 에이전트 실행 및 추적 데이터 수집
        agent = WeatherAgent(api_client=mock_api_client)
        user_query = "내일 서울 날씨 어때?"

        agent_result = agent.run(user_query)

        # 3. DeepEval TestCase 구성
        # 수집된 정보들을 DeepEval 평가 데이터 객체로 포장합니다.
        test_case = LLMTestCase(
            input=user_query,
            actual_output=agent_result["actual_output"],
            expected_output="내일 서울은 25도이며 대체로 온화합니다.", # 골든 데이터셋 기반 이상적 정답
            retrieval_context=agent_result["retrieved_context"]   # 에이전트가 툴로부터 획득한 진짜 로우 데이터
        )

        # 4. 평가 메트릭 정의 (LLM-as-a-Judge 설정)
        # 가공된 실제 답변(32도)과 취득한 컨텍스트(25도) 대조를 통해 환각을 검사합니다.
        hallucination_metric = HallucinationMetric(threshold=0.5, model="gpt-4o")

        # 에이전트가 지정된 스펙대로 Tool을 알맞게 호출했는지 검증합니다.
        tool_correctness_metric = ToolCorrectnessMetric(
            threshold=0.7,
            model="gpt-4o",
            should_mock=False # 이미 앞에서 unittest.mock으로 처리했으므로 False
        )

        # 5. 실행 및 리포팅
        # 해당 테스트 케이스를 명시된 지표에 맞춰 채점합니다.
        results = evaluate(
            test_cases=[test_case],
            metrics=[hallucination_metric, tool_correctness_metric]
        )

        # 6. 검증 성공 여부 체크 (Optional)
        # 평가 점수가 정해진 임계치(Threshold)를 넘었는지 테스트 프레임워크 수준에서 단언(Assert)합니다.
        for result in results:
            self.assertTrue(result.success, f"평가 지표 미달: {result.metric} - 점수: {result.score}")

if __name__ == "__main__":
    unittest.main()
```

### 6. 현업 도입 시 베스트 프랙티스 로드맵

테스트 데이터셋 확보 (Synthesizer 활용):

직접 100개의 골든 세트를 손수 짜기 어렵다면, Ragas나 DeepEval의 Synthesizer 패키지를 사용하여 보유 중인 서비스 시나리오 텍스트 문서로부터 대량의 '질문-API 응답 모델-정답 답변'을 자동 생성해 테스트 세트를 초기에 선구축합니다.

CI/CD 파이프라인 통합:

위의 unittest 또는 pytest 형태로 만들어진 평가 코드를 깃허브 액션(GitHub Actions)과 연동합니다.

개발자가 에이전트의 시스템 프롬프트를 교체하고 Push할 때마다, 50개의 골든 케이스에 대해 전체 평가 프로세스를 자동 가동하여 Hallucination 점수가 상승하거나 Tool Correctness가 하락하면 병합(Merge)을 차단하는 보호 장치로 활용합니다.

프로덕션 런타임 모니터링 및 로깅:

유저의 모든 대화 흐름을 론칭 이후 실시간으로 수집하고, LangSmith 혹은 Langfuse와 같은 가시성(Observability) 도구를 연결하여 Agent가 실제로 무한 루프에 돌지 않는지, 응답 속도가 늘어나지 않는지 실시간 모니터링 대시보드를 연계 구축합니다.

## 관련 글

- [[blog/AI(MCP)/index|AI(MCP)]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 4. 검증1 - Validation|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 4. 검증1 - Validation]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 3. 메시지와 국제화|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 3. 메시지와 국제화]]
- [[blog/INFLEARN/스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술- 2. 타임리프 - 스프링 통합과 폼|[스프링 MVC 2편 - 백엔드 웹 개발 핵심 기술] 2. 타임리프 - 스프링 통합과 폼]]
