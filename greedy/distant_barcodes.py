# https://leetcode.com/problems/distant-barcodes/description/
# In a warehouse, there is a row of barcodes, where the ith barcode is barcodes[i].
# Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer, and it is guaranteed an answer exists.

# Example 1:
# Input: barcodes = [1,1,1,2,2,2]
# Output: [2,1,2,1,2,1]

# Example 2:
# Input: barcodes = [1,1,1,1,2,2,3,3]
# Output: [1,3,1,3,1,2,1,2]

import heapq
from collections import Counter

barcodes = [1,1,1,2,2,2]


hash_map = dict(Counter(barcodes))
max_heap = []
heapq.heapify(max_heap)

for key in hash_map:
    heapq.heappush(max_heap, [-hash_map[key], key])

ans = []
while max_heap:
    elem1 = heapq.heappop(max_heap)
    ans.append(elem1[1])
    if max_heap:
        elem2 = heapq.heappop(max_heap)
        ans.append(elem2[1])
        if elem2[0] != -1:
            elem2[0] += 1
            heapq.heappush(max_heap, elem2)
        if elem1[0] != -1:
            elem1[0] += 1
            heapq.heappush(max_heap, elem1)
print(ans)