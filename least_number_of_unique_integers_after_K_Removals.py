# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/description/?envType=daily-question&envId=2024-02-16
# Least Number of Unique Integers after K Removals

# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

# Example 1:

# Input: arr = [5,5,4], k = 1
# Output: 1
# Explanation: Remove the single 4, only 5 is left.
# Example 2:
# Input: arr = [4,3,1,1,3,3,2], k = 3
# Output: 2
# Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.

import heapq

# arr = [4,3,1,1,3,3,2]
# k = 3
arr = [5,5,4]
k = 1
hash_map = {}
for i in arr:
    if i not in hash_map:
        hash_map[i] = 0
    hash_map[i] += 1

print(hash_map)
min_heap = []
heapq.heapify(min_heap)
for i in hash_map:
    heapq.heappush(min_heap, [hash_map[i], i])

while k:
    elem = heapq.heappop(min_heap)
    if elem[0] <= k:
        k-=elem[0]
        hash_map.pop(elem[1])
    else:
        break

print(hash_map)
print(len(hash_map))
