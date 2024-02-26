# Coin Change
# Unbounded Knapsack
# You are given coins of different denominations, represented by an array - coins of size n. You are also given a value - target. Find the different number of combinations that make up the amount target. Assume that you have infinite number of each kind of coin.

# Example
# coins: [5, 2, 4]
# target: 13
# Result: 3
# Explanation: The three ways are-
# 2, 2, 2, 2, 5
# 2, 2, 4, 5
# 4, 4, 5
from typing import List

class Solution:
    def recursive(self, coins, n, target):
        if target == 0:
            return 1
        if n == 0 or target < 0:
            return 0
        take_elem = self.recursive(coins, n, target - coins[n-1])
        no_take_elem = self.recursive(coins, n-1, target)
        return take_elem + no_take_elem
    
    def recursive_memoize(self, coins, n, target, t):
        if target == 0:
            return 1
        if n == 0 or target < 0:
            return 0
        if t[n][target] != -1:
            return t[n][target]
        take_elem = self.recursive_memoize(coins, n, target - coins[n-1], t)
        no_take_elem = self.recursive_memoize(coins, n-1, target, t)
        t[n][target] = take_elem + no_take_elem
        return t[n][target]
    
    def numberOfCombinations(self, coins: List[int], target: int) -> int:
        t = []
        n = len(coins)
        for _ in range(n+1):
            t.append([-1]*(target+1))
        
        for i in range(target+1):
            t[0][i] = 0
        for i in range(n+1):
            t[i][0] = 1
        
        t[0][0] = 1
        for i in range(1, n+1):
            for j in range(1, target+1):
                if coins[i-1] <= j:
                    t[i][j] = t[i-1][j] + t[i][j-coins[i-1]]
                else:
                    t[i][j] = t[i-1][j]
        
        return t[n][target]

sol = Solution()
coins = [1, 2, 4, 5]
n = len(coins)
target = 28
print(sol.numberOfCombinations(coins, target))
print(sol.recursive(coins, n, target))
t = []
for _ in range(n+1):
    t.append([-1]*(target+1))

print(sol.recursive_memoize(coins, n, target, t))