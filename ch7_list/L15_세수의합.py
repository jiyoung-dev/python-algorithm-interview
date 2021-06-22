'''
배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.

nums = [-1, 0, 1, 2, -1, -4]

[
  [-1, 0, 1].
  [-1, -1, 2]
]
'''

# 투포인터로 풀이
from typing import List

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()  # 입력된 배열을 정렬 (투포인터 문제풀이를 위한)

        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # 두개의 포인터 (left, right)를 두고 간격을 좁혀가면서 sum 구하기
            left, right = i + 1, len(nums) - 1

            # 인덱스 0번째를 기준 i로 두고, i+1 번째를 left, 마지막 숫자를 right로 둔다
            # for문을 돌면서 세 수의 합이 0보다 작다면 left를 한칸 우측으로 이동
            # 세 수의 합이 0보다 크다면 right를 한칸 좌측으로 이동시킨다
            # 세 수의 합이 0과 같아지면 결과 리스트에 추가한다
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:  # sum = 0인 경우다
                    results.append([nums[i], nums[left], nums[right]])

                    # left, right 양 옆의 동일한 값 처리
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return results

# nums = [-1, 0, 1, 2, -1, -4]
# sol = Solution()
# print(sol.threeSum(nums))

# [[-1, -1, 2], [-1, 0, 1]]


