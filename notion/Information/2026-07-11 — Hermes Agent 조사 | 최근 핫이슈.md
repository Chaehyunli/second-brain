---
source: Notion Information
notion_url: https://app.notion.com/p/39a1d84bf68e81e5b2f0d3d7f60b70c2
notion_page_id: 39a1d84b-f68e-81e5-b2f0-d3d7f60b70c2
synced_at_utc: 2026-08-20T04:18:03Z
notion_content_sha256: ea87dabdf0c158622dc9fee7cae25fb1c361da8d286ef1c667425c1c8d64873e
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
<td>반복 작업 절차를 스킬 문서 형태로 축적하고 다음 작업에서 재사용한다.</td>
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
---
## 7. 출처·관심도 근거
<callout icon="📌" color="yellow_bg">
	앞선 요약에서 부족했던 부분을 보강했다. 아래 수치는 **2026-07-11 UTC에 GitHub 공식 REST API와 공식 문서에서 직접 확인한 값**이다. GitHub 별 수는 개별 글의 좋아요가 아니라, Hermes Agent 저장소 전체에 대한 공개 관심도 지표다.
</callout>
### 7.1 핵심 출처
<table fit-page-width="true" header-row="true">
<tr>
<td>플랫폼·출처</td>
<td>확인한 내용</td>
<td>관심도·신뢰도 근거</td>
</tr>
<tr>
<td>[GitHub — NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)</td>
<td>Hermes의 공개 소스 저장소. 프로젝트 설명은 “The agent that grows with you”이며, 기본 브랜치는 main이다.</td>
<td>⭐ **212,874 stars** · 🍴 **39,315 forks** · 👁️ **830 subscribers**. 오픈소스 에이전트 프로젝트로서 매우 큰 공개 관심과 파생·실험 수요를 보여주는 지표다.</td>
</tr>
<tr>
<td>[GitHub Release — v2026.7.7.2](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.7.7.2)</td>
<td>조사 시점 설치 버전과 동일한 `Hermes Agent v0.18.2 (2026.7.7.2)` 릴리스다.</td>
<td>2026-07-08 공개. 실제 설치 버전과 릴리스 태그가 일치해, 기능 설명을 단순 홍보 문구가 아니라 현재 배포 흐름과 대조할 수 있다.</td>
</tr>
<tr>
<td>[공식 문서 — Hermes Agent Docs](https://hermes-agent.nousresearch.com/docs)</td>
<td>설치, CLI, Skills, Memory, Gateway, MCP, Cron, Profiles 등의 사용자·운영 문서다.</td>
<td>개별 반응 수는 제공하지 않지만, 프로젝트 운영 주체가 제공하는 **1차 출처**다. 지원 범위와 설정 방법의 사실 확인에 사용했다.</td>
</tr>
</table>
### 7.2 GitHub 지표 해석
- ⭐ **Stars 212,874개**: 사용자가 저장소를 북마크·관심 프로젝트로 표시한 누적 수다. 실제 활성 사용자 수나 품질을 직접 증명하지는 않지만, 공개 인지도와 탐색 수요의 강한 신호다.
- 🍴 **Forks 39,315개**: 코드를 복제해 수정·실험·파생 개발하려는 움직임의 누적 수다. Stars보다 더 높은 실행 의도를 포함할 수 있지만, 자동화된 fork·일회성 실험도 섞일 수 있다.
- 📂 **Open issues 27,619개**: GitHub API의 이 값은 열려 있는 이슈와 Pull Request를 함께 포함할 수 있다. 따라서 “버그가 27,619개”라는 뜻은 아니며, 큰 기여자·개발 논의량이 있다는 맥락으로만 해석해야 한다.
- 🧾 **MIT License**: 수정·재배포·상용 활용의 법적 제약이 비교적 낮은 오픈소스 라이선스라서, 플러그인·도구·개인화 자동화를 확장하려는 사용자에게 중요한 선택 근거가 된다.
### 7.3 이번 조사에서 확인한 실제 관심 신호
1. **대규모 저장소 반응**: 21만 개 이상 Stars와 3.9만 개 이상 Forks는 Hermes가 단순한 소규모 개인 프로젝트가 아니라, 폭넓은 개발자 커뮤니티의 관찰·실험 대상임을 보여준다.
2. **빠른 변경 흐름**: 조사 당일에도 저장소 업데이트가 확인됐고, 설치된 버전은 2026-07-08 공개 릴리스와 일치했다. 기능이나 CLI 사용법은 오래된 블로그보다 공식 문서·릴리스를 우선 확인해야 한다.
3. **운영 복잡도도 함께 존재**: 높은 관심도와 별개로 이슈·PR 규모가 크므로, 새 기능을 그대로 도입하기보다 현재 환경에서 권한·모델·Gateway·자동화 충돌 여부를 검증하면서 적용하는 것이 적절하다.
### 7.4 출처 해석의 한계
- GitHub Stars·Forks는 **저장소 전체의 누적 지표**이며, 특정 기능(Skills, Cron, Discord 등) 하나의 인기나 만족도를 직접 측정하지 않는다.
- 공식 문서는 정확한 기능 확인에는 강하지만, 사용자 불만·도입 난이도 같은 커뮤니티 체감은 충분히 보여주지 못한다.
- 따라서 향후 Hermes 기능을 도입하거나 비교 조사할 때는 공식 문서·릴리스뿐 아니라 GitHub 이슈, 실제 사용자 사용 사례, 관련 커뮤니티 반응을 분리해 추가 확인하는 방식이 좋다.