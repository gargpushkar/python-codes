# Rat In A Maze
# You are given a maze in the form of a matrix of size n * m. Each cell is either clear or blocked denoted by 1 and 0 respectively.
# A rat sits at the top-left cell and there exists a block of cheese at the bottom-right cell. Both these cells are guaranteed to be clear.
# You need to find if the rat can get the cheese if it can move only in one of the two directions - down and right. It can’t move to blocked cells.

from typing import List
from collections import deque

maze = [
    [1, 1, 0, 1],
    [1, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 1]
]

def canGetCheese(self, maze: List[List[int]]) -> bool:
    directions = [(0, 1), (1, 0)]
    n = len(maze)
    m = len(maze[0])
    start_x = 0
    start_y = 0
    visited = [[0 for _ in range(m)] for __ in range(n)]
    q = deque()
    q.append([start_x, start_y])
    visited[start_x][start_y] = 1

    def is_safe(x, y, n, m, maze, visited):
        if x >= 0 and y >= 0 and x < n and y < m and not visited[x][y] and maze[x][y]:
            return True
        return False

    while q:
        q_len = len(q)
        for _ in range(q_len):
            x, y = q.popleft()
            if x == n-1 and y == m-1:
                return True
            for i, j in directions:
                if is_safe(x+i, y+j, n, m, maze, visited):
                    q.append([x+i, y+j])
                    visited[x+i][y+j] = 1
    return False

print(canGetCheese("self", maze))