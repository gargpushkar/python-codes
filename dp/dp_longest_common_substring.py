# Longest Common Substring
# Given two strings. The task is to find the length of the longest common substring.


# Example 1:

# Input: S1 = "ABCDGH", S2 = "ACDGHR", n = 6, m = 6
# Output: 4
# Explanation: The longest common substring
# is "CDGH" which has length 4.
# Example 2:

# Input: S1 = "ABC", S2 "ACB", n = 3, m = 3
# Output: 1
# Explanation: The longest common substrings
# are "A", "B", "C" all having length 1.

S1 = "ABCDGH"
S2 = "ACDGHR"
n = len(S1)
m = len(S2)

t = [[-1 for _ in range(m+1)] for __ in range(n+1)]
def LCSubstring(S1, S2, n, m):
    maxi = -1
    t_i = 0
    t_j = 0
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                t[i][j] = 0
            else:
                if S1[i-1] == S2[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                    if t[i][j] > maxi:
                        maxi = t[i][j]
                        t_i = i
                        t_j = j
                else:
                    t[i][j] = 0
    ans = ""
    while t_i > 0 and t_j > 0 and t[t_i] != 0:
        if S1[t_i-1] == S2[t_j-1]:
            ans += S1[t_i - 1]
        t_i -=1
        t_j -=1
    print(ans[::-1])
    return maxi

print(LCSubstring(S1, S2, n, m))
