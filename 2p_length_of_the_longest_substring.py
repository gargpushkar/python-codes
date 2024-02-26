# Length of the longest substring
# Given a string S, find the length of the longest substring without repeating characters.


# Example 1:

# Input:
# S = "geeksforgeeks"
# Output:
# 7
# Explanation:
# Longest substring is
# "eksforg".

s = "geeksforgeeks"
n=len(s)
i=0
j=0
st = set()
k = 1
ans = 0
while(j<n):
    while(j < n and s[j] not in st):
        st.add(s[j])
        j+=1
    ans = max(ans, len(st))
    while(j< n and s[j] in st):
        st.remove(s[i])
        i+=1
    
print(ans)

# 2nd approach

s = "mississippi"
n=len(s)
i=0
j=0
hash_map = {}
ans = 0
while(j<n):
    if s[j] not in hash_map:
        hash_map[s[j]] = 0
    hash_map[s[j]] += 1
    if  len(hash_map) == j-i+1:
        ans = max(ans, j-i+1)
        j+=1
    elif len(hash_map) < j-i+1:
        while(len(hash_map) < j-i+1):
            hash_map[s[i]] -= 1
            if not hash_map[s[i]]:
                hash_map.pop(s[i])
            i+=1
        j+=1
print(ans)
