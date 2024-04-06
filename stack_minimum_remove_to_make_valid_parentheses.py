# Minimum Remove to Make Valid Parentheses
# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
 

# Example 1:
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

# Example 2:
# Input: s = "a)b(c)d"
# Output: "ab(c)d"

# Example 3:
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.

from collections import deque

s = "lee(t(c)o)de)"
# s = "))(("
# s = "a)b(c)d"
# s = "())()((("

stack1 = deque()
stack2 = deque()
for itr, i in enumerate(s):
    if i == "(":
        stack1.append([i, itr])
    if i == ")":
        if stack1 and stack1[-1][0] == "(":
            stack1.pop()
        else:
            stack2.append([i, itr])

ans = ""
for itr, i in enumerate(s):
    if stack2 and itr == stack2[0][1]:
        stack2.popleft()
        continue
    if stack1 and itr == stack1[0][1]:
        stack1.popleft()
        continue
    ans += i
print(ans)
