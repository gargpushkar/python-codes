# https://workat.tech/problem-solving/practice/number-of-islands
# Number of Islands
# You are given a 2-D matrix surface of size n*m. Each cell of the surface is either 1 (land) or 0 (water).
# Find the number of islands on the surface.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. Assume all four edges of the surface are all surrounded by water.

# Example:
# surface: [
#  [1, 1, 0, 1]
#  [1, 0, 1, 1]
#  [0, 1, 0, 1]
# ]
# Num islands: 3

# n = 3
# m = 4
# surface = [
#     [1, 1, 0, 1],
#     [1, 0, 1, 1],
#     [0, 1, 0, 1]
# ]
n = 2
m = 2
surface = [
    [1, 1],
    [1, 1]
]


def dfs(i, j, n, m, dx, dy, visited, surface):
    visited[i][j] = 1
    for x, y in zip(dx, dy):
        if is_valid(i+x, j+y, n, m, visited, surface):
            dfs(i+x, j+y, n, m, dx, dy, visited, surface)

def is_valid(i, j, n, m, visited, surface):
    if i < 0 or j < 0 or i >= n or j >= m or visited[i][j] or surface[i][j] == 0:
        return 0
    return 1

def get_number_of_islands(n, m, surface):
    visited = []
    for _ in range(n):
        visited.append([0]*m)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    x, y = 0, 0
    no_of_islands = 0
    for i in range(n):
        for j in range(m):
            if is_valid(i, j, n, m, visited, surface):
                dfs(i, j, n, m, dx, dy, visited, surface)
                no_of_islands += 1
    return no_of_islands

print(get_number_of_islands(n, m, surface))