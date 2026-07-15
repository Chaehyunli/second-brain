---
title: "OpenCode로 보는 코딩 에이전트 내부 구조"
notion_page_id: "39e1d84b-f68e-81ff-a1f8-c72d47d8ee09"
notion_url: "https://app.notion.com/p/39e1d84bf68e81ffa1f8c72d47d8ee09"
source_url: "https://cefboud.com/posts/coding-agents-internals-opencode-deepdive/"
type: "manual-learning-note"
---

## 원문
[How Coding Agents Actually Work: Inside OpenCode](https://cefboud.com/posts/coding-agents-internals-opencode-deepdive/)

## 핵심
- 코딩 에이전트는 LLM이 파일 읽기·수정, 명령 실행, 테스트 결과 관찰을 반복하는 **도구 호출 루프**로 동작한다.
- OpenCode는 Bun 기반 HTTP 서버와 Go TUI의 client/server 구조를 사용하며, 다양한 모델 공급자를 공통 인터페이스로 연결한다.
- LSP 진단, 권한 제어, 세션 기억, 변경 되돌리기 같은 하네스 기능이 단순 챗봇을 신뢰 가능한 개발 도구로 확장한다.
