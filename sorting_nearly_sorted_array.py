# Given an array of n elements, where each element is at most k away from its target position, devise an algorithm that sorts in O(n log k) time. For example, let us consider k is 2, an element at index 7 in the sorted array, can be at indexes 5, 6, 7, 8, 9 in the given array.

# Example:
# Input : arr[] = {6, 5, 3, 2, 8, 10, 9}
# k = 3 
# Output : arr[] = {2, 3, 5, 6, 8, 9, 10} . 

import heapq
arr = [6, 5, 3, 2, 8, 10, 9]
k=3
min_heap = []
heapq.heapify(min_heap)

for i in range(len(arr)):
    heapq.heappush(min_heap, arr[i])
    if len(min_heap) > k:
        element = heapq.heappop(min_heap)
        arr[i-k] = element
i+=1
while(len(min_heap)):
    arr[i-k] = heapq.heappop(min_heap)
    i+=1

print(arr)