# Perfect Squares

# Given an integer n, return the least number of perfect square numbers that sum to n.
# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

# Example 1:
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.

# Example 2:
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
import math

n = 64
# arr = [i**2 for i in range(1, math.ceil(math.sqrt(n)))]
# arr = [i**2 for i in range(1, n//2)]
arr = []
for i in range(1, n):
    if i**2 > n:
        break
    arr.append(i**2)
arr_length = len(arr)
print(arr)

t = [[-1 for _ in range(n+1)] for __ in range(arr_length+1)]

def solve(arr, arr_length, number):
    if number == 0:
        return 0
    if number < 0 or arr_length == 0:
        return float('inf')
    if t[arr_length][number] != -1:
        return t[arr_length][number]
    
    if arr[arr_length-1] > number:
        t[arr_length][number] = solve(arr, arr_length-1, number)
    else:
        t[arr_length][number] = min(solve(arr, arr_length-1, number), 1 + solve(arr, arr_length, number-arr[arr_length-1]))
    
    return t[arr_length][number]

print(solve(arr, arr_length, n))
