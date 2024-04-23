# Permutation in String
# https://leetcode.com/problems/permutation-in-string/

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false


s1 = "ab"
s2 = "eidbaooo"
# s2 = "eidboaoo"
s1 = "adc"
s2 = "dcda"
# s2 = "eidboaoo"

n1 = len(s1)
n2 = len(s2)

hash_map = {}
for i in s1:
    if i not in hash_map:
        hash_map[i] = 0
    hash_map[i] += 1

count = len(hash_map)

i = 0
j = 0
hash_map2 = {}

print(hash_map)
while(j<n2):
    if s2[j] not in hash_map2:
        hash_map2[s2[j]] = 0
    hash_map2[s2[j]] += 1
    print(i, j, hash_map2)
    if sum(hash_map2.values()) < n1:
        j += 1
    elif sum(hash_map2.values()) == n1:
        ans = True
        for key in hash_map:
            if hash_map.get(key) != hash_map2.get(key):
                ans = False
        if ans:
            # return ans
            break
        hash_map2[s2[i]] -= 1
        if not hash_map2[s2[i]]:
            hash_map2.pop(s2[i])
        i+=1
        j+=1

        
print(ans)