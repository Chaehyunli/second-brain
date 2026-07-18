---
title: "[기계학습] Python Pandas 란?? ( 4 )"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "AI", "CS"]
category: "AI(ML & DL)"
published: 2025-04-07
source_url: https://ch010104.tistory.com/47
---

# [기계학습] Python Pandas 란?? ( 4 )

## 원문

https://ch010104.tistory.com/47

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

lambda를 이용하여 함수를 직접 선언하고 그 함수의 매개변수로 dataframe을 넘기는 것(apply)

## 원문 기반 개념 정리

### 1. loc() 메서드: 라벨 기반

```python
import pandas as pd
import numpy as np

data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])

#            one  two  three  four
# Ohio         0    1      2     3
# Colorado     4    5      6     7
# Utah         8    9     10    11
# New York    12   13     14    15
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

1) 단일 행 인덱스

```text
data.loc['Colorado'] # 행의 인덱스에 대해, index의 이름으로 반환

# one      4
# two      5
# three    6
# four     7
# Name: Colorado, dtype: int64
```

2) 행+열 조합 접근

```text
data.loc['Colorado', 'three']

# 6
```

3) 여러 열 선택

```text
data.loc['Colorado', ['two', 'three']]

# two      5
# three    6
# Name: Colorado, dtype: int64
```

.loc은 원래의 시리즈를 변경하지 않음

### 2. iloc() 메서드: 정수 기반

1) 특정 행 및 열

```text
# data
#            one  two  three  four
# Ohio         0    1      2     3
# Colorado     4    5      6     7
# Utah         8    9     10    11
# New York    12   13     14    15

data.iloc[2] # 행의 인덱스에 대해, index의 번호(0, 1, 2, ...)으로 반환
# Utah

# one       8
# two       9
# three    10
# four     11
# Name: Utah, dtype: int64

data.iloc[1, 2]   # Colorado 행의 three 열
# 6

data.iloc[2, [3, 0, 1]]
# four    11
# one      8
# two      9
# Name: Utah, dtype: int64

data.iloc[[1, 2], [3, 0, 1]]

#           four  one  two
# Colorado     7    4    5
# Utah        11    8    9
```

.iloc은 원래의 시리즈를 변경하지 않음

### 3. 인덱스 + 조건 필터링

1) 행 슬라이싱 + 열 지정

```text
# data
#            one  two  three  four
# Ohio         0    1      2     3
# Colorado     4    5      6     7
# Utah         8    9     10    11
# New York    12   13     14    15

data.loc[:'Colorado', 'two']
# Ohio        1
# Colorado    5
# Name: two, dtype: int64
```

2) 조건 필터링

```text
data.iloc[:, :3][data['three'] > 5]

#            one  two  three
# Colorado     4    5      6
# Utah         8    9     10
# New York    12   13     14
```

### 4. drop() 메서드: 행/열 제거

1) 시리즈

```text
obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
obj.drop('c')

# a    0.0
# b    1.0
# d    3.0
# e    4.0
# dtype: float64
```

2) 데이터프리임 행 제거

```text
data.drop(['Colorado', 'Ohio'])

#            one  two  three  four
# Utah         8    9     10    11
# New York    12   13     14    15
```

3) 데이터프리임 열 제거

```text
data.drop(['two', 'four'], axis='columns') # axis=1과 동일

           one  three
Ohio         0       2
Colorado     4       6
Utah         8      10
New York    12      14
```

4) isplace=True

```text
data.drop('two', axis=1, inplace=True) # inplace=True를 할 경우, drop이 원본 data에도 변영됨.

# 			one		three	four
# Ohio		0		2		3
# Colorado	4		6		7
# Utah		8		10		11
# New York	12		14		15
```

기존의 .drop은 원래의 시리즈를 변경하지 않음

### 5. sort_values() & sort_index()

1) 인덱스 기준 정렬

```text
obj = pd.Series([4, 7, -3, 2], index=['d', 'a', 'b', 'c'])
obj.sort_index() # 기본적으로는 행 index에 대해 오름차순

# obj
# a    7
# b   -3
# c    2
# d    4

obj.sort_index(axis='columns') # 열에 대해 정렬

frame.sort_index(axis=1, ascending=False) # ascending=False를 통해 내림차순 가능
```

2) 값 기준 정렬

```text
obj.sort_values() # value 값을 기준으로 오름차순

