# https://leetcode.com/problems/count-complete-subarrays-in-an-array/description/
# You are given an array nums consisting of positive integers.
# We call a subarray of an array complete if the following condition is satisfied:
# The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
# Return the number of complete subarrays.
# A subarray is a contiguous non-empty part of an array.

# Example 1:
# Input: nums = [1,3,1,2,2]
# Output: 4
# Explanation: The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].

# Example 2:
# Input: nums = [5,5,5,5]
# Output: 10
# Explanation: The array consists only of the integer 5, so any subarray is complete. The number of subarrays that we can choose is 10.

nums = [1,3,1,2,2]
n = len(nums)
distinct = len(set(nums))
hash_map = {}

left = 0
right = 0
ans_count = 0

while right < n:
    if nums[right] not in hash_map:
        hash_map[nums[right]] = 0
    hash_map[nums[right]] += 1

    if len(hash_map) == distinct:
        ans_count+=1
    
    right += 1
    if right == n:
        left += 1
        right = left
        hash_map = {}

print(ans_count)
