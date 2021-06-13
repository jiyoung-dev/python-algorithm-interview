'''
팰린드롬이란, 앞뒤가 똑같은 단어나 문장을 의미한다.   
'소주 만 명만 주소'를 뒤집어도 똑같은 문장이다. 
주어진 문자열이 팰린드롬인지 확인하시오. (대소문자 구분X, 영문자와 숫자만 가능하다.)
 
 [input]
 "A man, a plan, a cancal: Panama"

 [output]
 true
'''

# 슬라이싱 사용
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)    # 정규식으로 불피요한 문자 필터링

        return s == s[::-1]  # 슬라이싱


sol = Solution()

s = "A man, a plan, a canal: Panama"
print(sol.isPalindrome(s))
