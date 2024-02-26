# https://workat.tech/problem-solving/practice/search-rotated-array
# You are given a list of unique integers which are sorted but rotated at some pivot. You are also given a target value and you have to find its index in the list. If it is not present in the list, return -1.

# Example:
# List: [4, 5, 6, 7, 8, 1, 2, 3]
# Target value: 6
# Resultant index: 2

from typing import List

class Solution:
	def getElementIndex(self, array: List[int], target: int) -> int:
		# add your logic here
		l, h = 0, len(array) - 1
		while(l<=h):
			mid = (l+h)//2
			if array[mid] == target:
				return mid
			if array[l] < array[mid]:
				if target >= array[l] and target <= array[mid]:
					h = mid - 1
				else:
					l = mid + 1
			else:
				if target >= array[mid] and target <= array[h]:
					l = mid + 1
				else:
					h = mid -1
		return -1


sol = Solution()
# A = [4, 5, 7, 8, 1, 2, 3]
A = [8, 1, 2, 3, 4, 7]
key = 8
print(sol.getElementIndex(A, key))