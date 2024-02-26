# https://workat.tech/problem-solving/practice/matrix-search
# Given a matrix, check if the matrix contains a given key.

# The matrix has the following properties:

# Integer in each row is arranged in non-decreasing order from left to right.
# The first integer in every row is greater than the last integer of the previous row.
# Expected Time Complexity: O(log (n*m))

from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], key: int) -> bool:
        l, r = 0, len(matrix) - 1
        row = 0
        while(l <= r):
            mid = (l+r)//2
            if matrix[mid][0] == key:
                return True
            if matrix[mid][0] < key:
                l = mid + 1
                row = mid
            else:
                r = mid - 1
        l, r = 0, len(matrix[0]) - 1
        while(l<=r):
            mid = (l+r) // 2
            if matrix[row][mid] == key:
                return True
            if matrix[row][mid] < key:
                l = mid + 1
            else:
                r = mid - 1
        return False

sol = Solution()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [11, 12, 13],
    [14, 15, 16],
    [17, 18, 19],
]
key = 9
print(sol.searchMatrix(matrix, key))