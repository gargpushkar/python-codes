# https://workat.tech/problem-solving/practice/non-repeating-element
# Given a sorted list of numbers in which all elements appear twice except one element that appears only once, find the number that appears only once.

from typing import List
class Solution:
    def findNonRepeatingElement(self, arr: List[int]) -> int:
        l, h = 0, len(arr) - 1
        while(l<=h):
            mid = (l+h)//2
            if mid == len(arr) - 1:
                return arr[mid]
            if arr[mid] != arr[mid + 1] and arr[mid] != arr[mid - 1]:
                return arr[mid]
            if mid % 2 == 1:
                if arr[mid] == arr[mid - 1]:
                    l = mid + 1
                else:
                    h = mid - 1
            else:
                if arr[mid] == arr[mid + 1]:
                    l = mid + 1
                else:
                    h = mid - 1

sol = Solution()
arr = [0, 0, 1, 1, 3, 3, 4, 4, 5, 5, 6]
print(sol.findNonRepeatingElement(arr))