# https://workat.tech/problem-solving/practice/valid-path
# Valid Path
# You have an n*m matrix with start position at (0, 0) and end position at (n, m).

# There are c circles with centers inside the matrix, each with radius r. You are given the center co-ordinates (x, y) of each of those circles.

# Note: You can move from any point to any of its 8 adjecent neighbours.

# Find if there is a way to travel from start to end without touching any of these circles.

# n: 5
# m: 4
# r: 1
# circles(x, y): [(0, 2), (2, 3), (3, 0), (4, 1)]
# Answer: True
import math
from collections import deque

n = 5
m = 4
r = 1
circles = [(0, 2), (2, 3), (3, 0), (4, 1)]
# r = 1
# circles = [(0, 2), (2, 3), (3, 0), (4, 1)]
# X = [0, 2, 3, 4]
# Y = [2, 3, 0, 1]
# k = 4
# circles = [(0, 1)]

matrix = []
visited = []
for _ in range(n):
    matrix.append([1]*(m))
    visited.append([0]*m)

def print_matrix(matrix):
    for i in matrix:
        print(i)

# print_matrix(matrix)

dx = [0, 0, -1, -1, -1, 1, 1, 1]
dy = [-1, 1, -1, 0, 1, -1, 0, 1]
print()

# print_matrix(matrix1)
def is_safe(i, j, n, m, visited, matrix):
    if i < 0 or j < 0 or i >= n or j >= m or visited[i][j] or matrix[i][j] == 0:
        return False
    return True

def distance(x1, x2, y1, y2, r):
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    dx *= dx
    dy *= dy
    if math.sqrt(dx + dy) <= r:
        return 0
    return 1

for i in range(n):
    for j in range(m):
        for x, y in circles:
            # print(x, y, i, j)
            if not distance(x, i, y, j, r):
                matrix[i][j] = distance(x, i, y, j, r)


print_matrix(matrix)

print()
queue = deque()
if is_safe(0, 0, n, m, visited, matrix):
    queue.append([0, 0])

while queue:
    point = queue.popleft()
    x, y = point[0], point[1]
    visited[x][y] = 1
    for i, j in zip(dx, dy):
        if is_safe(x+i, y+j, n, m, visited, matrix):
            queue.append([x+i, y+j])
            visited[x+i][y+j] = 1
        

print(visited[n-1][m-1])