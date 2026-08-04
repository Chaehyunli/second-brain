# Information Notion 원문 미러링 정책

## 목적

`Information`의 Notion 페이지를 Obsidian/GitHub에 **원문 사본**으로 보관한다. 이 경로는 요약·해석·재구성 공간이 아니다.

## 적용 범위

이 정책은 **자동 실행되는 Information → Obsidian/GitHub 동기화 작업에만** 적용한다.

사용자가 “Information에 정리해줘”, “Information의 해당 페이지를 수정해줘”, “Information 아래에 새 페이지를 만들어줘”라고 명시적으로 요청한 경우에는 Hermes가 Notion `Information`에 새 페이지를 만들거나 기존 페이지를 수정할 수 있다. 그 작성·수정 작업은 원문 미러링 cron과 별개의 사용자 요청 작업이다.

## 공개 Notion 링크를 원문으로 받았을 때

사용자가 `*.notion.site` 공개 링크를 제공하면 원문 수집은 **브라우저 공개 페이지 조회를 우선**한다. 외부 공개 페이지는 HERMES Notion API·CLI 연동 범위 밖일 수 있으므로, API/CLI 404를 권한 연결 요청이나 작업 차단 사유로 삼지 않는다.

1. 브라우저에서 공개 본문을 읽어 사용자 요청 범위로 정리한다.
2. 정리 결과는 HERMES `Information` 하위 Notion 페이지로 만든다.
3. GitHub에는 외부 원문이 아니라, 새로 만든 HERMES `Information` 페이지의 본문을 이 정책에 따라 원문 미러링한다.
4. 공개 페이지가 브라우저에서도 실제로 접근 불가할 때만, 원문 접근 불가 사실을 알린다. 사용자에게 Notion API·CLI 연결을 요구하지 않는다.

## 동기화 원칙

1. Notion 페이지의 본문은 Markdown 파일의 frontmatter 뒤에 **그대로** 저장한다.
2. 동기화 과정에서 본문을 요약·확장·재서술·섹션 재배치·표 변환·제목/H1 추가·위키링크 삽입하지 않는다.
3. 앞부분 frontmatter에는 아래처럼 출처 식별용 메타데이터만 둘 수 있다.
   - `source: Notion Information`
   - `notion_url`
   - `notion_page_id`
   - `synced_at_utc`
   - `notion_content_sha256`
4. Notion 제목을 사용한 안전한 파일명은 최초 동기화 때 결정하고, 이후 제목 변경만으로 파일명을 자동 변경하지 않는다.
5. `notion_content_sha256`은 **Notion 원문 본문만** 기준으로 계산한다. frontmatter나 동기화 시각이 바뀌었다는 이유로 본문 변경으로 판단하지 않는다.
6. 해시가 같으면 파일을 쓰거나 Git commit/push하지 않는다.
7. Notion 제목에 `(수정중)`이 포함된 페이지는 동기화하지 않는다.

## 예외: 만료형 서명 URL

Notion 응답의 이미지·파일 URL에 `X-Amz-` 등 시간 제한 서명 파라미터가 있으면 credential 노출과 링크 만료를 막기 위해 해당 URL은 Vault에 저장하지 않는다. 이 경우에만 해당 첨부 줄을 제외할 수 있으며, 본문 설명을 요약하거나 다른 내용으로 대체하지 않는다.

## 금지

- 원문 미러 파일을 요약본으로 덮어쓰기
- 원문 미러 파일의 본문에 그래프용 링크나 해설 삽입
- Notion 원문이 바뀌지 않았는데 렌더링 방식 변경만으로 전체 파일 재작성
- 원문과 요약을 같은 파일에서 혼합

## 검증

동기화 전후에는 Notion에서 받은 본문과 Vault의 frontmatter 뒤 본문이 같은지 확인한다. 서명 URL 예외가 발생한 경우만 그 차이를 명시적으로 기록한다.
