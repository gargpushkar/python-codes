# https://workat.tech/problem-solving/practice/combinations
# Combinations

# Given two integers n and k, return all possible combinations of size k containing distinct numbers between 1 and n.

# Note: The list should not contain any duplicate combinations.

# Example
# n: 4
# k: 2
# Combinations: [
#     [1, 2],
#     [1, 3],
#     [1, 4],
#     [2, 3],
#     [2, 4],
#     [3, 4]
# ]


n = 4+1
k = 2

ans = []
def solve(cur_indx, output_list, ans, n, k):
    if len(output_list) == k:
        ans.append(output_list[::])
        return
    
    for i in range(cur_indx, n):
        output_list.append(i)
        solve(i+1, output_list, ans, n, k)
        output_list.pop()

solve(1, [], ans, n, k)
print(ans)