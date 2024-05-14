# https://leetcode.com/problems/map-of-highest-peak/description/
# Map of Highest Peak

# You are given an integer matrix isWater of size m x n that represents a map of land and water cells.
# If isWater[i][j] == 0, cell (i, j) is a land cell.
# If isWater[i][j] == 1, cell (i, j) is a water cell.
# You must assign each cell a height in a way that follows these rules:

# The height of each cell must be non-negative.
# If the cell is a water cell, its height must be 0.
# Any two adjacent cells must have an absolute height difference of at most 1. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).
# Find an assignment of heights such that the maximum height in the matrix is maximized.
# Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. If there are multiple solutions, return any of them.


# Example 1:
# Input: isWater = [[0,1],[0,0]]
# Output: [[1,0],[2,1]]
# Explanation: The image shows the assigned heights of each cell.
# The blue cell is the water cell, and the green cells are the land cells.

# Example 2:
# Input: isWater = [[0,0,1],[1,0,0],[0,0,0]]
# Output: [[1,1,0],[0,1,1],[1,2,2]]
# Explanation: A height of 2 is the maximum possible height of any assignment.
# Any height assignment that has a maximum height of 2 while still meeting the rules will also be accepted.

from collections import deque

isWater = [[0,0,1],[1,0,0],[0,0,0]]

n = len(isWater)
m = len(isWater[0])

ans = []

directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
q = deque()

for i in range(n):
    temp = []
    for j in range(m):
        if isWater[i][j]:
            q.append([(i, j), 0])
        temp.append(0)
    ans.append(temp[::])


def is_valid(x, y):
    if x < 0 or y < 0 or x >= n or y >= m or ans[x][y] or isWater[x][y]:
        return False
    return True

while q:
    current_cell, height = q.popleft()
    x, y = current_cell[0], current_cell[1]
    for dx, dy in directions:
        if is_valid(x+dx, y+dy):
            ans[x+dx][y+dy] = height+1
            q.append([(x+dx, y+dy), height+1])



# print(isWater)
print(ans)