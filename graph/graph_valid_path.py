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

n = 10
m = 10
r = 5
circles = [(5, 5)]
# n = 5
# m = 4
# r = 1
# circles = [(0, 2), (2, 3), (3, 0), (4, 1)]
# circles = [(0, 1)]

matrix = []
visited = []
for _ in range(n):
    matrix.append([1]*(m))
    visited.append([0]*m)

def print_matrix(matrix):
    for i in matrix:
        print(i)

print_matrix(matrix)

dx = [0, 0, -1, -1, -1, 1, 1, 1]
dy = [-1, 1, -1, 0, 1, -1, 0, 1]
print()
for x, y in circles:
    for i in range(0, r+1):
        if x+i >= 0 and x+i < n and y < m:
            matrix[x+i][y] = 0
        if x-i >= 0 and x-i < n and y < m:
            matrix[x-i][y] = 0
        if y+i >= 0 and y+i < m and x < n:
            matrix[x][y+i] = 0
        if y-i >= 0 and y-i < m and x < n:
            matrix[x][y-i] = 0

print_matrix(matrix)

def is_safe(i, j, n, m, visited, matrix):
    if i < 0 or j < 0 or i >= n or j >= m or visited[i][j] or matrix[i][j] == 0:
        return False
    return True

def dfs(x, y, n, m, dx, dy, visited, matrix):
    visited[x][y] = 1
    for i, j in zip(dx, dy):
        if is_safe(x+i, y+j, n, m, visited, matrix):
            dfs(x+i, y+j, n, m, dx, dy, visited, matrix)

if is_safe(0, 0, n, m, visited, matrix):
    dfs(0, 0, n, m, dx, dy, visited, matrix)
print()
print_matrix(visited)
print(visited[n-1][m-1])
