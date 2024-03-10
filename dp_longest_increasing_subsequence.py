# Longest Increasing Subsequence
# Given an array A, find the length of the longest strictly increasing subsequence (LIS).

# A subsequence is a sequence that can be derived from an array by deleting some or no elements such that the order of the remaining elements remain the same.

# Example
# A: [10, 20, 2, 5, 3, 8, 8, 25, 6]
# Result: 4
# Explanation: Longest increasing subsequence: [2, 5, 8, 25]


import bisect

# A = [10, 20, 2, 5, 3, 8, 8, 25, 6]
# A = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
A = [4, 8, 13, 6, 5, 8, 8, 8, 11, 13, 9, 10, 11]
n = len(A)
# Brute Force
def solve(arr, n, curr, prev):
    # base case
    if curr == n:
        return 0
    
    # include elem
    take = 0
    if prev == -1 or arr[curr] > arr[prev]:
        take = 1 + solve(arr, n, curr+1, curr)
    
    not_take = 0 + solve(arr, n, curr+1, prev)

    return max(take, not_take)

print(solve(A, n, 0, -1))


# Memoization
t = [[-1 for _ in range(n+1)] for __ in range(n+1)]

def solve_memo(arr, n, curr, prev, t):
    if curr == n:
        return 0

    if t[curr][prev] != -1:
        return t[curr][prev]
    
    # inclue
    take = 0
    if prev == -1 or arr[curr] > arr[prev]:
        take = 1 + solve_memo(arr, n, curr+1, curr, t)
    
    not_take = 0 + solve_memo(arr, n, curr+1, prev, t)
    t[curr][prev] = max(take, not_take)
    return t[curr][prev]


print(solve_memo(A, n, 0, -1, t))



def solve_tab(arr, n):
    t = [1 for i in range(n)]
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                t[i] = max(t[i], 1 + t[j])
    return max(t)

print(solve_tab(A, n))



# Binary Search
# https://www.youtube.com/watch?v=MYHajVcnXSA

def lower_bound(A, n, elem):
    l = 0
    r = n-1
    while l < r:
        mid = l + (r-l)//2
        if elem <= A[mid]:
            r = mid
        else:
            l = mid + 1
    return r

def solve_binary(arr, n):
    ans = [arr[0]]
    for i in range(1, n):
        if arr[i] > ans[-1]:
            ans.append(arr[i])
        else:
            # Binary Search
            mid = lower_bound(ans, len(ans), arr[i])
            # mid = bisect.bisect_left(ans, arr[i])
            # l = 0
            # r = len(ans) - 1
            # while l<=r:
            #     mid = l + (r-l)//2
            #     if ans[mid] > arr[i]:
            #         r = mid - 1
            #     else:
            #         l = mid + 1
            ans[mid] = arr[i]
    return len(ans)

print(solve_binary(A, n))
