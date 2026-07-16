---
title: "[기계학습] Python NumPy란?? ( 1 )"
created: 2026-07-13
updated: 2026-07-13
type: blog-post
tags: ["blog", "technical-writing", "AI", "CS", "Python"]
category: "AI(ML & DL)"
published: 2025-03-21
source_url: https://ch010104.tistory.com/21
---

# [기계학습] Python NumPy란?? ( 1 )

## 원문

https://ch010104.tistory.com/21

## 노트 유형

`concept`

## 핵심 개념과 선택 맥락

NumPy는 Python에서 과학/수치 계산을 위한 가장 기본적인 라이브러리.

4. np.empty(): 초기화되지 않은 배열 (속도는 빠르나 값은 예측 불가)

## 원문 기반 개념 정리

### 📦 NumPy란?

NumPy는 Python에서 과학/수치 계산을 위한 가장 기본적인 라이브러리.

고성능 다차원 배열 객체: ndarray

선형대수, 푸리에 변환, 난수 생성 기능 포함

빠른 벡터 연산 가능

### 배열 생성 방법

1. np.zeros(): 0으로 채워진 배열 생성

```python
import numpy as np

np.zeros(5)
# → array([0., 0., 0., 0., 0.])

np.zeros((3, 4))
# → 3행 4열 배열 (shape: (3, 4))
# x 축으로 4만큼, y 축으로 3만큼
#
# array([[0., 0., 0., 0.],
#       [0., 0., 0., 0.],
#       [0., 0., 0., 0.]])
```

2. np.ones(): 1로 채워진 배열

```text
np.ones((3, 4))

# array([[1., 1., 1., 1.],
#       [1., 1., 1., 1.],
#       [1., 1., 1., 1.]])
```

3. np.full(): 지정한 값으로 초기화

```text
np.full((3, 4), np.pi)

# array([[3.14159265, 3.14159265, 3.14159265, 3.14159265],
#       [3.14159265, 3.14159265, 3.14159265, 3.14159265],
#       [3.14159265, 3.14159265, 3.14159265, 3.14159265]])
```

4. np.empty(): 초기화되지 않은 배열 (속도는 빠르나 값은 예측 불가)

```text
np.empty((2, 3))

# array([[1.69594975e-316, 0.00000000e+000, 1.61271680e-312],
#       [2.33419537e-312, 2.48273508e-312, 2.18565567e-312]])
```

5. np.array(): 기존 Python 리스트로부터 생성

```text
np.array([[1, 2, 3, 4], [10, 20, 30, 40]])

# array([[ 1,  2,  3,  4],
#       [10, 20, 30, 40]])
```

### 배열 관련 용어 정리

```text
a = np.zeros((3, 4))
a.shape # (3, 4)
a.ndim # 2
a.size # 12
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

### N차원 배열 (3차원 예시)

```text
np.zeros((2, 3, 4)) # z, y, x 순서

# array([[[0., 0., 0., 0.],
#         [0., 0., 0., 0.],
#         [0., 0., 0., 0.]],
#
#        [[0., 0., 0., 0.],
#         [0., 0., 0., 0.],
#         [0., 0., 0., 0.]]])
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

2개의 3×4 매트릭스 (총 3차원)

shape: (z=2, y=3, x=4)

축 0: 깊이(z) = 2

축 1: 행(y) = 3

축 2: 열(x) = 4

### 난수 생성: rand vs randn

```text
np.random.rand(2, 3)

# array([[0.764, 0.243, 0.312],
#        [0.789, 0.536, 0.990]])

np.random.randn(2, 3)

# array([[-0.438,  1.004,  0.242],
#        [ 0.316, -0.944,  0.815]])
```

시각화 예시

```text
import matplotlib.pyplot as plt

plt.hist(np.random.rand(100000), density=True, bins=100, histtype="step", color="blue", label="rand")
# 0에서 1까지의 랜덤

plt.hist(np.random.randn(100000), density=True, bins=100, histtype="step", color="red", label="randn")
# 평균 0, 표준편차 1의 정규분포

plt.axis([-2.5, 2.5, 0, 1.1])
plt.legend(loc="upper left")
plt.title("Random distributions")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()
```

np.rand.rand(100000)

np.random.nrand(100000)

### np.arange() vs np.linspace()

1. np.arange(): 범위와 간격으로 생성

np.arrange(start, end) 형식 - 범위의 시작 start와 end를 이용하여 1씩 증가. 범위의 끝인 end 값은 포함 x

