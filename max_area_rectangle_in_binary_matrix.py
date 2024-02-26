# Given a binary matrix M of size n X m. Find the maximum area of a rectangle formed only of 1s in the given matrix.
# Input:
# n = 4, m = 4
# M[][] = {{0 1 1 0},
#          {1 1 1 1},
#          {1 1 1 1},
#          {1 1 0 0}}
# Output: 8
# Explanation: For the above test case the
# matrix will look like
# 0 1 1 0
# 1 1 1 1
# 1 1 1 1
# 1 1 0 0
# the max size rectangle is 
# 1 1 1 1
# 1 1 1 1
# and area is 4 *2 = 8.


# matrix = [
#     [0, 1, 1, 0],
#     [1, 1, 1, 1],
#     [1, 1, 1, 1],
#     [1, 1, 0, 0]
# ]
from collections import deque

matrix = [
    [1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0]
]

def max_area_histogram(arr):
    NS_stack = deque()
    array_left = []
    array_right = []
    n = len(arr)
    for i in range(n):
        while(NS_stack and NS_stack[-1][0] >= arr[i]):
            NS_stack.pop()
        if NS_stack:
            array_left.append(NS_stack[-1][1])
        else:
            array_left.append(-1)
        NS_stack.append([arr[i], i])
    
    NS_stack = deque()
    for i in range(n-1, -1, -1):
        while(NS_stack and NS_stack[-1][0]>=arr[i]):
            NS_stack.pop()
        if NS_stack:
            array_right.append(NS_stack[-1][1])
        else:
            array_right.append(n)
        NS_stack.append([arr[i], i])
    array_right = array_right[::-1]


    ans = -1
    for i in range(n):
        ans = max(ans, (array_right[i] - array_left[i] - 1) * arr[i])
    # width_array = []
    # for i in range(n):
    #     width_array.append(array_right[i] - array_left[i] - 1)

    # ans = -1
    # for i in range(n):
    #     ans = max(ans, width_array[i] * arr[i])
    return ans

n = len(matrix)
m = len(matrix[0])


arr = matrix[0]
ans = max_area_histogram(arr)
for i in range(1, n):
    for j in range(m):
        if matrix[i][j] == 0:
            arr[j] = 0
        else:
            arr[j] = arr[j] + matrix[i][j]
    area_histogram = max_area_histogram(arr)
    ans = max(area_histogram, ans)

print(ans)