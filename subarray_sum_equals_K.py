# Subarray Sum Equals K

# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

from typing import List


nums = [1,1,1]
k = 2

class Solution:
    # TLE 
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        for i in range(0, n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                if total == k:
                    count += 1
        return count
    
    # using hash_map/dict
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        hash_map = {}
        hash_map[0] = 1
        total = 0
        for i in range(0, n):
            total += nums[i]
            count += hash_map.get(total-k, 0)
            hash_map[total] = hash_map.get(total, 0) + 1
            
        return count
    
sol = Solution()
print(sol.subarraySum(nums, k))
