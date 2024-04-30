# https://workat.tech/problem-solving/practice/combination-sum-2
# Combination Sum 2
# Given an array of integers A and a target value val, find all unique combinations of integers from A where their sum is equal to val.

# Note: Each integer in the array may be used once in the combination.

# Example
# A: [10, 1, 2, 7, 6, 1, 5]
# val: 8
# Combinations: [
#   [1, 1, 6],
#   [1, 2, 5],
#   [1, 7],
#   [2, 6]
# ]

A = [10, 1, 2, 7, 6, 1, 5]
val = 8

A.sort()

n = len(A)
ans = []
hash_map = {}

def solve(cur_indx, curr_sum, outputlist, ans):
    if curr_sum == val:
        output_str = ""
        for elem in outputlist:
            output_str += str(elem)
        if output_str in hash_map:
            return
        ans.append(outputlist[::])
        hash_map[output_str] = 1
        return
    if curr_sum > val:
        return
    
    for i in range(cur_indx, n):
        curr_sum += A[i]
        outputlist.append(A[i])
        solve(i+1, curr_sum, outputlist, ans)
        curr_sum -= A[i]
        outputlist.pop()
    
solve(0, 0, [], ans)
print(ans)