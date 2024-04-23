# https://leetcode.com/problems/minimum-size-subarray-sum/description/
# Minimum Size Subarray Sum
# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0



from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = 0
        total = 0
        ans = 100001
        while(j<n):
            total+= nums[j]
            if total < target:
                j+=1
            else:
                while(total >= target):
                    ans = min(ans, j-i+1)
                    total -= nums[i]
                    i+=1
                j+=1
        return 0 if ans == 100001 else ans

sol = Solution()

nums = [2, 3, 1, 2, 4, 3]
target = 7
print(sol.minSubArrayLen(target, nums))
