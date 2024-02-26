# Given an array A and an integer target, find the indices of the two numbers in the array whose sum is equal to the given target.

# Note: The problem has exactly one solution. Do not use the same element twice.
# A: [1, 3, 3, 4]
# target: 5
# Answer: [0, 3]
from typing import List

class Solution:
    def twoSum(self, A: List[int], target: int) -> List[int]:
        # for i in range(0, len(A)):
        #     second_element = target - A[i]
        #     for j in range(i+1, len(A)):
        #         if A[j] == second_element:
        #             return [i, j]
        hash_map = {}
        for i in range(0, len(A)):
            hash_map[A[i]] = i
        for i in range(0, len(A)):
            second_element = target - A[i]
            if hash_map.get(second_element, None):
                return [i, hash_map.get(second_element)]

            
            
s = Solution()
A = [8, 2, 10, 4, 1, 3]
target = 9
print(s.twoSum(A, target))

