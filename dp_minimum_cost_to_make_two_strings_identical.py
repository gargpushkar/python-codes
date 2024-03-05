# https://www.geeksforgeeks.org/problems/minimum-cost-to-make-two-strings-identical1107/1
# Minimum Cost To Make Two Strings Identical

# Given two strings X and Y, and two values costX and costY, the task is to find the minimum cost required to make the given two strings identical. You can delete characters from both the strings. The cost of deleting a character from string X is costX and from Y is costY. The cost of removing all characters from a string is the same.

# Example 1:
# Input: X = "abcd", Y = "acdb", costX = 10 
#        costY = 20.
# Output: 30
# Explanation: For Making both strings 
# identical we have to delete character 
# 'b' from both the string, hence cost 
# will be = 10 + 20 = 30.

# Example 2:
# Input : X = "ef", Y = "gh", costX = 10
#         costY = 20.
# Output: 60
# Explanation: For making both strings 
# identical, we have to delete 2-2 
# characters from both the strings, hence 
# cost will be = 10 + 10 + 20 + 20 = 60.

X = "ef"
Y = "gh"
costX = 10 
costY = 20

def findMinCost(X, Y, costX, costY):
    n = len(X)
    m = len(Y)
    t = [[-1 for _ in range(m+1)] for __ in range(n+1)]
    
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                t[i][j] = 0
            else:
                if X[i-1] == Y[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
    # i = n
    # j = n
    # s = ""
    # while i > 0 and j > 0:
    #     if X[i-1]==Y[j-1]:
    #         s+= X[i-1]
    #         i-=1
    #         j-=1
    #     else:
    #         if t[i-1][j] > t[i][j-1]:
    #             i-=1
    #         else:
    #             j-=1
    
    return (n-t[n][m])*costX + (m-t[n][m])*costY

print(findMinCost(X, Y, costX, costY))
