# Longest Palindromic Substring (LPS)
# Given a string, return the longest palindromic substring (LPS) in it.

# Note: There can be multiple palindromic substrings with the max length. In case of conflict, return the substring that has the smallest starting index.

# Examples
# str: "abcdcab"
# LPS: "cdc"
# str: "abcdcba"
# LPS: "abcdcba"
# str: "abcd"
# LPS: "a"
# str: "abaadcd"
# LPS: "aba"


class Solution:
	def lps(self, s: str) -> str:
		# add your logic here
		s1 = s
		s2 = s[::-1]
		n = len(s1)
		t = [[-1 for _ in range(n+1)] for __ in range(n+1)]
		ans = -1
		ans_string = ""
		t_i = 0
		t_j = 0
		for i in range(n+1):
			for j in range(n+1):
				if i == 0 or j == 0:
					t[i][j] = 0
				else:
					if s1[i-1] == s2[j-1]:
						t[i][j] = 1 + t[i-1][j-1]
						if t[i][j] > ans:
							ans = t[i][j]
							t_i = i
							t_j = j
					else:
						t[i][j] = 0
		while t_i > 0 and t_j > 0 and t[t_i] != 0:
			if s1[t_i-1] == s2[t_j-1]:
				ans_string += s1[t_i-1]
			t_i -= 1
			t_j -= 1
		return ans_string[::-1]


