from typing import List

class Solution:
	def getPivotIndex(self, arr: List[int], key) -> int:
		# add your logic here
		l, h = 0, len(arr) - 1
		pivot_index = -1
		while(l<=h):
			mid = (l + h) // 2
			if arr[mid] > arr[mid + 1]:
				pivot_index = mid
				break
			if arr[mid] > arr[l]:
				l = mid + 1
			else:
				h = mid - 1 
		arr_1 = arr[0:pivot_index + 1]
		arr_2 = arr[pivot_index + 1:]
		l, h = 0, len(arr_1) - 1
		while(l<=h):
			mid = (l+h)//2
			if arr_1[mid] == key:
				return mid
			elif arr_1[mid] < key:
				l = mid + 1
			else:
				h = mid - 1
		

		l, h = 0, len(arr_2) - 1

		while(l<=h):
			mid = (l+h)//2
			if arr_2[mid] == key:
				return len(arr_1) + mid
			elif arr_2[mid] < key:
				l = mid + 1
			else:
				h = mid - 1
		return -1

sol = Solution()
A = [4, 5, 7, 8, 1, 2, 3]
# key = 4
# A = [8, 1, 2, 3, 4, 7]
# A = [1, 2, 3, 4, 7]
key = 2
print(sol.getPivotIndex(A, key))