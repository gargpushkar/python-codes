# Best Time to Buy and Sell Stocks II

# You are given an array prices where prices[i] denotes the price of a stock on the ith day. You want to maximize the profit by buying a stock and then selling it at a higher price.

# Suppose you can do as many transactions as you want, what is the maximum profit that you can make?

# Note:

# Return 0 if you cannot make a profit.
# You cannot buy/hold more than 1 stock at a time.
# You need to sell a stock before buying again.
# You can sell a stock and buy it again on the same day.

# Examples

# prices: [6, 1, 4, 2, 5, 3]
# Answer: 6
# Explanation
# Buy on day 2 (price: 1) and Sell on day 3 (price: 4).
# Buy on day 4 (price: 2) and Sell on day 5 (price: 5).
# Profit: (4 - 1) + (5 - 2) = 6.

# prices: [1, 2, 3, 4, 5]
# Answer: 4
# Explanation
# Buy on day 1 (price: 1) and Sell on day 5 (price: 5).
# Profit: (5 - 1) = 4.
from typing import List


prices = [1, 2, 3, 4, 5]
prices = [1, 2, 3, 4, 5]
n = len(prices)

# Brute Force
def solve(prices, i, n, buy):
    if i == n:
        return 0
    if buy:
        with_buy = -prices[i] + solve(prices, i+1, n, 0)
        without_buy = 0 + solve(prices, i+1, n, 1)
        return max(with_buy, without_buy)
    else:
        with_sell = prices[i] + solve(prices, i+1, n, 1)
        without_sell = solve(prices, i+1, n, 0)
        return max(with_sell, without_sell)

print(solve(prices, 0, n, 1))

# Memo
def maxProfit(self, prices: List[int]) -> int:
    def solve_memo(prices, i, n, buy, t):
        if i == n:
            return 0
        if t[i][buy] != -1:
            return t[i][buy]
        
        if buy:
            with_buy = -prices[i] + solve_memo(prices, i+1, n, 0, t)
            without_buy = 0 + solve_memo(prices, i+1, n, 1, t)
            t[i][buy] = max(with_buy, without_buy)
            return t[i][buy]
        else:
            with_sell = prices[i] + solve_memo(prices, i+1, n, 1, t)
            without_sell = solve_memo(prices, i+1, n, 0, t)
            t[i][buy] = max(with_sell, without_sell)
            return t[i][buy]

    t = [[-1 for _ in range(n+1)] for __ in range(n+1)]
    return solve_memo(prices, 0, n, 1, t)



