---
title: "[기계학습] Python Pandas 란 ?? ( 2 )"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "AI", "CS", "Python"]
category: "AI(ML & DL)"
published: 2025-04-04
source_url: https://ch010104.tistory.com/42
---

# [기계학습] Python Pandas 란 ?? ( 2 )

## 원문

https://ch010104.tistory.com/42

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

삭제하려는 인덱스 'Ohio state' 가 있을 경우, 해당 열이 삭제됨.

## 원문 기반 개념 정리

### 1. 열 삭제 - del

```python
import pandas as pd
import numpy as np

# DataFrame
data = {
    'year': [2000, 2001, 2002, 2001, 2002, 2003, 2002, 2003, 2004],
    'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada', 'NY', 'NY', 'NY'],
    'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2, 8.3, 8.4, 8.5],
    'debt': [np.nan] * 9
}
index = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
frame2 = pd.DataFrame(data, index=index)

# frame2
#        year  state   pop  debt
# one    2000   Ohio   1.5   NaN
# two    2001   Ohio   1.7   NaN
# three  2002   Ohio   3.6   NaN
# four   2001 Nevada   2.4   NaN
# five   2002 Nevada   2.9   NaN
# six    2003 Nevada   3.2   NaN
# seven  2002     NY   8.3   NaN
# eight  2003     NY   8.4   NaN
# nine   2004     NY   8.5   NaN

del frame2['Ohio state'] # 'Ohio state' 열을 삭제

print(frame2.columns)
# Index(['year', 'state', 'pop', 'deft'], dtype='object')
```

삭제하려는 인덱스 'Ohio state' 가 있을 경우, 해당 열이 삭제됨.

없을 경우, 에러 발생

### 2. 특정 행만 인덱싱 ('one', 'three', 'five')

```text
print(frame2.loc['three']) # 특정 index의 행만 반환

# year     2002
# state    Ohio
# pop       3.6
# Name: three, dtype: object

print(frame2.loc[['three', 'four']])

#        year  state   pop
# three  2002   Ohio   3.6
# four   2001 Nevada   2.4
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### 3. 열 업데이트 (브로드캐스팅)

```text
frame2['debt'] = 16.5
print(frame2)

#        year  state   pop  debt
# one    2000   Ohio   1.5  16.5
# two    2001   Ohio   1.7  16.5
# three  2002   Ohio   3.6  16.5
# four   2001 Nevada   2.4  16.5
# five   2002 Nevada   2.9  16.5
# six    2003 Nevada   3.2  16.5
# seven  2002     NY   8.3  16.5
# eight  2003     NY   8.4  16.5
# nine   2004     NY   8.5  16.5
```

### 4. 각 행별로 다른 값 할당

```text
frame2['debt'] = np.arange(9.)
print(frame2)

#        year  state   pop  debt
# one    2000   Ohio   1.5   0.0
# two    2001   Ohio   1.7   1.0
# three  2002   Ohio   3.6   2.0
# four   2001 Nevada   2.4   3.0
# five   2002 Nevada   2.9   4.0
# six    2003 Nevada   3.2   5.0
# seven  2002     NY   8.3   6.0
# eight  2003     NY   8.4   7.0
# nine   2004     NY   8.5   8.0
```

### 5. Series로 부분 업데이트

```text
val = pd.Series([-1.2, -1.5, -1.7, 2.2], index=['two', 'four', 'five', 'eleven'])
frame2['debt'] = val
print(frame2)

#        year  state   pop  debt
# one    2000   Ohio   1.5   NaN
# two    2001   Ohio   1.7  -1.2
# three  2002   Ohio   3.6   NaN
# four   2001 Nevada   2.4  -1.5
# five   2002 Nevada   2.9  -1.7
# six    2003 Nevada   3.2   NaN
# seven  2002     NY   8.3   NaN
# eight  2003     NY   8.4   NaN
# nine   2004     NY   8.5   NaN
```

### 6. 열 / 인덱스 존재 여부 확인 - in 연산자

```text
print('year' in frame2.columns)
print('ten' in frame2.index)