# b   -3
# c    2
# d    4
# a    7
```

3) 데이터프리임 값 정렬 (by)

```text
frame = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
# 	 b	a
# 0	 4	0
# 1	 7	1
# 2	 -3	0
# 3	 2  1

frame.sort_values(by='b') # b를 기준으로 오름차순
# 	 b	a
# 2	 -3	0
# 3	 2	1
# 0	 4	0
# 1	 7	1


frame.sort_values(by=['a', 'b']) # a에 대해서 먼저 정렬 후, 같은 a에 대해서는 b를 가지고 오름차순 정렬

#    b  a
# 2 -3  0
# 0  4  0
# 3  2  1
# 1  7  1
```

### 6. 산술 연산 & fill_value

```text
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
s1 + s2 # s1, s2에서 두 값이 모두 있는 것에 대해서만 결과가 나오고 나머진 NaN

# a    5.2
# c    1.1
# d    NaN
# e    5.5
# f    NaN
# g    NaN
# dtype: float64
```

1) fill_value

```text
df1.add(df2, fill_value=0)
# 둘 중 어느 한쪽만 결측치인 경우 fill_value=0을 적용하여 연산 수행. 양쪽 모두 결측치인 경우에는 NaN으로 표기됨.
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

NaN 값을 0으로 바꾼 연산

### 7. 브로드커스트

```text
arr = np.arange(12.).reshape((3, 4))
arr - arr[0]

# [[0. 0. 0. 0.]
#  [4. 4. 4. 4.]
#  [8. 8. 8. 8.]]
```

1) 범위 변경

```text
arr_1 = arr[:,1][:, np.newaxis]
arr + arr_1

# [[ 1.  2.  3.  4.]
#  [ 9. 10. 11. 12.]
#  [17. 18. 19. 20.]]
```

### 8. 연산 메서드 + 함수 적용

lambda를 이용하여 함수를 직접 선언하고 그 함수의 매개변수로 dataframe을 넘기는 것(apply)

```text
frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'),
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])
frame.apply(lambda x: x.max() - x.min())
```

열 별 평균

```text
frame.apply(lambda x: x.max() - x.min(), axis=1)
```

행 별 평균

### 9. 실습 1: 결측치 처리 및 새로운 열 추가

```text
1. dframe2의 행의 순서를 역순(8-0)으로 재배치한 dframe3을 생성하시오. (Hint: reindex() 이용)
2. dframe3에 debt 열을 추가하고 8, 7, 5, 3, 1 행의 값을 각각 2.1, -1.3, 1.2, -2.5, 0.7로 설정하시오. debt 열의 나머지 행들은 결측치로 설정되도록 하시오.
3. dframe3의 pop 열에 대해서 8, 5, 2 행의 값을 결측치로 변경하시오. (Hint: np.nan이 결측치를 의미함)
4. dframe3에서 한개 이상의 결측치가 포함된 모든 행들을 출력하시오. (Hint: any()와 all() 함수의 경우에도 axis 파라미터 설정 가능함)
5. dframe3에서 결측치가 전혀 포함되지 않은 행들만으로 구성된 dframe3_wo_nan을 생성하시오.
6. dframe3_wo_nan의 pop 열에 포함된 모든 값들의 합, debt 열에 포함된 모든 값들의 합을 출력하시오.
7. dframe3에 isDebtNegative라는 이름의 새로운 열을 추가하고, dframe3의 debt 열의 값이 음수이면 true, 양수이면 false 값으로 채우시오.
```

```text
dict2 = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada', 'NY', 'NY', 'NY'],
         'year': [2000, 2001, 2002, 2001, 2002, 2003, 2002, 2003, 2004],
         'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2, 8.3, 8.4, 8.5]}
dframe2 = pd.DataFrame(dict2)
dframe2

#     state  year  pop
# 0    Ohio  2000  1.5
# 1    Ohio  2001  1.7
# 2    Ohio  2002  3.6
# 3  Nevada  2001  2.4
# 4  Nevada  2002  2.9
# 5  Nevada  2003  3.2
# 6      NY  2002  8.3
# 7      NY  2003  8.4
# 8      NY  2004  8.5

# Code for 1
dframe3 = dframe2.reindex(dframe2.index[::-1])
# dframe3 = dframe2.reindex(index=list(reversed(range(9))))
dframe3

#     state  year  pop
# 8      NY  2004  8.5
# 7      NY  2003  8.4
# 6      NY  2002  8.3
# 5  Nevada  2003  3.2
# 4  Nevada  2002  2.9
# 3  Nevada  2001  2.4
# 2    Ohio  2002  3.6
# 1    Ohio  2001  1.7
# 0    Ohio  2000  1.5
```

