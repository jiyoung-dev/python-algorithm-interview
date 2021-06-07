# https://leetcode.com/problems/number-of-islands/
from typing import *
'''
1을 육지로, 0을 물로 가정한 2D 그리드맵이 주어질때, 섬의 개수를 계산하라. (연결되어 있는 1의 덩어리개수) 

[input]
11110
11010
11000
00000

[output]
3
'''
class Solution:
	def dfs(self, grid: List[List[str]], i: int, j: int):
		# 더이상 땅이 아닌경우 종료(return)한다. 
		if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
			return 
		grid[i][j] = '0'
		# 동서남북 탐색
		self.dfs(grid, i+1, j)
		self.dfs(grid, i-1, j)
		self.dfs(grid, i, j+1)
		self.dfs(grid, i, j-1)
		
	def numIslands(self, grid: List[List[str]]) -> int:
		# 예외처리 
		if not grid:
			return 0
			
		count = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == '1':
					self.dfs(grid, i, j)
					# 모든 육지 탐색 후 카운트 1 증가
					count += 1
		return count 

s = Solution()

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(s.numIslands(grid))
