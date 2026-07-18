---
title: "[기계학습] Python Pandas 란 ?? ( 1 )"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "AI", "OS"]
category: "AI(ML & DL)"
published: 2025-03-31
source_url: https://ch010104.tistory.com/35
---

# [기계학습] Python Pandas 란 ?? ( 1 )

## 원문

https://ch010104.tistory.com/35

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

Pandas는 이전 NumPy와 함께 데이터 분석에 자주 사용되는 라이브러리로, 시리즈(Series) 와 데이터프레임(DataFrame) 이 있다.

만약, name이 없는 시리즈로 dataFrame을 만들 경우에는 name 이 0으로 생성됨.

## 원문 기반 개념 정리

Pandas는 이전 NumPy와 함께 데이터 분석에 자주 사용되는 라이브러리로, 시리즈(Series) 와 데이터프레임(DataFrame) 이 있다.

### 1. 시리즈 생성과 인덱스

```text
obj1 = pd.Series([4, 7, -5, 3])
# 시리즈는 1차원 배열에 대해서만 생성 가능함!!

# obj1
# 0     4
# 1     7
# 2    -5
# 3     3
# dtype: int64

ojb1.values
# [ 4,  7, -5,  3]

ojb1.index
# RangeIndex(start=0, stop=4, step=1)
# 자동으로 생성되는 index는 RangeIndex 객체임
```

### 2. 인덱스 변경

```text
obj1.index = ['Bob', 'Steve', 'Jeff', 'Ryan']

# Bob       4
# Steve     7
# Jeff     -5
# Ryan      3

obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
obj2

# 이처럼 인덱스와 value 값을 지정하면서 생성 가능
# d    4
# b    7
# a   -5
# c    3
# dtype: int64

obj2.index

# Index(['d', 'b', 'a', 'c'], dtype='object')
# 직접 지정한 index의 경우 index onject 객체임
```

### 3. 사전으로 생성

```text
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata) # 사전(딕셔너리) 형태에서도 시리즈를 생성 가능

# Ohio      35000
# Texas     71000
# Oregon    16000
# Utah       5000
# dtype: int64

sdata
# {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}

states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)

# 사전을 사용해서도 index 지정 가능
# 사전에 키는 states를 사용하며, index 리스트에 포함되지 않은 index(Utah)는 포함 x
# Utah의 경우, 값은 존재하지만, index에 없음
# 사전에 키는 있지만 값이 없는 경우, 결측치라는 의미로 NaN으로 표시
# California의 경우 index 리스트에는 포함되어 있지만, 값이 없음

# obj4
# California        NaN
# Ohio          35000.0
# Oregon        16000.0
# Texas         71000.0
# dtype: float64
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### 6. Series.name 및 index.name 속성

```text
# 시리즈 생성 (결측치 포함)
obj4 = pd.Series([NaN, 35000.0, 16000.0, 71000.0],
                 index=['California', 'Ohio', 'Oregon', 'Texas'])

# 시리즈와 인덱스 이름 지정
obj4.name = 'population'
obj4.index.name = 'state'

# obj4

# state
# California        NaN
# Ohio          35000.0
# Oregon        16000.0
# Texas         71000.0
# Name: population, dtype: float64

# 이 시리즈의 이름을 population으로 하고 index의 이름을 state로 지정
#-----------------------------------------------------------------
# pandas.Series는 NumPy 배열처럼 항목별 연산이 가능
# obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])

# d     4
# b     7
# a    -5
# c     3
# dtype: int64

obj2 * 2

# d     8
# b    14
# a   -10
# c     6
# dtype: int64
#-------------------------------------------------------------------
# 시리즈 onj2의 해당 index가 있는지 확인
# 사전(딕셔너리)의 key 확인과 같이 작동
'b' in obj2   # True
'e' in obj2   # False
```

### 5. 연산 및 결측치 확인

```text
obj4 = pd.Series([None, 35000.0, 16000.0, 71000.0],
                 index=['California', 'Ohio', 'Oregon', 'Texas'])
obj4.name = 'population'
obj4.index.name = 'state'
obj4

# state
# California        NaN
# Ohio          35000.0
# Oregon        16000.0
# Texas         71000.0
# Name: population, dtype: float64

obj4.isnull() # 결측치가 있는가?? 있으면 True, 없으면 False

# state
# California     True
# Ohio          False
# Oregon        False
# Texas         False
# Name: population, dtype: bool

# obj4.notnull() # 결측치가 없는가?? 있으면 False, 없으면 True

