# Ways to Express an Integer as Sum of Powers

# Given two positive integers n and x.
# Return the number of ways n can be expressed as the sum of the xth power of unique positive integers, in other words, the number of sets of unique integers [n1, n2, ..., nk] where n = n1x + n2x + ... + nkx.
# Since the result can be very large, return it modulo 109 + 7.
# For example, if n = 160 and x = 3, one way to express n is n = 2**3 + 3**3 + 5**3.

# Example 1:

# Input: n = 10, x = 2
# Output: 1
# Explanation: We can express n as the following: n = 3**2 + 1**2 = 10.
# It can be shown that it is the only way to express 10 as the sum of the 2nd power of unique integers.

# Example 2:
# Input: n = 4, x = 1
# Output: 2
# Explanation: We can express n in the following ways:
# - n = 41 = 4.
# - n = 31 + 11 = 4.

import math

n = 91
x = 1

arr = [i**x for i in range(1, math.ceil(math.pow(n+1, 1/x)))]
arr_len = len(arr)
print(arr)

t = [[-1 for _ in range(n+1)] for __ in range(arr_len+1)]
MOD = 10**9 + 7
def solve(arr, number, arr_len):
    if number == 0:
        return 1
    if number < 0 or arr_len == 0:
        return 0
    if t[arr_len][number] != -1:
        return t[arr_len][number]
    take = solve(arr, number - arr[arr_len-1], arr_len-1)
    notake = solve(arr, number, arr_len-1)
    t[arr_len][number] = (take%MOD + notake%MOD)%MOD
    return t[arr_len][number]

print(solve(arr, n, arr_len))
