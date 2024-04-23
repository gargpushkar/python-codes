# Rod Cutting
# Unbounded Knapsack
# You are given a rod of length n, and an array prices of size n which contains the prices of rods of lengths 1 to n. Find the maximum amount you can make if you cut up the rod optimally.

# Example
# n: 8
# A: [1, 3, 4, 5, 7, 9, 10, 11]
# Result: 12
# Explanation: Rods of length 2 and 6 cost: 3 + 9

from typing import List


def solve(price, arr, rod_length, n):
    if rod_length == 0:
        return 0
    if n == 0:
        return 0
    
    if arr[n-1] > rod_length:
        return solve(price, arr, rod_length, n-1)
    else:
        nocut = solve(price, arr, rod_length, n-1)
        cut = price[n-1] + solve(price, arr, rod_length - arr[n-1], n)
        return max(nocut, cut)


t = [[-1 for i in range(n+1)] for ii in range(n+1)]
def solve_memo(price, arr, rod_length, n):
    if rod_length == 0 or n == 0:
        return 0
    
    if t[rod_length][n] != -1:
        return t[rod_length][n]
    
    if arr[n-1] > rod_length:
        t[rod_length][n] = solve_memo(price, arr, rod_length, n-1)
    else:
        nocut = solve_memo(price, arr, rod_length, n-1)
        cut = price[n-1] + solve_memo(price, arr, rod_length - arr[n-1], n)
        t[rod_length][n] = max(nocut, cut)
    return t[rod_length][n]


class Solution:
    def maximumProfit(self, n: int, prices: List[int]) -> int:
        length_array = range(1, n+1)
        t = [[0 for _ in range(n+1)]for _ in range(n+1)]
        for i in range(0, n+1):
            for j in range(0, n+1):
                if length_array[i-1] <= j:
                    t[i][j] = max(t[i-1][j], prices[i-1] + t[i][j-length_array[i-1]])
                else:
                    t[i][j] = t[i-1][j]
        return t[n][n]

sol = Solution()
n = 8
A = [1, 3, 4, 5, 7, 9, 10, 11]
print(sol.maximumProfit(n, A))