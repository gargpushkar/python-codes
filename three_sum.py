# Three Sum
# Given an array A, find all unique triplets in the array whose sum is equal to zero.

# Example:
# A: [1, 1, 0, -1, -2]
# Triplets: [
#   [-2, 1, 1],
#   [-1, 0, 1]
# ]
# Note: Each triplet should be sorted. The resultant array should be sorted as well.

from typing import List
class Solution:
	def threeSum(self, A: List[int]) -> List[List[int]]:
		# add your logic here
		hash_map = {}
		for i in A:
			if i not in hash_map:
				hash_map[i] = 0
			hash_map[i] += 1
		
		i=0
		j = len(A) - 1
		ans = []
		A.sort()
		print(A)
		print(hash_map)
		while(i<j):
			num = A[i] + A[j]
			if -num in hash_map:
				ans.append(sorted([A[i], A[j], -num]))
				i+=1
			elif num > 0:
				j-=1
			else:
				i+=1
		n = len(ans)
		ans.insert(0, n)
		return ans
	
sol = Solution()
n = 4
A = [-1, 0, 1, 2]
print(sol.threeSum(A))