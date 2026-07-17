---
title: "[기계학습] Python Pandas 란?? ( 3 )"
created: 2026-07-17
updated: 2026-07-17
type: blog-post
tags: ["blog", "technical-writing", "AI", "CS", "Python"]
category: "AI(ML & DL)"
published: 2025-04-04
source_url: https://ch010104.tistory.com/43
---

# [기계학습] Python Pandas 란?? ( 3 )

## 원문

https://ch010104.tistory.com/43

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

새로운 index 'e' 를 만들 경우, 해당 인덱스에 대한 value 값은 결측치인 NaN으로 설정됨

결측치는 인덱스가 오름 또는 내림차순으로 정렬되어 있을 경우에만 사용 가능함

## 원문 기반 개념 정리

### 1. 기본 설정

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(12345)
np.set_printoptions(precision=4, suppress=True)
plt.rc('figure', figsize=(10, 6))

# 행 표시 수 기본 60 → 20으로 변경
PREVIOUS_MAX_ROWS = pd.options.display.max_rows
pd.set_option("display.max_rows", 20)
```

### 2. 리인덱싱 (Reindexing)

1) 시리즈 리인덱싱

```text
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
print(obj)

# d    4.5
# b    7.2
# a   -5.3
# c    3.6
# dtype: float64

obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj2)

# a   -5.3
# b    7.2
# c    3.6
# d    4.5
# e    NaN
# dtype: float64
```

새로운 index 'e' 를 만들 경우, 해당 인덱스에 대한 value 값은 결측치인 NaN으로 설정됨

2) 데이터프레임 리인덱싱

```text
frame = pd.DataFrame(np.arange(9).reshape((3, 3)),
                     index=['a', 'c', 'd'],
                     columns=['Ohio', 'Texas', 'California'])
print(frame)

#    Ohio  Texas  California
# a     0      1           2
# c     3      4           5
# d     6      7           8

frame2 = frame.reindex(['a', 'b', 'c', 'd'])
print(frame2)

#    Ohio  Texas  California
# a   0.0    1.0         2.0
# b   NaN    NaN         NaN
# c   3.0    4.0         5.0
# d   6.0    7.0         8.0

states = ['Texas', 'Utah', 'California']
print(frame.reindex(columns=states))
# 기존 frame에서는 열 'Utah'이 없기 때문에 모든 요소가 결측치인 NaN이 됨

#    Texas  Utah  California
# a      1   NaN           2
# c      4   NaN           5
# d      7   NaN           8
```

### 3. 결측치 채우기

결측치는 인덱스가 오름 또는 내림차순으로 정렬되어 있을 경우에만 사용 가능함

1) method='ffill'

```text
obj3 = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 5])
print(obj3)

# 0      blue
# 2    purple
# 5    yellow
# dtype: object

print(obj3.reindex(range(6), method='ffill'))
# 결측치가 있을 경우, 결측치의 이전 항목의 인덱스의 값을 가져와서 채움
# 예를 들어, 인덱스 1의 경우, 결측치였기 때문에 이전 인덱스인 0의 값인 blue를 가져와 채움
# 만약에, 이전 인덱스의 값이 없을 경우, 채우지 못하고 NaN으로 표시됨

# 0      blue
# 1      blue
# 2    purple
# 3    purple
# 4    purple
# 5    yellow
# dtype: object
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

2) method='bfill'

```text
print(obj3.reindex(range(-1, 6), method='bfill'))
# 결측치가 있을 경우, 결측치의 이후 항목의 인덱스의 값을 가져와서 채움
# 예를 들어, 인덱스 -1의 경우, 결측치였기 때문에 이후 인덱스인 0의 값인 blue를 가져와 채움
# 만약에, 이후 인덱스의 값이 없을 경우, 채우지 못하고 NaN으로 표시됨

# -1    blue
#  0    blue
#  1    purple
#  2    purple
#  3    yellow
#  4    yellow
#  5    yellow
# dtype: object
```

3) method='nearest'

```text
print(obj3.reindex(range(-1, 6), method='nearest'))
# 결측치가 있을 경우, 결측치의 가장 가까운 항목의 인덱스의 값을 가져와서 채움
# 예를 들어, 인덱스 -1의 경우, 결측치였기 때문에 가장 가까운 인덱스인 0의 값인 blue를 가져와 채움
# 만약에 이전과 이후 인덱스에 값으 모두 있을 경우에는 이후의 인덱스를 선택함
# 예를 들어, 인덱스 1의 경우, 인덱스 0, 2 모두 값이 있지만, 이후 인덱스인 2의 값인 purple를 가져와 채움

# -1    blue
#  0    blue
#  1    purple
#  2    purple
#  3    purple
#  4    yellow
#  5    yellow
# dtype: object
```

4) fill_value 사용

