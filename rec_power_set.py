# Given a string s of length n, find all the possible subsequences of the string s in lexicographically-sorted order.

# Example 1:
# Input : 
# s = "abc"
# Output: 
# a ab abc ac b bc c
# Explanation : 
# There are a total 7 number of subsequences possible 
# for the given string, and they are mentioned above 
# in lexicographically sorted order.

# Example 2:
# Input: 
# s = "aa"
# Output: 
# a a aa
# Explanation : 
# There are a total 3 number of subsequences possible 
# for the given string, and they are mentioned above 
# in lexicographically sorted order.

def power_set(s, ans, otpt):
    if len(s) == 0:
        if otpt:
            ans.append(otpt)
        return
    elem = s[0]
    s = s[1:]
    with_elem = otpt + elem
    without_elem = otpt
    power_set(s, ans, with_elem)
    power_set(s, ans, without_elem)
    return ans

s = "aa"
s = "abca"

ans = []
power_set(s, ans, "")
print(sorted(ans))