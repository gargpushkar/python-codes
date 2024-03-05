# Longest Common Prefix
# Given a list of strings A, find the longest common prefix among all the strings.

# Example
# A: [“abc”, “abef”, “abccc”, “abftg”]

# Longest common prefix: “ab”

s = ["apple", "apply", "apollo", "abracadabra"]
# s = ["abc", "abef", "abccc", "abftg"]

# Brute Force
n = len(s)
ans = s[0]
for k in range(1, n):
    i = 0
    temp = ""
    n1 = min(len(ans), len(s[k]))
    while i < n1:
        if ans[i] == s[k][i]:
            temp += ans[i]
            i+=1
        else:
            break
    ans = temp

print(ans)

# Efficient approach
# The optimal and better approach for this problem is to sort the given strings and compare the first and last string to find the longest common prefix. 
# The reason behind checking the first and last strings only is that all the strings in-between must have the same prefix as the strings are sorted lexicographically. 
s.sort()
s1 = s[0]
s2 = s[-1]
n1 = min(len(s1), len(s2))
ans = ""
i = 0
while i < n and s1[i] == s2[i]:
    ans += s1[i]
    i+=1

print(ans)