# https://workat.tech/problem-solving/practice/sliding-window-maximum
# You are given an array of integers A and a number k which represents the size of the window. The window covers k elements and starts at the left-end of the array. The window moves one index to the right at every step.

# You need to return an array with the max element inside the window at every step.

# Example:
# A: [1, -2, 3, 4, 5, 3, 4, -1]
# k: 3
# Result: [3, 4, 5, 5, 5, 4]

from typing import List
from collections import deque

class Solution:
	def maxSlidingWindow(self, A: List[int], k: int) -> List[int]:
		# add your logic here
		max_list = []
		dq = deque()
		i = 0
		j = 0
		n = len(A)
		while(j<n):
			elem = A[j]
			while(len(dq) and dq[-1] < elem):
				dq.pop()
			dq.append(elem)
			if j-i+1 < k:
				j+=1
			elif j-i+1 ==k:
				max_list.append(dq[0])
				if dq[0] == A[i]:
					dq.popleft()
				i+=1
				j+=1
		return max_list


sol = Solution()
A = [1, -2, 3, 4, 5, 3, 4, -1]
k = 3
print(sol.maxSlidingWindow(A, k))