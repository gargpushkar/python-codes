# Word Search Board

# You are given a board of size n*m, containing an English alphabet in each cell. You are also given a word, find if the word exists on the board.

# The word can be constructed from letters of sequentially adjacent cells. Cells which have a common edge are considered adjacent. The same cell may not be used more than once.

# 2
# 3 4
# WORKAT
# A W O R
# T E R K
# T A K A
# 3 4
# ATTECH
# A W O R
# T E R K
# T E T A

board = [
    ["C","A","A"],
    ["A","A","A"],
    ["B","C","D"]
]
word = "AAB"

ans = [False]
n = len(board)
m = len(board[0])

visited = [[0 for _ in range(m)] for _ in range(n)]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

curr_indx = 0
output_array = []

def is_valid(i, j, curr_indx):
    if i < 0 or j < 0 or i >= n or j >= m or visited[i][j] or board[i][j] != word[curr_indx]:
        return False
    return True


def dfs(x, y, curr_indx, output_array):
    if curr_indx == len(word) - 1:
        ans[0] = True
        print(output_array)
        return 
    visited[x][y] = 1
    for dx, dy in directions:
        if is_valid(x+dx, y+dy, curr_indx+1):
            output_array.append(word[curr_indx+1])
            dfs(x+dx, y+dy, curr_indx+1, output_array)
            output_array.pop()
    visited[x][y] = 0


for i in range(n):
    for j in range(m):
        if is_valid(i, j, curr_indx):
            output_array.append(word[curr_indx])
            dfs(i, j, curr_indx, output_array)
            output_array.pop()

print(ans[0])