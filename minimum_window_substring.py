# Minimum Window Substring
# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.

s = "ADOBECODEBANC"
t = "ABC"


n = len(s)
k = len(t)
hash_map = {}
for i in t:
    if i not in hash_map:
        hash_map[i] = 0
    hash_map[i] += 1
sz = len(hash_map)
i = 0
j = 0
ans = 999999
ans_string = ""
while(j<n):
    if s[j] in hash_map:
        hash_map[s[j]] -= 1
        if hash_map[s[j]] == 0:
            sz -= 1
    if sz > 0:
        j+=1
    elif sz == 0:
        while(sz == 0):
            if j-i+1 < ans:
                ans_string = s[i:j+1]
                ans = j-i+1
            if s[i] in hash_map:
                hash_map[s[i]] += 1
                if hash_map[s[i]] > 0:
                    sz+=1
            i+=1
        j+=1
print(ans)
print(ans_string)