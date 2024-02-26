# Row Column Zero
# Given a matrix, if any of the cells in the matrix is 0, set all the elements in its row and column to 0.

# 1 1 1        1 0 1
# 1 0 1   =>   0 0 0
# 1 1 1        1 0 1

# 0 1 2        0 0 0
# 3 4 5   =>   0 4 5
# 1 2 3        0 2 3

# 0 1 0        0 0 0
# 3 4 5   =>   0 4 0
# 1 2 3        0 2 0

# 0 1 0        0 0 0
# 3 0 5   =>   0 0 0
# 1 2 3        0 0 0

matrix = [
    [1, 1, 0],
    [1, 1, 5],
    [1, 2, 3]
]
# matrix = [
#     [1, 1, 1],
#     [1, 0, 1],
#     [1, 1, 1]
# ]

n = len(matrix)
m = len(matrix[0])
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            t_i = i
            while(t_i >= 0):
                if matrix[t_i][j] !=0:
                    matrix[t_i][j] = -1
                t_i-=1
            t_i = i
            while(t_i < n):
                if matrix[t_i][j] !=0:
                    matrix[t_i][j] = -1
                t_i+=1
            t_j = j
            while(t_j >= 0):
                if matrix[i][t_j] != 0:
                    matrix[i][t_j] = -1
                t_j -=1
            t_j = j
            while(t_j < m):
                if matrix[i][t_j] != 0:
                    matrix[i][t_j] = -1
                t_j +=1
            
for i in range(n):
    for j in range(m):
        if matrix[i][j] == -1:
            matrix[i][j] = 0

for i in matrix:
    print(i)