```text
# Code for 2
dframe3['debt'] = np.nan  # 초기화
dframe3.loc[8, 'debt'] = 2.1
dframe3.loc[7, 'debt'] = -1.3
dframe3.loc[5, 'debt'] = 1.2
dframe3.loc[3, 'debt'] = -2.5
dframe3.loc[1, 'debt'] = 0.7
dframe3

#     state  year  pop  debt
# 8      NY  2004  8.5   2.1
# 7      NY  2003  8.4  -1.3
# 6      NY  2002  8.3   NaN
# 5  Nevada  2003  3.2   1.2
# 4  Nevada  2002  2.9   NaN
# 3  Nevada  2001  2.4  -2.5
# 2    Ohio  2002  3.6   NaN
# 1    Ohio  2001  1.7   0.7
# 0    Ohio  2000  1.5   NaN
```

```text
# Code for 3
dframe3.loc[8, 'pop'] = np.nan
dframe3.loc[5, 'pop'] = np.nan
dframe3.loc[2, 'pop'] = np.nan
dframe3

#     state  year  pop  debt
# 8      NY  2004  NaN   2.1
# 7      NY  2003  8.4  -1.3
# 6      NY  2002  8.3   NaN
# 5  Nevada  2003  NaN   1.2
# 4  Nevada  2002  2.9   NaN
# 3  Nevada  2001  2.4  -2.5
# 2    Ohio  2002  NaN   NaN
# 1    Ohio  2001  1.7   0.7
# 0    Ohio  2000  1.5   NaN
```

```text
# Code for 4
# print(dframe3.isnull().any(axis=1))
nan_mask = dframe3.isnull().any(axis=1)
rows_with_nan = dframe3[nan_mask]

# rows_with_nan = dframe3[dframe3.isnull().any(axis=1)]
print("결측치가 포함된 행들:")
print(rows_with_nan)

# 결측치가 포함된 행들:
#     state  year  pop  debt
# 8      NY  2004  NaN   2.1
# 6      NY  2002  8.3   NaN
# 5  Nevada  2003  NaN   1.2
# 4  Nevada  2002  2.9   NaN
# 2    Ohio  2002  NaN   NaN
# 0    Ohio  2000  1.5   NaN
```

```text
# Code for 5
# dframe3_wo_nan = dframe3[dframe3.notnull().all(axis=1)]

no_nan_mask = ~nan_mask # dataframe에 대해서는 ~를 사용 불가하지만, mask에 대해서는 가능!!
dframe3_wo_nan = dframe3[no_nan_mask]

print("결측치가 하나도 없는 행들:")
print(dframe3_wo_nan)

# 결측치가 하나도 없는 행들:
#     state  year  pop  debt
# 7      NY  2003  8.4  -1.3
# 3  Nevada  2001  2.4  -2.5
# 1    Ohio  2001  1.7   0.7
```

```text
# Code for 6
pop_sum = dframe3_wo_nan['pop'].sum()
debt_sum = dframe3_wo_nan['debt'].sum()
print("dframe3_wo_nan의 pop 합:", pop_sum)
print("dframe3_wo_nan의 debt 합:", debt_sum) # 부동소수점 오차가 있음.

# dframe3_wo_nan의 pop 합: 12.5
# dframe3_wo_nan의 debt 합: -3.0999999999999996
```

```text
# Code for 7
dframe3['isDebtNegative'] = dframe3['debt'] < 0
print("dframe3 최종 결과:")
print(dframe3)

# dframe3 최종 결과:
#     state  year  pop  debt  isDebtNegative
# 8      NY  2004  NaN   2.1           False
# 7      NY  2003  8.4  -1.3            True
# 6      NY  2002  8.3   NaN           False
# 5  Nevada  2003  NaN   1.2           False
# 4  Nevada  2002  2.9   NaN           False
# 3  Nevada  2001  2.4  -2.5            True
# 2    Ohio  2002  NaN   NaN           False
# 1    Ohio  2001  1.7   0.7           False
# 0    Ohio  2000  1.5   NaN           False
```

