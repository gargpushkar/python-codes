# https://leetcode.com/problems/target-sum/description/
# Target Sum
# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.

# SELFNOTE same as # https://www.geeksforgeeks.org/problems/partitions-with-given-difference/ 

# Example 1:

# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# Example 2:

# Input: nums = [1], target = 1
# Output: 1

nums = [1]
target = 1
n = len(nums)

def get_count(arr, n, target):
    arr_sum = sum(arr)
    if target > arr_sum:
        return 0
    if (target + arr_sum)%2 != 0:
        return 0
    sum_to_find = (target + arr_sum)//2

    t = []
    for _ in range(n+1):
        t.append([-1]*(sum_to_find+1))
    
    for _ in range(n+1):
        t[_][0] = 1
    
    for _ in range(sum_to_find+1):
        t[0][_] = 0
    
    t[0][0] = 1

    for i in range(1, n+1):
        for j in range(0, sum_to_find+1):
            if arr[i-1] > j:
                t[i][j] = t[i-1][j]
            else:
                t[i][j] = t[i-1][j] + t[i-1][j-arr[i-1]]
    
    return t[n][sum_to_find]

print(get_count(nums, n, target))