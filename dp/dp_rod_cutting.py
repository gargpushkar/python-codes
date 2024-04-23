# Rod Cutting
# Unbounded Knapsack
# You are given a rod of length n, and an array prices of size n which contains the prices of rods of lengths 1 to n. Find the maximum amount you can make if you cut up the rod optimally.

# Example
# n: 8
# A: [1, 3, 4, 5, 7, 9, 10, 11]
# Result: 12
# Explanation: Rods of length 2 and 6 cost: 3 + 9

from typing import List

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