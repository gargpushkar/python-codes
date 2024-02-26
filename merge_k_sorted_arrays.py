# Merge K Sorted Arrays

# You are given k sorted arrays in the form of 2D integer matrix arr of size k*n.
# Merge them into a single sorted array.

# Testing
# Input Format
# The first line contains two space-separated integers k and n.

# The next k lines have n space-separated integers each denoting the elements of the array.

# Output Format
# Space-separated results of the resultant sorted array.

# Sample Input
# 3 4
# 1 3 7 10
# 3 3 6 8
# 2 4 7 9
# Expected Output
# 1 2 3 3 3 4 6 7 7 8 9 10
from typing import List
import heapq

# k, n = 3, 4

arr = [
    [1, 3, 7, 10],
    [3, 3, 6, 8],
    [2, 4, 7, 9]
]
def mergeKArrays(self, arr: List[List[int]]) -> List[int]:
    k = len(arr)
    ans = []
    min_heap = []
    heapq.heapify(min_heap)

    for i in range(k):
        heapq.heappush(min_heap, [arr[i].pop(0), i])
        # print(arr[i][0])
        

    while(min_heap):
        data = heapq.heappop(min_heap)
        ans.append(data[0])
        indx = data[1]
        if len(arr[indx]):
            heapq.heappush(min_heap, [arr[indx].pop(0), indx])

    return ans
# print(min_heap)