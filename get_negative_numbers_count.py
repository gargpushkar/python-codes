# Given a sorted array of integers, find the number of negative numbers.

# Expected Time Complexity: O(log n)
from typing import List

class Solution:
    def getNegativeNumbersCount(self, arr: List[int]) -> int:
        key = 0
        l,h = 0, len(arr) - 1
        ans = 0
        while(l<=h):
            mid = (l+h)//2
            if arr[mid] > key:
                h = mid -1
            elif arr[mid] < key:
                l = mid + 1
                ans = l
            else:
                ans = l
                h = mid -1
        return ans
            
s = Solution()
A = [-1, -1, -1, -1, -2, -3, -4, -6, -7]
print(s.getNegativeNumbersCount(A))

