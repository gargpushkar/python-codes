# Kth Largest Element

import heapq

A = [3, 5, 2, 4, 6, 1]

def get_k_largest_element(arr, k):
    min_heap = []
    heapq.heapify(min_heap)
    for i in arr:
        heapq.heappush(min_heap, i)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    print(min_heap)
    return min_heap[0]

A.sort()
print(A)
print(get_k_largest_element(A, 4))