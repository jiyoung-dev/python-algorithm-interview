# 문자열 슬라이싱 활용하기

- 대부분의 문자열 작업은 슬라이싱으로 처리하는게 가장 빠르다.

## Example

> <pre>     0 1 2 3 4 <br>
> s = "안녕하세요" <br>
>      -5-4-3-2-1</pre>

- `s[1:4]`: 녕하세
- `s[1:-2]`: 녕하
- `s[1:]`: 녕하세요
- `s[:]`: 안녕하세요
- `s[1:100]`: 녕하세요
- `s[-1]`: 요
- `s[-4]`: 녕
- `s[:-3]`: 안녕
- `s[-3:]`: 하세요
- `s[::1]`: 안녕하세요 (한칸씩 앞으로 이동한다)
- `s[::-1]`: 요세하녕안 (뒤집는다)
- `s[::2]`: 안하요 (두칸씩 앞으로 이동한다)

# 람다표현식

> 람다표현식이란, 식별자 없이 실행 가능한 함수를 말한다. 함수 선언 없이 하나의 식으로 함수를 단순하게 표현할 수있다.

## Example

s = ['2 A', '1 B', '4 C', '1 A'] 배열을 문자 순으로 정렬하려면?

- sorted()로 정렬하기

```python
s = ['2 A', '1 B', '4 C', '1 A']
sorted(s)

# ['1 A', '1 B', '2 A', '4 C']
```

이처럼 단순히 sorted() 함수를 사용하면 맨앞에 열인 숫자를 기준으로 정렬이 이루어진다. 우리가 원하는건 두번째열 기준!

- 람다 표현식 사용

```python
s.sort(key=lambda x: (x.split()[1], x.split()[0]))

# ['1 A', '2 A', '1 B', '4 C']
```

이처럼 특정 데이터를 기준으로 정렬하기위해 람다와 key 매개변수를 사용했다. key= 옵션으로 정렬에 적용할 함수를 미리 지정할 수 있는것.

# 여러가지 정렬 방법

> sorted()와 sort() 차이점 알아보기

1. sorted() 함수 사용

```python
a = [2, 5, 1, 9, 7]
sorted(a)

# [1, 2, 5, 7, 9]

b = 'zbdaf'
sorted(b)

# ['a', 'b', 'd', 'f', 'z']

# 문자 sorted 결과는 리스트로 리턴된다.
# 다시 문자열로 되돌리기

"".join(sorted(b))

# 'abdfz'
```

sorted()를 그냥 사용하면 숫자와 문자 모두 오름차순 정렬.

2. sort() 함수 사용

- sort()는 리스트 자체를 정렬하는 자료형이다.
- 제자리 정렬 알고리즘. 입력을 출력으로 덮어쓰므로 추가공간이 필요하지않아, 리턴값이 없다.

```python
a.sort()
arr = b.sort()  # 잘못된 표현이다.
```

3. key, lambda 사용

- key= 옵션은 문자열에서 특정 조건을 걸어 정렬할때 주로 사용.

```python
# 단어 길이순서로 정렬하시오.

c = ['ccc', 'd', 'bb']
sorted(c, key=len)

# ['d', 'bb', 'ccc']

# 첫 문자열과 마지막 문자열 순으로 정렬하시오.
d = ['cde', 'cfc', 'abc']

def fn(s):
  return s[0], s[-1]

print(sorted(a, key=fn))

# ['abc', 'cfc', 'cde']
```

```python
d = ['cde', 'cfc', 'abc']

sorted(d, key=lambda: x: (x[0], x[-1]))

# ['abc', 'cfc', 'cde']
```

람다 표현법은 문자열 정렬에서 자주쓰이므로 형태 꼭 외워두기!!
