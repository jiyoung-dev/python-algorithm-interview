'''
2에서 9까지 숫자가 주어졌을 때 각 숫자에 해당하는 문자는 다음과 같다.  
전화번호로 조합 가능한 모든 문자를 출력하라. 

dic = {
  "2": "abc",
  "3": "def",
  "4": "ghi",
  "5": "jkl",
  "6": "mno",
  "7": "pqrs",
  "8": "tuv",
  "9": "wxyz"
}

[input]
23

[output]
["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
'''  

# 두개의 그룹에서 문자를 뽑아 나타낼 수 있는 모든 경우의수를 구해야한다. 
# 전체를 탐색하고, 백트래킹하면서 결과를 조합할 수 있다. 

from typing import List

class Solution:

  def letterCombinations(self, digits: str) -> List[str]:
    def dfs(index, path):
      # 끝까지 탐색완료하면 백트래킹
      if len(path) == len(digits):
        result.append(path)
        return

      # 입력값 자릿수 단위 반복
      for i in range(index, len(digits)):
        # 숫자에 해당하는 모든 문자열 반복
        for j in dic[digits[i]]:
          dfs(i+1, path+j)
  
    # 예외처리
    if not digits:
      return []

    dic = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
    }

    result = []
    dfs(0, "")

    return result

Solution().letterCombinations("23")
