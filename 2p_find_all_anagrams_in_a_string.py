# Find All Anagrams in a String
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pattern_dict = {}
        string_dict = {}
        for i in p:
            if i not in pattern_dict:
                pattern_dict[i] = 0
            pattern_dict[i] += 1
        i = 0
        j = 0
        ans = []
        n = len(s)
        k = len(p)
        while j < n:
            if s[j] not in string_dict:
                string_dict[s[j]] = 0
            string_dict[s[j]] += 1
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                flag = True
                for key in pattern_dict:
                    if key not in string_dict or string_dict[key] != pattern_dict[key]:
                        flag = False
                        break
                if flag:
                    ans.append(i)
                if string_dict[s[i]]:
                    string_dict[s[i]] -= 1
                i += 1
                j += 1
        return ans
