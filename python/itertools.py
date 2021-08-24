import itertools

# 1. product
# 곱집합 함수다 'ab'와 '12'의 곱집합은 a1, a2, b1, b2 이다.
arr1 = ['012', 'abc']
result1 = list(itertools.product(*arr1))  # list() 필수
print(result1)
# [('0', 'a'), ('0', 'b'), ('0', 'c'), ('1', 'a'), ('1', 'b'), ('1', 'c'), ('2', 'a'), ('2', 'b'), ('2', 'c')]