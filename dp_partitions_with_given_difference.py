# https://www.geeksforgeeks.org/problems/partitions-with-given-difference/1?ref=header_search
# Partitions with Given Difference
# Given an array arr, partition it into two subsets(possibly empty) such that their union is the original array. Let the sum of the element of these two subsets be S1 and S2. 

# Given a difference d, count the number of partitions in which S1 is greater than or equal to S2 and the difference S1 and S2 is equal to d. since the answer may be large return it modulo 109 + 7.

# Example 1:

# Input:
# n = 4, d = 3
# arr[] =  { 5, 2, 6, 4}
# Output:
# 1
# Explanation:
# There is only one possible partition of this array. Partition : {6, 4}, {5, 2}. The subset difference between subset sum is: (6 + 4) - (5 + 2) = 3.
# Example 2:

# Input:
# n = 4, d = 0 arr[] = {1, 1, 1, 1} Output: 6 

n = 4
d = 0
arr =  [1, 1, 1, 1]


def count_partitions(n, d, arr):
    arr_total = sum(arr)
    mod = 10**9 + 7
    if (arr_total + d)%2 != 0:
        return 0
    else:
        sum_to_find = (arr_total + d)//2
    
    t = []
    for _ in range(n+1):
        t.append([-1]*(sum_to_find+1))

    for _ in range(n+1):
        t[_][0] = 1
    
    for _ in range(sum_to_find+1):
        t[0][_] = 0
    t[0][0] = 1

    for i in range(1, n+1):
        for j in range(0, sum_to_find+1):
            if arr[i-1] > j:
                t[i][j] = t[i-1][j]
            else:
                t[i][j] = (t[i-1][j] + t[i-1][j-arr[i-1]])%mod
    
    return t[n][sum_to_find]

print(count_partitions(n, d, arr))