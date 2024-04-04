# A peak element is an element that is strictly greater than its neighbors.
# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
# You must write an algorithm that runs in O(log n) time.


# Example 1:
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

# Example 2:
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right-left)//2
            if mid > 0 and mid < n-1:
                if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                    return mid
                elif nums[mid-1] > nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if mid == 0:
                    if nums[mid] > nums[mid+1]:
                        return mid
                    else:
                        return mid+1
                else:
                    if nums[mid] > nums[mid-1]:
                        return mid
                    else:
                        return mid-1


nums = [1, 15, 25, 45, 42, 21, 17, 12, 11]
sol = Solution()
print(nums[sol.findPeakElement(nums)])