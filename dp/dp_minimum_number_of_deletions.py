# Minimum number of deletions
# Given a string 'str' of size ‘n’. The task is to remove or delete the minimum number of characters from the string so that the resultant string is a palindrome. Find the minimum numbers of characters we need to remove.
# Note: The order of characters should be maintained.

# Example 1:

# Input: n = 7, str = "aebcbda"
# Output: 2
# Explanation: We'll remove 'e' and
# 'd' and the string become "abcba".

Str = "aebcbda"
n = 7

def min_deletions(Str, n):
    str1 = Str
    str2 = Str[::-1]
    t = [[-1 for _ in range(n+1)] for __ in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                t[i][j] = 0
            else:
                if str1[i-1] == str2[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
    return n - t[n][n]