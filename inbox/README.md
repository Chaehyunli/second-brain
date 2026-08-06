# Inbox / Staging

> 자동 수집물과 AI 초안의 **검토 대기 영역**입니다. 이 폴더의 내용은 아직 Vault의 검증된 지식이 아닙니다.

## 넣는 자료

- 신뢰되지 않은 외부 웹 자료
- 출처는 있으나 분류·중복·사실 검토가 끝나지 않은 초안
- AI가 제안했으나 사람이 확인하지 않은 요약·연결 후보

## 필수 Frontmatter

```yaml
schema_version: 1
title:
type: research-note
status: draft
captured_at:
review_status: pending
agent_generated: true
source_url:
```

## 처리 원칙

1. 원문 URL·수집일·생성 주체를 유지한다.
2. 검증·분류가 끝난 뒤에만 적합한 canonical 폴더로 이동한다.
3. 자동화는 이 폴더의 노트를 삭제·대량 이동·사실 확정하지 않는다.
4. 사용자가 직접 요청한 Notion·티스토리 기준본 동기화에는 이 staging 단계를 강제하지 않는다.
5. `python3 scripts/build_inbox_review_queue.py --root /root/wiki`로 검토 대기열을 생성할 수 있다. 대기열은 안내용이며 승격·삭제·사실 확정을 수행하지 않는다.
6. 승격은 사용자가 검토한 뒤에만 `python3 scripts/promote_inbox_note.py <inbox-source> <destination> --approve --review-note "검토 근거"`로 실행한다. 이 명령은 dirty worktree·출처 누락·기존 대상 파일을 거부한다.
