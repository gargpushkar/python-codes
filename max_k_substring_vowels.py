class Solution:
	
	def get_vowel_count(self, s: str) -> int:
		count = 0
		for i in s:
			if i in ['a', 'e', 'i', 'o', 'u']:
				count += 1
		return count
	
	def maxKSubstringVowels(self, s: str, k: int) -> int:
		# add your logic here
		max_vowel = self.get_vowel_count(s[:k])
		vowel = max_vowel
		i = k
		while(i < len(s)):
			print(s[i-k], s[i], max_vowel, vowel)
			if vowel:
				if s[i-k] in ['a', 'e', 'i', 'o', 'u']:
					vowel -= 1
			if s[i] in ['a', 'e', 'i', 'o', 'u']:
				vowel += 1
			max_vowel = max(max_vowel, vowel)
			i+=1
		return max_vowel


sol = Solution()
print(sol.maxKSubstringVowels("workaattech", 3))
