---
title: "[7/14] Git & AI코딩 & 환경구성 — 강의 정리"
notion_page_id: "39d1d84b-f68e-8134-9337-f9f71471b3e3"
source_url: "https://app.notion.com/p/39d1d84bf68e81349337f9f71471b3e3"
---

# [7/14] Git & AI코딩 & 환경구성 — 강의 정리

## 원문
[Notion 원문 — 64개 슬라이드](https://app.notion.com/p/39d1d84bf68e81349337f9f71471b3e3)

## 학습 목표
이 강의의 흐름은 **IT 용어와 웹 구조 이해 → macOS 개발 환경 준비 → VS Code·Git으로 작은 결과물을 검증·배포 → Codex CLI로 생성·리뷰·테스트를 반복**하는 것이다. 도구를 설치하는 것보다, 각 도구가 개발·협업·운영 흐름에서 왜 필요한지 이해하고 실제 결과로 검증하는 습관이 핵심이다.

## 1. 제품·운영·협업에서 쓰는 기본 언어 (슬라이드 3~11)
### 화면과 사용자 경험
| 용어 | 의미 | 실무에서 확인할 점 |
| --- | --- | --- |
| Wireframe | 색·폰트·이미지 전의 화면 구조 | 콘텐츠 우선순위와 영역 배치 |
| Mock-up | 시각 디자인을 적용한 정적 시안 | 브랜드 톤과 디자인 결과 |
| Prototype | 클릭·이동을 연결한 시제품 | 사용자 흐름·예외 흐름 |
| Persona | 대표 사용자를 구체화한 모델 | 기능이 누구의 문제를 푸는가 |
| IA | 메뉴·페이지·콘텐츠의 전체 구조 | 탐색성과 정보 우선순위 |
| Design System | 재사용 가능한 UI 규칙 | 화면이 늘어도 일관성 유지 |

UI는 화면 자체이고 UX는 사용자가 목표를 달성하는 전체 과정이다. 예쁜 화면이 곧 좋은 UX는 아니므로, 프로토타입에서 실제 흐름을 검증해야 한다.

### 출시와 운영
MVP는 기능을 적게 넣는 제품이 아니라 **검증할 가설에 필요한 최소 핵심가치**다. Release는 버전을 내보내는 행위, Launch는 공식 공개, Go-Live는 운영 환경 시작 시점이다. Deployment는 결과물을 서버·클라우드에서 실행 가능하게 만드는 작업이다.

Rollout은 단계 공개, Rolling Update는 서버를 순차 교체해 중단을 줄이는 방식이다. Hotfix·Patch·Rollback을 구분하고, 배포 계획에는 항상 “문제가 생기면 어디까지·어떻게 되돌릴지”를 포함한다. Issue는 실행 단위, Roadmap은 방향·우선순위를 담는 상위 계획이다.

### 인프라·애자일·개발 용어
- Physical Server / VM / Bare Metal: 물리 장비, 그 위 가상 서버, 가상화 없이 물리 장비를 직접 쓰는 환경.
- Backup은 별도 위치에 복제하는 예방책이고 Recovery는 실제로 되돌리는 대응이다. 백업은 존재 여부가 아니라 **복구 시험 성공 여부**로 검증한다.
- Agile은 짧게 만들고 피드백으로 개선하는 철학이다. Sprint Planning → Daily Scrum → Review → Retrospective 흐름에서 Product Backlog와 Sprint Backlog를 구분한다.
- DoD(Definition of Done)는 구현만이 아니라 테스트·리뷰·배포 가능 상태를 포함한 완료 기준이다.
- CI/CD는 커밋 이후 테스트·배포를 자동화하는 흐름이며, Container/Docker/Kubernetes/IaC는 실행 환경을 재현·배포·확장하는 도구와 방식이다.

## 2. 웹 서비스가 동작하는 구조 (슬라이드 13~20)
프론트엔드는 HTML(구조), CSS(표현), JavaScript(상호작용)로 사용자 화면을 만들고 API 결과를 표시한다. 백엔드는 요청을 받아 검증·계산·저장한 뒤 API를 반환하며, 인증·인가·암호화·로깅·성능 관리도 담당한다.

### MPA와 SPA
- **MPA**: 페이지 이동마다 서버가 HTML을 렌더링해 반환한다. 서버사이드 렌더링, SEO, 단순한 화면 흐름에 유리할 수 있다.
- **SPA**: 최초 정적 리소스를 받은 뒤 REST API의 JSON을 가져와 클라이언트에서 화면을 갱신한다. 복잡한 상호작용에 유리하지만 초기 로딩·상태 관리·SEO 전략을 함께 고려한다.

둘 중 하나가 무조건 낫지 않다. 렌더링 위치, 검색 노출, 초기 로딩, 개발·배포 구조에 따라 선택한다. BFF는 웹·모바일처럼 클라이언트별로 필요한 응답 조합이 다를 때 그 차이를 백엔드에서 흡수하는 패턴이다.

### JSON·YAML과 처리 방식
JSON은 API 데이터 교환의 키-값 형식이고, YAML은 설정 파일에 많이 쓰는 사람이 읽기 쉬운 형식이다. YAML은 **들여쓰기 자체가 계층**이므로 탭·공백 혼용이 오류를 만든다.

동기 처리는 응답을 기다리는 순차 흐름이고, 비동기 처리는 결과를 기다리지 않고 다음 작업을 진행한다. 결제처럼 즉시 결과·순서가 중요한 흐름과 대량 알림·큐처럼 재시도·실패 감지가 필요한 흐름을 구분한다. Monolith는 배포가 단순할 수 있지만 책임이 섞일 수 있고, Microservice는 독립 배포·확장과 함께 네트워크·관측·운영 복잡도를 낳는다.

## 3. macOS 개발 환경: 설치보다 검증 (슬라이드 21~24)
제공 스크립트는 Xcode CLT, Homebrew, Git, zsh, JDK 21, Python 3.11, Node.js, PostgreSQL, VS Code, Docker, AWS CLI, kubectl 등을 표준화한다. 스크립트는 신뢰 가능한 교육 경로에서 받은 파일만 실행하고, 관리자 권한·셸 설정 변경이 포함된다는 점을 인지한다.

```bash
source ~/.zprofile
source ~/.zshrc
open -a Docker

git --version
java -version
python3 --version
node -v
docker --version
code --version
aws --version
kubectl version --client
```

버전 출력은 설치 파일이 내려받아졌다는 사실이 아니라 **현재 셸에서 명령이 실제로 실행되는지** 확인하는 검증이다. Docker Desktop은 설치 후 최초 실행·권한 동의까지 완료되어야 daemon이 동작한다.

하위 상세 노트: [[notion/SKALA/7-14 Git 이해 및 활용/SKALA 개발환경 설치 스크립트 — 원문·주석·동작 해설]]

## 4. IDE·파일 시스템·Git의 기본 흐름 (슬라이드 25~33)
VS Code에서는 Explorer, Search, Source Control, Run & Debug, Extensions, 통합 터미널을 사용한다. 파일 명령은 작은 실습에서도 위험도를 이해하고 쓴다.

```bash
pwd          # 현재 경로 확인
ls -al       # 숨김 파일 포함 목록
cd <경로>    # 이동
mkdir <이름> # 디렉터리 생성
cp/mv        # 복사/이동
rm <경로>    # 삭제: 되돌리기 어려우므로 대상 확인
```

Git은 파일 이력을 저장하고 협업을 돕는 VCS다. Repository는 이력 저장소, Commit은 의미 있는 변경의 스냅샷, Branch는 독립 작업 흐름, Merge는 결과 통합, Conflict는 같은 부분을 다르게 수정해 자동 통합이 불가능한 상태다. Pull Request는 리뷰와 병합 요청을 묶는다.

```text
원격 저장소 --clone/pull--> 로컬 작업공간 --add/commit--> 로컬 이력 --push--> 원격 저장소
```

협업을 시작할 때는 먼저 `git pull`로 원격 상태를 맞추고, 매 작업 전 `git status`로 무엇이 바뀌었는지 확인한다.

## 5. Vibe Coding 결과물을 GitHub까지 검증하기 (슬라이드 34~44)
AI에게 HTML 페이지를 만들게 할 때는 목적·필수 섹션·스타일·반응형 조건을 구체화한다. 하지만 AI가 파일을 만들었다는 보고는 완료가 아니다.

1. 필요한 파일과 `.gitignore`가 실제로 생성됐는지 확인한다.
2. `.env`, 토큰, 빌드 산출물, 불필요한 로컬 파일이 `git status`에 없는지 확인한다.
3. Live Server로 브라우저에서 화면·링크·반응형을 확인한다.
4. Initialize Repository 후 변경을 스테이징하고, 변경 의도가 드러나는 커밋 메시지를 작성한다.
5. GitHub 원격 저장소에서 파일·브랜치·커밋이 실제로 보이는지 확인한다.
6. 기능을 하나 더 추가하고 같은 생성→검토→실행→커밋→원격 확인 사이클을 반복한다.

Live Server는 정적 페이지 확인용 개발 서버이며 운영 배포 도구가 아니다. 실행을 끝내면 포트 점유를 멈춘다.

## 6. Git CLI와 브랜치 전략 (슬라이드 45~48)
```bash
mkdir skala-intro && cd skala-intro
git init
echo "# SKALA codes" > readme.md
git add .
git commit -m "Initial message"
git remote add origin https://github.com/<user>/skala-intro.git
git branch -M main
git push -u origin main
```

작업 전후에는 다음 명령을 목적에 맞게 쓴다.

| 명령 | 목적 |
| --- | --- |
| `git status` | 워킹 트리·스테이징 상태 확인 |
| `git log --oneline` | 커밋 이력 빠르게 확인 |
| `git switch -c feature/login` | 기능 브랜치 생성·이동 |
| `git merge feature/login` | 작업 결과 통합 |
| `git restore <파일>` | 워킹 트리 변경 취소 |
| `git reset --soft HEAD~1` | 직전 커밋만 취소하고 변경 유지 |
| `git revert <커밋>` | 공유된 이력을 안전하게 되돌리는 새 커밋 생성 |
| `git stash` / `pop` | 진행 중 변경을 임시 보관·복원 |

Git Flow는 main/develop/feature/release/hotfix 역할을 분리한다. 규모가 작고 CI/CD가 단순하면 `main + feature + Pull Request`의 GitHub Flow가 더 적합할 수 있다. 팀의 배포 빈도·리뷰·운영 절차가 전략 선택 기준이다.

## 7. GitHub 인증과 비밀값 보호 (슬라이드 49~51)
HTTPS Push에서 GitHub 비밀번호 대신 PAT를 사용한다. PAT는 최소 권한·만료 기간을 설정하고 한 번 표시된 값은 안전하게 보관한다. `gh auth login`의 브라우저 인증도 대안이 된다.

**API 키·토큰·비밀번호·`.env`는 절대 커밋하지 않는다.** 이미 노출했다면 Git 이력에서 지우는 것만으로 충분하지 않다. 즉시 폐기·재발급하고 영향을 점검해야 한다. 기존 로컬 프로젝트를 연결할 때 원격은 README 등을 미리 만들지 않은 빈 저장소로 시작하면 이력 충돌을 줄일 수 있다.

## 8. Codex CLI로 하는 AI 코딩의 올바른 순서 (슬라이드 52~64)
```bash
mkdir codex-intro && cd codex-intro
npm install -g @openai/codex
codex --version
codex
```

AI 코딩은 자연어 요청 한 번으로 끝내는 과정이 아니다.

```text
요구사항 구체화 → 생성 → 코드 흐름 이해 → 실행 → 리뷰 → 테스트 → 결과 재검증 → 커밋
```

- `/init`은 프로젝트 지침 성격의 `AGENTS.md`를 만든다. 현재 버전의 도움말·공식 문서를 확인한다.
- 코드 생성 뒤에는 함수·입출력·예외·의존성을 질문해 이해한다.
- 리뷰 요청에는 버그 가능성, 가독성, 보안, 테스트 누락 등 검토 범위를 함께 준다.
- 테스트는 생성만 요청하지 않고 실제로 실행해 성공·실패 경로를 확인한다.
- 정규표현식, 비밀번호 검증, Mermaid처럼 구체적 요구는 입력 예시·언어·검증 기준을 함께 제공한다.

## 학습 점검
- [ ] MPA와 SPA의 렌더링 위치·데이터 흐름 차이를 설명할 수 있다.
- [ ] 설치 뒤 셸 설정·버전·Docker daemon까지 검증해야 하는 이유를 안다.
- [ ] `status → add → commit → push` 전 각 단계에서 무엇을 확인해야 하는지 안다.
- [ ] 노출된 토큰은 삭제가 아니라 폐기·재발급해야 함을 안다.
- [ ] AI 생성 코드를 실행·리뷰·테스트 없이 수용하지 않는다.

## 연결 노트
- [[notion/SKALA/7-14 Git 이해 및 활용/SKALA 개발환경 설치 스크립트 — 원문·주석·동작 해설]]
- [[notion/SKALA/7-15 Prompt 설계와 Context/7-15 Prompt 설계 및 Context Engineering]]
