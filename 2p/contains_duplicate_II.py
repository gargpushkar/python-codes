# Contains Duplicate II

# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        j = 0
        n = len(nums)
        hash_map = {}
        while j < n:
            if j-i+1 <= k+1:
                if nums[j] in hash_map and hash_map[nums[j]]:
                    return True
                hash_map[nums[j]] = 1
                j+=1
            else:
                hash_map[nums[i]] -= 1
                if not hash_map[nums[i]]:
                    hash_map.pop(nums[i])
                i+=1
        return False
    
sol = Solution()
nums = [1,2,3,1,2,3]
k = 2
print(sol.containsNearbyDuplicate(nums, k))
