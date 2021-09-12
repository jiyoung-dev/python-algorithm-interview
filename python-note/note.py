# 1. 간결한 배열 입력
"""
3
1 2 3
4 5 6
7 8 9
"""

# bad code
n = int(input())
MAP = []
for i in range(n):
    inputStr = input().split(' ')
    arr = list(inputStr)
    MAP.append(arr)
print(MAP)  # [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

# # good code
MAP = [list(map(int, input().split())) for _ in range(int(input()))]
print(MAP)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 2. 정수와 배열이 같은줄에 들어오는 경우
"""
4 10 20 30 40
3 7 5 12
3 125 15 25
"""

n, *arr = map(int, input().split())
print(arr)  # [10, 20, 30, 40]

# 3. 문자열을 한글자씩 배열에 저장
"""
3
AAAA 
ABCA 
AAAA
"""
n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
print(arr)  # [['A', 'A', 'A', 'A'], ['A', 'B', 'C', 'A'], ['A', 'A', 'A', 'A']]

# 4. 배열을 연결해서 출력
arr = [1, 2, 3, 4]
print("".join(map(str, arr)))  # 1234
print(*arr)  # 1 2 3 4

# 5. 끝을 알수없는 입력이 들어오는 경우
try:
    while 1:
        a, b = map(int, input().split())
        print(a+b)
except:
    exit()

# 6. 배열 순회하면서 최솟값 구하기
import sys
ans = sys.maxsize
arr = [10, 20, 30]
for num in arr:
    if ans > num:
        ans = num
print(ans)  # 10

# 7. 문자열 거꾸로
alph = "abcd"
print(alph[::-1])  # dcba

# 8. 배열 초기화
"""
가로 3, 세로 5인 크기의 배열을 0으로 초기화 
"""
n, m = map(int, input().split())
arr = [[0] * n for _ in range(m)]
print(arr)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

# 9. 배열 원소의 갯수
arr = [1, 1, 2, 3, 4, 1]
print(arr.count(1))  # 3

# 10. 원소 중복 제거 (중복없이 저장)
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'c', 'd' ]
alpha = list(set(alpha))
print(alpha)  # ['a', 'f', 'b', 'c', 'd', 'g', 'e']

lst = [[1,2], [1,2], [1]]
print(list(set(map(tuple, lst))))  # [(1, 2), (1,)]

# 11. 오름차순 정렬
arr.sort()

# 12. 내림차순 정렬
arr.sort(reverse=True)

# 13. 배열의 원소가 리스트인 경우 정렬
# x[0] (x좌표)을 정렬하고, x[0] 값이 같다면 x[1] (y좌표)을 기준으로 오름차순 정렬
arr.sort(key=lambda x:(x[0], x[1]))

# 14. 삼항연산자
a = 10
b = 20
res = a if a > b else b
print(res)  # 20

# 15. 순열과 조합
import itertools
# param1: 배열, param2: 길이
print(list(itertools.permutations([1, 2, 3], 3)))  # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
print(list(itertools.combinations([1, 2, 3, 4], 3)))  # [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]

# 16. Counter (빈도 계산)
from collections import Counter
arr = [1, 1, 1, 2, 3, 4]
print(Counter(arr))  # Counter({1: 3, 2: 1, 3: 1, 4: 1})

# 17. heap
# 파이썬에서 힙의 default는 최소힙으로, 값을 저장하면 최솟값이 이진트리의 루트에 위치함 (인덱스 0)
import heapq
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 8)
print(heap)  # [1, 3, 10, 5, 8]
print(heapq.heappop(heap))  # 1 (왼쪽부터 pop)
"""
     1 <--- Root 
   /   \ 
  3     5 
 / \   / 
4   8 7
"""

# 18. deque
from _collections import deque
deq = deque([1, 2, 3, 4])
"""
               -----------
appendleft() ->   deque    <- append()
popleft()    <-            -> pop()
               ----------- 
"""
# 비어있는 덱을 pop 하는 경우, error
deq.rotate(-1)  # 음수이면 왼쪽으로 회전
deq.rotate(1)  # 양수이면 오른쪽으로 회전

# 19. 우선순위 큐
from queue import PriorityQueue

que = PriorityQueue()
que.put(4)
que.put(10)
que.put(2)

for i in range(len(que.queue)):
    print(que.queue[i], end=" ")  # 2 10 4
print(que.get())  # 2
