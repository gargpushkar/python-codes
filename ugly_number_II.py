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
ugly_list = [1]
ugly_2s_pt = 0
ugly_3s_pt = 0
ugly_5s_pt = 0
for i in range(1, n):
    ugly2 = ugly_list[ugly_2s_pt] * 2
    ugly3 = ugly_list[ugly_3s_pt] * 3
    ugly5 = ugly_list[ugly_5s_pt] * 5

    ugly_list.append(min(ugly2, ugly3, ugly5))
    if ugly_list[-1] == ugly2:
        ugly_2s_pt += 1
    
    if ugly_list[-1] == ugly3:
        ugly_3s_pt += 1
    
    if ugly_list[-1] == ugly5:
        ugly_5s_pt += 1

print(ugly_list[n-1])