# Find the Duplicate Number
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.

# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2

# Example 2:
# Input: nums = [3,1,3,4,2]
# Output: 3

# Example 3:
# Input: nums = [3,3,3,3,3]
# Output: 3
 
# Constraints:
# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.

nums = [3,1,3,4,2]

# Approach Negative Marking

for i in nums: 
    if nums[abs(i)] < 0:
        print(abs(i))
        break
    nums[abs(i)] *= -1

# Floyd Warshell Cycle Detection Algo
nums = [3, 1, 3, 4, 2]

def findDuplicate():
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    finder = nums[0]

    while True:
        if slow == finder:
            return slow
        slow = nums[slow]
        finder = nums[finder]