# state
# California    False
# Ohio           True
# Oregon         True
# Texas          True
# Name: population, dtype: bool

obj4.isnull().any()  # True (California가 NaN이므로)
obj4.notnull().all()  # False (NaN이 1개 있으므로)

#--------------------------------------------------------------
obj3 = pd.Series({
    'Ohio': 35000,
    'Texas': 71000,
    'Oregon': 16000,
    'Utah': 5000
})

obj3 + obj4 # obj3는 California에 대한 정보가 없고, obj4에서는 Utah에 대한 정보가 없음
# obj3, obj4에 공통으로 들어있는 index에 대해서만 연산이 잘 수행되고, 어느 한쪽만 있는 경우에는 NaN으로 표시

# California         NaN
# Ohio           70000.0
# Oregon         32000.0
# Texas         142000.0
# Utah               NaN
# dtype: float64
```

### 5 . 시리즈 인덱싱 및 조건 필터

```text
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)

# d     4
# b     7
# a    -5
# c     3
# dtype: int64

# 각 index의 값을 반환
obj2['a'] # -5

obj2['d'] = 6 # 각 index에 대해 값을 변경할 수 있음
print(obj2)

# d     6
# b     7
# a    -5
# c     3
# dtype: int64

obj2_1 = obj2[['c', 'a', 'd']]
print(obj2_1)
# obj2 시리즈에서 index 리스트를 이용해 새로운 시리즈 생성 가능

# c     3
# a    -5
# d     6
# dtype: int64

#-----------------------------------------------------------
mask = obj2 > 0
print(mask)
# 위와 같이 mask에 조건을 걸어주면, boolean 타입으로 반환!!

# d     True
# b     True
# a    False
# c     True
# dtype: bool

print(obj2[mask]) # mask의 조건이 True 인 index에 대해서만 반환

# d    6
# b    7
# c    3
# dtype: int64
```

실습 문제

```text
다음과 같이 mySeries를 생성하시오.

- mySeries 각 항목의 값은 10, 20, 30, 40, 50으로, 인덱스 a, b, c, d, e가 되도록 하시오.
- mySeries에 대해서 index, values, size 속성 값을 확인해보세요.
- mySeries에 대해서 값이 20을 초과하는 항목들만 선택적으로 출력하시오.
- mySeries의 인덱스 c와 e인 항목의 값을 결측치로 변경하시오.(결측치를 위해 np.nan을 사용하면 됩니다.)
- mySeries에 결측치가 포함되어 있는지 여부를 확인하기 위한 코드를 작성하시오.
- mySeries에 포함된 결측치의 총 개수를 확인해서 출력해주는 코드를 작성하시오
#------------------------------------------------------------------------------------------------

mySeries = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print("📌 mySeries:")
print(mySeries)

print("\n🔍 index, values, size 출력")
print("index:", mySeries.index)
print("values:", mySeries.values)
print("size:", mySeries.size)

mask2 = mySeries > 20
print("\n✅ 값이 20을 초과하는 항목:")
print(mySeries[mask2])

mySeries['c'] = np.nan
mySeries['e'] = np.nan
print("\n⚠️ after NaN c, e:")
print(mySeries)

print("\n🔎 결측치 여부 판단")
print(mySeries.isnull().any()) # 결측치 여부 판단

print("\n📊 결측치 개수 확인")
print(mySeries.isnull().sum()) # sum은 합을 더하는 함수, isnull()의 결과는 true, false이기 때문에 true를 1, false를 0으로 하여 합을 구하면 true의 개수이다.

# 결과
# 📌 mySeries:
# a    10
# b    20
# c    30
# d    40
# e    50
# dtype: int64

# 🔍 index, values, size 출력
# index: Index(['a', 'b', 'c', 'd', 'e'], dtype='object')
# values: [10 20 30 40 50]
# size: 5

# ✅ 값이 20을 초과하는 항목:
# c    30
# d    40
# e    50
# dtype: int64

# ⚠️ after NaN c, e:
# a    10.0
# b    20.0
# c     NaN
# d    40.0
# e     NaN
# dtype: float64

# 🔎 결측치 여부 판단
# True

# 📊 결측치 개수 확인
# 2
```

### 6. 데이터프레임 생성 및 조작

### 1) 시리즈로부터 DataFrame 생성

```text
series1 = pd.Series([4, 5, 6, 3, 1], name="Mango")
series2 = pd.Series([5, 4, 3, 0, 2], name="Apple")
series3 = pd.Series([2, 3, 5, 2, 7], name="Banana")

