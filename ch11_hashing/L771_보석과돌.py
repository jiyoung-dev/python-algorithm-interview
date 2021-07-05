'''
https://leetcode.com/problems/jewels-and-stones/

J는 보석, S는 갖고있는 돌이다. S에는 보석이 몇개나 있을까? 대소문자는 구분한다. 

Input: J = "aA", S = "aAAbbbb"
Output: 3
'''

# 가지고 있는 S의 개수를 각각 구한뒤 (빈도수), J의 각 요소를 키로 두고 S에 있는 값들의 개수 합을 구한다.

# -------------------- 해시 테이블 사용 --------------------
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # 해시테이블 선언
        freqs = {}
        count = 0

        # 돌(S)의 빈도수 계산
        for char in S:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1

        # 보석(J) 빈도수 계산
        for char in J:
            # 보석의 문자들이 freqs안에 존재하는 경우 각 value들을 모두 더해줌
            if char in freqs:
                count += freqs[char]

        # print(freqs)
        return count

J = "aA"
S = "aAAbbbb"
print(Solution().numJewelsInStones(J, S))

# -------------------- Counter() 사용 --------------------
import collections

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freqs = collections.Counter(S)
        count = 0

        # 보석(J)의 빈도수 바로 합산하기
        for char in J:
            count += freqs[char]

        return count

# -------------------- 파이썬다운 방식 --------------------
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(s in J for s in S)
