# Given a sorted array and a number key, find the smallest array element which is greater than the key.

# If the key is greater than or equal to the largest element then return the key itself.

# Expected Time Complexity: O(log n)
from typing import List

class Solution:
    def getNextGreaterElement(self, arr: List[int], key: int) -> int:
        l, h = 0, len(arr) - 1
        if arr[h] <= key:
            return key
        if arr[l] > key:
            return arr[l]
        ans = None
        while(l<=h):
            mid = (l + h) // 2
            if arr[mid] < key:
                l = mid + 1
            elif arr[mid] > key:
                h = mid - 1
            else:
                l = mid + 1
        return arr[l]
            
s = Solution()
A = [1, 2, 3, 3, 3, 4, 4, 7, 8, 9]
target = 11
print(s.getNextGreaterElement(A, target))

