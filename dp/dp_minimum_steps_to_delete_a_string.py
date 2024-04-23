# Minimum steps to delete a string
# Given string s containing characters as integers only, the task is to delete all characters of this string in a minimum number of steps wherein one step you can delete the substring which is a palindrome. After deleting a substring remaining parts are concatenated.

# Example 1:

# Input: s = "2553432"
# Output: 2
# Explanation: In first step remove "55", 
# then string becomes "23432" which is a 
# palindrome.
# Example 2:
# Input: s = "1234"
# Output: 4
# Explanation: Remove each character in 
# each step

s = "xyzxcc"
s = "35577171707053"
# s = "1234321"
n = len(s)

def lcs(s, n):
    s1 = s
    s2 = s[::-1]
    t = [[-1 for _ in range(n+1)] for __ in range(n+1)]
    t_i = 0
    t_j = 0
    count = -1
    for i in range(n+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                t[i][j] = 0
            else:
                if s1[i-1] == s2[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                    if t[i][j] > count:
                        count = t[i][j]
                        t_i = i
                        t_j = j
                else:
                    t[i][j] = 0
    # pal_substr = ""
    while t_i > 0 and t_j > 0:
        if s1[t_i-1] == s2[t_j-1]:
            # pal_substr += s1[t_i-1]
            tt_i = t_i-1
        t_i -=1
        t_j -=1
    # print(pal_substr)
    return 1, s[0:tt_i] + s[tt_i + count:]

s1 = s
s2 = s[::-1]

ans = 0
while len(s):
    n = len(s)
    count, s = lcs(s, n)
    ans += count
print(ans)