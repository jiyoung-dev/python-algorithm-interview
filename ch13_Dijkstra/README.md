# 최단 경로 문제

- 최단 경로는 가장 짧은 경로를 찾는 문제이다.
- 그래프의 종류와 특성에 따라 각각 최적화된 다양한 최단 경로 알고리즘이 존재한다.
- 정점(Vertex), 간선(Edge), 가중치(Weight)가 포함된 그래프가 주어진다.
- 그중 가장 유명한것이 다익스트라 알고리즘.

## 다익스트라 알고리즘

- 항상 노드 주변의 최단 경로만을 택하는 대표적인 그리디 알고리즘 중 하나로, 단순하고 실행속도가 빠르다.
-
- 노드 주변 탐색시, BFS를 이용한다.

### 시간복잡도

정점의 개수가 V, 간선의 개수가 E일때 시간복잡도

- 선형탐색시, `O(V^2)`
- BFS와 우선순위 큐 적용시, `O((V+E)logV)`
- 모든 정점이 출발지에서 도달 가능한 경우, `O(ElogV)`

### 문제 구성

- 어떤 정점 하나를 시작으로 선택하고, 나머지 정점들로부터 최단거리를 모두 구한다. (시작점 = 0)
- 그래프는 대체로 유향인 경우가 많음.
- 간선다마 이동거리가 존재하는데, 거리가 음수가 아닐때만 사용 가능함.
- 최소비용을 구하라고 할 때 거리대신 비용(cost)이라는 용어로 대체되고 맥락은 똑같다.

### 다익스트라 동작 원리

1. 아직 방문하지 않은 정점들 중 거리가 가장 짧은 정점 하나를 방문한다.
2. 해당 정점에서 인접하고, 아직 방문하지 않은 정점의 거리를 갱신한다.

### Template
```python
"""
정점과 간선, 가중치가 주어지고 지정된 시작 노드부터 도착 노드까지 최단경로를 구하는 기본문제.
다익스트라 알고리즘, 우선순위 큐
"""
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())  # 노드수(V), 정점수(E)
k = int(input())  # 시작노드(k)
graph = [[]for i in range(V+1)]  # 연결된 노드 정보를 저장할 리스트
distance = [INF] * (V+1)  # 최단경로를 저장할 리스트, 무한대로 초기화

# 간선정보 입력
for _ in range(E):
    u, v, w = map(int, input().split())
    # u에서 v로 이동하는 가중치가 w라는 의미
    graph[u].append((v, w))

# 다익스트라 구현
def dijkstra(k):
    q = []
    # 시작노드로 가기위한 최단경로는 0으로 설정해서 큐에 넣는다
    heapq.heappush(q, (0, k))
    distance[k] = 0

    while q:
        # 가장 최단거리가 짧은 노드의 정보를 꺼낸다
        dist, now = heapq.heappop(q)  # 거리값(dist), 현재노드(now)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐, 다른노드로 가는 거리가 더 짧은경우, 해당 거리로 갱신
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                # 우선순위 큐에 해당정보 기록
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 실행
dijkstra(k)

# 주어진 시작점에서 다른 모든 정점으로의 최단경로를 출력
for i in range(1, V+1):
    # 경로가 존재하지 않는 경우, INF 출력
    if distance[i] == INF:
        print("INF")
    # 경로가 존재하면 해당 경로값 출력
    else:
        print(distance[i])
 ```


[참고자료 | 다익스트라 알고리즘](https://blog.naver.com/kks227/220796029558)
