# 0/1 Knapsack Problem
# Given N items where each item has some weight and profit associated with it and also given a bag with capacity W, [i.e., the bag can hold at most W weight in it]. 
# The task is to put the items into the bag such that the sum of profits associated with them is the maximum possible. 

# Note: The constraint here is we can either put an item completely into the bag or cannot put it at all [It is not possible to put a part of an item into the bag].

# Input: N = 3, W = 4, profit[] = {1, 2, 3}, weight[] = {4, 5, 1}
# Output: 3
# Explanation: There are two items which have weight less than or equal to 4. If we select the item with weight 4, the possible profit is 1. And if we select the item with weight 1, the possible profit is 3. So the maximum possible profit is 3. Note that we cannot put both the items with weight 4 and 1 together as the capacity of the bag is 4.

# Input: N = 3, W = 3, profit[] = {1, 2, 3}, weight[] = {4, 5, 6}
# Output: 0

N = 3
profit = [60, 100, 120]
weight = [10, 20, 30]
W = 50
# N = 4
# profit = [1, 4, 5, 7]
# weight = [1, 3, 4, 5]
# W = 7


# RECURSIVE SOLUTION
def get_max_val(weight, profit, W, N, i):
    if N == 0 or W == 0:
        return 0
    curr_weight = weight[i]
    if curr_weight <= W:
        curr_profit1 = profit[i] + get_max_val(weight, profit, W-curr_weight, N-1, i+1)
        curr_profit2 = get_max_val(weight, profit, W, N-1, i+1)
        return max(curr_profit1, curr_profit2)
    else:
        return get_max_val(weight, profit, W, N-1, i+1)

print(get_max_val(weight, profit, W, N, 0))


N = 3
profit = [60, 100, 120]
weight = [10, 20, 30]
W = 50

dp = []
for i in range(N+1):
    dp.append([-1]*(W+1))


def dp_knapsack(profit, weight, N, W, i):
    if W == 0 or N == 0:
        return 0
    current_weight = weight[i]
    if current_weight <= W:
        if dp[i][W] != -1:
            return dp[i][W]
        
        elem_profit = profit[i]
        profit_with_elem = elem_profit + dp_knapsack(profit, weight, N-1, W-current_weight, i+1)
        profit_without_elem = dp_knapsack(profit, weight, N-1, W, i+1)
        dp[i][W] = max(profit_with_elem, profit_without_elem)
        return dp[i][W]
    else:
        if dp[i][W] != -1:
            return dp[i][W]
        dp[i][W] = dp_knapsack(profit, weight, N-1, W, i+1)
        return dp[i][W]


print(dp_knapsack(profit, weight, N, W, 0))


N = 58
W = 41
profit = [57, 95, 13, 29, 1, 99, 34, 77, 61, 23, 24, 70, 73, 88, 33, 61, 43, 5, 41, 63, 8, 67, 20, 72, 98, 59, 46, 58, 64, 94, 97, 70, 46, 81, 42, 7, 1, 52, 20, 54, 81, 3, 73, 78, 81, 11, 41, 45, 18, 94, 24, 82, 9, 19, 59, 48, 2, 72]
weight = [83, 84, 85, 76, 13, 87, 2, 23, 33, 82, 79, 100, 88, 85, 91, 78, 83, 44, 4, 50, 11, 68, 90, 88, 73, 83, 46, 16, 7, 35, 76, 31, 40, 49, 65, 2, 18, 47, 55, 38, 75, 58, 86, 77, 96, 94, 82, 92, 10, 86, 54, 49, 65, 44, 77, 22, 81, 52]
dp = []
for i in range(N+1):
    dp.append([-1]*(W+1))

print(dp_knapsack(profit, weight, N, W, 0))


N = 58
W = 41
profit = [57, 95, 13, 29, 1, 99, 34, 77, 61, 23, 24, 70, 73, 88, 33, 61, 43, 5, 41, 63, 8, 67, 20, 72, 98, 59, 46, 58, 64, 94, 97, 70, 46, 81, 42, 7, 1, 52, 20, 54, 81, 3, 73, 78, 81, 11, 41, 45, 18, 94, 24, 82, 9, 19, 59, 48, 2, 72]
weight = [83, 84, 85, 76, 13, 87, 2, 23, 33, 82, 79, 100, 88, 85, 91, 78, 83, 44, 4, 50, 11, 68, 90, 88, 73, 83, 46, 16, 7, 35, 76, 31, 40, 49, 65, 2, 18, 47, 55, 38, 75, 58, 86, 77, 96, 94, 82, 92, 10, 86, 54, 49, 65, 44, 77, 22, 81, 52]
# N = 3
# profit = [60, 100, 120]
# weight = [10, 20, 30]
# W = 50
t = []
for i in range(N+1):
    t.append([-1]*(W+1))

def knapsack(profit, weight, n, w, t):
    if n == 0 or t == 0:
        return 0
    
    if t[n][w] != -1:
        return t[n][w]
    else:
        if weight[n-1] <= w:
            profit_with_elem = profit[n-1] + knapsack(profit, weight, n-1, w-weight[n-1], t)
            profit_without_elem = knapsack(profit, weight, n-1, w, t)
            t[n][w] = max(profit_with_elem, profit_without_elem)
            return t[n][w]
        else:
            t[n][w] = knapsack(profit, weight, n-1, w, t)
            return t[n][w]

print(knapsack(profit, weight, N, W, t))


N = 58
W = 41
profit = [57, 95, 13, 29, 1, 99, 34, 77, 61, 23, 24, 70, 73, 88, 33, 61, 43, 5, 41, 63, 8, 67, 20, 72, 98, 59, 46, 58, 64, 94, 97, 70, 46, 81, 42, 7, 1, 52, 20, 54, 81, 3, 73, 78, 81, 11, 41, 45, 18, 94, 24, 82, 9, 19, 59, 48, 2, 72]
weight = [83, 84, 85, 76, 13, 87, 2, 23, 33, 82, 79, 100, 88, 85, 91, 78, 83, 44, 4, 50, 11, 68, 90, 88, 73, 83, 46, 16, 7, 35, 76, 31, 40, 49, 65, 2, 18, 47, 55, 38, 75, 58, 86, 77, 96, 94, 82, 92, 10, 86, 54, 49, 65, 44, 77, 22, 81, 52]

t = []
for i in range(N+1):
    t.append([-1]*(W+1))

for i in range(N+1):
    for j in range(W+1):
        if i == 0 or j == 0:
            t[i][j] = 0


def tab_knapsack(n, t):
    for i in range(1, n+1):
        for j in range(1, W+1):
            if weight[i-1] <= j:
                t[i][j] = max(profit[i-1] + t[i-1][j-weight[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    print(t[n][W])
tab_knapsack(N)
# print(t)