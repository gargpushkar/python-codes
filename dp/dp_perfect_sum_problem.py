# https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1
# Given an array arr of non-negative integers and an integer sum, the task is to count all subsets of the given array with a sum equal to a given sum.

# Note: Answer can be very large, so, output answer modulo 109+7.

# Example 1:

# Input: 
# N = 6
# arr = [5, 2, 3, 10, 6, 8]
# sum = 10
# Output: 
# 3
# Explanation: 
# {5, 2, 3}, {2, 8}, {10} are possible subsets.
# Example 2:
# Input: 
# N = 5
# arr = [2, 5, 1, 4, 3]
# sum = 10
# Output: 
# 3
# Explanation: 
# {2, 1, 4, 3}, {5, 1, 4}, {2, 5, 3} are possible subsets.

# arr = [5, 2, 3, 10, 6, 8]
# n = 6
# total = 10
arr = [9, 7, 0, 3, 9, 8, 6, 5, 7, 6]
n = 10
total = 31

# Incorrect Logic
# Recursive
def get_count(arr, n, total):
    if total == 0:
        return 1
    if n == 0:
        return 0
    if arr[n-1] > total:
        return get_count(arr, n-1, total)
    else:
        return get_count(arr, n-1, total) + get_count(arr, n-1, total-arr[n-1])

print(get_count(arr, n, total))

# Incorrect Logic
# Memoization
arr = [9, 7, 0, 3, 9, 8, 6, 5, 7, 6]
n = 10
total = 31
t = []
for i in range(n+1):
    t.append([-1]*(total+1))

for j in range(total+1):
    t[0][j] = 0
for i in range(n+1):
    t[i][0] = 0
# for i in range(n+1):
#     for j in range(total+1):
#         if i == 0:
#             t[i][j] = 0
#         if j == 0:
#             t[i][j] = 1

t[0][0]=1

def get_count_memo(arr, n, total):
    if total == 0:
        return 1
    if n == 0:
        return 0
    if t[n][total] != -1:
        return t[n][total]
    if arr[n-1] > total:
        t[n][total] = get_count_memo(arr, n-1, total)
    else:
        t[n][total] = get_count_memo(arr, n-1, total) + get_count_memo(arr, n-1, total-arr[n-1])
    return t[n][total]

print(get_count_memo(arr, n, total))

# Correct Logic
# Tabular
arr = [9, 7, 0, 3, 9, 8, 6, 5, 7, 6]
n = 10
total = 31
t = []
for i in range(n+1):
    t.append([-1]*(total+1))

for j in range(total+1):
    t[0][j] = 0
for i in range(n+1):
    t[i][0] = 1

t[0][0]=1

for i in range(1, n+1):
    for j in range(0, total+1):
        if arr[i-1] > j:
            t[i][j] = t[i-1][j]
        else:
            t[i][j] = t[i-1][j] + t[i-1][j-arr[i-1]]

print(t[n][total])