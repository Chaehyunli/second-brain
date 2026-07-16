---
source: Notion Information
notion_url: https://app.notion.com/p/39a1d84bf68e81e5b2f0d3d7f60b70c2
notion_page_id: 39a1d84b-f68e-81e5-b2f0-d3d7f60b70c2
synced_at_utc: 2026-07-16T05:40:05Z
---

<callout icon="🔎" color="blue_bg">
	**조사 기준:** 공식 문서와 GitHub 저장소, 이 서버의 실제 Hermes 상태를 함께 확인했다.
	- 공식 문서: [Hermes Agent Docs](https://hermes-agent.nousresearch.com/docs)
	- 소스 저장소: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
</callout>

## 한 줄 정의

**Hermes Agent**는 Nous Research가 개발한 오픈소스 자율형 AI 에이전트 프레임워크다. 단순 챗봇이나 IDE 전용 코딩 보조 도구가 아니라, LLM이 도구를 호출해 파일·터미널·웹·브라우저·메신저·스케줄러를 실제로 사용하면서 작업을 수행하도록 설계됐다.

## 1. 핵심 특징

<table fit-page-width="true" header-row="true">
	<tr>
		<td>영역</td>
		<td>설명</td>
	</tr>
	<tr>
		<td>지속 메모리</td>
		<td>사용자 선호, 환경, 장기 맥락을 세션 간 보존한다.</td>
	</tr>
	<tr>
		<td>Skills</td>
		<td>반복 작업 절차를 SKILL.md 형태로 축적하고 다음 작업에서 재사용한다.</td>
	</tr>
	<tr>
		<td>다중 플랫폼</td>
		<td>CLI, TUI, Desktop, Web Dashboard와 Discord·Telegram·Slack·WhatsApp 등 메신저를 지원한다.</td>
	</tr>
	<tr>
		<td>실행 도구</td>
		<td>터미널, 파일 편집, 웹 조사, 브라우저 자동화, 이미지 생성·분석, TTS 등을 연결할 수 있다.</td>
	</tr>
	<tr>
		<td>모델 유연성</td>
		<td>OpenAI Codex OAuth, Anthropic, OpenRouter, Gemini, xAI, 로컬/커스텀 엔드포인트 등 여러 공급자를 사용할 수 있다.</td>
	</tr>
	<tr>
		<td>자동화</td>
		<td>cron 기반 정기 작업과 웹훅 기반 이벤트 트리거를 지원한다.</td>
	</tr>
	<tr>
		<td>확장성</td>
		<td>MCP 서버, 플러그인, 커스텀 도구, 프로필 분리를 제공한다.</td>
	</tr>
</table>

## 2. 일반 챗봇과의 차이

Hermes의 핵심 흐름은 **대화 → 실행 → 검증 → 기억**이다.

예를 들어 “매일 아침 주식 뉴스를 정리해줘”라는 요청을 받으면, 단순 답변 생성에 그치지 않고 다음을 수행할 수 있다.

1. 정기 실행 작업을 등록한다.
2. 웹·API·문서에서 최신 근거를 수집한다.
3. 지정된 형식으로 요약하고 출처를 남긴다.
4. Discord 같은 대상 채널로 전달한다.
5. 사용자 선호 종목, 언어, 전달 형식을 이후 실행에도 반영한다.

따라서 개인 비서, 개발 에이전트, 리서치 자동화, 지식관리, 서버 운영 도우미 역할을 하나의 시스템에서 조합할 수 있다.

## 3. 주요 구성 요소

- **Profile**: 목적별로 모델·도구·기억·설정을 분리하는 독립 실행 공간
- **Skill**: 성공한 작업 절차를 문서화해 재사용하는 절차 지식
- **Memory**: 사용자 선호와 장기 사실을 세션 간 유지하는 저장소
- **MCP**: 외부 서비스와 도구를 에이전트 도구처럼 연결하는 표준
- **Gateway**: Discord 같은 메신저와 Hermes 실행 엔진을 연결하는 계층
- **Cron / Webhook**: 시간 기반 또는 이벤트 기반 자동화
- **Delegation / Kanban**: 복잡한 작업을 격리된 여러 에이전트에 분배하는 기능

## 4. 이 서버의 확인된 상태

<callout icon="✅" color="green_bg">
	2026-07-11 UTC 기준으로 실제 설치 상태를 확인했다.
</callout>

- Hermes Agent: `v0.18.2 (2026.7.7.2)`
- 설치 방식: Git 설치
- Python: `3.11.15`
- 기본 모델: `gpt-5.6-terra`
- 기본 공급자: OpenAI Codex OAuth
- Discord Gateway: 구성 및 실행 중
- 예약 작업: 활성 작업이 존재하며, Discord 기반 자동화에 사용 중
- 터미널 실행 환경: 로컬 Linux

> 위 상태는 조사 시점의 운영 환경 점검 결과이며, 자격 증명·토큰 값은 기록하지 않는다.

## 5. 활용 분야

- **개발:** 코드 작성, 리팩터링, 테스트, GitHub 이슈·PR 작업
- **리서치:** 뉴스·논문·시장·커뮤니티 반응 수집 및 비교
- **개인 지식관리:** Notion/Obsidian 정리, 문서화, 개인 LLM Wiki 구축
- **정기 브리핑:** 주식, AI 뉴스, 채용공고, 서버 상태 알림
- **운영 자동화:** cron, webhook, 로그 점검, 반복 작업 실행
- **다중 채널 비서:** 여러 메신저에서 동일한 도구와 개인화 맥락을 활용

## 6. 장점과 운영 시 유의점

### 장점

- 특정 모델·벤더에 고정되지 않는 구조
- 메모리와 Skills를 통한 사용자별 개인화 누적
- 채팅, 서버, 문서, 자동화를 한 작업 흐름으로 통합 가능
- 오픈소스이므로 플러그인·도구를 직접 확장할 수 있음

### 유의점

- 터미널·파일·메신저 권한이 강력하므로 **승인 정책과 권한 분리**가 중요하다.
- Skills와 메모리가 쌓이면 중복·오래된 절차가 생길 수 있어 정기적인 점검과 정리가 필요하다.
- 자동화는 수집 작업과 판단·전송 작업을 분리하면 비용, 오류, 유지보수 부담을 낮출 수 있다.
- 프로필별로 비밀값·도구·기억을 분리하면 운영 안정성과 보안성이 높아진다.

## 최종 요약

Hermes는 **대화형 AI를 실제 작업 실행 시스템으로 확장하고, 그 과정에서 사용자별 지식과 자동화 역량을 누적시키는 오픈소스 에이전트 플랫폼**이다. 이 환경에서는 Discord를 접점으로 삼아 리서치, Notion 정리, 정기 브리핑, 개발·운영 업무를 연결하는 방식으로 활용할 수 있다.
