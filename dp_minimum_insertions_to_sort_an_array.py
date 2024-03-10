# Minimum insertions to sort an array

# Given an array arr of size N, the task is to sort this array in a minimum number of steps where in one step you can remove any array element from its position and insert it in any other position.

# Example 1:

# Input:
# N = 7
# arr[] = {2, 3, 5, 1, 4, 7, 6}
# Output: 3
# Explanation: 
# We can sort above array in 3 insertion 
# steps as shown below,
# 1 before array value 2
# 4 before array value 5
# 6 before array value 7
# Example 2:

# Input:
# N = 4
# arr[] = {4, 6, 5, 1}
# Output: 2
# Explanation: 
# We can sort above array in 2 insertion 
# steps as shown below, 
# 1 before array value 4
# 6 after array value 5 

# arr = [4, 6, 5, 1]
# arr = [4, 3, 2, 1]
arr = [9, 20, 17, 8, 9, 19, 18, 9, 11, 16]
n = len(arr)

def minimum_insertions(arr, n):
    t = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if arr[i] >= arr[j]:
                t[i] = max(t[i], 1 + t[j])
    return n - max(t)

print(minimum_insertions(arr, n))