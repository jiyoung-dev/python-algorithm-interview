# 힙 자료구조

- 트리 기반의 자료구조
- 파이썬에서는 최소힙이 구현되어 있다.
  - Min Heap: 부모 노드가 항상 자식 노드보다 작거나 같은 힙 구조.
  - 부모, 자식간의 관계만 정의할 뿐, 정렬된 구조는 아니다.
- 우선순위 큐를 사용할때 활용하는 `heapq` 모듈이 힙으로 구현되어 있음
- 코딩테스트 문제 중, 최솟값 혹은 최댓값을 계속해서 호출해야하는 상황인 경우 Heap 구조를 이용해서 구현하면 시간 측면에서 굉장히 효율적임.

## heapq 내장함수

```python
import heapq
```

- heapq 모듈을 이용해 힙 자료구조를 사용할 수 있고 기본적으로 Min-priority-queue 구조임

### heapify()

- 기존 배열을 Heap 구조로 만들기

```python
testheap = [1,3,2,6,8,0,6]
heapq.heapify(testheap)
print(testheap)

# 실행결과 => Heap 구조로 변함
[0,3,1,6,8,2,6]
```

### heappush(배열이름, 요소)

- Heap에 요소 추가하기

```python
testheap = []
heapq.heappush(testheap, 3)
heapq.heappush(testheap, 5)
heapq.heappush(testheap, 1)
heapq.heappush(testheap, -3)
print(testheap)

# 실행결과
[-3,1,3,5]
```

### heappop(배열이름)

- Heap 요소 삭제하기

```python
testheap = []
# 요소 추가
heapq.heappush(testheap, 3)
heapq.heappush(testheap, 5)
heapq.heappush(testheap, 1)
heapq.heappush(testheap, -3)
# 요소 꺼내기
heapq.heappop(testheap)
heapq.heappop(testheap)

print(testheap)

# 실행결과
[3,5]

```

덱에서 popleft()와 유사하게 큐의 가장 왼쪽부터 삭제된다.
