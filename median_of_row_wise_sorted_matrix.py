# Median of Row-wise Sorted Matrix
# Given an n*m matrix which is sorted row-wise, you need to find the median of the matrix.

# Median of a group of numbers is the middle element after they are sorted. Both n and m are guaranteed to be odd numbers, therefore there’s only one middle number.

# Example
# 1 2 3
# 3 3 4
# 1 1 2
# Median: 2

import heapq
from typing import List

class Solution:
	def calculateMedianOfMatrix(self, matrix: List[List[int]]) -> int:
		# add your logic here
		nr = len(matrix)
		nc = len(matrix[0])
		minHeap = []
		count = 0
		median = -1
		median_indx = nr*nc//2
		for i in range(nr):
			heapq.heappush(minHeap, [matrix[i][0], i, 0])

		while count <= median_indx:
			elem = heapq.heappop(minHeap)
			median = elem[0]
			row = elem[1]
			col = elem[2]
			count += 1
			
			col+=1
			if col < nc:
				heapq.heappush(minHeap, [matrix[row][col], row, col])
		return median
