# Rotting Apples
# You are given an n * m grid where each position can contain one of the three values:

# Cell Value	Represents
# 0	Empty Cell
# 1	Fresh Apple
# 2	Rotten Apple
# Every day, all fresh apples which are adjacent to any rotten apple become rotten.

# Two cells are adjacent if they have a common edge, i.e., each cell can have upto four adjacent cells.

# Find the minimum number of days required for all the apples to be rotten. If this is not possible return -1.

# n = 3 
# m = 3
# grid = [
#     [2, 1, 0],
#     [1, 1, 0],
#     [0, 1, 1]
# ]
# ans = 4

from collections import deque

n = 3
m = 3
grid = [
    [2, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
ans = 4
no_of_ones = 0
queue = deque()
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            queue.append([i, j])
        if grid[i][j] == 1:
            no_of_ones+=1

if no_of_ones == 0:
    print(0)

days = 0
while queue:
    days+=1
    queue_length = len(queue)
    for _ in range(queue_length):
        i,j = queue.popleft()
        t_i = i+1
        t_j = j+0
        
        if t_i >=0 and t_i < n and t_j >=0 and t_j<m:
            if grid[t_i][t_j] == 1:
                grid[t_i][t_j] = 2
                no_of_ones-=1
                queue.append([t_i, t_j])

        t_i = i-1
        t_j = j+0
        if t_i >=0 and t_i < n and t_j >=0 and t_j<m:
            if grid[t_i][t_j] == 1:
                grid[t_i][t_j] = 2
                no_of_ones-=1
                queue.append([t_i, t_j])
        
        t_i = i+0
        t_j = j+1
        if t_i >=0 and t_i < n and t_j >=0 and t_j<m:
            if grid[t_i][t_j] == 1:
                grid[t_i][t_j] = 2
                no_of_ones-=1
                queue.append([t_i, t_j])
        
        t_i = i+0
        t_j = j-1
        if t_i >=0 and t_i < n and t_j >=0 and t_j<m:
            if grid[t_i][t_j] == 1:
                grid[t_i][t_j] = 2
                no_of_ones-=1
                queue.append([t_i, t_j])

print(days-1)
print(no_of_ones)



from collections import deque
from typing import List

class Solution:
	def getDaysToRot(self, grid: List[List[int]]) -> int:
		# add your logic here
		directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
		no_of_ones = 0
		queue = deque()
		n = len(grid)
		m = len(grid[0])
		for i in range(n):
			for j in range(m):
				if grid[i][j] == 2:
					queue.append([i, j])
				if grid[i][j] == 1:
					no_of_ones += 1
		days = -1
		while queue:
			days += 1
			queue_length = len(queue)
			for _ in range(queue_length):
				i, j = queue.popleft()
				for d in range(4):
					x, y = i + directions[d][0], j + directions[d][1]
					if x >= 0 and y >= 0 and x < n and y < m:
						if grid[x][y] == 1:
							grid[x][y] = 2
							queue.append([x, y])
							no_of_ones -= 1
		return -1 if no_of_ones else days
		


