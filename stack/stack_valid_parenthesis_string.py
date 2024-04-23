# Valid Parenthesis String

# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
# The following rules define a valid string:
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "(*)"
# Output: true

# Example 3:
# Input: s = "(*))"
# Output: true

from collections import deque

# s = "(()()*))(())"
s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
# s = "*)"
def solve():
    stack = deque()
    star_stack = deque()
    n = len(s)
    for i in range(n):
        if s[i] == "(":
            stack.append(i)
        elif s[i] == "*":
            star_stack.append(i)
        else:
            if stack:
                stack.pop()
            elif star_stack:
                star_stack.pop()
            else:
                return False
    if stack:
        while star_stack and stack and star_stack[-1] >= stack[-1]:
            stack.pop()
            star_stack.pop()
        if stack:
            return False
        else:
            return True
    else:
        return True
print(solve())

# Another approach Using recursion

# def is_valid(s, count, i, n):
#     if i == n:
#         return count == 0
    
#     if s[i] == "(":
#         return is_valid(s, count+1, i+1, n)
#     elif s[i] == ")":
#         if count > 0:
#             return is_valid(s, count-1, i+1, n)
#     else:
#         is_valid_flag = is_valid(s, count+1, i+1, n)
#         if count > 0:
#             is_valid_flag = is_valid_flag or is_valid(s, count-1, i+1, n)
#         is_valid_flag = is_valid_flag or is_valid(s, count, i+1, n)
#         return is_valid_flag

# print(is_valid(s, 0, 0, len(s)))
    

# Using DP
n = len(s)
t = [[-1 for i in range(n+1)] for __ in range(n+1)]
def is_valid_memo(s, count, i, n):
    if i == n:
        return count == 0
    if t[count][i] != -1:
        return t[count][i]
    if s[i] == "(":
        is_valid_flag = is_valid_memo(s, count+1, i+1, n)
        t[count][i] = is_valid_flag
        return t[count][i]
    elif s[i] == ")":
        if count > 0:
            is_valid_flag = is_valid_memo(s, count-1, i+1, n)
            t[count][i] = is_valid_flag
            return t[count][i]
        else:
            t[count][i] = False
        return t[count][i]
    else:
        is_valid_flag = is_valid_memo(s, count+1, i+1, n)
        if count > 0:
            is_valid_flag = is_valid_flag or is_valid_memo(s, count-1, i+1, n)
        is_valid_flag = is_valid_flag or is_valid_memo(s, count, i+1, n)
        t[count][i] = is_valid_flag
        return t[count][i]

print(is_valid_memo(s, 0, 0, len(s)))