np.arrange(start, end, step) 형식 - 범위의 시작 start와 end를 이용하여 step씩 증가. 범위의 끝인 end 값은 포함 x - step이 실수일 경우에는 오차문제가 발생할 수 있음

```text
np.arange(1, 5)

# array([1, 2, 3, 4])

np.arange(1.0, 5.0, 0.5)

# array([1. , 1.5, 2. , 2.5, 3. , 3.5, 4. , 4.5])

# 간격을 나타내는 step이 실수일 경우, 오차 발생 가능
print(np.arange(0, 5/3, 1/3)) # depending on floating point errors, the max value is 4/3 or 5/3.
print(np.arange(0, 5/3, 0.333333333))
print(np.arange(0, 5/3, 0.333333334))

#  [0.         0.33333333 0.66666667 1.         1.33333333 1.66666667]
#  [0.         0.33333333 0.66666667 1.         1.33333333 1.66666667]
#  [0.         0.33333333 0.66666667 1.         1.33333334]
```

⚠️ 실수 간격을 쓸 때는 오차 문제로 np.linspace() 사용 권장

2. np.linspace(): 일정 개수로 균등 분할

np.linspace(start, end, num) 형식 - 범위의 시작 start와 end를 이용하여 배열 생성, 생성된 배열값들을 개수를 num으로 정함 - 범위 내에서 개수가 num이 되게 균등하게 추출

```text
np.linspace(0, 5/3, 6)

# array([0.        , 0.33333333, 0.66666667, 1.        , 1.33333333, 1.66666667])
# 0부터 5/3까지의 범위에서 6개의 원소값으로 배열 생성
```

### np.fromfunction(): 함수 기반 배열 생성

배열 생성후에 초기값을 채우는 것을 함수를 이용하여 정함

def my_function(z, y, x) 형식으로 함수를 선언

np.fromfuction(my_function, (3, 2, 4) ) 형식으로 사용

```text
(z, y, x) # (3, 2, 4)

array([[[ (0,0,0), (0,0,1), (0,0,2), (0,0,3)],
        [ (0,1,0), (0,1,1), (0,1,2), (0,1,3)]],

       [[ (1,0,0), (1,0,1), (1,0,2), (1,0,3)],
        [ (1,1,0), (1,1,1), (1,1,2), (1,1,3)]],

       [[ (2,0,0), (2,0,1), (2,0,2), (2,0,3)],
        [ (2,1,0), (2,1,1), (2,1,2), (2,1,3)]]])

각 (z, y, x)에 맞게 my_function에서의 값이 정해짐
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

배열 (3, 2, 3)

```python
def my_function(z, y, x):
    return x + 10*y + 100*z

np.fromfunction(my_function, (3, 2, 4))

# array([[[  0.,   1.,   2.,   3.],
#         [ 10.,  11.,  12.,  13.]],
#
#        [[100., 101., 102., 103.],
#         [110., 111., 112., 113.]],
#
#        [[200., 201., 202., 203.],
#         [210., 211., 212., 213.]]])
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

```python
def my_function2(z, y, x):
    return 100*x + 10*y + z

np.fromfunction(my_function2, (3, 2, 3))

# array([[[  0., 100., 200.],
#         [ 10., 110., 210.]],
#
#        [[  1., 101., 201.],
#         [ 11., 111., 211.]],
#
#        [[  2., 102., 202.],
#         [ 12., 112., 212.]]])
```

> 원문 코드가 길어 이 노트에서는 앞부분만 보존했습니다. 전체는 원문에서 확인합니다.

z, y, x는 각각의 좌표 위치를 나타내며, 계산 결과는 해당 좌표의 수학적 조합으로 결정

x가 가장 빨리 변하고 → 100 단위로 증가

y는 중간 → 10 단위 증가

z는 가장 느리게 → 1 단위 증가

## 관련 글

- [[blog/AI(ML & DL)/index|AI(ML & DL)]]
- [[blog/AI(ML & DL)/기계학습- Python Pandas 란 -- ( 2 )|[기계학습] Python Pandas 란 ?? ( 2 )]]
- [[blog/AI(ML & DL)/기계학습- Python Pandas 란-- ( 3 )|[기계학습] Python Pandas 란?? ( 3 )]]
- [[blog/AI(ML & DL)/기계학습- 선형 회귀 실습 (1인당 GDP와 삶의 만족도 예측) ( 1 )|[기계학습] 선형 회귀 실습 (1인당 GDP와 삶의 만족도 예측) ( 1 )]]
