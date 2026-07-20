#!/usr/bin/env python3
"""Expand statistics-course notes from their uploaded notebook/Python sources.

This preserves every note's frontmatter and vault links while replacing its short
summary body with source-order Markdown, complete code cells, and saved text outputs.
"""
from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path

VAULT = Path("/root/wiki")
COURSE = VAULT / "courses/통계·확률 기초"
SOURCE = Path("/tmp/7a35b440ed3d4588")
FRONT = re.compile(r"\A---\n.*?\n---\n", re.S)
SOURCE_PROP = re.compile(r'^source_original_file: "([^"]+)"$', re.M)
TITLE = re.compile(r"^# (.+)$", re.M)
CONNECTION = re.compile(r"\n## 연결\n.*\Z", re.S)
IMAGE = re.compile(r"<img\b[^>]*>", re.I)
HTML_TAG = re.compile(r"<[^>]+>")


def frontmatter(text: str) -> str:
    match = FRONT.match(text)
    if not match:
        raise ValueError("frontmatter missing")
    return match.group(0)


def demote_headings(text: str) -> str:
    return re.sub(r"^(#{1,5})(?=\s)", r"\1#", text, flags=re.M)


def clean_markdown(text: str) -> str:
    # Images in the upload point to unavailable local/external paths. Keep their prose,
    # rather than embedding an unverifiable broken image in the Vault.
    text = IMAGE.sub("", text)
    text = HTML_TAG.sub("", text)
    text = html.unescape(text).replace("\\*", "*")
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return demote_headings(text)


def output_text(output: dict) -> str:
    if "text" in output:
        raw = output["text"]
    elif "data" in output:
        raw = output["data"].get("text/plain", "")
    else:
        return ""
    if isinstance(raw, list):
        raw = "".join(raw)
    raw = str(raw).strip()
    if not raw or len(raw) > 6000:
        return ""
    return raw


def notebook_body(title: str, source_path: Path) -> str:
    notebook = json.loads(source_path.read_text(encoding="utf-8"))
    chunks = [
        f"# {title}",
        "",
        "## 학습 목표",
        "원본 노트북의 개념 설명·공식·예시·코드 실행 흐름을 순서대로 따라가며, 정의만 외우지 않고 계산과 해석까지 연결한다.",
        "",
        "## 원문 기반 학습 내용",
    ]
    code_no = 0
    for cell in notebook["cells"]:
        source = "".join(cell.get("source", [])).strip()
        if not source:
            continue
        if cell["cell_type"] == "markdown":
            cleaned = clean_markdown(source)
            if cleaned:
                chunks.extend(["", cleaned])
            continue
        if cell["cell_type"] != "code":
            continue
        code_no += 1
        chunks.extend(["", f"### 원문 코드 실습 {code_no}", "", "```python", source.rstrip(), "```"])
        results = [output_text(output) for output in cell.get("outputs", [])]
        results = [result for result in results if result]
        if results:
            chunks.extend(["", "**저장된 실행 결과**", "", "```text", "\n".join(results), "```"])
    chunks.extend([
        "",
        "## 복습 체크",
        "- 정의·공식의 각 기호가 무엇을 뜻하는지 말로 설명할 수 있는가?",
        "- 원문의 예제에서 어떤 가정과 계산을 거쳐 결론에 이르는지 따라갈 수 있는가?",
        "- 코드의 입력값을 바꾸었을 때 결과와 해석이 어떻게 달라지는지 확인할 수 있는가?",
    ])
    return "\n".join(line.rstrip() for line in chunks).rstrip() + "\n"


