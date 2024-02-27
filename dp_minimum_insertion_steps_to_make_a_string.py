# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/description/
# Minimum Insertion Steps to Make a String Palindrome
# Given a string s. In one step you can insert any character at any index of the string.

# Return the minimum number of steps to make s palindrome.

# A Palindrome String is one that reads the same backward as well as forward.

 

# Example 1:

# Input: s = "zzazz"
# Output: 0
# Explanation: The string "zzazz" is already palindrome we do not need any insertions.
# Example 2:

# Input: s = "mbadm"
# Output: 2
# Explanation: String can be "mbdadbm" or "mdbabdm".
# Example 3:

# Input: s = "leetcode"
# Output: 5
# Explanation: Inserting 5 characters the string becomes "leetcodocteel".

# s = "leetcode"
# s = "zzazz"
s = "mbadm"
s2 = s[::-1]
n = len(s)
t = [[-1 for _ in range(n+1)] for __ in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if i == 0 or j == 0:
            t[i][j] = 0
        else:
            if s[i-1] == s2[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])

print(n - t[n][n])