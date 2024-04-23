# Minimum Length of String After Deleting Similar Ends
# Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

# Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
# Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
# The prefix and the suffix should not intersect at any index.
# The characters from the prefix and suffix must be the same.
# Delete both the prefix and the suffix.
# Return the minimum length of s after performing the above operation any number of times (possibly zero times).

 

# Example 1:
# Input: s = "ca"
# Output: 2
# Explanation: You can't remove any characters, so the string stays as is.

# Example 2:
# Input: s = "cabaabac"
# Output: 0
# Explanation: An optimal sequence of operations is:
# - Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
# - Take prefix = "a" and suffix = "a" and remove them, s = "baab".
# - Take prefix = "b" and suffix = "b" and remove them, s = "aa".
# - Take prefix = "a" and suffix = "a" and remove them, s = "".

# Example 3:
# Input: s = "aabccabba"
# Output: 3
# Explanation: An optimal sequence of operations is:
# - Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
# - Take prefix = "b" and suffix = "bb" and remove them, s = "cca".

# s = "bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"
# s = "abbbbbbbbbbbbbbbbbbba"
# s = "abccba"


# WORKING BUT UGLY APPROACH WRITTEN BY ME
s = "a"
def minimumLength(s: str) -> int:
    n = len(s)
    i = 0
    j = n-1
    while i<j:
        n = len(s)
        if n == 0 or n == 1:
            return n
        i = 0
        j = n-1
        if s[i] != s[j]:
            return len(s)
        elem = s[i]
        while s[i] == elem:
            i+=1
            if i == n:
                return 0
        while elem == s[j]:
            j-=1
        j+=1
        s = s[i:j]
    return len(s)

print(minimumLength(s))
        


# BETTER APPROACH BY READING LEETCODE EDITORIAL
s = "a"
i = 0
j = len(s) - 1
while i < j and s[i] == s[j]:
    char = s[i]
    while i<=j and s[i] == char:
        i+=1
    while j > i and s[j] == char:
        j-=1

print(j-i+1)
