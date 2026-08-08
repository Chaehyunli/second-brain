---
source: Notion Information
notion_url: https://app.notion.com/p/2026-08-06-AWS-AI-Competency-SK-AX-AI-3b61d84bf68e819db04ac3968c693377
notion_page_id: 3b61d84b-f68e-819d-b04a-c3968c693377
synced_at_utc: 2026-08-08T14:45:31Z
notion_content_sha256: 2e4e86af9154dd8fc7ea81a9c21daede5937afcb2de8ac4ac71eef77220c0cd8
---

> **원문**: [SK AX Insight — AWS AI Competency를 통해 검증된 SK AX의 에이전틱 AI 구축 역량](https://www.skax.co.kr/insight/trend/3810)
> **게시일**: 2026-08-06
> **정리 기준**: SK AX 공식 인사이트 원문
## 한눈에 보기
SK AX는 AWS의 `Generative AI Consulting Services`와 `Agentic AI Consulting Services` AI Competency를 모두 취득했다고 밝혔다. 이 인증은 실제 고객 구축 사례와 조직 차원의 보안·운영·사후지원 체계를 AWS가 심사하는 방식이다.\[1\]
핵심은 **생성형 AI를 안전하게 도입하는 능력**과 **에이전트가 실제 업무를 실행하도록 설계하는 능력**은 구분되며, 후자에는 권한 통제·도구 호출 범위·실행 이력·실패 재처리까지 포함된다는 점이다.\[1\]
## AWS AI Competency가 검증하는 것
AWS AI Competency는 두 층위를 함께 본다.\[1\]
1. **조직 역량**: 프로젝트 착수 방법론, Foundation Model 선택 기준, 데이터 보안·컴플라이언스, Responsible AI 절차, 운영 전환과 사후지원 체계
2. **고객 사례**: 실제 프로덕션 배포 사례, 아키텍처 다이어그램·기술 문서·운영 산출물
따라서 특정 모델이나 데모를 만들 수 있다는 주장보다, 보안·신뢰성·운영 우수성을 갖춘 고객 환경의 경험을 외부 기준으로 검증받았다는 데 의미가 있다.\[1\]
## Generative AI와 Agentic AI 인증의 차이
<table header-row="true">
<tr>
<td>구분</td>
<td>Generative AI Consulting Services</td>
<td>Agentic AI Consulting Services</td>
</tr>
<tr>
<td>중심 과제</td>
<td>LLM 기반 인프라와 기업 AI 아키텍처</td>
<td>목표 분석·계획·도구 연계·업무 실행 파이프라인</td>
</tr>
<tr>
<td>핵심 검증</td>
<td>모델 선택, 기업 데이터 연결, 보안·거버넌스, 운영 안착</td>
<td>권한 설계, 내부 시스템 API 연계, 실행 이력, 실패 재처리</td>
</tr>
<tr>
<td>결과물 관점</td>
<td>답변·생성 기능을 운영 환경에 도입</td>
<td>AI가 ERP·CRM 등과 연결되어 업무를 수행</td>
</tr>
</table>
Agentic AI는 답변 생성에서 끝나지 않는다. 에이전트가 목표를 하위 작업으로 나누고 도구를 호출해 실행하는 만큼, “무엇을 할 수 있는가”와 “무엇을 할 수 없게 할 것인가”를 함께 구조화해야 한다.\[1\]
## 에이전틱 AI 구현을 위한 6개 검증 영역
1. **추론(Inference)**: Amazon Bedrock·SageMaker AI 기반의 신뢰성·비용 효율을 고려한 모델 활용\[1\]
2. **SDK·프레임워크**: Strands, LangGraph 등으로 계획·추론·자율 실행을 구현하는 역량\[1\]
3. **상호운용성**: MCP, A2A 등 표준으로 에이전트 협업과 외부 도구 연결을 안전하게 구성하는 역량\[1\]
4. **보안**: IAM, IaC, Security Hub, CloudTrail, Bedrock Guardrails, SSO·IdP 연계를 통한 식별·권한·관측\[1\]
5. **Responsible AI**: 유해 출력 방지, 가드레일, 사람의 피드백을 반영하는 통제 장치\[1\]
6. **컴퓨팅**: Bedrock AgentCore, EKS, ECS, Lambda, Fargate 환경에 에이전트 워크로드를 배포하는 역량\[1\]
이 분류는 에이전틱 AI를 모델 성능 하나의 문제가 아니라, **모델·프레임워크·표준·보안·안전성·배포 환경이 결합된 운영 시스템**으로 봐야 한다는 기준이다.\[1\]
## 소개된 운영 사례
### 한미전선 GenAI 업무지원 서비스
SK AX가 소개한 사례는 ERP·업무 문서 질의에 외부 정보 보강이 필요한 환경이다. Cognito의 ID·비밀번호·MFA로 사용자를 인증하고, API Gateway·Lambda에서 토큰을 검증한 뒤 승인된 요청만 Bedrock AgentCore Runtime에 전달한다.\[1\]
기사에 따르면 질문의 복잡도와 품질·비용 요구에 따라 Haiku·Sonnet·Opus 모델을 선택하고, MCP로 외부 검색 도구를 연계한다. 실행 과정은 DynamoDB에서, 모델 호출과 오류 상태는 CloudWatch Logs에서 추적한다.\[1\]
### SKI E&S 통합 데이터 플랫폼
정형·대용량·실시간 Tag·외부 데이터를 함께 다루는 환경에 DMS·MSK·Glue로 수집·가공을 분리하고, S3·Redshift의 데이터를 Athena·QuickSight·SageMaker에서 분석·AI 개발에 활용하는 사례다.\[1\]
여기에 Bedrock Agent와 Knowledge Base를 적용해 데이터 카탈로그, IT 가이드, 업무 문서, 메타데이터를 자연어로 통합 검색하도록 했다고 설명한다.\[1\]
## 자율성보다 먼저 설계할 통제 장치
- **사용자·권한 통제**: 기업 인증 연계로 사용자를 식별하고 승인된 요청만 에이전트 흐름에 전달\[1\]
- **도구·검색 범위 제한**: 승인된 Knowledge Base·데이터 카탈로그만 대상으로 삼고, 도구 호출 권한은 업무 목적에 필요한 최소 범위로 제한\[1\]
- **비밀·암호화 관리**: 암호화 키는 AWS KMS, 외부 연계 자격증명은 AWS Secrets Manager로 관리\[1\]
- **최소 권한 실행**: Fargate·Lambda는 IAM 역할로 필요한 순간에만 접근\[1\]
- **관측·감사**: Run ID·Job 상태, 로그, 오류 상태를 통해 실행 원인을 추적하고 재처리\[1\]
- **사람의 승인**: 데이터 변경·운영 명령처럼 영향이 큰 작업은 자동 실행하지 않고 검토·승인 범위 안에 둠\[1\]
핵심 질문은 “AI가 무엇을 할 수 있나”만이 아니라, **누가 어떤 근거로 요청했고, 어느 도구까지 어떤 권한으로 실행했으며, 문제가 생겼을 때 어떻게 추적·중단·복구할 수 있는가**다.\[1\]
## AXgenticWire의 계층적 접근
SK AX는 AXgenticWire를 통해 `AXO Infra → Data·Knowledge → LLM → Platform·Orchestration → Agent Ops → Agent Service·Applications`의 여섯 계층을 조합하는 접근을 제시한다. Enterprise Agentic Workspace인 AXgenticWire Core는 실제 업무와 에이전트를 연결하고 통합 관리하는 역할로 설명된다.\[1\]
이는 기업의 에이전틱 AI 도입을 단일 챗봇 프로젝트가 아니라, 인프라·지식·모델·오케스트레이션·운영·업무 애플리케이션을 연결하는 전환 과제로 다루는 방식이다.\[1\]
## 나의 학습 포인트
1. **에이전트의 완성 기준은 실행 능력뿐 아니라 통제 가능성이다.** 사용자 식별, 최소 권한, 실행 이력, 실패 복구가 없으면 기업 업무 자동화로 확장하기 어렵다.
2. **MCP·A2A는 연결의 시작일 뿐이다.** 연결 대상의 허용 목록, 권한, 입력·출력 검증, 감사 로그를 함께 설계해야 한다.
3. **RAG와 에이전트는 데이터 경계를 명확히 해야 한다.** 승인된 Knowledge Base·데이터 카탈로그로 검색 범위를 제한하는 것은 정보 정확성과 데이터 접근 통제를 함께 다루는 방법이다.
4. **운영 피드백은 에이전트 품질의 일부다.** 호출 실패, 지연, 도구 오류, 사용자 피드백으로 프롬프트·지식 문서·도구 호출·모델 선택 기준을 조정해야 한다.
## Sources
\[1\] [https://www.skax.co.kr/insight/trend/3810](https://www.skax.co.kr/insight/trend/3810) — SKAX Insight Trend 3810