def python_practice_body(title: str, source_path: Path) -> str:
    source = source_path.read_text(encoding="utf-8").strip()
    return f'''# {title}

## 실습 목표
모집단 표준편차를 알고 있다는 가정에서 표본 평균이 기준 모평균과 다른지 **양측 Z검정**으로 판정한다. 계산식·코드·판단 기준을 하나의 흐름으로 연결한다.

## 문제 설정과 가설
- 기준 모평균: $\\mu_0=100$
- 모집단 표준편차: $\\sigma=5$
- 표본 수: $n=50$
- 표본 평균: $\\bar{{x}}=101.5$
- 유의수준: $\\alpha=0.05$
- 귀무가설 $H_0$: 평균은 100g이다.
- 대립가설 $H_1$: 평균은 100g과 다르다. (양측 검정)

## 계산 흐름
표본 평균을 검정하므로 개별 관측치의 표준편차가 아니라 **표본 평균의 표준오차**를 사용한다.

$$SE=\\frac{{\\sigma}}{{\\sqrt{{n}}}}, \qquad Z=\\frac{{\\bar{{x}}-\\mu_0}}{{SE}}$$

양측 p-value는 표준정규분포 누적분포함수 $\\Phi$를 사용해 다음과 같이 구한다.

$$p=2\\left(1-\\Phi(|Z|)\\right)$$

이 예제에서는 $SE\\approx0.7071$, $Z\\approx2.1213$, $p\\approx0.0339$이다. 따라서 $p<0.05$이므로 귀무가설을 기각하며, 표본 평균은 100g과 통계적으로 유의하게 다르다고 해석한다.

## 원문 코드
```python
{source}
```

## 코드 읽기
1. `std_error`는 표본 평균의 변동성인 표준오차를 계산한다.
2. `z_score`는 표본 평균이 기준 평균에서 표준오차 몇 배만큼 떨어졌는지 나타낸다.
3. `norm.cdf(abs(z_score))`는 $|Z|$ 이하의 누적확률이고, `1 - ...`는 한쪽 꼬리확률이다.
4. 양측 검정이므로 꼬리확률을 2배 해 `p_value`를 만든다.
5. p-value를 유의수준과 비교해 기각 여부를 판단한다.

## 주의점
- p-value는 “귀무가설이 참일 확률”이 아니라, **귀무가설이 참이라고 가정할 때 현재만큼 또는 더 극단적인 결과가 나올 확률**이다.
- p-value가 크다고 귀무가설이 참으로 증명되는 것은 아니다. 기각할 증거가 부족하다는 뜻이다.
- Z검정은 모집단 표준편차를 알고 있거나 그 가정이 정당할 때 사용한다. 표준편차를 모르면 일반적으로 [[courses/통계·확률 기초/11 t검정|t검정]]을 검토한다.

## 연결
개념 설명: [[courses/통계·확률 기초/09 p-value와 Z검정|p-value·Z검정]] · 표준화: [[courses/통계·확률 기초/08 표준정규분포|표준정규분포]]
'''


def render(note: Path) -> str:
    old = note.read_text(encoding="utf-8")
    front = frontmatter(old)
    title_match = TITLE.search(old)
    source_match = SOURCE_PROP.search(front)
    if not title_match or not source_match:
        raise ValueError(note)
    title, original = title_match.group(1), source_match.group(1)
    original_path = SOURCE / original
    if not original_path.exists():
        raise FileNotFoundError(original_path)
    if original_path.suffix == ".ipynb":
        body = notebook_body(title, original_path)
    elif original_path.suffix == ".py":
        body = python_practice_body(title, original_path)
    else:
        raise ValueError(original_path)
    # Keep existing explicit learning links for notebooks whose original short note supplied them.
    connection = CONNECTION.search(old)
    if connection and "## 연결" not in body:
        body += connection.group(0).lstrip()
    return re.sub(r"[ \t]+$", "", front + "\n" + body, flags=re.M)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    notes = [path for path in COURSE.rglob("*.md") if path.name != "index.md"]
    changed = []
    for note in notes:
        rendered = render(note)
        if rendered != note.read_text(encoding="utf-8"):
            changed.append((note, rendered))
    if args.apply:
        for note, rendered in changed:
            note.write_text(rendered, encoding="utf-8")
    print(f"notes={len(notes)} changed={len(changed)} applied={args.apply}")


if __name__ == "__main__":
    main()
