# https://leetcode.com/problems/path-with-maximum-gold/description/?envType=daily-question&envId=2024-05-14
# Path with Maximum Gold


# In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.
# Return the maximum amount of gold you can collect under the conditions:
# Every time you are located in a cell you will collect all the gold in that cell.
# From your position, you can walk one step to the left, right, up, or down.
# You can't visit the same cell more than once.
# Never visit a cell with 0 gold.
# You can start and stop collecting gold from any position in the grid that has some gold.
 
# Example 1:
# Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
# Output: 24
# Explanation:
# [[0,6,0],
#  [5,8,7],
#  [0,9,0]]
# Path to get the maximum gold, 9 -> 8 -> 7.

# Example 2:
# Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
# Output: 28
# Explanation:
# [[1,0,7],
#  [2,0,6],
#  [3,4,5],
#  [0,3,0],
#  [9,0,20]]
# Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.

grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]

n = len(grid)
m = len(grid[0])

visited = [[0 for _ in range(m)] for __ in range(n)]

max_gold = [0]

directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def is_valid(x, y):
    if x < 0 or y < 0 or x >=n or y >= m or visited[x][y] or not grid[x][y]:
        return False
    return True

def dfs(x, y, current_sum):
    visited[x][y] = 1
    current_sum += grid[x][y]
    for dx, dy in directions:
        if is_valid(x+dx, y+dy):
            dfs(x+dx, y+dy, current_sum)
    max_gold[0] = max(max_gold[0], current_sum)
    visited[x][y] = 0
    current_sum -= grid[x][y]

for i in range(n):
    for j in range(m):
        if is_valid(i, j):
            dfs(i, j, 0)

print(max_gold[0])
