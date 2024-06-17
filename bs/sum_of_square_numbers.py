# Sum of Square Numbers
# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

# Example 1:
# Input: c = 5
# Output: true
# Explanation: 1 * 1 + 2 * 2 = 5

# Example 2:
# Input: c = 3
# Output: false

import math

c = 193

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        def binary_search(arr, element):
            left = 0
            right = len(arr) - 1
            while left <= right:
                mid = (left + right)//2
                if arr[mid] == element:
                    return True
                if arr[mid] > element:
                    right = mid - 1
                else:
                    left = mid + 1
            return False


        arr = [i*i for i in range(int(math.sqrt(c))+1)]
        for i in arr:
            if binary_search(arr, c - i):
                return True
        return False

# 2p approach
def solve():
    arr = [i for i in range(int(math.sqrt(c)))]

    i = 0
    j = len(arr) - 1

    while i<=j:
        if arr[i]*arr[i] + arr[j]*arr[j] == c:
            print(True)
            break
        elif arr[i]*arr[i] + arr[j]*arr[j] > c:
            j-=1
        else:
            i+=1
        