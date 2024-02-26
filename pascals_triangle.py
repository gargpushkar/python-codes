from typing import List

class Solution:
    def pascalTriangleRow(self, rowNo: int) -> List[int]:
        if rowNo == 1:
            return [1]
        level = [[1],[1, 1]]
        for i in range(2, rowNo+1):
            temp = []
            for j in range(0, i):
                if j == 0 or j+1 == i:
                    temp.append(level[i-1][0])
                else:
                    temp.append(level[i-1][j-1] + level[i-1][j])
            level.append(temp)
        return temp

    

		
solution = Solution()
n = 30
print(solution.pascalTriangleRow(n))

