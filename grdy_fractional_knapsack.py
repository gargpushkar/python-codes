# Fractional Knapsack

# Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
# Note: Unlike 0/1 knapsack, you are allowed to break the item here. 

# Example 1:
# Input:
# N = 3, W = 50
# value[] = {60,100,120}
# weight[] = {10,20,30}
# Output:
# 240.000000
# Explanation:
# Take the item with value 60 and weight 10, value 100 and weight 20 and split the third item with value 120 and weight 30, to fit it into weight 20. so it becomes (120/30)*20=80, so the total value becomes 60+100+80.0=240.0
# Thus, total maximum value of item we can have is 240.00 from the given capacity of sack. 

# Example 2:
# Input:
# N = 2, W = 50
# value[] = {60,100}
# weight[] = {10,20}
# Output:
# 160.000000
# Explanation:
# Take both the items completely, without breaking.
# Total maximum value of item we can have is 160.00 from the given capacity of sack.

N = 3
W = 50
value = [60,100,120]
weight = [10,20,30]
N = 2
W = 50
value = [60,100]
weight = [10,20]

ans = 0
arr = []
for i in range(N):
    arr.append([value[i]/weight[i], weight[i], value[i]])
arr.sort(reverse=True)

while W and arr:
    item_val_1, item_weight, item_val = arr.pop(0)
    if W >= item_weight:
        ans += item_val
        W -= item_weight
    else:
        ans += item_val_1*W
        W = 0

print(ans)