# Search in Rotated Sorted Array
# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1

from typing import List

# nums = [4,5,6,7,0,1,2]
# target = 3
# nums = [1]
# target = 1
nums = [1,0,1,1,1]
target = 0

class Solution:
    def get_pivot(self, nums, n):
        l = 0
        r = n-1
        while l<r:
            mid = (l+r)//2
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid
        return l

    def binary_search(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if nums[0] <= nums[-1]:
            return self.binary_search(nums, target)
        pivot = self.get_pivot(nums, n)
        print(pivot)
        if target >= nums[0]:
            return self.binary_search(nums[0:pivot], target)
        else:
            ans = self.binary_search(nums[pivot:], target)
            return pivot + ans if ans != -1 else -1

sol = Solution()
print(sol.search(nums, target))