dict1 = {
    series1.name: series1,
    series2.name: series2,
    series3.name: series3
}
# dict1 이라는 사전(딕셔너리)를 만들고, 이 사전으로 DataFrame을 만듬
# 세 개의 시리즈를 DataFrame으로 묶기 위해 키(key)는 각 시리즈의 name으로, 값(value)은 해당 시리즈로 지정

frame1 = pd.DataFrame(dict1)
frame1

# 이런식으로 생성하면 따로 index를 설정하지 못하기 때문에 0,1,2,3,4...로 되어 있음

#    Mango  Apple  Banana
# 0      4      5       2
# 1      5      4       3
# 2      6      3       5
# 3      3      0       2
# 4      1      2       7
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

만약, name이 없는 시리즈로 dataFrame을 만들 경우에는 name 이 0으로 생성됨.

### 2) pd.concat() 함수 활용

```text
pd.concat([series1, series2, series3], axis=1) # 3개의 시리즈를 x축 방향으로 합침

#    Mango  Apple  Banana
# 0      4      5       2
# 1      5      4       3
# 2      6      3       5
# 3      3      0       2
# 4      1      2       7

pd.concat([series1, series2, series3], axis=0 # 3개의 시리즈를 y축 방향으로 합침

# 0    4
# 1    5
# 2    6
# 3    3
# 4    1
# 0    5
# 1    4
# 2    3
# 3    0
# 4    2
# 0    2
# 1    3
# 2    5
# 3    2
# 4    7
# dtype: int64
```

### 3) 리스트 사전 → DataFrame

```text
dict2 = {
    'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada', 'NY', 'NY', 'NY'],
    'year': [2000, 2001, 2002, 2001, 2002, 2003, 2002, 2003, 2004],
    'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2, 8.3, 8.4, 8.5]
}
# key 값 state, year, pop에 대해 리스트로 값을 준 후, DataFrame을 만듬
frame2 = pd.DataFrame(dict2)
frame2

#    state  year  pop
# 0   Ohio  2000  1.5
# 1   Ohio  2001  1.7
# 2   Ohio  2002  3.6
# 3 Nevada  2001  2.4
# 4 Nevada  2002  2.9
# 5 Nevada  2003  3.2
# 6     NY  2002  8.3
# 7     NY  2003  8.4
# 8     NY  2004  8.5
```

### 4) 중첩 사전 → DataFrame

```text
dict3 = {
    'Nevada': {2001: 2.4, 2002: 2.9},
    'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}
}
frame3 = pd.DataFrame(dict3)
# 이 경우, 행에 대한 index까지 설정 가능, 하지만 key 값 Nevada의 value 2000이 없음.
# 이를 결측치라 보고, NaN으로 표기

#       Nevada  Ohio
# 2000     NaN   1.5
# 2001     2.4   1.7
# 2002     2.9   3.6
```

### 5) 행과 열 이름 지정

```text
frame3.index.name = 'year' # index의 이름을 정함
frame3.columns.name = 'state' # 열에 대한 이름을 정함

# state  Nevada  Ohio
# year
# 2000     NaN   1.5
# 2001     2.4   1.7
# 2002     2.9   3.6
```

### 6) values 속성으로 배열 추출

```text
frame3.values # DataFrame의 각 원소의 값만을 index나 column 없이 반환

# [[nan, 1.5],
#  [2.4, 1.7],
#  [2.9, 3.6]]
```

### 7) 열 추가 & 열 순서 지정

```text
frame2
#    state  year  pop
# 0   Ohio  2000  1.5
# 1   Ohio  2001  1.7
# 2   Ohio  2002  3.6
# 3 Nevada  2001  2.4
# 4 Nevada  2002  2.9
# 5 Nevada  2003  3.2
# 6     NY  2002  8.3
# 7     NY  2003  8.4
# 8     NY  2004  8.5

frame2 = pd.DataFrame(dict2, columns=['year', 'state', 'pop', 'debt'])
# 기존 dataFrame의 열의 순서를 다르게 하여 출력 가능
# 새로운 열 debt을 만들수도 있음. -> 이과 같이 이름만 지정할 경우, 모두 결측치 NaN으로 처리

frame2_ = frame2.copy() # frame2와의 충돌을 피하기 위해 복사 copy하여 사용

frame2_['debt2'] = pd.Series(np.linspace(0, 1, 9))
# np.linspace는 0부터 1까지의 범위를 9개로 균등하게 쪼개서 반환
# 새로운 열 debt2에 대해 값을 지정함.
frame2_

#    year  state  pop debt  debt2
# 0  2000   Ohio  1.5  NaN  0.000
# 1  2001   Ohio  1.7  NaN  0.125
# ...
# 8  2004     NY  8.5  NaN  1.000
```

