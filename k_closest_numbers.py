# Given an unsorted array and two numbers x and k, find k closest values to x.
# Input : arr[] = {10, 2, 14, 4, 7, 6}, x = 5, k = 3 . 

# A = [6, 4, 5, 2, 9, 7, 8]
A = [-21, 21, 4, -12, 20]
k = 4
x = 0
# A = [1,2,3,4,5]
# k = 4
# x = 3
import heapq

max_heap = []
for i in A:
    if len(max_heap) < k:
        heapq.heappush(max_heap, (-1*abs(i-x), i))
    else:
        if -1*max_heap[0][0] > abs(i-x):
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, (-1*abs(i-x), i))
    
while(len(max_heap)):
    print(heapq.heappop(max_heap))