### 실습 2: 정렬

```text
1. dframe3에 대해 행의 인덱스를 기준으로 오름차순 정렬된 상태의 dframe3_sorted_in_row를 생성하시오.
2. dframe3에 대해 열의 이름을 기준으로 내림차순 정렬된 상태의 dframe3_sorted_in_col를 생성하시오.
3. dframe3에 대해 state와 year 순으로 값을 기준으로 내림차순 정렬되도록 코드를 작성하시오. dframe3 자체가 수정되도록 코드를 작성하시오.
```

```text
dframe

#    state	year	pop		debt	isDebtNegative
# 8	 NY	    2004	NaN		2.1		False
# 7	 NY	    2003	8.4		-1.3	True
# 6	 NY		2002	8.3		NaN		False
# 5	 Nevada	2003	NaN		1.2		False
# 4	 Nevada	2002	2.9		NaN		False
# 3	 Nevada	2001	2.4		-2.5	True
# 2	 Ohio	2002	NaN		NaN		False
# 1	 Ohio	2001	1.7		0.7		False
# 0	 Ohio	2000	1.5		NaN		False
```

```text
# Code for 1
dframe3_sorted_in_row = dframe3.sort_index(axis=0, ascending=True)
print(dframe3_sorted_in_row)

#     state  year  pop  debt  isDebtNegative
# 0    Ohio  2000  1.5   NaN           False
# 1    Ohio  2001  1.7   0.7           False
# 2    Ohio  2002  NaN   NaN           False
# 3  Nevada  2001  2.4  -2.5            True
# 4  Nevada  2002  2.9   NaN           False
# 5  Nevada  2003  NaN   1.2           False
# 6      NY  2002  8.3   NaN           False
# 7      NY  2003  8.4  -1.3            True
# 8      NY  2004  NaN   2.1           False
```

```text
# Code for 2
dframe3_sorted_in_col = dframe3.sort_index(axis=1, ascending=False)
print(dframe3_sorted_in_col)

#    year   state  pop  isDebtNegative  debt
# 8  2004      NY  NaN           False   2.1
# 7  2003      NY  8.4            True  -1.3
# 6  2002      NY  8.3           False   NaN
# 5  2003  Nevada  NaN           False   1.2
# 4  2002  Nevada  2.9           False   NaN
# 3  2001  Nevada  2.4            True  -2.5
# 2  2002    Ohio  NaN           False   NaN
# 1  2001    Ohio  1.7           False   0.7
# 0  2000    Ohio  1.5           False   NaN
```

```text
# Code for 3
dframe3.sort_values(by=['state', 'year'], ascending=[False, False], inplace=True) # state 기준으로 내림차순으로 정렬한 후, 동일한 state 내에서 year에 대해 내림차순으로 정렬
dframe3 # inplace=True 이기 때문에 dframe3 자체가 변함

#     state  year  pop  debt  isDebtNegative
# 8      NY  2004  NaN   2.1           False
# 7      NY  2003  8.4  -1.3            True
# 6      NY  2002  8.3   NaN           False
# 5  Nevada  2003  NaN   1.2           False
# 4  Nevada  2002  2.9   NaN           False
# 3  Nevada  2001  2.4  -2.5            True
# 2    Ohio  2002  NaN   NaN           False
# 1    Ohio  2001  1.7   0.7           False
# 0    Ohio  2000  1.5   NaN           False
```

## 관련 글

- [[blog/AI(ML & DL)/index|AI(ML & DL)]]
- [[blog/AI(ML & DL)/기계학습- Python Pandas 란-- ( 3 )|[기계학습] Python Pandas 란?? ( 3 )]]
- [[blog/AI(ML & DL)/기계학습- Python Pandas 란 -- ( 2 )|[기계학습] Python Pandas 란 ?? ( 2 )]]
- [[blog/AI(ML & DL)/기계학습- 선형 회귀 실습 (1인당 GDP와 삶의 만족도 예측) ( 1 )|[기계학습] 선형 회귀 실습 (1인당 GDP와 삶의 만족도 예측) ( 1 )]]