### 8) 인덱스 지정

```text
frame2 = pd.DataFrame(dict2,
    index=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])

# 기존에 0,1,2,3,4....으로 되어 있던 index를 새롭게 지정

frame2

#        state  year  pop
# one     Ohio  2000  1.5
# two     Ohio  2001  1.7
# three   Ohio  2002  3.6
# four  Nevada  2001  2.4
# five  Nevada  2002  2.9
# six   Nevada  2003  3.2
# seven     NY  2002  8.3
# eight     NY  2003  8.4
# nine      NY  2004  8.5

frame2 = pd.DataFrame(dict2, columns=['year', 'state', 'pop', 'debt'], index=[
    'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
])
# column 과 index 등 여러 속성을 동시에 지정도 가능

frame2

#        year  state   pop debt
# one     2000   Ohio   1.5  NaN
# two     2001   Ohio   1.7  NaN
# three   2002   Ohio   3.6  NaN
# four    2001 Nevada   2.4  NaN
# five    2002 Nevada   2.9  NaN
# six     2003 Nevada   3.2  NaN
# seven   2002     NY   8.3  NaN
# eight   2003     NY   8.4  NaN
# nine    2004     NY   8.5  NaN
```

### 9) 중복 인덱스도 허용됨

```text
frame2

#        year  state   pop debt
# one     2000   Ohio   1.5  NaN
# two     2001   Ohio   1.7  NaN
# three   2002   Ohio   3.6  NaN
# four    2001 Nevada   2.4  NaN
# five    2002 Nevada   2.9  NaN
# six     2003 Nevada   3.2  NaN
# seven   2002     NY   8.3  NaN
# eight   2003     NY   8.4  NaN
# nine    2004     NY   8.5  NaN

dup_labels = pd.Index(['one', 'two', 'two', 'three', 'three', 'three'])
frame_dup = pd.DataFrame(frame2.values[:6], columns=frame2.columns, index=dup_labels)
# frame2.values[:6] 로 기존 frame2에서 index six까지의 value에 대해, 새로운 index dup_labels를 사용
# columns는 기존 frame2의 colums를 사용

frame_dup

#        year   state pop debt
# one   2000.0   Ohio  1.5  NaN
# two   2001.0   Ohio  1.7  NaN
# two   2002.0   Ohio  3.6  NaN
# three 2001.0 Nevada  2.4  NaN
# three 2002.0 Nevada  2.9  NaN
# three 2003.0 Nevada  3.2  NaN
```

### 10) 열 인덱싱 및 속성 방식

```text
obj = pd.Series(range(3), index=['a', 'b', 'c'])
index = obj.index

obj
# a    0
# b    1
# c    2
# dtype: int64

index
# Index(['a', 'b', 'c'], dtype='object')

print(index[1])    # 출력: 'b'
print(index[1:])   # 출력: Index(['b', 'c'], dtype='object')
# 이런식으로 index 객체의 index 속성을 직접 반환도 가능

index[1] = 'd'  # 오류 발생!!!
# TypeError: Index does not support mutable operations

# 직접 반환은 가능하지만, 위와 같이 하나의 index 항목은 변경하는 것은 불가능
# index 객체는 안정성 문제로 인해 불변 객체임.
# 따라서, 직접 수정은 못하고 index를 수정하고 싶으면, 새로운 index 리스트를 만들어서 리스트내에서 값을 변경한 후, index 리스트를 index 객체로 만들어서 재정의해야함.

# index 재정의 예시
new_index = list(index) # new_index 는 기존의 ['a', 'b', 'c']의 리스트임
new_index[1] = 'd' #  ['a', 'b', 'c'] ->  ['a', 'd', 'c']
obj2 = pd.Series(obj.values, new_index)
index = pd.Index(new_index)

print(index)
# Index(['a', 'd', 'c'], dtype='object')

print(obj2)
# a    0
# d    1
# c    2
# dtype: int64
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

## 관련 글

- [[blog/AI(ML & DL)/index|AI(ML & DL)]]
- [[blog/AI(ML & DL)/기계학습- Python NumPy 란 -- ( 4 )|[기계학습] Python NumPy 란 ?? ( 4 )]]
- [[blog/OS/운영체제- 가상 기억장치란|[운영체제] 가상 기억장치란??]]
- [[blog/AI(ML & DL)/기계학습- Python NumPy 란 -- ( 3 )|[기계학습] Python NumPy 란 ?? ( 3 )]]
