---
source: Notion Information
notion_url: https://www.notion.so/3b81d84bf68e812e9e33ca5adcc4f2de
notion_page_id: 3b81d84b-f68e-812e-9e33-ca5adcc4f2de
synced_at_utc: 2026-09-04T15:12:20Z
notion_content_sha256: e3821cb7de9fd06a0e970578f2264b8647abb7361c225ba6ee3eebe7c4bebcc0
---

> **원문**: [SK AX Case Study — 한미전선 ERP Agentic AI 구축 사례](https://www.skax.co.kr/case-study/story/3618/)
> **게시일**: 2026-08-10
> **정리 기준**: SK AX 공식 사례 원문
## 핵심 요약
케이블 제조기업 한미전선은 국내외 영업 확대로 제품·고객·수주 데이터가 늘어나자, ERP 데이터를 빠르게 분석하고 다음 행동(Action Item)까지 제안받을 수 있는 체계를 필요로 했다. SK AX는 Amazon Bedrock AgentCore Runtime·AgentCore Memory·Bedrock 관리형 LLM을 중심으로 AWS Native 기반의 Agentic AI 분석 환경과 전용 ERP 챗봇 `AI Assistant`를 구축했다고 설명한다.\[1\]
이 사례의 중심은 “ERP 데이터를 자연어로 조회한다”는 기능만이 아니다. 서버리스 실행 환경, 관리형 메모리, 사용자 인증·토큰 검증, IAM 기반 모델 접근 제어, 요청·실행 로그 추적을 함께 구성해 **업무용 AI를 운영 가능한 구조로 설계**했다는 데 있다.\[1\]
## 도입 배경: 조회를 넘어 판단과 행동을 지원하는 ERP
한미전선은 수주·매출·미발주·할인율 등 핵심 업무 데이터를 ERP에 축적하고 있었다. 데이터가 늘어날수록 현황 조회만으로는 부족해졌고, 데이터에서 이슈를 읽어 다음 행동을 제안하는 Agentic AI가 필요해졌다고 원문은 설명한다.\[1\]
또한 AI를 도입하면서 운영 부담까지 커지지 않도록, On-Premises보다 확장성과 관리 편의성이 높은 AWS Cloud 기반을 선택했다. 즉, 기능 구현 이전에 **장기 운영의 안정성과 관리 효율**을 아키텍처 선택 기준으로 둔 사례다.\[1\]
## 아키텍처: AWS 관리형 서비스 중심의 역할 분리
<table header-row="true">
<tr>
<td>계층</td>
<td>적용 구성</td>
<td>역할</td>
</tr>
<tr>
<td>실행</td>
<td>Amazon Bedrock AgentCore Runtime</td>
<td>에이전트를 서버리스 방식으로 배포·실행</td>
</tr>
<tr>
<td>배포</td>
<td>CI/CD</td>
<td>배포 자동화와 수작업·고정 용량 부담 축소</td>
</tr>
<tr>
<td>대화 맥락</td>
<td>AgentCore Memory</td>
<td>별도 저장소 구축 없이 대화 이력·업무 맥락 관리</td>
</tr>
<tr>
<td>모델</td>
<td>Amazon Bedrock 관리형 LLM</td>
<td>IAM 기반 접근 통제 안에서 모델 호출</td>
</tr>
<tr>
<td>사용자 인증</td>
<td>Amazon Cognito, MFA</td>
<td>사용자 식별과 인증</td>
</tr>
<tr>
<td>요청 관문</td>
<td>API Gateway, Lambda</td>
<td>토큰 검증 후 승인된 요청만 실행 환경에 전달</td>
</tr>
<tr>
<td>분석 결과·추적</td>
<td>DynamoDB</td>
<td>요청 단위 추적, 분석 결과 저장·후속 RAG 활용</td>
</tr>
<tr>
<td>관측</td>
<td>CloudWatch Logs</td>
<td>AgentCore Runtime 실행 로그 중앙 확인</td>
</tr>
</table>
원문에 따르면 담당자는 별도의 조회 조건 설정이나 데이터 추출 없이 자연어로 수주 현황, 매출 추이, 미발주 건, 할인율 분포 등을 질문한다. 분석 결과는 DynamoDB에 저장되고, 이후 챗봇 질의에서 RAG 데이터로 다시 활용된다.\[1\]
## 보안과 운영성: 에이전트 실행 전후의 통제
ERP는 기업의 핵심 경영 정보를 다루므로, 모델을 호출하는 경로 자체를 통제 범위 안에 두는 것이 중요하다. 이 사례에서는 Cognito의 ID·비밀번호·MFA로 인증한 뒤 API Gateway·Lambda에서 토큰을 검증하고, 승인된 요청만 AgentCore Runtime으로 전달한다.\[1\]
또한 IAM 기반 접근 제어로 Bedrock 모델 호출을 제한하고, 분석 요청은 DynamoDB에서, 런타임 실행 로그는 CloudWatch Logs에서 추적한다. 이 흐름은 “답변을 생성하는 AI”를 넘어서, **누가 요청했는지·무엇이 실행됐는지·문제가 생겼을 때 어디를 확인할지**를 운영 설계에 포함한 방식이다.\[1\]
## 기존 BI·리포트와의 차이
원문은 기존 BI·리포트가 사전에 정의된 화면·지표 조회에 강점이 있는 반면, 새 질문이 생기면 추출·가공이 추가로 필요하다고 설명한다. 반대로 ERP Agentic AI는 자연어 질문을 받아 필요한 데이터를 분석하고, 대화 맥락을 이어 후속 질문에도 답하며, 주요 리스크와 다음 행동 제안까지 범위를 확장한다.\[1\]
다만 이 차이는 “AI가 모든 판단을 대체한다”는 뜻은 아니다. 업무 환경에서 Action Item 추천을 신뢰할 수 있으려면 분석 근거, 데이터 범위, 권한, 로그, 검토 책임을 함께 관리해야 한다. 이 사례의 인증·토큰 검증·IAM·DynamoDB·CloudWatch 구성은 그러한 운영 조건을 뒷받침하는 요소로 볼 수 있다.\[1\]
## 나의 학습 포인트
1. **ERP AI의 가치는 자연어 UI만으로 결정되지 않는다.** 자연어 질문 뒤에 데이터 접근 경계, 모델 호출 권한, 실행 이력, 결과 재활용 구조가 있어야 업무 시스템이 된다.\[1\]
2. **관리형 서비스 선택은 운영 인력의 부담을 줄이는 제품 전략이다.** 서버리스 Runtime·관리형 Memory·Bedrock을 선택하면 인프라 유지관리보다 업무 품질과 에이전트 기준을 개선하는 데 집중할 수 있다.\[1\]
3. **RAG는 문서 검색에만 쓰이지 않는다.** 이 사례에서는 저장된 분석 결과도 이후 질의의 근거 데이터가 된다. 따라서 결과를 어떤 조건·권한·시점의 산출물로 저장할지 설계해야 한다.\[1\]
4. **Agentic AI에는 관측 가능성이 필수다.** 요청 식별자, 실행 로그, 오류 상태가 있어야 결과 오류·지연·권한 문제를 사후에 재현하고 개선할 수 있다.\[1\]
## Sources
\[1\] [https://www.skax.co.kr/case-study/story/3618](https://www.skax.co.kr/case-study/story/3618) — SK AX Case Study 3618