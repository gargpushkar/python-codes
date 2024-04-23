# Coin Change - II
# https://leetcode.com/problems/coin-change/description/
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:
# Input: coins = [2], amount = 3
# Output: -1

# Example 3:
# Input: coins = [1], amount = 0
# Output: 0

coins = [4]
amount = 20
n = len(coins)

t = [[-1 for _ in range(amount + 1)] for __ in range(n + 1)]
def solve(coins, amount, i):
    if amount == 0:
        return 0
    if amount < 0 or i >= n:
        return float('inf') - 1
    if t[i][amount] != -1:
        return t[i][amount]
    if coins[i] > amount:
        t[i][amount] = solve(coins, amount, i+1)
    else:
        t[i][amount] = min(solve(coins, amount, i+1), 1 + solve(coins, amount-coins[i], i))
    return t[i][amount]

ans = solve(coins, amount, 0)
print(ans)