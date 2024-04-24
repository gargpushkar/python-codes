# Unsolved

# https://leetcode.com/problems/combination-sum-iv/description/
# Combination Sum IV
# Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

# The test cases are generated so that the answer can fit in a 32-bit integer.
 
# Example 1:
# Input: nums = [1,2,3], target = 4
# Output: 7
# Explanation:
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# Note that different sequences are counted as different combinations.

# Example 2:
# Input: nums = [9], target = 3
# Output: 0

nums = [1, 2, 3]
target = 4
n = len(nums)
# def get_count(nums, n, target):
#     if target == 0:
#         return 1
#     if n == 0 or target < 0:
#         return 0

#     take = get_count(nums, n, target-nums[n-1])
#     notake = get_count(nums, n-1, target)
#     return notake + take
#     # if nums[n-1] > target:
#     #     return get_count(nums, n-1, target)
#     # else:
#     #     return get_count(nums, n, target-nums[n-1]) + get_count(nums, n-1, target)

# print(get_count(nums, len(nums), target))
from typing import List
class Solution:

    def solve_rec(self,nums,target):
        
        if target < 0:
            return 0

        if target==0:
            return 1
        ways = 0
        for i in nums:
            ways += self.solve_rec(nums,target-i)
        
        return ways 

    def solve_mem(self,nums,target,dp):
        
        if target < 0:
            return 0

        if target==0:
            return 1
        
        
        if target in dp:
            return dp[target]
        ways = 0
        for i in nums:
            ways += self.solve_mem(nums,target-i,dp)
        dp[target] = ways
        return dp[target]
        
    def combinationSum4(self, nums: List[int], target: int) -> int:

        return self.solve_mem(nums,target,{})
        
        


def get_count(nums, target):
    t = [1] + [0]*(target)

    for i in range(1, target+1):
        for num in nums:
            if i >= num:
                t[i] += t[i - num]
    return t[target]

print(get_count(nums, target))