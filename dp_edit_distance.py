# Edit Distance

# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character
 

# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:

# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')


word1 = "intention"
word2 = "execution"
word1 = "horse"
word2 = "ros"

class Solution:
    # Brute Force
    def recursion(self, word1, word2, i, j):
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i
        
        # No Operation case
        if word1[i] == word2[j]:
            return self.recursion(word1, word2, i+1, j+1)

        # Need to perform some operation
        ans = 0
        # 1st operation
        insert = 1 + self.recursion(word1, word2, i, j+1)
        # 2nd operation
        delete = 1 + self.recursion(word1, word2, i+1, j)
        # 3rd operation
        update = 1 + self.recursion(word1, word2, i+1, j+1)
        ans = min(insert, delete, update)
        return ans
    
    # Memoization
    def recursion_memo(self, word1, word2, i, j, t):
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i
        
        if t[i][j] != -1:
            return t[i][j]
        
        if word1[i] == word2[j]:
            t[i][j] = self.recursion_memo(word1, word2, i+1, j+1, t)
            return t[i][j]

        insert_operation = 1 + self.recursion_memo(word1, word2, i, j+1, t)
        delete_operation = 1 + self.recursion_memo(word1, word2, i+1, j, t)
        update_operation = 1 + self.recursion_memo(word1, word2, i+1, j+1, t)
        t[i][j] = min(insert_operation, delete_operation, update_operation)
        return t[i][j]
    
    def recursion_memo2(self, word1, word2, n, m, t):
        if n == 0:
            return m
        if m == 0:
            return n
        
        if t[n][m] != -1:
            return t[n][m]
        if word1[n-1] == word2[m-1]:
            t[n][m] = self.recursion_memo2(word1, word2, n-1, m-1, t)
            return t[n][m]
        else:
            t[n][m] = 1 + min(self.recursion_memo2(word1, word2, n, m-1, t), self.recursion_memo2(word1, word2, n-1, m, t), self.recursion_memo2(word1, word2, n-1, m-1, t))
            return t[n][m]
            

    def minDistance(self, word1: str, word2: str) -> int:
        # return self.recursion(word1, word2, 0, 0)
        t = [[-1 for _ in range(len(word2) + 1)] for __ in range(len(word1) + 1)]
        # return self.recursion_memo(word1, word2, 0, 0, t)
        return self.recursion_memo2(word1, word2, len(word1), len(word2), t)

sol = Solution()
print(sol.minDistance(word1, word2))

