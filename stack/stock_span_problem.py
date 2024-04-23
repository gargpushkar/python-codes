# https://www.geeksforgeeks.org/problems/stock-span-problem-1587115621/1
# The stock span problem is a financial problem where we have a series of n daily price quotes for a stock and we need to calculate the span of stocks price for all n days. 
# The span Si of the stocks price on a given day i is defined as the maximum number of consecutive days just before the given day, for which the price of the stock on the given day is less than or equal to its price on the current day.
# For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85}, then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}.
# Example 1:

# Input: 
# N = 7, price[] = [100 80 60 70 60 75 85]
# Output:
# 1 1 1 2 1 4 6
# Explanation:
# Traversing the given input span 
# 100 is greater than equal to 100 and there are no more elements behind it so the span is 1,
# 80 is greater than equal to 80 and smaller than 100 so the span is 1,
# 60 is greater than equal to 60 and smaller than 80 so the span is 1,
# 70 is greater than equal to 60,70 and smaller than 80 so the span is 2,
# 60 is greater than equal to 60 and smaller than 70 so the span is 1,
# 75 is greater than equal to 60,70,60,75 and smaller than 100 so the span is 4,
# 85 is greater than equal to 80,60,70,60,75,85 and smaller than 100 so the span is 6. 
# Hence the output will be 1 1 1 2 1 4 6.

# arr = [10, 4, 5, 90, 120, 80]
arr = [100, 80, 60, 70, 60, 75, 85]
# ans = [100, 80, 80, 80, 70, 80, 85]
# NGE = [-1, 10, 10, -1, -1, 120]
# ans = [1, 1, 2, 4, 5, 1]

stack = []
ans = []
for i in range(len(arr)):
    while(stack and stack[-1][0] <= arr[i]):
        stack.pop()
    if stack:
        ans.append(stack[-1])
    else:
        ans.append([-1, -1])
    stack.append([arr[i], i])

# print(ans)
for i in range(len(ans)):
    print(abs(ans[i][-1] - i), end=" ")

