# 이진탐색

## 정의

- 정렬된 리스트에서 탐색의 범위를 절반씩 좁혀가면서 데이터를 탐색하는 기법

## 특징

- 시작점, 중간점, 끝점을 이용해 탐색의 범위를 설정한다
- 순차탐색과 차이점: 순차는 특정 데이터를 맨앞에서 부터 차례데로 찾는것

## template

1. 재귀함수 사용

```python
# target의 위치를 찾는 함수
def binary_search(array, target, start, end):
  # 시작점이 끝점보다 큰 경우
  if start > end:
    return None
  mid = (start + end) // 2  # 중간점
  # 중간점이 target인 경우 바로찾음
  if array[mid] == target:
    return mid
  # 중간점보다 target이 작으면 target을 기준으로 왼쪽만 탐색
  elif array[mid] > target:
    return binary_search(array, target, start, mid-1)
  # 중간점보다 target이 큰 경우 오른쪽만 확인
  else:
    return binary_search(array, target, mid+1, end)

# main
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
  print("원소가 없습니다.")
else:
  print(result + 1)
```

2. 반복문 사용

```python
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None
```

3. bisect 모듈사용

```python
import bisect

def binary_search(array, target):
  idx = bisect.bisect_left(array, target)

  if idx < len(array) and array[idx] == target:
    return idx
  else:
    return -1
```

위의 세가지 풀이방식은 속도차이가 거의 없지만, 가장 느린건 재귀를 이용한 풀이이다.

코딩테스트 시에는 가급적 재귀나 반복으로 풀이하자.
