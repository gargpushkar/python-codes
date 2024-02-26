# Minimum number of deletions and insertions
# Given two strings str1 and str2. The task is to remove or insert the minimum number of characters from/in str1 so as to transform it into str2. It could be possible that the same character needs to be removed/deleted from one point of str1 and inserted to some another point.

# Example 1:
# Input: str1 = "heap", str2 = "pea"
# Output: 3
# Explanation: 2 deletions and 1 insertion
# p and h deleted from heap. Then, p is 
# inserted at the beginning One thing to 
# note, though p was required yet it was 
# removed/deleted first from its position 
# and then it is inserted to some other 
# position. Thus, p contributes one to the 
# deletion_count and one to the 
# insertion_count.

# Example 2:
# Input : str1 = "geeksforgeeks"
# str2 = "geeks"
# Output: 8
# Explanation: 8 deletions

str1 = "geeksforgeeks"
str2 = "geeks"

n = len(str1)
m = len(str2)

t = [[-1 for _ in range(m+1)] for __ in range(n+1)]

def LCS(str1, str2, n, m):
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                t[i][j] = 0
            else:
                if str1[i-1] == str2[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
    return t[n][m]

lcs = LCS(str1, str2, n, m)

print(m - lcs + n - lcs)