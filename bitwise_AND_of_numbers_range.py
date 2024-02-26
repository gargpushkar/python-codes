# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
# Bitwise AND of Numbers Range
# Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

 

# Example 1:

# Input: left = 5, right = 7
# Output: 4
# Example 2:

# Input: left = 0, right = 0
# Output: 0
# Example 3:

# Input: left = 1, right = 2147483647
# Output: 0
left = 1
right = 2147483647

# Brute Force
# ans = left
# for i in range(left+1, right+1):
#     ans&=i
# print(ans)

# Better
def get_MSB(num):
    return len(bin(num)[2:])-1

ans = 0
while(left > 0 and right > 0):
    l_msb = get_MSB(left)
    r_msb = get_MSB(right)
    if l_msb != r_msb:
        break
    msb_value = 1<<l_msb # 2**l_msb
    ans += msb_value
    left -= msb_value
    right -= msb_value

print(ans)