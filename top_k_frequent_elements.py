# Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

import heapq

# nums = [1,1,1,2,2,3]
nums = [1,1,1,3,2,2,4]
nums = [1]
k = 1

hash_map = {}
for i in nums:
    if i not in hash_map:
        hash_map[i] = 0
    hash_map[i] += 1

min_heap = []
for i in hash_map:
    heapq.heappush(min_heap, [hash_map[i], i])
    if len(min_heap) > k:
        heapq.heappop(min_heap)

while(len(min_heap)):
    print(heapq.heappop(min_heap)[-1])
