# Longest Substring Without Repeat
# Given a string s, find the length of the longest substring without repeating characters.

# Example
# s: “workattech”
# Result: 6
# Explanation: Longest vaild substring is “workat”.
# s: “mississippi”
# Result: 3
# Explanation: Longest vaild substrings are “mis” and “sip”, both of length 3.

s =  "“mississippi”"

n = len(s)

hash_map = {}
i = 0
j = 0
ans = 0
while(j<n):
    if s[j] not in hash_map:
        hash_map[s[j]] = 0
    hash_map[s[j]] += 1
    if len(hash_map) == j - i + 1:
        ans = max(ans, j - i + 1)
        j+=1
    elif len(hash_map) < j-i+1:
        while(len(hash_map) < j-i+1):
            hash_map[s[i]] -= 1
            if not hash_map[s[i]]:
                hash_map.pop(s[i])
            i+=1
        j+=1

print(ans)