# Matrix Rotation
# Given a matrix, rotate the matrix 90 degrees clockwise.

# Examples
# Matrix:
# 1 2 3
# 4 5 6
# 7 8 9
# After rotation:
# 7 4 1
# 8 5 2
# 9 6 3
# Matrix:
# 1 2
# 3 4
# 5 6
# After rotation:
# 5 3 1
# 6 4 2

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix = [
    [5, 3, 1],
    [6, 4, 2]
]
matrix = [
    [1 , 2],
    [3 , 4],
    [5 , 6]
]
n = len(matrix)
m = len(matrix[0])
temp = []
for _ in range(m):
    temp.append([0]*n)


# for i in range(n):
#     for j in range(m):
#         temp[i][j] = matrix[m-j-1][i]
# print(temp)
    
for i in range(m):
    for j in range(n):
        temp[i][j] = matrix[n-j-1][i]

print(temp)