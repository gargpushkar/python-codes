# Surrounded Regions

# Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Example 1:
# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Notice that an 'O' should not be flipped if:
# - It is on the border, or
# - It is adjacent to an 'O' that should not be flipped.
# The bottom 'O' is on the border, so it is not flipped.
# The other three 'O' form a surrounded region, so they are flipped.


# Example 2:
# Input: board = [["X"]]
# Output: [["X"]]

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# board = [["X"]]

n = len(board)
m = len(board[0])

visited = [[0 for i in range(m)] for j in range(n)]

def is_safe(i, j, n, m, visited, board):
    if i < 0 or j < 0 or i >= n or j >= m or visited[i][j] or board[i][j] == "X":
        return False
    return True

borders = []

for i in range(n):
    borders.append([i, 0])
    borders.append([i, m-1])

for j in range(m):
    borders.append([0, j])
    borders.append([n-1, j])

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(x, y, n, m, visited, board):
    visited[x][y] = 1
    board[x][y] = "S"
    for dx, dy in directions:
        if is_safe(x+dx, y+dy, n, m, visited, board):
            dfs(x+dx, y+dy, n, m, visited, board)

for x, y in borders:
    if is_safe(x, y, n, m, visited, board):
        dfs(x, y, n, m, visited, board)

for i in range(n):
    for j in range(m):
        if board[i][j] == "O":
            board[i][j] = "X"
        if board[i][j] == "S":
            board[i][j] = "O"

print(board)