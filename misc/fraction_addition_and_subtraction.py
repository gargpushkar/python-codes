# Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.

# The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.

 

# Example 1:

# Input: expression = "-1/2+1/2"
# Output: "0/1"
# Example 2:

# Input: expression = "-1/2+1/2+1/3"
# Output: "1/3"
# Example 3:

# Input: expression = "1/3-1/2"
# Output: "-1/6"


from fractions import Fraction
class Solution:
    def fractionAddition(self, expression: str) -> str:
        arr = []
        i = 0
        n = len(expression)
        queue = []
        while i < n:
            if expression[i] == "+" or expression[i] == "-":
                queue.append(expression[i])
                i+=1
            while i < n and expression[i] not in ["+", "-"]:
                queue.append(expression[i])
                i+=1
            num = ""
            queue = queue[::-1]
            while queue:
                num += queue.pop()
            numerator, denominator = map(int, num.split("/"))
            arr.append(numerator/denominator)
        ans = str(Fraction(sum(arr)).limit_denominator())
        if "/" not in ans:
            ans += "/1"
        return ans