```text
print(obj3.reindex(range(-1, 6), fill_value='No Color'))
# 결측치의 모든 값을 fill_value의 값으로 채움.
# 이 예시에서는, fill_value의 값이 'No Color' 이기 때문에, 인덱스 0, 2, 5를 제외한 모든 결측치를 해당 값으로 채움

# -1    No Color
#  0        blue
#  1    No Color
#  2      purple
#  3    No Color
#  4    No Color
#  5      yellow
# dtype: object
```

리인덱싱 과정은 항상 새로운 시리즈를 생성하기 때문에, reindex를 해도 기존의 값인 obj3 자체가 변하지는 않는다.

```text
print(obj3)

# 0      blue
# 2    purple
# 5    yellow
# dtype: object
```

### 4. 시리즈 인덱싱 / 슬라이싱 / 필터링

```text
obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(obj)

# a    0.0
# b    1.0
# c    2.0
# d    3.0
# dtype: float64

print(obj['b'])   # 1.0
print(obj[1])     # 1.0(1번 인덱스의 값을 가지고 옴. obj['b']와 의미가 같음)

print(obj[2:4])   # 슬라이싱 by 정수(정수 슬라이싱에서는 마지막 인덱스 4는 포함 x)
# c    2.0
# d    3.0
# dtype: float64

print(obj[['b', 'a', 'd']]) # 지정된 이름의 인덱스 사용시엔, 모든 인덱스 출력(지정 슬라이싱)
# b    1.0
# a    0.0
# d    3.0
# dtype: float64

print(obj[[1, 3]]) # 정수 슬라이싱에서는 마지막 인덱스 포함 x -> 인덱스 1, 2 번 출력
# b    1.0
# d    3.0
# dtype: float64
```

1) Boolean 인덱싱

```text
print(obj < 2)

# a     True
# b     True
# c    False
# d    False
# dtype: bool

print(obj[obj < 2]) # obj < 2 가 True인 값에 대해서만 출력

# a    0.0
# b    1.0
# dtype: float64
```

2) 문자열 슬라이싱 (label 기준)

```text
print(obj['b':'d']) # 지정된 이름을 이용한 슬라이싱에서는 마지막 인덱스인 d를 포함

# b    1.0
# c    2.0
# d    3.0
# dtype: float64

obj['b':'d'] = 5 # 이와 같이 지정된 인덱스에 대해 value 값 가능
print(obj)

# a    0.0
# b    5.0
# c    5.0
# d    5.0
# dtype: float64
```

### 5. DataFrame 인덱싱, 슬라이싱, 필터링

```text
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)

#            one  two  three  four
# Ohio         0    1      2     3
# Colorado     4    5      6     7
# Utah         8    9     10    11
# New York    12   13     14    15

print(data['two'])

# Ohio         1
# Colorado     5
# Utah         9
# New York    13
# Name: two, dtype: int64

print(data[['three', 'one']])

#            three  one
# Ohio           2    0
# Colorado       6    4
# Utah          10    8
# New York      14   12
```

1) 행 슬라이싱

```text
print(data[:2])  # 0~1번 행

#          one  two  three  four
# Ohio       0    1      2     3
# Colorado   4    5      6     7
```

2) 필터링

```text
mask1 = data['three'] > 5
print(mask1)

# Ohio        False
# Colorado     True
# Utah         True
# New York     True
# Name: three, dtype: bool

print(data[mask1]) # mask1의 값이 True인 행만 전체 출력

#            one  two  three  four
# Colorado     4    5      6     7
# Utah         8    9     10    11
# New York    12   13     14    15

data[~mask1] = 0 # ~mask1는 mask1의 반대 값을 의미함.
print(data)

#            one  two  three  four
# Ohio         0    0      0     0
# Colorado     4    5      6     7
# Utah         8    9     10    11
# New York    12   13     14    15
```

3) 조건 필터링 전체 적용

```text
mask2 = data < 6
print(mask2)

#             one   two  three   four
# Ohio        True  True   True   True
# Colorado    True   True  False  False
# Utah       False False  False  False
# New York   False False  False  False

data[mask2] = 0 # mask2의 값이 True인 대상에 대해서 0으로 설정
print(data)

#            one  two  three  four
# Ohio         0    0      0     0
# Colorado     0    0      6     7
# Utah         8    9     10    11
# New York    12   13     14    15
```

## 관련 글

- [[blog/AI(ML & DL)/index|AI(ML & DL)]]
- [[blog/AI(ML & DL)/기계학습- Python Pandas 란 -- ( 2 )|[기계학습] Python Pandas 란 ?? ( 2 )]]
- [[blog/AI(ML & DL)/기계학습- 선형 회귀 실습 (1인당 GDP와 삶의 만족도 예측) ( 1 )|[기계학습] 선형 회귀 실습 (1인당 GDP와 삶의 만족도 예측) ( 1 )]]
- [[blog/AI(ML & DL)/기계학습- 선형 회귀 실습 (1인당 GDP와 삶의 만족도 예측) ( 2 )|[기계학습] 선형 회귀 실습 (1인당 GDP와 삶의 만족도 예측) ( 2 )]]
