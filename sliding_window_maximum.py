# https://leetcode.com/problems/sliding-window-maximum/description/
# Sliding Window Maximum
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

 

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]

from collections import deque

nums = [1,3,-1,-3,5,3,6,7]
# nums = [1,3,1,2,0,5]
k = 3
n = len(nums)

dq = deque()

i=0
j=0
ans = []
while(j<n):
    elem = nums[j]
    print(dq, elem, nums[i])
    if len(dq) and dq[-1] < elem:
        while(len(dq) and dq[-1] < elem):
            dq.pop()
    dq.append(elem)
    if j-i+1 < k:
        j+=1
    elif j-i+1 == k:
        ans.append(dq[0])
        if dq and dq[0] == nums[i]:
            dq.popleft()
        i+=1
        j+=1

print(ans)