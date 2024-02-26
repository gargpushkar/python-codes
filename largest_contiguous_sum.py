# You are given an array of numbers (could be -ve as well). You need to find the largest contiguous sum from the array.
# Example
# Array: [4 -6 2 5]
# Answer: 7

from typing import List

class Solution:
    def largestContiguousSum(self, arr: List[int]) -> int:
        max_sum = []
        total = 0
        for i in arr:
            total += i
            max_sum.append(total)
            if total <= 0:
                total = 0
        return max(max_sum)
    

		
solution = Solution()
arr = [-1, -2, -3, -4, -5]
print(solution.largestContiguousSum(arr))

