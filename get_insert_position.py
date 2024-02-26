# https://workat.tech/problem-solving/practice/insert-position-in-sorted-array
# Given a sorted array containing distinct integers and a number 'key', find the index of the key in the array.
# If the key is not present, return the index at which it would be inserted considering that we need to maintain the sort order.

# Expected Time Complexity: O(log n)

from typing import List

class Solution:
	def getInsertPosition(self, arr: List[int], key: int) -> int:
		# add your logic here
		l, h = 0, len(arr) - 1
		while(l<=h):
			mid = (l+h)//2
			if arr[mid] < key:
				l = mid + 1
			elif arr[mid] > key:
				h = mid - 1
			else:
				h = mid - 1
		return l
	
A = [1, 2, 3, 4, 5]
key = 6

sol = Solution()
print(sol.getInsertPosition(A, key))