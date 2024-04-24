# Jump Game -- LEETCODE 55
# https://www.youtube.com/watch?v=Yan0cv2cLy8
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        self.nums = nums
        self.memo = {}
        return self.dfs(0)

    def dfs(self, index: int) -> bool:
        if index in self.memo:
            return self.memo[index]
        if index == len(self.nums) - 1:
            return True  # we reached the end of the array successfully
        if index > len(self.nums) - 1:
            return False  # out of bounds indexing 
        if self.nums[index] == 0:
            return False  # this path is unreachable, so we should backtrack
        value = self.nums[index]
        while value > 0:
            if self.dfs(index + value):
                self.memo[index] = True
                return True
            value -= 1
        self.memo[index] = False
        return False


# class Solution:
def canJump(self, nums: List[int]) -> bool:
    n = len(nums)
    goal = n - 1
    for i in range(n-2, -1, -1):
        print(i, nums[i], goal)
        if i + nums[i] >= goal:
            goal = i
    return goal == 0
    
nums = [2,3,1,1,4]
print(canJump("", nums))