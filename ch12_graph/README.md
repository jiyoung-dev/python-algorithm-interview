# 그래프 순회

- 그래프 순회란, 그래프 탐색(Search) 라고도 불리며, 그래프의 각 정점을 방문하는 과정을 말한다.
- 그래프 순회에는 크게 깊이우선탐색(DFS), 너비우선탐색(BFS)의 2가지 알고리즘이 있다.

## 그래프 표현하기

- 그래프를 나타내는 방법에는 인접행렬과 인접리스트의 2가지 방식이 있다. <br><br>
  <img src="https://user-images.githubusercontent.com/61649201/120933829-ec352780-c736-11eb-959a-4d5db3694dd5.png" width="25%"> <br>

다음은 위의 그래프를 인접리스트로 나타낸 것이다.

- Python 딕셔너리 자료형 사용
- 출발 노드를 key로, 도착 노드를 value로 표현한다
- 도착 노드는 여러개가 될 수 있으므로 리스트 형태가 된다

```python
graph = {
  1: [2, 3, 4],
  2: [5],
  3: [5],
  4: [],
  5: [6, 7],
  6: [],
  7: [3],
}
```

## DFS

- 주로 스택으로 구현하거나, 재귀로 구현한다.
- 코딩테스트 시에 대부분의 그래프 탐색은 DFS로 구현하게 될것이다.

1. stack 사용해서 구현하기

```python
def dfs_iteration(graph, root):
    # visited = 방문한 꼭지점들을 기록한 리스트
    visited = []
    # dfs는 stack, bfs는 queue개념을 이용한다.
    stack = [root]

    while(stack): #스택에 남은것이 없을 때까지 반복
        node = stack.pop()    # node : 현재 방문하고 있는 꼭지점

        #현재 node가 방문한 적 없다 -> visited에 추가한다.
        #그리고 해당 node의 자식 node들을 stack에 추가한다.
        if(node not in visited):
            visited.append(node)
            stack.extend(graph[node])
    return visited

print(dfs_iteration(graph, 1))    # [1, 4, 3, 5, 7, 6, 2]
```

2. 재귀함수로 구현하기

```python
def dfs_recursive(graph, start, visited=[]):

    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)

    return visited

print(dfs_recursive(graph, 1))    # [1, 2, 5, 6, 7, 3, 4]
```

## BFS

- 주로 큐로 구현한다.
- 그래프의 최단경로를 구하는 문제에 사용된다.

```python
from collections import deque

def bfs_iteration(graph, root):
    visited = []    # visited = 방문한 노드들을 기록한 리스트
    queue = deque([root])    # bfs는 queue개념을 이용한다.

    while(queue): ## queue에 남은 것이 없을 때까지 반복
        node = queue.pop()    # node : 현재 방문하고 있는 노드

        # 현재 node를 방문한 적 없다. -> visited에 추가
        # visited에 추가 후, 해당 노드의 자식 노드들을 queue에 추가
        if node not in visited:
            visited.append(node)
            queue.extendleft(graph[node])
    return visited

print(bfs_iteration(graph, 1))    # [1, 2, 3, 4, 5, 6, 7]
```

## 백트래킹

> 백트래킹이란, 해결책에 대한 후보를 구축하다가 가능성이 없다고 판단되는 즉시 후보를 포기 (백트랙, Backtrack)해 정답을 찾아가는 알고리즘.

즉, 백트래킹은 탐색하다가 더 갈수 없으면 왔던길을 되돌아 다른길을 찾는 방법이다. 브루트포스 알고리즘과 유사하지만, 백트래킹은 한번 방문 후 가능성이 없는 경우 즉시 포기한다는 점에서 매번 같은 경로를 방문하는 브루트포스보다 간결한 방식이다.

```python
def dfs_backtracking(graph,visited,V):

  for v in graph[V]:

    if not visited[v]:

      visited[V] = True
      dfs_backtracking(graph,visited,v)

      # dfs로 들어갔다가 다시 나왔을 때, False를 통해 백트래킹 해준다.
      visited[V] = False
```
