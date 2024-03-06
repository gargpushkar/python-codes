# https://workat.tech/problem-solving/practice/k-diff-pairs
# Given a sorted array A of size n and a number k, return the number of unique pairs which have a difference of k.

# |arr[i] - arr[j]| = k where i < j

# Example
# A: [1, 3, 5, 7, 10]
# k: 2
# Answer: 3
# A: [1, 3, 5, 7, 10]
# k: 3
# Answer: 1
# A: [1, 3, 5, 7, 10]
# k: 1
# Answer: 0

# NOTE: Take care of duplicates as unique pairs are asked

from typing import List

class Solution:
	def kDiffPairs(self, A: List[int], k: int) -> int:
		# add your logic here
		n = len(A)
		i = 0
		j = 1
		count = 0
		
		while j<n:
			while j < n-1 and (A[j] == A[j+1]):
				j+=1
			if A[j] - A[i] == k:
				i+=1
				j+=1
				count+=1
			elif A[j] - A[i] > k:
				i+=1
			else:
				j+=1
			if i == j:
				j+=1
		return count


