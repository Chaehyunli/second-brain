# Personal Career Wiki Schema

## Domain

임채현의 백엔드 개발자 포트폴리오, 프로젝트, 실무 경험, 학습·수상 이력, 기술 블로그 글, 그리고 향후 검증된 기술 지식. 개인 자료의 사실관계와 포트폴리오 서사를 장기적으로 축적한다.

## Privacy and evidence policy

- 이 Wiki는 개인 전용이며 디렉터리 권한은 `700`으로 유지한다.
- 주소·전화번호·생년월일·개인식별번호·로그인 정보는 Wiki 페이지에 복사하지 않는다.
- 수치·기간·수상·역할은 원본 근거가 있을 때만 단정한다. 원본 간 불일치는 삭제하지 않고 `contested: true`와 함께 기록한다.
- 원본은 `/root/portfolio-evidence/drive-archive/`에 보관하며 `raw/`에는 추적용 manifest만 둔다. 원본 파일은 수정하지 않는다.
- GitHub·Notion·기술 블로그 등 외부 공개물을 추가할 때는 해당 URL과 확인일을 `sources`에 기록한다.

## Conventions

- File names: lowercase kebab-case; project pages are under `entities/projects/`; 기술 블로그 글은 `blog/`에 둔다.
- Every agent-owned page has frontmatter: `title`, `created`, `updated`, `type`, `tags`, `sources` 또는 `source_url`.
- Every entity/concept page links to at least two other wiki pages with wiki links.
- New or changed pages must be listed in `index.md` and logged in `log.md`.
- New tags must be added below before use.

## Typed metadata contract

새로 생성하거나 명시적으로 갱신하는 노트에만 아래 공통 필드를 점진 적용한다. 기존 노트를 형식 통일만을 위해 일괄 재작성하지 않는다.

```yaml
schema_version: 1
id: stable-source-or-local-id
title:
type:
status: draft # draft | verified | frozen | superseded
created:
updated:
tags: []
sources: []
```

- `blog-post`: `source_url`, `published_at`, `category`를 추가한다.
- `notion-learning-note`: `notion_page_id`, `notion_url`, `content_sha256`를 추가한다.
- `project`·`experience`: `period`, `evidence_status`, `sources`를 추가한다.
- `course-note`: `course`, `module`, `source_material`을 추가한다.
- `research-note`: `source_url`, `checked_at`, `confidence`를 추가한다.
- `knowledge-note`: `checked_at`를 추가하며, `sources`에는 원본 URL·Notion ID 또는 원본 노트 경로를 남긴다. 본문에는 `## 핵심`, `## 연결된 근거`, `## 적용 기준`, `## 주의점 또는 한계`를 둔다. 기준본을 복사·대체하지 않고 출처 간 재사용 가능한 개념만 정리한다.

`id`는 파일명 변경과 별개로 유지하는 안정 식별자다. 외부 원본이 있으면 URL·Notion ID 등 원본 식별자를 우선하며, 제목 유사도만으로 병합하지 않는다. 태그는 자유어가 아니라 `domain/`, `concept/`, `kind/`, `source/`, `status/`, `evidence/` namespace를 우선한다.

## Inbox / Staging contract

- `inbox/`에는 신뢰되지 않은 외부 자동 수집물·AI 초안만 둔다. 사용자가 직접 승인한 Notion/티스토리 기준본은 기존 source 정책을 따른다.
- Inbox 노트에는 `captured_at`, `review_status: pending`, `source_url` 또는 `sources`, `agent_generated`를 남긴다.
- 검토가 끝난 자료만 적합한 canonical 폴더로 옮기며, 원본 링크·확인일·근거 상태를 유지한다.
- 자동화는 Inbox의 자료를 삭제·대량 이동·사실 확정하지 않는다.

## Tag taxonomy

- Profile: `profile`, `career`, `education`, `award`, `credential`
- Engineering: `backend`, `java`, `python`, `spring-boot`, `webflux`, `r2dbc`, `fastapi`, `sse`, `redis`, `postgresql`, `database`, `sql`, `security`, `testing`, `infrastructure`, `search`, `reliability`, `performance`
- AI/Data: `ai`, `ai-agent`, `machine-learning`, `rag`, `data-engineering`
- Work: `project`, `experience`, `architecture`, `quality`
- Writing: `blog`, `technical-writing`

## Page thresholds

- Create a project/experience page when it is central to one verified source.
- Archive each public technical blog article as a standalone `type: blog-post` page with canonical URL and publication metadata.
- Add technical knowledge only when it is demonstrated in code, a project source, a credential, a user-confirmed learning record, or a published blog post.
- Split pages over 200 lines; do not create pages for passing mentions.

## Update policy

1. Prefer dated, detailed source records over older summary material.
2. If sources conflict, preserve both claims and mark the page `contested: true`.
3. Never silently upgrade an inferred responsibility or outcome into a fact.
4. Re-archive blog posts by canonical URL; do not duplicate an article solely because its title changes.
