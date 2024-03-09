# Four Sum

# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# Example 2:
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]

from typing import List

nums = [1,0,-1,0,-2,2]
target = 0
nums = [2,2,2,2,2]
target = 8

def fourSum(self, A: List[int], target: int) -> List[List[int]]:
    A.sort()
    n = len(A)
    ans = []
    for i in range(n-3):
        if i > 0 and A[i] == A[i-1]:
            continue
        for j in range(i+1, n-2):
            if j > i+1 and A[j] == A[j-1]:
                continue
            l = j+1
            r = n-1
            while l < r:
                curr_sum = A[i] + A[j] + A[l] + A[r]
                if curr_sum == target:
                    ans.append([A[i], A[j], A[l], A[r]])
                    l+=1
                    r-=1
                elif curr_sum > target:
                    r-=1
                else:
                    l+=1
    return ans

print(fourSum("self", nums, target))
