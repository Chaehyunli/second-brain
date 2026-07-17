---
title: "[프로그래머스] 가장 많이 받은 선물(2024 KAKAO WINTER INTERNSHIP)"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "java", "programers"]
category: "JAVA"
published: 2025-03-07
source_url: https://ch010104.tistory.com/7
---

# [프로그래머스] 가장 많이 받은 선물(2024 KAKAO WINTER INTERNSHIP)

## 원문

https://ch010104.tistory.com/7

## 노트 유형

`guide`

## 적용 목적과 전제조건

친구들이 주고받은 선물 기록을 바탕으로, 다음 달에 가장 많은 선물을 받을 친구가 몇 개를 받을지 예측하는 문제

**선물 지수(준 선물 - 받은 선물)**가 더 큰 사람이 작은 사람에게 하나 받음.

## 구현 절차·검증·주의점

문제 요약

친구들이 주고받은 선물 기록을 바탕으로, 다음 달에 가장 많은 선물을 받을 친구가 몇 개를 받을지 예측하는 문제

선물 주고 받는 규칙

두 사람이 선물을 주고받은 적이 있다면

더 많은 선물을 줬던 사람이 다음 달에 하나 받음.

선물을 주고받은 적이 없거나 동일한 개수로 주고받았다면

**선물 지수(준 선물 - 받은 선물)**가 더 큰 사람이 작은 사람에게 하나 받음.

선물 지수도 같다면

선물을 주고받지 않음.

입출력 예시

friends: 친구들의 목록

gifts: "A B" 형식의 선물 기록 (A가 B에게 선물 줌)

result: 다음 달 가장 많은 선물을 받는 친구가 받을 선물 개수

내가 짠 코드

```text
import java.util.*;

class Solution {
    public int solution(String[] friends, String[] gifts) {

        int n = friends.length; // 전체 사람의 수
        Map<String, Integer> indexMap = new HashMap<>();

        for (int i = 0; i < n; i++) {
            indexMap.put(friends[i], i);
        }

        int[][] giftMatrix = new int[n][n]; // 선물 주고받은 기록
        int[] givenGifts = new int[n]; // 준 선물 개수
        int[] receivedGifts = new int[n]; // 받은 선물 개수

        // 선물 기록 저장
        for (String gift : gifts) {
            String[] parts = gift.split(" ");
            String giver = parts[0], receiver = parts[1];
            int giverIdx = indexMap.get(giver);
            int receiverIdx = indexMap.get(receiver);

            giftMatrix[giverIdx][receiverIdx]++;
            givenGifts[giverIdx]++;
            receivedGifts[receiverIdx]++;
        }

        int[] giftIndex = new int[n]; // 선물 지수 계산
        for (int i = 0; i < n; i++) {
            giftIndex[i] = givenGifts[i] - receivedGifts[i];
        }

        int[] nextMonthGifts = new int[n]; // 다음 달 받을 선물 개수

        // 다음 달 선물 교환 계산
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (i == j) continue;

                int givenToJ = giftMatrix[i][j];
                int givenToI = giftMatrix[j][i];

                if (givenToJ > givenToI) {
                    nextMonthGifts[i]++;
                } else if (givenToJ < givenToI) {
                    nextMonthGifts[j]++;
                } else {
                    if (giftIndex[i] > giftIndex[j]) {
                        nextMonthGifts[i]++;
                    } else if (giftIndex[i] < giftIndex[j]) {
                        nextMonthGifts[j]++;
                    }
                }
            }
        }

        // 가장 많이 받는 사람 찾기
        return Arrays.stream(nextMonthGifts).max().orElse(0);
    }
}
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

데이터 전처리

friends 배열을 통해 이름 → 인덱스 매핑을 만듦 (HashMap 사용, O(1) 검색 가능).

2차원 배열 giftMatrix를 사용해 선물 주고받은 기록 저장.

배열 givenGifts, receivedGifts로 각 사람이 준 선물 개수와 받은 선물 개수 저장.

선물 지수(gift index) 계산

giftIndex[i] = givenGifts[i] - receivedGifts[i]로 계산.

다음 달 선물 계산 (이중 루프 O(n²))

모든 친구 쌍 (i, j)에 대해 선물 주고받은 수 비교 → 선물 지수 비교 → 다음 달 선물 예측.

최대값 반환

Arrays.stream(nextMonthGifts).max().orElse(0);를 사용하여 최대 선물 개수 반환.

## 관련 글

- [[blog/JAVA/index|JAVA]]
- [[blog/JAVA/Spring Boot- 빈(Bean)이란- Autowired 란|[Spring Boot] 빈(Bean)이란? Autowired 란?]]
- [[blog/JAVA/Java- Set, Map, ArrayList, 2D Array|[Java] Set, Map, ArrayList, 2D Array]]
- [[blog/JAVA/SpingBoot- Api 호출시 Redis를 활용한 캐시 저장|[SpingBoot] Api 호출시 Redis를 활용한 캐시 저장]]
