# Personal Career Wiki Schema

## Domain

임채현의 백엔드 개발자 포트폴리오, 프로젝트, 실무 경험, 학습·수상 이력, 그리고 향후 검증된 기술 지식. 개인 자료의 사실관계와 포트폴리오 서사를 장기적으로 축적한다.

## Privacy and evidence policy

- 이 Wiki는 개인 전용이며 디렉터리 권한은 `700`으로 유지한다.
- 주소·전화번호·생년월일·개인식별번호·로그인 정보는 Wiki 페이지에 복사하지 않는다.
- 수치·기간·수상·역할은 원본 근거가 있을 때만 단정한다. 원본 간 불일치는 삭제하지 않고 `contested: true`와 함께 기록한다.
- 원본은 `/root/portfolio-evidence/drive-archive/`에 보관하며 `raw/`에는 추적용 manifest만 둔다. 원본 파일은 수정하지 않는다.
- GitHub·Notion·기술 블로그 등 외부 공개물을 추가할 때는 해당 URL과 확인일을 `sources`에 기록한다.

## Conventions

- File names: lowercase kebab-case; project pages are under `entities/projects/`.
- Every agent-owned page has frontmatter: `title`, `created`, `updated`, `type`, `tags`, `sources`.
- Every entity/concept page links to at least two other wiki pages with `[[wikilinks]]`.
- New or changed pages must be listed in `index.md` and logged in `log.md`.
- New tags must be added below before use.

## Tag taxonomy

- Profile: `profile`, `career`, `education`, `award`, `credential`
- Engineering: `backend`, `java`, `python`, `spring-boot`, `webflux`, `r2dbc`, `fastapi`, `sse`, `redis`, `postgresql`, `database`, `sql`, `security`, `testing`, `infrastructure`, `search`, `reliability`
- AI/Data: `ai`, `ai-agent`, `machine-learning`, `rag`, `data-engineering`
- Work: `project`, `experience`, `architecture`, `performance`, `quality`

## Page thresholds

- Create a project/experience page when it is central to one verified source.
- Add technical knowledge only when it is demonstrated in code, a project source, a credential, or a user-confirmed learning record.
- Split pages over 200 lines; do not create pages for passing mentions.

## Update policy

1. Prefer dated, detailed source records over older summary material.
2. If sources conflict, preserve both claims and mark the page `contested: true`.
3. Never silently upgrade an inferred responsibility or outcome into a fact.
