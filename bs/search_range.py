# Given a sorted array and a number key, return whether the key is present in the array or not.

# Expected Time Complexity: O(log n)
from typing import List

class Solution:
    def searchRange(self, arr: List[int], key: int) -> List[int]:
        l, h = 0, len(arr) - 1
        ans_l = -1
        while(l<=h):
            mid = l + (h - l)//2
            if arr[mid] < key:
                l = mid + 1
            elif arr[mid] > key:
                h = mid - 1
            else:
                l = mid + 1
                ans_l = mid
        
        l, h = 0, len(arr) - 1
        ans_r = -1
        while(l<=h):
            mid = l + (h - l)//2
            if arr[mid] < key:
                l = mid + 1
            elif arr[mid] > key:
                h = mid - 1
            else:
                h = mid - 1
                ans_r = mid

        return [ans_r, ans_l]

            
            
s = Solution()
A = [1, 2, 3, 3, 3, 4, 4, 5]
key = 6
print(s.searchRange(A, key))

