# https://leetcode.com/problems/reorder-data-in-log-files/
'''
로그를 재정렬하시오.
1. 로그의 가장 앞부분은 식별자다.
2. 문자로 구성된 로그가 숫자 로그보다 앞에온다.
3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일한 경우 식별자 순으로한다.
4. 숫자 로그는 입력 순서대로 한다.

Input:
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

Output:
["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
'''
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # 문자와 숫자를 구분해서 리스트에 저장
        letters, digits = [], []
        for log in logs:
            # isdigit() -> 숫자인지 판별
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits

# logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# sol = Solution()

# print(sol.reorderLogFiles(logs))
