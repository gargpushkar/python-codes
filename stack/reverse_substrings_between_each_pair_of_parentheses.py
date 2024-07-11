# You are given a string s that consists of lower case English letters and brackets.
# Reverse the strings in each pair of matching parentheses, starting from the innermost one.
# Your result should not contain any brackets.

# Example 1:
# Input: s = "(abcd)"
# Output: "dcba"

# Example 2:
# Input: s = "(u(love)i)"
# Output: "iloveu"
# Explanation: The substring "love" is reversed first, then the whole string is reversed.

# Example 3:
# Input: s = "(ed(et(oc))el)"
# Output: "leetcode"
# Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        n = len(s)
        ans = list(s)
        for i in range(n):
            if s[i] == '(':
                stack.append(i+1)
            elif s[i] == ')':
                st_indx = stack.pop()
                ans[st_indx:i] = list(reversed(ans[st_indx:i]))
        final_ans = ""
        for i in range(n):
            if ans[i] in ['(', ')']:
                continue
            final_ans += ans[i]
        return final_ans
    
s ="(ed(et(oc))el)"
sol = Solution()
print(sol.reverseParentheses(s))
