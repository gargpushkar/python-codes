# https://leetcode.com/problems/house-robber-ii/description/

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Example 1:
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 3:
# Input: nums = [1,2,3]
# Output: 3

nums = [94,40,49,65,21,21,106,80,92,81,679,4,61,6,237,12,72,74,29,95,265,35,47,1,61,397,52,72,37,51,1,81,45,435,7,36,57,86,81,72]

n = len(nums)
t = [[-1 for _ in range(n+1)] for __ in range(n+1)]

def solve(indx, parent):
    if indx == n-1 and parent == 0:
        return 0
    
    if indx >= n:
        return 0
    if t[indx][parent] != -1:
        return t[indx][parent]
    skip_house = solve(indx+1, parent)
    rob_house = nums[indx]
    if parent == -1:
        rob_house += solve(indx+2, indx)
    else:
        rob_house += solve(indx+2, parent)
    t[indx][parent] = max(skip_house, rob_house)
    return t[indx][parent]

print(solve(0, -1))
