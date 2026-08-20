---
title: "[8/19]Spring AI_Day2_실습"
notion_page_id: "3c11d84b-f68e-806c-a334-ef0cccda514f"
source_url: "https://app.notion.com/p/3c11d84bf68e806ca334ef0cccda514f"
synced_at: "2026-08-20T04:29:54+00:00"
content_sha256: "86756b94533aee9e6ef0eb7e88dc62b5d999b3d0d706db5599758eb6dc4cd143"
---

# [8/19]Spring AI_Day2_실습

[[notion/SKALA/index|SKALA 학습 노트]]
[[notion/SKALA/8-19Spring AI_Day2/8-19Spring AI_Day2_핵심 정리]]

> 원문: [Notion 페이지](https://app.notion.com/p/3c11d84bf68e806ca334ef0cccda514f)
>
> 원문의 임시 서명 이미지 URL은 보존하지 않았으며, 안정적으로 확인 가능한 텍스트·코드·표를 유지했다.

# Step 1 인제스트: 메타데이터가 절반
# Step 2 검색을 먼저 눈으로 본다
# Step 3 근거로 답하기
# Step 4 골든 세트로 측정
# Step 5 실험표를 채운다
## A(기준) / 청크(400토큰, 겹침 0) / top-k(4)
## B(작게) / 청크(200토큰) / top-k(4)
## C(크게) / 청크(800토큰) / top-k(4)
## D(기준) / 청크(400) / top-k(8)
## E(엄격) / 청크(400토큰, threshold 0.7) / top-k(4)
## F(겹침) / 청크(400토큰, 겹침 20%) / top-k(4)
