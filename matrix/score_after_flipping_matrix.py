# Score After Flipping Matrix

# You are given an m x n binary matrix grid.
# A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).
# Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.
# Return the highest possible score after making any number of moves (including zero moves).
 
# Example 1:
# Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# Output: 39
# Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

# Example 2:
# Input: grid = [[0]]
# Output: 1

grid = [
    [0, 1, 1],
    [1, 1, 1],
    [0, 1, 0]
]

n = len(grid)
m = len(grid[0])

def flip_col(grid, indx, n):
    for i in range(n):
        grid[i][indx] = 0 if grid[i][indx] else 1

def flip_row(grid, indx, n):
    for i in range(n):
        grid[indx][i] = 0 if grid[indx][i] else 1


for i in range(n):
    if not grid[i][0]:
        flip_row(grid, i, m)

for j in range(m):
    no_0 = 0
    no_1 = 0
    for i in range(n):
        if not grid[i][j]:
            no_0 += 1
        else:
            no_1 += 1
    if no_0 > no_1:
        flip_col(grid, j, n)


total = 0
for i in grid:
    total += int("".join(map(str, i)), 2)

print(total)