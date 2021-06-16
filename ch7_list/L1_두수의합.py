'''
덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하시오. 

Input
nums = [2, 7, 11, 15], target = 9

Output
[0, 1]
'''

from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):    # enumerate() -> 인덱스를 포함해 열거해주는 자료형
          # print(i, n)
          # 0 2
          # 1 7
          # 2 11
          # 3 15
            complement = target - n

            if complement in nums[i+1:]:
                return [nums.index(n), nums[i+1:].index(complement)+(i+1)]


# nums = [2, 7, 11, 15]
# target = 9

# sol = Solution()
# print(sol.twoSum(nums, target))
