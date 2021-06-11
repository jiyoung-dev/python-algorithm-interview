# 파이썬 네이밍 컨벤션

- 스네이크 케이스 (Snake Case)를 따른다.
  - 각 단어를 밑줄로 구분함.
  - `snake_case: int = 1`

# 리스트 컴프리헨션

- 리스트 컴프리헨션을 사용하지 않은경우

```python
a = []
for n in range(1, 10+1):
  if n % 2 == 1:
    a.append(n * 2)
```

- 리스트 컴프리헨션 적용

```python
[n * 2 for n in range(1, 10+1) if n % 2 == 1]
```

사용하지 않은 경우, 라인 수가 훨씬 길고 a라는 별도의 리스트 변수 또한 필요해졌다.

# enumerate

- `enumerate()`는 열거하다 라는 의미로, 여러 자료형을 인덱스를 포함한 enumerate 개체로 리턴한다.

```python
a = [1,2,3,2,45]
print(list(enumerate(a)))

# [(0, 1), (1, 2), (2, 3), (3, 2), (4, 45)]
```

이처럼 인덱스를 자동으로 부여해주기 때문에 매우 편리하다.

```python
a = ['a1', 'b2']

for i, v in enumerate(a):
    print(i, v)

'''
0 a1
1 b2
'''
```

# print()

```python
print('a1', 'b2')  # a1 b2
print('a1', 'b2', sep=',') # a1,b2
```

```python
print('aa', end=' ')
print('bb')

# aa bb
```

- `.format` 적용

```python
idx = 1
fruit = "Apple"
print('{}: {}'.format(idx + 1, fruit))

# 2: Apple
```

- `f-string` 적용
  - 이 방식은 3.6이상 버전에서만 사용 가능하다. 자바스크립트랑 생긴게 비슷하다!

```python
idx = 1
fruit = "Apple"
print(f'{idx + 1}: {fruit}')

# 2: Apple
```
