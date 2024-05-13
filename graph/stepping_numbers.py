# Stepping Numbers
# Given two numbers begin and end, find all the stepping numbers in the range [begin, end].

# A positive integer is called a stepping number if the adjacent digits have a difference of 1. All single-digit numbers are stepping numbers.

# 123, 121, 654, 5 are all stepping numbers. 124, 122, 46 are not stepping numbers.

# Example:
# begin: 8
# end: 15
# stepping numbers: [8, 9, 10, 12]

from collections import deque
from typing import List

begin = 10
end = 10

class Solution:
    def getSteppingNumbers(self, begin: int, end: int) -> List[int]:

        q = deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

        ans = []
        while q:
            num = q.popleft()
            if num > end:
                break
            if begin <= num <= end:
                ans.append(num)
            if num == 0:
                continue
            last_digit = num%10
            new_num1 = num*10 + last_digit - 1
            new_num2 = num*10 + last_digit + 1
            if last_digit == 0:
                q.append(new_num2)
            elif last_digit == 9:
                q.append(new_num1)
            else:
                q.append(new_num1)
                q.append(new_num2)
        

        return ans

sol = Solution()
print(sol.getSteppingNumbers(begin, end))