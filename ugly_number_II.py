# Ugly Number II
# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return the nth ugly number.

 

# Example 1:

# Input: n = 10
# Output: 12
# Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
# Example 2:

# Input: n = 1
# Output: 1
# Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
 

# Constraints:

# 1 <= n <= 1690

n = 10
ugly_2s = [1]*n
ugly_3s = [1]*n
ugly_5s = [1]*n
for i in range(1, n):
    ugly_2s[i] = i*2
    ugly_3s[i] = i*3
    ugly_5s[i] = i*5

print(ugly_2s)
print(ugly_3s)
print(ugly_5s)