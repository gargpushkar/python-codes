# Given a sorted array and a number key, return whether the key is present in the array or not.

# Expected Time Complexity: O(log n)
from typing import List

class Solution:
    def containsElement(self, arr: List[int], key: int) -> bool:
        l, h = 0, len(arr) - 1
        while(l<=h):
            mid = l + (h - l)//2
            if arr[mid] < key:
                l = mid + 1
            elif arr[mid] > key:
                h = mid - 1
            else:
                return True
        return False

            
            
s = Solution()
A = [1, 2, 5, 6, 7, 8, 9, 9, 9]
key = 4
print(s.containsElement(A, key))

