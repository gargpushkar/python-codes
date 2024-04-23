# # Counting Sort


# arr = [5, 4, 2, 5, 3, 1]
# # arr = [3, 11, 4, 200]

# n = len(arr)
# k = max(arr)
# count_arr = [0]*(k+1)
# for i in arr:
#     count_arr[i] += 1


# for i in range(1, k+1):
#     count_arr[i] = count_arr[i] + count_arr[i-1]


# ans_arr = [-1]*n
# for i in range(n-1, -1, -1):
#     count_arr[arr[i]] -= 1
#     ans_arr[count_arr[arr[i]]] = arr[i]

# print(ans_arr)

from typing import List

class Solution:
	def countingSort(self, arr: List[int]) -> None:
		# add your logic here
		n = len(arr)
		min_element = 0
		if min(arr) < 0:
			min_element = min(arr)
			for i in range(n):
				arr[i] += -min_element
		k = max(arr)
		count_arr = [0]*(k+1)
		for i in arr:
			count_arr[i] += 1
		
		for i in range(1, k+1):
			count_arr[i] = count_arr[i] + count_arr[i-1]
		
		ans_arr = [-1]*n
		
		for i in range(n-1, -1, -1):
			count_arr[arr[i]] -= 1
			ans_arr[count_arr[arr[i]]] = arr[i]		
		print(min_element)
		for i in range(n):
			arr[i] = ans_arr[i] + min_element
		return arr

sol = Solution()
print(sol.countingSort([-3, 11, 4, 200]))