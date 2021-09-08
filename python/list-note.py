# 1차원 리스트를 원소마다 쪼개서 2차원으로 변환
board = ["CCBDE","AAADE", "AAABF", "CCBBF"]
for i in range(len(board)):
    popped = board.pop(0)
    board.append([p for p in popped])
print(board)
"""
[['C', 'C', 'B', 'D', 'E'],
 ['A', 'A', 'A', 'D', 'E'],
 ['A', 'A', 'A', 'B', 'F'],
 ['C', 'C', 'B', 'B', 'F']]
"""


# 문자열을 공백을 기준으로 분리 - list() 함수 이용
words = "apple banana kiwi"
print(list(words))
# ['a', 'p', 'p', 'l', 'e', ' ', 'b', 'a', 'n', 'a', 'n', 'a', ' ', 'k', 'i', 'w', 'i']


# 문자열을 공백을 기준으로 분리 - split() 함수 이용
print(words.split())
# ['apple', 'banana', 'kiwi']


# split(maxsplit=n) - maxsplit: 최대 몇번 쪼갤지 지정하는 파라미터
print(words.split(maxsplit=1))  # 처음으로 나오는 공백만 쪼갠다는 의미
# ['apple', 'banana kiwi']


# split(sep='string') - sep: 특정 문자열로 쪼개는 파라미터
test = "banana:바나나"
print(test.split(sep=':'))
# ['banana', '바나나']


# 리스트를 문자열로 합치기 - join() 함수 이용
print((' ').join(words.split()))
# apple banana kiwi

s = ["My", "name", "is", "Jiyoung"]
print((' ').join(s))
# My name is Jiyoung

# 특정 문자열을 삽입하여 합치기
print((' and ').join(words.split()))
# apple and banana and kiwi

# 리스트 원소마다 공백기준으로 분리하기
lines = ["apple 10 fruits", "kiwi 5 fruits", "carrot 4 vegetable"]
result = []
for line in lines:
    result.append(line.split())
print(result)
# [['apple', '10', 'fruits'], ['kiwi', '5', 'fruits'], ['carrot', '4', 'vegetable']]

