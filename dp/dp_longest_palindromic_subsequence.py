# Longest Palindromic Subsequence
# Given a String, find the longest palindromic subsequence.

# NOTE: Subsequence of a given sequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the order of the remaining elements

# Example 1:
# Input:
# S = "bbabcbcab"
# Output: 7
# Explanation: Subsequence "babcbab" is the
# longest subsequence which is also a palindrome.

# LCS Variation

class Solution:
	def lps(self, s: str) -> str:
		# add your logic here
		s1 = s
		s2 = s[::-1]
		n = len(s1)
		t = [[-1 for _ in range(n+1)] for __ in range(n+1)]
		for i in range(n+1):
			for j in range(n+1):
				if i == 0 or j == 0:
					t[i][j] = 0
				else:
					if s1[i-1] == s2[j-1]:
						t[i][j] = 1 + t[i-1][j-1]
					else:
						t[i][j] = max(t[i-1][j], t[i][j-1])
		return t[n][n]


