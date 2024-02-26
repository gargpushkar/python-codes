# https://workat.tech/problem-solving/practice/k-substring-vowels
# Given a string s and a number k, find the number of vowels in every substring of size k.
from typing import List

class Solution:
	def get_vowel_count(self, s) -> int:
		count = 0
		for i in s:
			if i in ['a', 'e', 'i', 'o', 'u']:
				count += 1
		return count
	
	def kSubstringVowels(self, s: str, k: int) -> List[int]:
		# add your logic here
		k_subtring = []
		k_subtring.append(self.get_vowel_count(s[:k]))
		i=k
		while(i<len(s)):
			prev_vowel_count = k_subtring[i-k]
			if prev_vowel_count:
				if s[i-k] in ['a', 'e', 'i', 'o', 'u']:
					prev_vowel_count -= 1
			if s[i] in ['a', 'e', 'i', 'o', 'u']:
				prev_vowel_count += 1
			i+=1
			k_subtring.append(prev_vowel_count)
		return k_subtring

sol = Solution()
print(sol.kSubstringVowels("substring", 2))