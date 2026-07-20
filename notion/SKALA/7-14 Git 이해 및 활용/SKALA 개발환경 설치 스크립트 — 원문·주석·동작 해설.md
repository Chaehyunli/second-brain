---
title: "SKALA 개발환경 설치 스크립트 — 원문·주석·동작 해설"
notion_page_id: "39d1d84b-f68e-81e8-b8ab-ce8fb3b6c428"
source_url: "https://app.notion.com/p/39d1d84bf68e81e8b8abce8fb3b6c428"
---

# SKALA 개발환경 설치 스크립트 — 원문·주석·동작 해설

## 원문
[Notion 원문](https://app.notion.com/p/39d1d84bf68e81e8b8abce8fb3b6c428) · [전체 `skala-config-setup.sh` 원문](https://h.uguu.se/aLaiyQwt.sh)

> 이 문서는 제공 설치 스크립트의 학습용 해설이다. 외부 스크립트는 실행 전에 출처·변경 내용·권한 요구를 반드시 확인한다.

## 목적: 설치 자동화가 아니라 재실행 가능한 표준 환경
이 스크립트는 Apple Silicon/Intel 판별, Xcode CLT·Homebrew 준비, Git·JDK 21·Python 3.11·Node.js·PostgreSQL·VS Code·Docker·AWS CLI·kubectl 설치, zsh PATH 설정, 실패 항목 수집과 버전 검증을 한 흐름으로 묶는다. 핵심은 패키지를 많이 설치하는 것이 아니라, 여러 번 실행해도 설정이 중복되지 않고 실패 항목을 마지막에 확인할 수 있게 만드는 것이다.

## 1. 시작부의 안전 옵션과 실패 수집
```bash
#!/usr/bin/env bash
set -uo pipefail
ZSHRC="$HOME/.zshrc"
ZPROFILE="$HOME/.zprofile"
FAILED_ITEMS=()
```
- `set -u`: 선언되지 않은 변수를 오류로 처리한다.
- `pipefail`: 파이프라인 앞 단계의 실패를 숨기지 않는다.
- `set -e`를 쓰지 않은 이유: 교육 환경에서는 한 도구 설치 실패가 전체 설치를 멈추지 않게 하고, 마지막에 실패 목록을 보여 주기 위해서다.

```bash
try() {
  local label="$1"; shift
  if "$@"; then return 0; fi
  echo "❌ 실패: $label (건너뛰고 계속)"
  FAILED_ITEMS+=("$label")
  return 0
}
```
`try "Homebrew 업데이트" brew update`처럼 사용한다. 단, Homebrew처럼 뒤 단계 전체의 기반인 도구가 없으면 계속 진행하는 대신 명시적으로 중단해야 한다.

## 2. sudo 세션 유지와 종료 정리
`sudo -v`로 한 번 인증한 뒤 백그라운드에서 인증 캐시를 갱신하고, `trap ... EXIT`로 종료 시 프로세스를 정리한다. 설치 중 반복 비밀번호 입력은 줄지만 관리자 권한을 오래 유지하므로 스크립트 출처 검토가 선행되어야 한다.

## 3. idempotent 설계: 다시 실행해도 설정이 중복되지 않게
```bash
append_block_once() {
  local marker_line="# === SKALA: $marker ==="
  grep -qF "$marker_line" "$file" && return 0
  { echo; echo "$marker_line"; echo "$content"; } >> "$file"
}
```
`# === SKALA: java21 ===` 같은 마커를 먼저 찾고 없을 때만 `.zshrc`·`.zprofile` 끝에 추가한다. 설치가 중간에 실패해 재실행해도 PATH·alias가 계속 중복되는 문제를 막는다. 패키지도 `brew list --formula` 또는 `brew list --cask`로 설치 여부를 먼저 확인한다.

## 4. 단계별 흐름과 확인 지점
| 단계 | 수행 내용 | 반드시 확인할 점 |
| --- | --- | --- |
| 0 | `uname -m`으로 아키텍처 판별 | Apple Silicon=`/opt/homebrew`, Intel=`/usr/local` 경로 차이 |
| 1 | Rosetta 2 설치 | Apple Silicon에서 x86 도구가 필요한 경우만 |
| 2 | Xcode Command Line Tools | GUI 설치 창을 닫으면 스크립트가 대기할 수 있음 |
| 3~5 | Homebrew 설치·PATH·update | 원격 설치 스크립트 URL·현재 셸 PATH |
| 6 | Git, wget, curl, tree, jq | 팀의 pull merge/rebase 정책은 전역 설정보다 우선 |
| 7 | Oh My Zsh·플러그인 | macOS `sed -i ''` 문법은 Linux와 다름 |
| 8~10 | Java 21, Python 3.11, Node | 전역 alias·전역 npm 도구가 프로젝트 설정을 가리지 않는지 |
| 11 | PostgreSQL 17 서비스 | 서비스 시작, 기본 DB, `psql --version` |
| 12 | VS Code·확장 | `code .` 실행을 위한 PATH 반영 |
| 13~15 | Docker, iTerm2, AWS CLI, kubectl | Docker Desktop 최초 실행·권한·daemon |

## 5. 언어 런타임과 서비스의 주의점
Java는 `/usr/libexec/java_home -v 21`로 실제 경로를 찾아 `JAVA_HOME`을 설정한다. Python은 Homebrew 3.11 경로와 alias를 맞추며, 여러 버전을 병행한다면 전역 alias가 프로젝트 요구 버전을 가리지 않는지 확인한다. Node 전역 패키지는 편하지만 프로젝트 재현성은 `devDependencies`와 lockfile이 우선이다.

PostgreSQL은 `brew services start postgresql@17`로 사용자 서비스로 등록한다. `createdb "$(whoami)"` 실패는 이미 DB가 존재하는 경우일 수 있으므로, 실제 서비스 상태와 접속 가능 여부를 별도로 확인한다.

Docker Desktop은 앱 설치만으로 daemon이 즉시 준비되지 않는다. `open -a Docker` 뒤 약관·권한 절차를 완료하고 `docker version`으로 client와 server 모두 확인한다.

## 6. 종료 코드와 실행 후 검증
각 버전 명령은 `|| true`로 모두 출력하게 하되, 실패 목록이 하나라도 있으면 마지막에 `exit 1`을 반환한다. 일부 성공 메시지가 있어도 자동화는 종료 코드를 실패로 판단할 수 있다.

```bash
source ~/.zprofile
source ~/.zshrc
git config --global user.name "본인 이름"
git config --global user.email "GitHub 등록 이메일"
open -a Docker
```

### 실행 전 체크
- [ ] 아키텍처·macOS 버전·관리자 권한을 확인했다.
- [ ] 스크립트 출처와 현재 내용을 확인했다.
- [ ] 기존 `.zshrc`, `.zprofile`을 백업했다.
- [ ] 팀 Git pull 정책을 확인했다.

### 실행 후 체크
- [ ] `brew`, `git`, `java`, `python3.11`, `node`, `docker`, `kubectl` 버전이 출력된다.
- [ ] `code .`가 열리고 필요한 확장이 설치됐다.
- [ ] PostgreSQL 서비스와 기본 DB를 확인했다.
- [ ] `.env`, PAT, API 키가 `.gitignore`로 제외된다.

## 연결 노트
[[notion/SKALA/7-14 Git 이해 및 활용/7-14 Git & AI코딩 & 환경구성 — 강의 정리]]
