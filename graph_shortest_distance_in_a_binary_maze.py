# https://www.geeksforgeeks.org/problems/shortest-path-in-a-binary-maze-1655453161/1
# Shortest Distance in a Binary Maze
# Given a n * m matrix grid where each element can either be 0 or 1. You need to find the shortest distance between a given source cell to a destination cell. The path can only be created out of a cell if its value is 1. 

# If the path is not possible between source cell and destination cell, then return -1.

# Note : You can move into an adjacent cell if that adjacent cell is filled with element 1. Two cells are adjacent if they share a side. In other words, you can move in one of the four directions, Up, Down, Left and Right. The source and destination cell are based on the zero based indexing. The destination cell should be 1.
# Input:
# grid[][] = {{1, 1, 1, 1},
#             {1, 1, 0, 1},
#             {1, 1, 1, 1},
#             {1, 1, 0, 0},
#             {1, 0, 0, 1}}
# source = {0, 1}
# destination = {2, 2}
# Output:
# 3

from collections import deque

grid = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0],
    [1, 0, 1, 0, 1]
]
source = [0, 0]
destination = [3, 4]

# grid = [
#     [1, 1, 1, 1],
#     [1, 1, 0, 1],
#     [1, 1, 1 ,1],
#     [1, 1, 0, 0],
#     [1, 0, 0, 1]
# ]
# source = [0, 1]
# destination = [2, 2]

n = len(grid)
m = len(grid[0])

visited = []
for _ in range(n):
    visited.append([0]*m)


queue = deque()
s_x = source[0]
s_y = source[1]
d_x = destination[0]
d_y = destination[1]

directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

ans = -1
if grid[s_x][s_y] == 0 or grid[d_x][d_y] == 0:
    ans = -1        # ans
else:
    queue.append([s_x, s_y])
    visited[s_x][s_y] = 1
    distance = 0
    while queue:
        q_length = len(queue)
        for _ in range(q_length):
            cell = queue.popleft()
            cell_x = cell[0]
            cell_y = cell[1]
            if cell_x == d_x and cell_y == d_y:
                print(distance)       # ans
                ans = distance        # ans
                break
            else:
                for dx, dy in directions:
                    if cell_x + dx >=0 and cell_y + dy >= 0  and cell_x + dx < n and cell_y + dy < m and not visited[cell_x + dx][cell_y + dy] and grid[cell_x + dx][cell_y + dy]:
                        visited[cell_x + dx][cell_y + dy] = 1
                        queue.append([cell_x + dx, cell_y + dy])

        distance += 1

print(ans)       # ans