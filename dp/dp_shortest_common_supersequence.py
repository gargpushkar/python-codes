# https://www.geeksforgeeks.org/problems/shortest-common-supersequence0322/1
# Shortest Common Supersequence
# Given two strings X and Y of lengths m and n respectively, find the length of the smallest string which has both, X and Y as its sub-sequences.
# Note: X and Y can have both uppercase and lowercase letters.

# Example 1
# Input:
# X = abcd, Y = xycd
# Output: 6
# Explanation: Shortest Common Supersequence
# would be abxycd which is of length 6 and
# has both the strings as its subsequences.

# Example 2
# Input:
# X = efgh, Y = jghi
# Output: 6
# Explanation: Shortest Common Supersequence
# would be ejfghi which is of length 6 and
# has both the strings as its subsequences.

X = "abac"
Y = "cab"
n = len(X)
m = len(Y)

def LCS(s1, s2, n, m, t):
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                t[i][j] = 0
            else:
                if s1[i-1] == s2[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
    return t[i][j]

t = [[-1 for _ in range(m+1)] for __ in range(n+1)]
lcs = LCS(X, Y, n, m, t)

print(n+m-lcs)

# Now Printing
lcs_string = ""
i = n
j = m
while i > 0 and j > 0:
    if X[i-1] == Y[j-1]:
        lcs_string += X[i-1]
        i-=1
        j-=1
    else:
        if t[i-1][j] > t[i][j-1]:
            i-=1
        else:
            j-=1

lcs_string = lcs_string[::-1]
print(lcs_string)

i = 0
j = 0
k = 0
ans_string = ""
while i < n and j < m and k < len(lcs_string):
    if X[i] == Y[j] == lcs_string[k]:
        ans_string += X[i]
        i+=1
        j+=1
        k+=1
    else:
        if X[i] != lcs_string[k]:
            ans_string += X[i]
            i+=1
        elif Y[j] != lcs_string[k]:
            ans_string += Y[j]
            j+=1
while i < n:
    ans_string += X[i]
    i+=1
while j < m:
    ans_string += Y[j]
    j+=1
print(ans_string)
