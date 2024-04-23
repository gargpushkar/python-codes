# Minimum Subset Sum Difference
# https://www.geeksforgeeks.org/problems/minimum-sum-partition3317/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

# Given an array arr of size n containing non-negative integers, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum and find the minimum difference


# Example 1:

# Input: N = 4, arr[] = {1, 6, 11, 5} 
# Output: 1
# Explanation: 
# Subset1 = {1, 5, 6}, sum of Subset1 = 12 
# Subset2 = {11}, sum of Subset2 = 11   
# Example 2:
# Input: N = 2, arr[] = {1, 4}
# Output: 3
# Explanation: 
# Subset1 = {1}, sum of Subset1 = 1
# Subset2 = {4}, sum of Subset2 = 4

arr = [8, 5, 6, 6, 5, 7, 4, 7, 6]
arr = [1, 4]
# arr = [1, 6, 11, 5]
n = len(arr)
total_sum = sum(arr)

t = []
for i in range(n+1):
    t.append([-1]*(total_sum+1))

for i in range(n+1):
    for j in range(total_sum+1):
        if i == 0:
            t[i][j] = False
        if j == 0:
            t[i][j] = True

t[0][0] = True

for i in range(1, n+1):
    for j in range(1, total_sum+1):
        if arr[i-1] > total_sum:
            t[i][j] = t[i-1][j]
        else:
            t[i][j] = t[i-1][j] or t[i-1][j - arr[i-1]]

total_sum = sum(arr)
min_sum = 10000001

new_arr = []
for i in range(total_sum+1):
    if t[-1][i]:
        new_arr.append(i)
    # print(i, t[-1][i])

# print(new_arr)
# print(len(new_arr)//2)
# print(new_arr[len(new_arr)//2])
# print(total_sum)
new_arr_length = len(new_arr)
if new_arr_length%2==0:
    new_arr_length = new_arr_length//2
else:
    new_arr_length = new_arr_length//2 + 1
for i in range(new_arr_length):
    min_sum = min(min_sum, total_sum - 2*new_arr[i])
print(min_sum)