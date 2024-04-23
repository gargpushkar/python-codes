# Subset Sum Problem
# Given a set of non-negative integers and a value sum, the task is to check if there is a subset of the given set whose sum is equal to the given sum. 

# Examples: 

# Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
# Output: True
# Explanation: There is a subset (4, 5) with sum 9.

# Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
# Output: False
# Explanation: There is no subset that add up to 30.

arr = [16, 15, 12, 16, 4, 20, 16]
n = len(arr)
sub_sum = 21

t = []
for i in range(n+1):
    t.append([-1]*(sub_sum+1))

def is_subset_sum(arr, n, sub_sum, t):
    if sub_sum == 0:
        return True
    if n == 0:
        return False
    if t[n][sub_sum] != -1:
        return t[n][sub_sum]
    
    if arr[n-1] > sub_sum:
        t[n][sub_sum] = is_subset_sum(arr, n-1, sub_sum, t)
    else:
        t[n][sub_sum] = is_subset_sum(arr, n-1, sub_sum - arr[n-1], t) or is_subset_sum(arr, n-1, sub_sum, t)
    return t[n][sub_sum]
    

print(is_subset_sum(arr, n, sub_sum, t))

arr = [16, 15, 12, 16, 4, 20, 16]
n = len(arr)
sub_sum = 21
# arr = [3, 34, 4, 12, 5, 2]
# n = len(arr)
# sub_sum = 36

t = []
for i in range(n+1):
    t.append([-1]*(sub_sum+1))

for i in range(n+1):
    for j in range(sub_sum+1):
        if i == 0:
            t[i][j] = False
        if j == 0:
            t[i][j] = True
t[0][0] = True

for i in range(1, n+1):
    for j in range(1, sub_sum+1):
        if arr[i-1] > j:
            t[i][j] = t[i-1][j]
        else:
            t[i][j] = t[i-1][j] or t[i-1][j-arr[i-1]]

print(t[n][sub_sum])
