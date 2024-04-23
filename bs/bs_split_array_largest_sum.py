# Split Array Largest Sum

# Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

# Return the minimized largest sum of the split.

# A subarray is a contiguous part of the array.

 

# Example 1:

# Input: nums = [7,2,5,10,8], k = 2
# Output: 18
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.
# Example 2:

# Input: nums = [1,2,3,4,5], k = 2
# Output: 9
# Explanation: There are four ways to split nums into two subarrays.
# The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.
from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def is_valid(mid):
            total = 0
            no_of_subarray = 1
            for i in nums:
                total += i
                if total > mid:
                    total = i
                    no_of_subarray += 1
                
                if no_of_subarray > k:
                    return False
            return True
        
        left = max(nums)
        right = sum(nums)
        ans = -1
        while left <= right:
            mid = left + (right-left)//2
            if is_valid(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
    
nums = [1,4,4]
k = 3

sol = Solution()
print(sol.splitArray(nums, k))
