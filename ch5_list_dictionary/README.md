# list

- 기본형식

```python
a = [1, 2, 3]
a.append(4)
# [1, 2, 3, 4]

a.insert(3, 5)  # 3번째 인덱스에 5를 삽입한다.
# [1, 2, 3, 5, 4]
```

- 슬라이싱

```python
a = [1, 2, 3, 4, 5]
a[1:3]
# [2, 3]

a[:3]  # 시작 인덱스 생략가능
# [1, 2, 3]

a[3:]  # 종료 인덱스 생략가능
# [4, 5]

a[1:4:2]  # 1부터 인덱스 3까지 두칸씩 건너뛰기
# [2, 4]
```

- 인덱스로 요소 삭제하기

```python
a = [1, 2, 3, 5, 4, '안녕']
del a[1]
# [1, 3, 5, 4, '안녕']
```

- 값으로 삭제하기

```python
a = [1, 2, 3, 5, 4, '안녕']
a.remove(2)
# [1, 3, 5, 4, '안녕']
```

- pop()

```python
a = [1, 2, 3, 5, 4, '안녕']
a.pop(5)
# [1, 2, 3, 5, 4]
```

# dictionary

- 딕셔너리 주요 시간 복잡도는 O(1)이다.
- 키/값 구조로 이루어져있다.

## 종류

- `len(a)`: 요소의 개수를 리턴한다.
- `a[key]`: 키를 조회하여 값을 리턴
- `a[key] = value`: 키/값을 삽입한다
- `key in a`: 딕셔너리에 키가 존재하는지 확인한다.

## 표현방법

```python
a = dict()
a = {}
```

```python
a = {'key1':'value1', 'key2':'value2'}
a['key3'] = 'value3'
# a = {'key1':'value1', 'key2':'value2', 'key3':'value3'}

a['key1']
# value1

for k,v in a.items():
  print(k,v)
'''
key1 value1
key2 value2
key3 value3
'''
```

이처럼 키를 지정해서 값을 조회할 수 있고, for문과 items() 메소드를 사용해서 키와 값을 각각 꺼내올 수 있다.