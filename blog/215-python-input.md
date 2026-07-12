---
title: "[백준(Python)] Input()"
created: 2026-07-12
updated: 2026-07-12
type: blog-post
tags: [blog, technical-writing]
category: "BACKJOON"
published: 2026-03-10
source_url: https://ch010104.tistory.com/215
archive_method: Tistory sitemap + HTML content extraction
---

# [백준(Python)] Input()

> 원문: https://ch010104.tistory.com/215

## 본문

1. input()의 본질  성질: 무조건 **문자열(String)**로 읽음 주의: 숫자 10을 넣어도 파이썬은 글자 "10"으로 인식합니다. 산술 연산을 하려면 반드시 형 변환이 필요  2. split()의 역할  기능: 공백(스페이스, 탭, 엔터)을 기준으로 문자열을 자룸. 예시: "10 20" → ["10", "20"] (리스트 형태)  3. map(int, ...)  기능: 여러 개의 데이터를 한꺼번에 정수(int)로 변환. 비유: 리스트 안의 모든 글자들에게 "숫자로 변신해!"라고 명령하는 컨베이어 벨트  ① 변수 여러 개에 나눠 담기 (언패킹) - 개수가 정확히 정해져 있을 때 백준에서 가장 많이 쓰는 방식    a, b = map(int, input().split()) # a에는 10, b에는 20이 들어감       ② 리스트로 묶기 - 개수가 몇 개인지 모르거나, 나중에 리스트 기능을 써야 할 때 사용    numbers = list(map(int, input().split())) # [10, 20, 30] 처럼 리스트로 만들어짐      4. map을 쓰는 이유 (장점) 만약 map을 쓰지 않는다면 아래와 같이 복잡하게 짜야 함.    map 사용 전:     temp = input().split() # ["10", "20"] result = [] for i in temp: result.append(int(i)) # 하나씩 꺼내서 int로 바꾸고 다시 넣기      map 사용 후:     result = list(map(int, input().split())) # 단 한 줄로 끝!
