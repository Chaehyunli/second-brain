# Visual Note Pipeline

PDF/웹의 핵심 시각 자료를 읽고 Notion 노트에 원본 이미지와 해석을 함께 넣기 위한 로컬 파이프라인이다.

## 1. PDF를 흰 배경 PNG로 렌더링

```bash
cd /root/wiki
python3 scripts/render_note_visuals.py \
  /path/to/lecture.pdf \
  --pages 12,15-16 \
  --output-dir /tmp/lecture-visuals \
  --dpi 180
```

- 결과물은 `page-012.png` 같은 개별 PNG와 `manifest.json`이다.
- `pdftocairo` 렌더를 사용해 투명 배경·embedded-image 추출 문제를 피한다.
- 에이전트는 생성된 PNG를 `vision_analyze`로 읽고, **핵심 도식·흐름·UI 상태만** 선별한다.
- 코드·로그는 이미지로 대체하지 않고 원문 텍스트 코드 블록으로 보존한다.

## 2. Notion에 원본 PNG 업로드

`ntn`은 설치되어 있다. 최초 1회, **VPS 터미널에서 직접** OAuth 로그인을 수행한다. 토큰이나 인증 코드를 Discord에 공유하지 않는다.

```bash
ntn login
ntn files list --plain
```

로그인 후:

```bash
python3 scripts/stage_notion_visual_assets.py \
  /tmp/lecture-visuals/manifest.json \
  --receipt /tmp/lecture-visuals/notion_uploads.json
```

- receipt에는 페이지 번호와 Notion file-upload ID가 기록된다.
- 에이전트는 receipt의 file-upload ID를 Notion Markdown 이미지 블록으로 삽입한 뒤, 대상 Notion 페이지를 다시 fetch해 이미지·설명·부모 연결을 검증한다.
- 로컬 강의 PDF/스크린샷을 외부 공개 URL이나 임시 터널로 노출하지 않는다.

## 3. 작업 규칙

1. PDF/웹 페이지의 모든 이미지를 넣지 않는다. 구조·흐름·비교를 실제로 보완하는 자료만 선택한다.
2. 이미지 바로 아래에 “이 그림이 보여 주는 관계·순서·주의점”을 해석 중심으로 쓴다.
3. 이미지 안의 세부 코드/문장은 원문 코드·본문으로 별도 보존한다.
4. crop 전후를 시각 검토해 라벨·화살표·도형이 잘리지 않았는지 확인한다.
5. 업로드와 Notion 반영 후에는 대상 페이지를 fetch하여 실제 렌더링을 검증한다.
