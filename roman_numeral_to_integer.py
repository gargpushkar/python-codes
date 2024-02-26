# Roman Numeral to Integer
# Given a roman numeral s, convert it to an integer.

# Roman numerals are denoted by a combination of some symbols.

# Symbol	Value
# I	1
# V	5
# X	10
# L	50
# C	100
# D	500
# M	1000

# Example 1
# s: “X”

# Result: 10

# Example 2
# s: “VI”

# Result: 6

# Example 3
# s: “XII”

# Result: 12

s = "CMXCIV"
hash_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

n = len(s)
ans = 0
i = 0
while i < n:
    if i+1 < n and hash_map[s[i]] < hash_map[s[i+1]]:
        ans += hash_map[s[i+1]] - hash_map[s[i]]
        i+=2
    else:
        ans += hash_map[s[i]]
        i+=1
print(ans)