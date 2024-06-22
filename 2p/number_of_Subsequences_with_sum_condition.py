# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/
# 1498. Number of Subsequences That Satisfy the Given Sum Condition

from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        right = n-1
        ans = 0
        MOD = 10**9+7
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                ans += pow(2, right-left, MOD)
                left += 1
        return ans%MOD