# True
# False
```

### 7. head / tail 메서드

```text
# frame2
#        year  state   pop  debt
# one    2000   Ohio   1.5   NaN
# two    2001   Ohio   1.7   NaN
# three  2002   Ohio   3.6   NaN
# four   2001 Nevada   2.4   NaN
# five   2002 Nevada   2.9   NaN
# six    2003 Nevada   3.2   NaN
# seven  2002     NY   8.3   NaN
# eight  2003     NY   8.4   NaN
# nine   2004     NY   8.5   NaN

print(frame2.head(3)) # frame2를 앞에서부터 3개 출력

#        year  state  pop  debt
# one    2000   Ohio  1.5   NaN
# two    2001   Ohio  1.7  -1.2
# three  2002   Ohio  3.6   NaN

print(frame2.head()) # 기본 5개를 출력함.

#        year  state   pop  debt
# one    2000   Ohio   1.5   NaN
# two    2001   Ohio   1.7  -1.2
# three  2002   Ohio   3.6   NaN
# four   2001 Nevada   2.4  -1.5
# five   2002 Nevada   2.9  -1.7

print(frame2.tail(3)) # frame2를 뒤에서부터 3개 출력

#        year state  pop  debt
# seven  2002    NY  8.3   NaN
# eight  2003    NY  8.4   NaN
# nine   2004    NY  8.5   NaN

print(frame2.tail()) # 기본 5개를 출력함.

#        year  state  pop  debt
# five   2002 Nevada  2.9  -1.7
# six    2003 Nevada  3.2   NaN
# seven  2002     NY  8.3   NaN
# eight  2003     NY  8.4   NaN
# nine   2004     NY  8.5   NaN
```

### 8. 전치 (Transpose)

```text
frame3 = pd.DataFrame({
    'Nevada': {2001: 2.4, 2002: 2.9, 2000: 1.7},
    'Ohio': {2000: 1.5, 2001: 3.6}
})
print(frame3)

#        Nevada  Ohio
# 2001     2.4   3.6
# 2002     2.9   NaN
# 2000     1.7   1.5

print(frame3.T)

#         2001  2002  2000
# Nevada   2.4   2.9   1.7
# Ohio     3.6   NaN   1.5
```

### 9. 실습

```text
# 실습

1. frame2에 대해 row index one, three, five 행들만을 출력하는 코드를 작성해보세요.
2. frame2에 대해 Nevada 주만의 데이터를 출력하는 코드를 작성해보세요.
3. frame2에 대해 결측치가 존재하는 행들의 인덱스를 출력하는 코드를 작성해보세요.
4. frame2에 index six와 ten 인 행이 존재하는지를 확인하는 코드를 작성해보세요.

# 1 번
print(frame2.loc[['one', 'three', 'five']])
print("--------------------------------")
# 2 번
print(frame2[frame2['state'] == 'Nevada']) # frame2['state'] == 'Nevada'는 bool 타입의 True 반환
print("--------------------------------")
# 3 번
print(frame2[frame2.isnull().any(axis=1)].index)
print("--------------------------------")
# 4 번
print("six index 존재 여부:", 'six' in frame2.index)
print("ten index 존재 여부:", 'ten' in frame2.index)

#       year   state  pop  debt
# one   2000    Ohio  1.5   NaN
# three 2002    Ohio  3.6   NaN
# five  2002  Nevada  2.9  -1.7
# --------------------------------
#       year   state  pop  debt
# four  2001  Nevada  2.4  -1.5
# five  2002  Nevada  2.9  -1.7
# six   2003  Nevada  3.2   NaN
--------------------------------
# Index(['one', 'three', 'six', 'seven', 'eight', 'nine'], dtype='object')
--------------------------------
# six index 존재 여부: True
# ten index 존재 여부: False
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

## 관련 글

- [[blog/AI(ML & DL)/index|AI(ML & DL)]]
- [[blog/AI(ML & DL)/기계학습- Python Pandas 란-- ( 3 )|[기계학습] Python Pandas 란?? ( 3 )]]
- [[blog/AI(ML & DL)/기계학습- 선형 회귀 실습 (1인당 GDP와 삶의 만족도 예측) ( 1 )|[기계학습] 선형 회귀 실습 (1인당 GDP와 삶의 만족도 예측) ( 1 )]]
- [[blog/AI(ML & DL)/기계학습- 선형 회귀 실습 (1인당 GDP와 삶의 만족도 예측) ( 2 )|[기계학습] 선형 회귀 실습 (1인당 GDP와 삶의 만족도 예측) ( 2 )]]
