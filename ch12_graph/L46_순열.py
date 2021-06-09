'''
서로다른 정수를 입력받아 가능한 모든 순열을 리턴하시오. 

[input]
[1, 2, 3]

[output]
[
  [1, 2, 3], 
  [1, 3, 2], 
  [2, 1, 3],
  [2, 3, 1],
  [3, 1, 2],
  [3, 2, 1]
]
'''
# DFS로 구현
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 이전 엘리먼트를 하나씩 덧붙이면서 계속 재귀호출을 진행하다가 마지막 노드에 도달할 경우, 결과를 담아서 출력해준다.
        results = []
        prev_elements = []  # 이전값을 저장할 리스트

        def dfs(elements):
            if len(elements) == 0:
                # [:]를 쓰지않으면, prev_elements에 대한 참조가 추가되는 것.
                results.append(prev_elements[:])

            # 순열 생성 재귀호출
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return results


print(Solution().permute([1, 2, 3]))
