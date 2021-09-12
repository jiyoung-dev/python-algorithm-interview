"""
zip(*iterable): 동일한 개수로 이루어진 자료형을 묶어주는 역할을 하는 함수
"""

arr1 = list(zip([1, 2, 3], [4, 5, 6]))
print(arr1)  # [(1, 4), (2, 5), (3, 6)]

arr2 = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(list(map(list, zip(*arr2))))  # [['C', 'A', 'A', 'C'], ['C', 'A', 'A', 'C'], ['B', 'A', 'A', 'B'], ['D', 'D', 'B', 'B'], ['E', 'E', 'F', 'F']]
