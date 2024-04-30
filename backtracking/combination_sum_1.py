# https://workat.tech/problem-solving/practice/combination-sum-1
# Combination Sum 1

# Given an array of distinct integers A and a target value val, find all unique combinations of integers from A where their sum is equal to val.

# Note: Each integer may be used multiple times in the combination.

# Example
# A: [1, 2]
# val: 4
# Combinations: [
#   [1, 1, 1, 1],
#   [1, 1, 2],
#   [2, 2]
# ]

A = [1, 2]
val = 4

n = len(A)
ans = []

def solve(cur_indx, curr_sum, output_list, ans, n):
    if curr_sum == val:
        ans.append(output_list[::])
    
    if curr_sum > val:
        return

    for i in range(cur_indx, n):
        output_list.append(A[i])
        curr_sum += A[i]
        solve(i, curr_sum, output_list, ans, n)
        output_list.pop()
        curr_sum -= A[i]

solve(0, 0, [], ans, n)
print(ans)
    