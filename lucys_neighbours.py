# Lucy's Neighbours
# Lucy lives in house number X. She has a list of N house numbers in the society. Distance between houses can be determined by studying the difference between house numbers. Help her find out K closest neighbors.
# Note: If two houses are equidistant and Lucy has to pick only one, the house with the smaller house number is given preference.

# Input:
# N = 5, X = 0, K = 4
# a[] = {-21, 21, 4, -12, 20}, 
# Output:
# -21 -12 4 20
# Explanation:
# The closest neighbour is house
# number 4. Followed by -12 and 20. -21 and 21 
# are both equal distance from X=0. Therefore, 
# Lucy can only pick 1. Based on the given 
# condition she picks -21 as it is the smaller 
# of the two. 

# Input:
# N = 6, X = 5, K = 3 
# a[] = {10, 2, 14, 4, 7, 6},
# Output:
# 4 6 7 

import heapq
# n = 6
# x = 5
# k = 3
# arr = [10, 2, 14, 4, 7, 6]
# n = 2
# x = -42
# k = 1
# arr = [-68, 45]
n = 5
x = 0
k = 4
arr = [-21, 21, 4, -12, 20]
ans = []
min_heap = []
heapq.heapify(min_heap)
for i in arr:
    heapq.heappush(min_heap, [abs(abs(i-x)), i])
print(min_heap)

while k:
    elem = heapq.heappop(min_heap)
    print(elem)
    ans.append(elem[1])
    k-=1
print(sorted(ans))