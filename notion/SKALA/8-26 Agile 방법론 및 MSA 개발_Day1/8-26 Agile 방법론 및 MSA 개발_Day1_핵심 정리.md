---
title: "[8/26] Agile 방법론 및 MSA 개발_Day1_핵심 정리"
notion_page_id: "3c71d84b-f68e-8005-99c3-cc98666222e1"
source_url: "https://app.notion.com/p/3c71d84bf68e800599c3cc98666222e1"
synced_at: "2026-08-26T15:08:13+00:00"
content_sha256: "be63ef28e2814c7f8895ed84bf3bd13f41821dc604b2e41edca161e4f039d007"
---

# [8/26] Agile 방법론 및 MSA 개발_Day1_핵심 정리

[[notion/SKALA/index|SKALA 학습 노트]]

> 원문: [Notion 페이지](https://app.notion.com/p/3c71d84bf68e800599c3cc98666222e1)
>
> 원문의 임시 서명 이미지 URL은 보존하지 않았으며, 안정적으로 확인 가능한 텍스트·코드·표를 유지했다.

### Agile 개요 — 왜 필요한가?

전통적인 Waterfall 방식은 초기에 요구사항을 100% 확정한 뒤 순차적으로 진행하기 때문에, 후반 단계에서 결함이나 변경이 발견되면 수정 비용이 매우 커짐. 시장·고객 요구가 빠르게 변하는 환경에서는 짧은 주기로 동작하는 제품을 자주 검증해 **리스크를 조기에 낮추는 접근**이 필요함.
Agile이 특히 잘 맞는 상황은 다음과 같음.

- **요구사항 변동성이 큰** 신규 서비스·스타트업형 프로젝트
- 출시 후 사용자 반응을 보며 **방향을 조정해야 하는 제품** (빠른 피드백 중요)
- 기능 단위로 쪼개어 **순차적으로 릴리즈**할 수 있는 구조 (점진적 가치 전달)
- PO·개발팀 간 **상시 커뮤니케이션이 가능한 소규모 협업팀**

---

### Agile vs. Waterfall — 기존 방법론과의 차이

| 구분        | Waterfall                       | Agile                                  |
| ----------- | ------------------------------- | -------------------------------------- |
| 개발 방식   | 순차적(설계→개발→테스트)        | 반복·점진적(짧은 Sprint 단위 반복)     |
| 요구사항    | 초기에 상세히 확정, 변경 최소화 | 지속적으로 수집·재우선순위화(Backlog)  |
| 고객 피드백 | 프로젝트 종료 시점에 주로 확인  | 매 Sprint마다 Review로 상시 확인       |
| 산출물 확인 | 최종 단계에 통합 결과물 확인    | 매 Sprint마다 동작하는 Increment 확인  |
| 변경 대응   | 비용이 크고 절차가 무거움       | 변경을 전제로 유연하게 재계획          |
| 팀 구조     | 역할별 분업, 문서 기반 전달     | 교차기능팀, 상시 협업·짧은 피드백 루프 |

---

### Agile 도입 프로세스 — 5단계 로드맵

이론 적용과 실제 팀 도입은 다름. 처음부터 전사 적용을 시도하지 않고, **전체 영향이 없는 단위로 시작해 검증 성공 결과를 바탕으로 확산**하는 것이 핵심 원칙임.

---

### 실제 적용 시 흔한 문제 상황과 대응

| 문제 상황          | 증상                                               | 대응 방안                                             |
| ------------------ | -------------------------------------------------- | ----------------------------------------------------- |
| 무늬만 Agile       | Sprint 이름만 쓰고 기존 Waterfall 방식 그대로 진행 | 이벤트·산출물을 형식이 아닌 목적에 맞게 실제로 운영   |
| 역할 겸직 병목     | PO가 다른 업무와 겸직하여 의사결정 지연            | PO 전담 배치, 또는 일부 의사결정 권한을 팀에 위임     |
| 회고 없는 반복     | Sprint만 반복하고 프로세스 개선이 없음             | Retrospective 액션 아이템을 다음 Sprint에 반드시 반영 |
| 과도한 문서화 병행 | Waterfall식 문서 프로세스를 Agile과 병행 유지      | 꼭 필요한 산출물만 유지, 대화·시각화 중심으로 전환    |
| 진행상황 미가시화  | Sprint Board 없이 진행 상태를 아무도 모름          | Sprint Board·Burndown Chart로 매일 가시화             |

---

### Agile 전환 체크리스트

Sprint 단계별로 확인해야 할 항목을 정리한 실행 기준임.

---

### Agile 공정 — Scrum이란?

Scrum은 Agile을 실현하는 대표적인 프레임워크임. Scrum.org가 정의하는 **5가지 핵심 가치**는 팀 문화의 토대가 됨.

| 가치       | 의미                                       |
| ---------- | ------------------------------------------ |
| Courage    | 어려운 문제에 직면하고 올바른 일을 할 용기 |
| Focus      | Sprint 목표와 팀 목표에 집중               |
| Commitment | 팀 목표 달성에 개인이 헌신                 |
| Respect    | 서로를 독립적이고 유능한 사람으로 존중     |
| Openness   | 작업과 그 어려움에 대해 투명하게 공개      |

---

### Scrum 구조 및 프로세스

#### 역할 (Role)

| 역할               | 책임                                      |
| ------------------ | ----------------------------------------- |
| Product Owner (PO) | 제품 백로그 관리, 우선순위 결정, ROI 책임 |
| Scrum Master (SM)  | 프로세스 촉진, 장애물 제거, 팀 보호       |
| Development Team   | 기능 설계·구현·테스트, Increment 완성     |

#### Sprint 프로세스 (반복 주기)

---

### Scrum 산출물 (Artifacts)

- **Product Backlog** — 제품에 필요한 모든 요구사항의 우선순위 목록. PO가 소유·관리하며 지속적으로 Refinement됨
- **Sprint Backlog** — 이번 Sprint에서 완료하기로 선택한 백로그 항목 + 이를 구현하기 위한 Task 계획
- **Increment** — Sprint 종료 시점까지 완료된 모든 백로그 항목의 합. '완료(Done)' 기준을 충족해야 함
  **Definition of Done (완료의 정의)** — Increment가 '완료'로 인정받기 위한 팀 공통 기준. 실습 시작 전 팀 합의 필요.

---

### 이벤트별 실전 진행 가이드

| 이벤트                                                                                          | 권장 소요시간           | 참석자            | 핵심 아젠다                           |
| ----------------------------------------------------------------------------------------------- | ----------------------- | ----------------- | ------------------------------------- |
| Sprint Planning                                                                                 | 2시간 (2주 Sprint 기준) | 전체 팀           | 목표 합의 → Backlog 선택 → Task 분할  |
| Daily Scrum                                                                                     | 15분                    | Dev팀 + SM        | 어제 한 일 / 오늘 할 일 / 장애물 공유 |
| Sprint Review                                                                                   | 1시간                   | 전체 + 이해관계자 | 동작하는 결과물 데모, 피드백 수집     |
| Retrospective                                                                                   | 45분                    | 전체 팀           | Keep / Problem / Try 회고             |
| **Timebox를 정하고 지키는 것이 핵심.** 논의가 길어지면 별도 회의로 분리해 이벤트 시간을 보호함. |

---

### 2주 Sprint 캘린더 예시

| 기간                              | 활동                          |
| --------------------------------- | ----------------------------- |
| Day 1                             | Sprint Planning               |
| Day 2–4                           | 개발 + Daily Scrum            |
| Day 5–8                           | 개발 + Daily Scrum            |
| Day 9                             | 개발 마무리 + Daily Scrum     |
| Day 10                            | Sprint Review + Retrospective |
| 하루 일과 예시 (Daily Scrum 기준) |

- 09:30–09:45 Daily Scrum (어제/오늘/장애물 공유)
- 09:45–12:00 개발 집중 시간 (Task 작업)
- 14:00–17:00 개발 집중 시간 + 필요 시 Backlog Refinement
- 17:00–17:15 Sprint Board 업데이트 (Task 상태 갱신)

---

### Daily Scrum 대화 예시

3문항(어제/오늘/장애물) 형식으로 각자 간결하게 공유하는 것이 원칙임.

- 팀원 A(백엔드): 어제 로그인 API 개발 완료 → 오늘 토큰 갱신 로직 진행, 장애물 없음
- 팀원 B(백엔드): 어제 Gateway 라우팅 설정 진행 → 오늘 이어서 진행, Kafka 연동 설정 관련 SM 논의 필요
- 팀원 C(프론트): 어제 로그인 화면 UI 완성 → 오늘 API 연동 시작, 팀원 A의 API 완료 시점 확인 필요
  **장애물은 Daily Scrum에서 발견만 하고, 실제 논의는 종료 후 별도 시간에 진행함.**

---

### Agile Delivery 공정 — Sprint Zero와 본격 수행 단계

표준 Scrum에 착수/준비 단계(Sprint Zero)를 추가해 SI 프로젝트 수행 방식에 맞게 커스터마이징한 공정임.

---

### User Story — 정의와 방법론상 위치

요구사항이 구현 단위로 구체화되는 흐름: **비즈니스 요구 → Epic → User Story → Task**
Product Backlog는 Epic/User Story 단위로 구성되며, Sprint에 투입된 User Story가 Task로 쪼개져 Sprint Backlog가 됨.
**작성 템플릿**

```plain text
As a [사용자 유형], I want [원하는 기능/행동], So that [얻고자 하는 가치/이유]

예: As a 회원, I want 비밀번호를 재설정하고 싶다, So that 계정 접근 권한을 다시 얻을 수 있다
```

---

### User Story 작성 원칙 — INVEST

| 원칙                                       | 의미                                     |
| ------------------------------------------ | ---------------------------------------- |
| Independent                                | 다른 스토리와 독립적으로 개발 가능       |
| Negotiable                                 | 세부 구현은 협의 가능 (계약이 아닌 대화) |
| Valuable                                   | 사용자·고객에게 명확한 가치 제공         |
| Estimable                                  | 팀이 규모를 추정할 수 있을 정도로 명확   |
| Small                                      | 한 Sprint 내 완료 가능한 크기            |
| Testable                                   | 완료 여부를 검증할 수 있는 기준 존재     |
| **실전 적용 수준 — 얼마나 상세히 쓰는가?** |

- 백로그 초기 등록 시: 제목 + 한 줄 가치 정도로 개략 기록 (Epic 수준)
- Backlog Refinement 시점: Sprint 진입 후보로 좁혀지면 세부 조건·인수 기준 논의
- Sprint Planning 직전: INVEST 기준 충족하도록 상세화 (Task 분할 가능한 수준)
- Sprint 진행 중: 필요 이상 앞서 상세화하지 않음 (**Just-in-time 원칙**)

---

### 백로그 그루밍(Refinement) 실전 프로세스

| 항목          | 내용                                                |
| ------------- | --------------------------------------------------- |
| 주기          | Sprint 중반 1회, 1시간 이내                         |
| 참석자        | PO 필수, Dev팀 일부 순환 참석                       |
| 목표          | 다음 1\~2 Sprint 분량의 Story가 'Ready' 상태로 유지 |
| **진행 순서** |

1. **우선순위 재정렬** — PO가 비즈니스 가치 기준으로 Backlog 순서 재검토
2. **상위 항목 상세화** — Sprint 진입 후보 Story의 세부 조건·인수 기준을 팀과 논의
3. **INVEST 체크** — 각 Story가 INVEST 6개 기준을 충족하는지 점검
4. **Story Point 추정** — Planning Poker 등으로 팀이 함께 규모를 추정

---

### User Story Before / After 비교

| 구분                                     | 내용                                                                                                           |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Before (모호한 작성)                     | "로그인 기능 개발" — 누가 사용하는지 불명확, 가치 이유 없음, 인수 조건 없어 검증 불가, 팀마다 다르게 해석 위험 |
| After (INVEST 적용)                      | As a 회원, I want 이메일/비밀번호로 로그인하고 싶다, So that 내 계정에 안전하게 접근할 수 있다                 |
| **인수 기준 (Acceptance Criteria) 예시** |

- 올바른 이메일/비밀번호 입력 시 메인 화면으로 이동
- 잘못된 정보 입력 시 오류 메시지 표시
- 5회 연속 실패 시 계정이 일시 잠김

---

### 팀 Backlog 채우기 가이드

Backlog를 처음 구성할 때 실전 절차는 다음과 같음.

1. **기능 브레인스토밍 (Epic 단위)** — 팀 전체가 모여 제품에 필요한 큰 기능 덩어리를 나열
2. **Epic을 User Story로 분해** — 각 Epic을 "As a \~, I want \~, So that \~" 형식의 작은 단위로 쪼갬
3. **MoSCoW로 우선순위 태깅** — Must / Should / Could / Won't 기준으로 각 Story에 우선순위 부여
4. **상위 10개 INVEST 체크 및 상세화** — 우선순위 상위 항목부터 INVEST 기준으로 다듬고 인수 기준 작성
5. **Planning Poker로 추정** — 팀이 함께 Story Point를 추정하여 규모에 대한 공통 이해 형성

---

### 제품 백로그와 완료 기준 (1/2)

- **제품 백로그(Product Backlog)** — 개발할 제품 요구사항인 User Story 집합이며, 우선순위로 관리됨
- **사용자 스토리(User Story)** — 업무 범위를 구체화하기 위한 개발자 입장이 아닌, **사용자가 사용하는 관점에서 어떤 가치를 제공할 것인지를 설명**하는 단위. PO는 이 기능이 누구에게 무슨 value를 제공하는지를 설명하고, 개발자는 그 기능의 Value를 제공하기 위한 기술적 역할과 책임을 가짐
- **완료 기준(Definition of Done) / 인수 기준(Acceptance Criteria)** — User Story를 완료시키기 위한 조건 명세. Given / When / Then 형식으로 작성함

---

### 제품 백로그와 완료 기준 (2/2)

요구사항 → User Story → 제품 백로그로 이어지는 흐름을 정리하면 다음과 같음.

- User Story는 사용자 관점에서 짧게 기술된 기능 설명이며, 제품 특징·기능·기술·개선사항·오류 등 제품과 관련하여 해야 할 일 모두를 포함함
- 제품 백로그는 **우선순위가 부여된 User Story의 집합체 목록**이며, Ownership은 제품 책임자(PO)가 가짐
- 요구사항 ≒ 사용자 스토리 ≒ 백로그 ≒ 일감으로 이해할 수 있음
- **팀이 일하는 근거는 백로그가 되며, 모든 커뮤니케이션 및 성과 측정은 백로그를 중심으로 이루어짐**

---

### Release Planning (1/4)

릴리즈 계획은 **백로그의 우선순위에 기반하여 제품의 출시 계획 및 Sprint 일정을 수립**하는 활동임. Sprint Zero의 Planning 단계에서 수행됨.

구성 예시 (화물 운송 서비스):

- **Product Backlog**: 차량정보(A), 운송정보(B), 오더처리(C), 정산(D), VIP 관리(E), 카톡 연계(F) 등 Epic 단위로 구성
- **Release #1.0 (1차 오픈)**: 차주가 차량·운송 정보를 등록하고 물동량에 따라 수수료를 선택할 수 있는 기능 — A, B, C Epic의 상위 Story를 Sprint #1\~#4에 배분
- **Release #2.0 (2차 오픈)**: 화주가 오더를 내고 차주를 예약/선택할 수 있는 기능 — D(정산) Epic 추가, Sprint #5 이후로 이어짐

---

### Release Planning (2/4) — 비즈니스 우선순위 정의

릴리즈 계획의 첫 단계는 **고객 관점에서 비즈니스 우선순위를 결정**하는 것임. 이후 Release Roadmap 수립(릴리즈별 Epic 배치) → Sprint 일정 수립(Sprint 주기 결정) 순으로 진행됨.
우선순위를 정하는 대표적인 두 가지 기법은 다음과 같음.

#### MoSCoW 기법

기능을 4단계 중요도로 분류하는 방법임. 펜 비유로 설명하면 잉크 리필이 Must have, 몸통이 Should have, 뚜껑이 Could have, 회사 로고가 Won't have에 해당함.

| 등급        | 의미                                 |
| ----------- | ------------------------------------ |
| Must have   | 반드시 있어야 하는 핵심 기능         |
| Should have | 중요하지만 없어도 동작은 가능한 기능 |
| Could have  | 있으면 좋지만 우선순위 낮은 기능     |
| Won't have  | 이번 릴리즈에서는 포함하지 않는 기능 |

#### User 행동 기법

사용자가 실제로 행동하는 순서와 빈도/중요도를 기준으로 기능에 우선순위를 부여하는 방법임. 예를 들어 퀴즈 서비스라면 ① 문제 나온다 → ② 답 입력 → ③ 정답 오답 표시 → ④ 반복풀이 순서가 핵심 흐름이고, 빈도/중요도가 낮은 ⑦ 통계보기나 ⑪ 누적 점수 Rank는 뒤쪽 Sprint에 배치됨. 이 방식은 **사용자 여정을 따라가며 자연스럽게 릴리즈 단위를 나눌 수 있음.**
---

### Release Planning (3/4) — Release Roadmap 및 Sprint 일정 수립

우선순위가 정해진 제품 백로그를 릴리즈 단위로 묶고, 각 릴리즈를 여러 Sprint에 배분하는 단계임.

- Must Have 항목(User Story #1, #2)을 **Release #1.0**에 배치하고, 이후 Should Have 항목들이 Release #1.1, #1.2 등 중간 릴리즈로 이어짐
- Could Have는 **Release #2.0** 이후로 미룸
- **Sprint 주기는 2\~4주 사이**로 결정하며, 전체 기간과 출시 계획을 함께 고려함
  이 구조를 통해 팀은 언제 무엇을 릴리즈할지 이해관계자와 공유할 수 있는 **전체 로드맵**을 확보함.

---

### Release Planning (4/4) — 실제 Release Plan 예시

이해관계자와 공유하기 위한 Release Plan은 **전체 Sprint 일정과 주요 Milestone을 한 장으로 시각화**한 형태로 작성함.
예시 구조 (M개월 단위):

| 구간                                                                                                                                                                       | 주요 활동                                                                                                     |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Sprint #0 (M)                                                                                                                                                              | 요구사항 확인·상세화, To-Be 업무프로세스·화면 구성 방안, 개발환경 구성, Issue/Risk 식별                       |
| Sprint #1\~#2 (M+1\~M+2)                                                                                                                                                   | 연동 CI·CD 기술 검증, To-Be 화면 제시(Designed, Published), Service Workflow 초안, Atlassian S/W Upgrade 준비 |
| Sprint #3 (M+2\~M+3)                                                                                                                                                       | App Core CI/CD 전환 완료, To-Be ITRM Wireframe, GitLab Pipeline Update, 운영환경 구성                         |
| Sprint #4\~#5 (M+3\~M+4)                                                                                                                                                   | 핵심 영역 구현, IT지원요청 프로세스 완성, Admin 구현 (통합Test)                                               |
| Sprint #6 (M+5)                                                                                                                                                            | 시범운영, 안정화 (1차·2차 Release)                                                                            |
| 주요 Milestone: 착수보고 → Demo-day → 통합Test → 1차 Release → 2차 Release                                                                                                 |
| 시범운영 단계에서는 IT Service Desk를 통한 IT 지원요청 접수, GitLab을 통한 일감 관리·배포 연계 수행, ITRM과 병행 운영하여 **운영 반영 Risk를 최소화**하는 방식으로 진행함. |

---

### Sprint Planning (1/2)

Sprint Planning은 **Sprint 목표와 Sprint 백로그를 구체적으로 정의**하는 이벤트임. 각 Sprint 시작 시점에 전체 팀이 참여해 수행함.
**Sprint Planning Meeting에서 하는 일**

- Sprint 목표(Goal)를 한 문장으로 수립
- 목표에 필요한 제품 백로그 항목을 선정
- 백로그 완료를 위한 Task/Activity를 상세화
- 개발팀 구성원이 각자 역량에 따라 작업을 할당
- Sprint 주기와 일감 크기를 고려해 완료 일정 계획
- 스크럼 팀 전체와 Sprint 백로그 및 일정을 공유
  **주의사항**
- 스크럼 팀은 **주도적·자율적으로** 일감을 선택하며, PO가 강제 배정하지 않음
- 작업량 불균형 발생 시 개발팀이 PO와 백로그 항목을 재협상할 수 있음
- **Sprint Planning 소요시간은 Sprint 주기(2\~4주)에 따라 4\~8시간을 넘지 않도록** 함

---

### Sprint Planning (2/2) — Sprint 백로그 상세화

Sprint 백로그는 **제품 백로그 중 이번 Sprint를 위해 선택된 항목 + 이를 구현하기 위해 상세화된 Task의 묶음**임.
백로그 내용이 충분하지 않을 경우 → 제품 책임자와 함께 User Story를 먼저 구체화해야 함.
**User Story → Task 분해 예시 (HTML 편집 기능)**
Product Backlog의 Story (Story Point 20 → Refinement 후 9로 축소):

```plain text
[user role: 블로그 작성자]는
[goal: 블로그 포스팅]을 하기 위해
[task: HTML 편집 기능]을 원한다.
```

Definition of Done (정제 후):

- Preview 제공
- Preview 시 HTML5 지원
- Tag 입력 시 기존 Tag 자동으로 선제공
- 저장 버튼 클릭 시 Syntax 체크 후 Warning
  이 Story가 Sprint에 투입되면 아래 Task로 쪼개짐:
- 웹 에디터(오픈소스) 후보 조사
- 웹 에디터 검증 및 선정
- 웹 에디터 커스터마이징
- 태그 입력 및 저장 기능 개발
- Warning 창 보여주기 개발
  **Story Point 숫자가 클수록 추정 불확실성이 크다는 신호**이므로, Refinement를 통해 실현 가능한 크기로 쪼개는 것이 중요함.

---

### Daily Scrum (일일 스크럼)

일일 스크럼은 **스크럼 팀의 집중도를 높이고, 팀원 간 유대와 신뢰를 형성**하기 위한 짧은 동기화 이벤트임.
**세 가지 질문을 중심으로 진행**

- 나는 어제 하루 동안 Sprint 목표 달성을 위해 무엇을 했는지?
- 나는 오늘 하루 동안 Sprint 목표 달성을 위해 무엇을 할 것인지?
- 나 혹은 개발팀이 Sprint 목표 달성을 하는 데 방해요소가 있는지?
  **특징**
- 매일 같은 시간에 수행, **15분을 넘지 않음**
- Timebox를 지키기 위해 **서서 진행 (Stand-Up Meeting)**
- 작업 상태 공유를 위해 Sprint Board 등을 함께 활용
  **주의사항**
- 한 사람이 발언권을 독점하지 않음
- 특정 이슈의 해결 논의가 필요한 경우 **별도 SoS Meeting**으로 분리
- **Scrum Master가 원활한 진행을 책임**지며, 장애물 해소를 지원함

---

#### MSA는 정말 필요한가?

MSA(Microservice Architecture)는 도입 자체가 목적이 아님. **마이크로서비스 아키텍처로 달성해야 하는 Biz. 요구사항이 먼저 명확히 정의**되어야 함.
두 가지 현실적인 압박이 MSA 필요성을 만들어냄.

- **Time to market** — 시장 출시 속도가 점점 빨라져야 하는 압박
- **Cost of quality** — 품질 확보 비용도 함께 증가
  이 두 압박의 해답이 **"작고, 독립적인"** 서비스 단위임. 서비스를 작게 쪼개 독립적으로 개발·배포할 수 있어야 속도와 품질을 동시에 잡을 수 있음.

---

### DT Platform으로써 XaaS / MSA 개요

#### 서비스 제공 모델 비교

Application을 작은 단위로 쪼개 개발하는 것이 MicroService Architecture(MSA)의 핵심임.

| 모델       | 개념                                            |
| ---------- | ----------------------------------------------- |
| On Premise | 인프라, 서비스, 보고 생성을 모두 직접 관리      |
| IaaS       | 인프라는 제공받고, 서비스 아키텍처는 직접 관리  |
| PaaS       | 인프라·서비스 아키텍처 관리 제공받고, 앱만 관리 |
| XaaS       | 보고·결과만 받음 (Anything as a Service)        |

---

### MSA의 효과 — Cloud-Native가 아니면 현재와 동일

MSA를 도입해도 **Cloud-Native 방식으로 운영하지 않으면 기대 효과가 없음.** 아래 세 가지 질문이 그 핵심을 짚음.

- **Speed** — 한 줄의 코드 변경이 2주 후에나 반영된다는 사실이 자연스러운가?
- **Safety** — 장애 발생으로 인한 서버 다운 시간을 프로세스로 줄일 수 있다고 믿는가?
- **Scale** — DB Connection Pool이 모자라거나 이중화가 안 돼서 장애가 발생하는 것이 장애 사유가 될 수 있는가?
  세 질문에 자신 있게 답하지 못한다면, 구조만 바꾸고 Cloud-Native를 달성하지 못한 상태임.

---

### MSA 적합 영역

기존 IT 서비스 중 MSA가 적합한 영역과 그렇지 않은 영역이 나뉨.

- **빨라야 하는 것** (MSA 적합) — 커머스, 인터넷 서비스 등 빠른 변화와 빈번한 배포가 필요한 영역
- **느려도 되는 것** (MSA 효과 제한적) — 금융, 건설, 제조, 에너지/화학 등 상대적으로 변경 주기가 느리고 안정성이 우선인 영역

---

### Bounded Context Map (Domain Driven Design)

MSA 서비스 경계를 정의하는 방법으로 \*\*Domain Driven Design(DDD)\*\*의 Bounded Context를 활용함. 서비스를 도메인 단위로 모듈화하여 각 Context 내부의 모델과 언어를 독립적으로 유지함.
예시 (운송 도메인):

- **Vehicle Context** — Option, Model, Make, Warranty, Owner, Vehicle
- **Transport Context** — Transport, Transport Consumer, Transport Supplier, Transported Item, Location
- **Business Partner Context** — BusinessPartner, Contact, Address
  컨텍스트 간 경계(점선)를 넘을 때는 명시적인 관계(빨간 화살표)로 연결됨. 이 경계가 곧 **마이크로서비스의 분리 단위**가 됨.

---

### MSA에서 DB는 어떻게?

Monolith → MSA로 전환할 때 DB도 함께 분리됨. 흐름은 다음과 같음.
**Application 모듈화 → API만으로 Communication → Database 분리**

| 구조                                                                                                                                                    | 특징                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| Monolithic                                                                                                                                              | 단일 Silo logic, 단일 Silo database                     |
| Internally componentized                                                                                                                                | 로직은 분리되었으나 DB는 아직 공유                      |
| Microservices                                                                                                                                           | 각 Microservice component가 자신의 DB를 독립적으로 소유 |
| 서비스 간 직접 DB 접근은 금지되며, **API를 통해서만 데이터를 주고받음.** DB 분리는 큰 리팩토링 작업이므로 _Refactoring Databases_ 같은 방법론을 참고함. |

---

#### Cloud Application 유형별 상세 비교

| 특징          | Cloud Ready                                     | Cloud Friendly                                         | Cloud Native                                |
| ------------- | ----------------------------------------------- | ------------------------------------------------------ | ------------------------------------------- |
| 전환 유형     | Replatforming                                   | Refactoring                                            | ReArchitecturing                            |
| 전환 이점     | PaaS 플랫폼 사용 이점                           | 자동 스케일링, 설정 자동화, 신규 환경 적응 비용 최소화 | 새 요구사항·장애에 빠른 대응                |
| 전환 고려사항 | PaaS 배포를 위해 수정해야 할 내용               | Scalability, 설정 자동화, CI/CD                        | Microservice                                |
| 기술 요건     | PaaS 플랫폼 특징 이해                           | 12factor, 배포 파이프라인                              | Design for failure, API First, Event driven |
| 전환 목적     | 진화된 Cloud Application으로 발전하기 위한 단계 | 현재 아키텍처 수준에서 클라우드 효과 최대화            | 변화·수정에 유연한 구조로 전환              |

- Cloud Application 유형 분류는 절대 기준이 아니라 **단계적으로 진화 가능한 수준을 보여주기 위한 분류**임
- 실제 전환 시 기존 시스템 특성에 따라 최대 효과를 낼 수 있는 전환 수준을 도출해야 함
- **Cloud Ready \< Cloud Friendly \< Cloud Native** 순으로 성숙도가 높아지며, Cloud Native 설계 시 하위 단계의 특징을 모두 고려해야 함

---

#### Replatforming — Cloud Ready 고려사항

| 영역    | 고려사항               | 설명                                                                                                            |
| ------- | ---------------------- | --------------------------------------------------------------------------------------------------------------- |
| JDK     | JDK 버전               | 빌드팩에서 지원하는 JDK 버전 확인 및 업그레이드 필요                                                            |
| Library | Spring Framework 버전  | 빌드팩에서 지원하는 버전 확인 및 업그레이드                                                                     |
| Library | WAS 및 JAVA Dependency | WAS, JDK 변경에 따른 라이브러리 오류 발생 시 최신 library로 대체하거나 불필요한 것은 삭제 (ex. JDBC 업그레이드) |
| Library | 3rd party library      | PaaS에서 구동 가능한지 확인, 필요 시 교체 (설치형 → 클라우드 호환형)                                            |
| Library | 기타                   | 3rd party library의 라이선스가 Cloud 환경에서 적합한지 확인                                                     |

---

#### Refactoring — Cloud Friendly를 위한 12 Factors 리팩토링

12 Factors는 **Cloud Application 구축을 위한 표준 설계 원칙**으로, 개발 방법 및 개발/운영 환경을 포함함. PaaS와 DevOps만으로도 4\~7개 Factor를 달성할 수 있음.

| #                                                                                                                                                                                           | Factor         | 달성 방법                        | 주요 수단                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | -------------------------------- | ------------------------ |
| 1                                                                                                                                                                                           | 동일한 Repo    | 개발/운영을 하나의 저장소로 관리 | DevOps Pipeline          |
| 2                                                                                                                                                                                           | 의존성 설정    | 소스가 아닌 설정으로 의존성 관리 | Maven                    |
| 3                                                                                                                                                                                           | 환경변수       | 소스가 아닌 환경변수로 관리      | ENV, Spring Config       |
| 4                                                                                                                                                                                           | 서비스바인딩   | DB, 연계는 서비스바인딩으로 간주 | Backing Services         |
| 5                                                                                                                                                                                           | 릴리스 분리    | 빌드/릴리스/실행의 완전한 분리   | DevOps Pipeline          |
| 6                                                                                                                                                                                           | 무상태         | 무상태 처리를 기본으로 함        | Stateless/Shared Nothing |
| 7                                                                                                                                                                                           | Self-Contained | 컨테이너가 아닌 앱 자체가 URL    | Menifest & Container     |
| 8                                                                                                                                                                                           | 동시성         | 스케일 아웃을 위한 프로세스 모델 | Router, Microservices    |
| 9                                                                                                                                                                                           | 빠른 Reboot    | 빠른 부팅과 Graceful 셧다운      | Cloud Foundry Container  |
| 10                                                                                                                                                                                          | 실행환경일치   | 개발/검증/운영 환경 일치         | DevOps Pipeline          |
| 11                                                                                                                                                                                          | 중앙 로깅      | 플랫폼에서 이벤트 로그를 수집    | Metric & Logging         |
| 12                                                                                                                                                                                          | JOB 관리       | DB 변경과 같은 JOB을 소스에 포함 | Infrastructure as a Code |
| Cloud Friendly 전환 실무에서는 **Code Inspector** 같은 도구로 12 Factors 위배 요소를 자동 탐지하고 리포팅함. 예를 들어, 이메일 주소를 하드코딩하는 것이 Factor 3(환경변수) 위반으로 검출됨. |

---

#### ReArchitecture — Cloud Native Microservice 아키텍처 설계

Cloud Native 상태를 위한 Microservice 아키텍처의 전체 처리 흐름은 다음과 같음.

**Client → Edge Layer (BFF + API G/W) → Microservices (PaaS) → Legacy**

- **BFF (Backend For Frontend)** — 채널별(Web UI, Mobile UI, 3rd Party UI) 화면 UI 구성을 위한 Data를 처리하여 Client에 전달하는 Application
- **API G/W** — BFF의 요청을 받아 Microservice를 호출하고, 전달받은 Data를 BFF로 전달하는 Gateway. Load Balancing 역할도 담당
- **ACL (Anti-Corruption Layer)** — Microservice의 변화에 따른 Legacy Application 수정을 최소화하기 위한 Adaptor
- **PaaS** — 여러 Microservice가 각자의 DB와 함께 독립 운영됨

---

#### 모놀리식 인증/로그인 vs SOLID 적용 구조

#### Before — Pure Java 단일 클래스의 문제

- `LoginService` 클래스 하나가 입력 검증, 비밀번호 확인, 세션 생성, 로그 기록을 모두 담당
- 책임이 얽혀 있어 **인증 로직만 따로 재사용하거나 다른 서비스로 옮기기 어려움**
- 테스트 시 전체 클래스를 실행해야 하며, 일부 로직만 검증하기 힘듦

#### After — SOLID 적용 후 구조

- **SRP** — CredentialValidator / SessionManager / AuthLogger로 책임 분리
- **OCP** — 인증 방식(비밀번호/OAuth) 추가 시 기존 코드 수정 없이 확장
- **DIP** — UserRepository 인터페이스에 의존, 구현체는 주입받아 교체 가능
  분리된 CredentialValidator/SessionManager가 각각 **인증서버의 독립 컴포넌트로 이관**됨.

---

#### SOLID 원칙 정리 (Java SpringBoot 예시)

| 약자    | 원칙                 | 핵심 내용                                                | SpringBoot 예시                              |
| ------- | -------------------- | -------------------------------------------------------- | -------------------------------------------- |
| S (SRP) | 단일 책임 원칙       | 하나의 클래스는 하나의 책임만 가져야 함                  | Controller, Service, Repository 등 계층 분리 |
| O (OCP) | 개방-폐쇄 원칙       | 기존 코드는 수정하지 않고 기능을 확장할 수 있어야 함     | 인터페이스 기반 구현체 추가, 전략 패턴 활용  |
| L (LSP) | 리스코프 치환 원칙   | 부모 타입 대신 자식 객체를 사용해도 동일하게 동작해야 함 | 인터페이스 구현체 교체 가능                  |
| I (ISP) | 인터페이스 분리 원칙 | 필요한 기능만 가진 작은 인터페이스로 분리                | 역할별 인터페이스 설계                       |
| D (DIP) | 의존성 역전 원칙     | 구현 클래스가 아닌 추상화(인터페이스)에 의존             | Spring의 DI와 IoC의 핵심 원칙                |

---

#### 실행 시나리오 — 인증/로그인 컴포넌트 분리 매핑

모놀리스의 LoginService를 SOLID 적용 후 MSA 서비스로 분리하는 구체적 매핑임.

| 기존 모놀리스 컴포넌트                                                                             | SOLID 적용 후 역할                       | 이관될 MSA 서비스                             |
| -------------------------------------------------------------------------------------------------- | ---------------------------------------- | --------------------------------------------- |
| CredentialValidator                                                                                | 회원 자격 검증 (SRP 적용)                | 인증서버 (Auth Server) 내부 로직              |
| SessionManager / TokenIssuer                                                                       | 세션 관리 → JWT/OAuth 토큰 발급으로 전환 | 인증서버 (Auth Server) OAuth 모듈             |
| LoginController                                                                                    | 요청 수신 및 응답 반환                   | API Gateway 진입점 + 인증서버 REST API        |
| AuthLogger                                                                                         | 인증 이력 기록                           | 이벤트 발행 후 Kafka로 비동기 전달 (Sprint 3) |
| **이 매핑표가 Sprint 1의 Product Backlog 항목(= User Story)이 되며, 다음 단계에서 Task로 분할됨.** |

---

#### 인증서버 & API Gateway 개요 (1/4)

이 섹션에서 다루는 내용:

- 인증(Authentication)/인가(Authorization) 흐름 — OAuth 2.0 및 JWT 토큰 발급·검증
- API Gateway의 역할 — 모든 요청의 단일 진입점, 라우팅 및 인증 필터 처리
- 기반 코드 구조 설명 (인증서버 프로젝트 / Gateway 프로젝트)
- Sprint 1 Planning부터 실제 구현 프로세스까지 이어짐

---

#### Sprint 1 Planning — 인증서버(OAuth) 구축 Task 분할

**Sprint 목표: Pure Java 인증/로그인을 SOLID 적용 후 Spring Boot 기반 OAuth 인증서버로 전환한다**

| Task                                | 세부 내용                                                     | Point |
| ----------------------------------- | ------------------------------------------------------------- | ----- |
| 기존 로그인 로직 분석               | CredentialValidator/SessionManager 등 책임 단위 식별          | 3     |
| SOLID 리팩토링                      | SRP/OCP/DIP 적용하여 인터페이스·클래스 분리                   | 5     |
| Spring Boot 프로젝트 구조화         | 분리된 클래스를 Spring Boot 프로젝트로 이관                   | 3     |
| OAuth 2.0 Authorization Server 설정 | Spring Authorization Server 설정 및 토큰 발급 엔드포인트 구현 | 5     |
| Gateway 라우팅 설정                 | 인증서버로 향하는 라우팅 규칙 및 인증 필터 구성               | 3     |

---

#### SOLID → Spring Boot OAuth 인증서버 구현 프로세스 (3/4)

1. **기존 Pure Java 로그인 로직 분석** — LoginService 내부에서 검증/세션/로깅 책임이 어떻게 얽혀 있는지 식별
2. **인터페이스 분리 (SRP/DIP 적용)** — CredentialValidator, TokenIssuer 등을 인터페이스로 책임 분리하고 구현체는 주입
3. **Spring Boot 프로젝트로 이관** — 분리된 클래스를 `@Service`/`@Component`로 등록, 기존 로직은 최대한 재사용
4. **OAuth 2.0 Authorization Server 구성** — `spring-security-oauth2-authorization-server`로 토큰 발급 엔드포인트 구현
5. **Gateway 인증 필터 연동** — Gateway에서 발급된 JWT를 검증하는 필터를 추가해 인증서버와 연결

---

#### 실행 시나리오 — Gateway 라우팅 & 인증 필터 데모 (4/4)

**수강신청 시스템 로그인 요청 흐름**
학생 로그인 요청 → API Gateway 수신 → 인증서버로 라우팅 → OAuth 토큰 발급 → **Gateway 필터 검증**
**데모 진행 대본**

- ① 학생이 Postman(또는 프론트)으로 `/api/login`에 학번/비밀번호를 전송
- ② Gateway가 요청을 인증서버로 라우팅 (Eureka에서 위치 조회, Sprint 2에서 연동)
- ③ 인증서버가 CredentialValidator로 자격을 검증 후 OAuth 토큰(JWT)을 발급
- ④ 이후 모든 요청은 Gateway의 인증 필터가 토큰을 검증한 뒤 대상 서비스로 전달

---

#### 서비스 디스커버리(Eureka) & 서비스 간 통신 (1/4)

이 섹션에서 다루는 내용:

- Eureka의 서비스 등록(Register)/조회(Discovery) 원리
- 동기(REST) 통신과 비동기(Kafka) 통신의 차이 및 각각의 적용 상황
- 서비스 간 통신 시 장애 대응(Fallback 등) 개념
- Sprint 2 Planning부터 실제 연동 과정까지 이어짐

---

#### Sprint 2 Planning — Eureka 연동 Task 분할

**Sprint 목표: 인증서버·Gateway·수강신청 서비스가 서로를 자동으로 찾아 통신하게 한다**

| Task                           | 세부 내용                                                              | Point |
| ------------------------------ | ---------------------------------------------------------------------- | ----- |
| Eureka Server 구축             | Spring Cloud Netflix Eureka Server 프로젝트 생성 및 실행               | 3     |
| 각 서비스에 Eureka Client 등록 | 인증서버·Gateway·수강신청 서비스에 `@EnableEurekaClient` 적용          | 3     |
| Gateway 동적 라우팅 설정       | 서비스명 기반 라우팅으로 전환 (고정 IP 제거)                           | 3     |
| 서비스 간 REST 호출 구현       | 수강신청 서비스가 인증서버 사용자 정보를 조회하는 REST 클라이언트 구현 | 5     |

---

#### Eureka 등록/조회 실전 연동 프로세스 (3/4)

1. **Eureka Server 실행** — `spring-cloud-starter-netflix-eureka-server` 의존성 추가 후 기본 포트(8761)로 기동
2. **각 서비스에 Client 설정 추가** — `application.yml`에 `eureka.client.service-url` 지정, `@EnableEurekaClient` 어노테이션 부여
3. **서비스 등록 확인** — Eureka 대시보드에서 인증서버·Gateway·수강신청 서비스가 모두 등록되었는지 확인
4. **Gateway 라우팅을 서비스명 기반으로 전환** — `lb://AUTH-SERVICE` 형태로 라우팅 규칙 수정 (고정 IP 제거)
5. **서비스 간 호출 테스트** — 수강신청 서비스에서 인증서버를 이름으로 호출해 정상 응답 확인

---

#### 실행 시나리오 — 수강신청 서비스의 인증서버 탐색 흐름 (4/4)

**흐름**: 수강신청 요청 수신 → Eureka에 AUTH-SERVICE 위치 조회 → 인증서버로 REST 호출 → 사용자 정보 확인 → **수강신청 처리**
**데모 진행 대본**

- ① 학생이 로그인 후 발급받은 토큰으로 `/api/courses/apply` 요청
- ② 수강신청 서비스가 Eureka에게 "AUTH-SERVICE 어디 있어?"라고 조회
- ③ Eureka가 인증서버의 현재 위치(IP:Port)를 응답
- ④ 수강신청 서비스가 해당 위치로 직접 REST 호출하여 사용자 유효성 확인 후 신청 처리

---

#### Kafka 기본 (1/4)

이 섹션에서 다루는 내용:

- Producer / Consumer / Topic 핵심 개념
- MSA에서 이벤트 기반(비동기) 통신이 필요한 이유 — 서비스 간 느슨한 결합
- 제공되는 기반 코드의 Kafka 연동 구조 설명
- Sprint 3 Planning부터 수강신청 이벤트 데모까지 이어짐
  **핵심 3요소**
  | 구성 요소 | 역할 |
  | --- | --- |
  | Producer | 데이터를 생성해 Topic으로 전송하는 주체 |
  | Topic | 메시지가 저장·분류되는 논리적 채널 |
  | Consumer | Topic을 구독해 메시지를 읽어가는 주체 |
  REST(동기) 통신과 달리 Kafka(비동기) 통신은 **Producer가 메시지를 보낸 뒤 Consumer의 응답을 기다리지 않음.** 서비스 간 결합도를 낮추는 것이 핵심 효과임.

---

#### Sprint 3 Planning — Kafka 연동 Task 분할

**Sprint 목표: 수강신청 완료 시 이벤트를 발행하고, 다른 서비스가 이를 비동기로 구독한다**

| Task                            | 세부 내용                                                          | Point |
| ------------------------------- | ------------------------------------------------------------------ | ----- |
| Kafka 브로커 기동 및 Topic 생성 | `course-applied` Topic 생성, Partition/Replication 기본값 설정     | 2     |
| Producer 구현                   | 수강신청 서비스에 KafkaTemplate으로 이벤트 발행 로직 작성          | 3     |
| Consumer 구현                   | 알림 서비스(또는 로그 서비스)에서 `@KafkaListener`로 이벤트 구독   | 3     |
| 통합 테스트                     | 수강신청 → 이벤트 발행 → 구독 서비스 로그 확인까지 End-to-End 검증 | 3     |

---

#### Kafka Producer/Consumer 구현 프로세스 (3/4)

1. **Topic 설계** — `"course-applied"` 등 이벤트 성격이 드러나는 이름으로 Topic 이름 결정
2. **Producer 작성** — 수강신청 처리 로직 마지막에 `KafkaTemplate.send()`로 이벤트 발행
3. **이벤트 메시지 설계** — 학번·과목코드·신청시각을 포함한 **최소한의 JSON 페이로드**로 구성
4. **Consumer 작성** — `@KafkaListener(topics="course-applied")`로 구독 서비스에서 이벤트 수신
5. **장애 대응 고려** — Consumer 처리 실패 시 **재시도** 또는 **Dead Letter Topic** 개념 적용

---

#### 실행 시나리오 — 수강신청 완료 이벤트 발행/구독 데모 (4/4)

**흐름**: 수강신청 완료 → course-applied 이벤트 발행 → Kafka Topic 적재 → 알림 서비스 구독 → **완료 알림 로그 출력**
**데모 진행 대본**

- ① 학생이 원하는 과목에 수강신청을 완료
- ② 수강신청 서비스가 `course-applied` Topic으로 이벤트(학번/과목코드/시각)를 발행
- ③ 알림 서비스가 해당 Topic을 구독하고 있다가 이벤트를 즉시 수신
- ④ 알림 서비스 콘솔에 "OOO님 OOO 과목 신청 완료" 로그가 실시간으로 출력됨을 시연

---

#### 서비스 간 통신 — Circuit Breaker

MSA에서 한 서비스가 장애가 나면 **의존하는 다른 서비스로 장애가 전파(Cascade Failure)될 수 있음.** Circuit Breaker는 이를 막기 위한 패턴임.
**역할 — 실패에 대한 설계**

- 서비스 간 의존성이 발생하는 접근 포인트에 설계하여 **장애 전파를 막고 fallback 함수를 지원**함
- 현재 Circuit Breaker의 상태를 **대시보드(Hystrix Stream 등)를 통해 모니터링**함
  동작 방식: 특정 서비스 호출 실패율이 임계치를 넘으면 Circuit이 "Open" 상태로 전환되고, 이후 요청은 실제 서비스로 가지 않고 즉시 fallback 응답을 반환함. 일정 시간 후 다시 "Half-Open" 상태로 전환해 복구 여부를 확인함.

---

#### 서비스 간 통신 — Anti-Corruption Layer (ACL)

MSA에서 서비스 간에는 **API만으로 통신하며, 서로 모델을 직접 공유하지 않음.** 필요한 경우 API를 호출한 서비스에서 **Anti-Corruption Layer를 두고 API 결과를 이 영역에서 가공**함.
**핵심 원칙**

- 마이크로서비스는 각 서비스가 다른 서비스와 영향 없이 **독립적으로 개발**하는 것이 가장 중요함
- 서비스 간 모델을 서로 공유하는 형태가 아니라, **API 결과를 가져와 자기 서비스에서 가공하여 사용**하는 방식으로 개발함
- 서비스별 중복 코드 발생은 허용되며, 중복 데이터 발생도 허용함
  예시: Sales Context의 `Customer`와 Support Context의 `Customer`는 같은 이름이지만 서로 다른 모델로 독립 유지됨. ACL이 두 Context 사이의 변환을 담당함.

---

#### 서비스 간 통신 — Monitoring

MSA는 여러 마이크로서비스가 하나의 단일 애플리케이션으로 구성되므로, **서비스 간 연계에서 오는 복잡도가 증가함.** 따라서 단일 서비스는 물론 **여러 마이크로서비스의 연관관계에 대한 모니터링이 필수**임.
주요 모니터링 도구:

- **분산 추적(Distributed Tracing)** — 하나의 요청이 여러 서비스를 거칠 때 각 구간의 응답 시간을 시각화함 (예: edge-service → catalog-service → inventory-service 흐름의 각 소요시간 확인)
- **Circuit Breaker 대시보드(Hystrix Stream)** — getCatalog, getProduct 등 각 Circuit의 상태(Closed/Open), 에러율, 응답 시간 분포, Thread Pool 상태를 실시간 모니터링

---

<empty-block/>

## 보충 — [8/26] Agile 방법론 및 MSA 개발_개인 서브 노트

> 원문: [Notion 페이지](https://app.notion.com/p/3c81d84bf68e80e0bf55fa1654595ac5)

- **사례(AgentPass)**: 기존 수강신청 서비스의 `Course`/`Enrollment`를 Mission/Passport 도메인으로 전환하고, 자연어 업무 요청에 맞춘 Agent·최소 권한 추천과 관리자 승인 흐름을 설계했다.
- **Agile 적용**: 제한된 실습 시간에 맞춰 50분 작업과 5분 스크럼을 반복했으며, Sprint Review에서는 결제부터 Kafka를 거친 크레딧 반영과 화면 잔액 변경까지 E2E 기준으로 확인했다.
- **MSA 경계**: User·Course(Mission)·Enrollment(Passport)·Payment·Recommend를 API로 분리했다. 서비스 간 존재 여부 확인도 직접 DB 조회가 아니라 내부 API로 처리한 사례다.
- **운영상 학습**: 독립 배포에서는 애플리케이션과 DB 스키마의 배포 순서, 이벤트 소비자의 하위 호환성, 내부 API의 URL·응답 계약 통일이 함께 관리되어야 한다. 원문은 `ddl-auto`에 의존한 제약 변경 실패와 서비스별 설정/API 계약 불일치를 사례로 든다.
