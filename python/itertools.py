import itertools

# 1. product
# 곱집합 함수다 'ab'와 '12'의 곱집합은 a1, a2, b1, b2 이다.
arr1 = ['012', 'abc']
result1 = list(itertools.product(*arr1))  # list() 필수
print(result1)
# [('0', 'a'), ('0', 'b'), ('0', 'c'), ('1', 'a'), ('1', 'b'), ('1', 'c'), ('2', 'a'), ('2', 'b'), ('2', 'c')]

# 2. combinations
# 조합함수. itertools.combinations(iterable, r)는 iterable 중에서 r개를 선택하는 조합이다.
arr2 = "abc"
result2 = list(itertools.combinations(arr2, 2))  # 순서에 영향 안받음
print(result2)
# [('a', 'b'), ('a', 'c'), ('b', 'c')]

# 3. permutations
# 순열. 가능한 모든 경우를 반환하는데, 순서가 영향을 미친다.
arr3 = "abc"
result3 = list(itertools.permutations(arr3, 3))
print(result3)
# [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

# 4. combinations_with_replacement
# 중복조합을 의미한다.
arr4 = [1, 2, 3]
result4 = list(itertools.combinations_with_replacement(arr4, 2))
print(result4)
# [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
