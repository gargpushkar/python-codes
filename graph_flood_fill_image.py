# Flood Fill Image
# Given an image as a matrix of colored cells. Each cell has a value ranging from 0 to 65535 denoting its color. You have to apply flood-fill to a particular cell of the matrix with color c.
# Two cells are considered as part of the same connected component if they have a common side and the same color value.
# When you apply flood-fill to a particular cell, all its connected components are also applied the same color.

# https://workat.tech/problem-solving/practice/flood-fill-image

from typing import List
class Solution:
	
	def is_valid(self, i, j, n, m, visited, image, color):
		if i < 0 or i >= n or j < 0 or j >= m or visited[i][j] or image[i][j] != color:
			return False
		return True
	
	def dfs(self, i, j, n, m, visited, image, c, color, dx, dy):
		visited[i][j] = 1
		image[i][j] = c
		for a, b in zip(dx, dy):
			if self.is_valid(i+a, j+b, n, m, visited, image, color):
				visited[i+a][j+b] = 1
				image[i+a][j+b] = c
				self.dfs(i+a, j+b, n, m, visited, image, c, color, dx, dy)
				
	
	def applyFloodFill(self, image: List[List[int]], x: int, y: int, c: int) -> List[List[int]]:
		# add your logic here
		dx = [1, -1, 0, 0]
		dy = [0, 0, 1, -1]
		n = len(image)
		m = len(image[0])
		visited = []
		for _ in range(n):
			visited.append([0]*m)
		color = image[x][y]
		self.dfs(x, y, n, m, visited, image, c, color, dx, dy)
		return image
		


