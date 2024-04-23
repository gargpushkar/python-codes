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

def get_count(nums, n, target):
    if target == 0:
        return 1
    if n == 0:
        return 0
    if nums[n-1] > target:
        return get_count(nums, n-1, target)
    else:
        return get_count(nums, n, target-nums[n-1]) + get_count(nums, n-1, target)

print(get_count(nums, len(nums), target))