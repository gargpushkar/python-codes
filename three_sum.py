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
# class Solution:
# 	def threeSum(self, A: List[int]) -> List[List[int]]:
# 		# add your logic here
# 		hash_map = {}
# 		A.sort()
# 		n = len(A)
# 		for i in range(n):
# 			hash_map[A[i]] = i
		
# 		i = 0
# 		j = n - 1
# 		ans = []
# 		while(i<j):
# 			num = A[i] + A[j]
# 			if -num in hash_map and hash_map[-num] != i and hash_map[-num] != j:
# 				ans.append(sorted([A[i], A[j], -num]))
# 				i+=1
# 				j-=1
# 			elif num > 0:
# 				j-=1
# 			else:
# 				i+=1
# 		return ans
	
# sol = Solution()
# A = [-1, 0, 1, 2]
# A = [-1,0,1,2,-1,-4]
A = [-2,0,1,1,2]
# A = [0, 0, 0]
# print(sol.threeSum(A))


# A = [1, 1, 0, -1, -2]

def threeSum(A: List[int]) -> List[List[int]]:
	A.sort()
	n = len(A)
	s = set()
	for i in range(n-2):
		l = i+1
		r = n-1
		while l < r:
			if A[i] + A[l] + A[r] == 0:
				s.add((A[i], A[l], A[r]))
				l+=1
				# r-=1
			if A[i] + A[l] + A[r] > 0:
				r-=1
			else:
				l+=1
	return s

print(threeSum(A))