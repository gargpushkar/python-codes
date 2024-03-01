# Knight's Journey On A Chessboard

# You have a chessboard of size n*n. A knight sits on the board at a position start(x, y). The knight wants to go to another cell end(x, y).

# Find the minimum number of moves required to go from the start position to the end position. If this is not possible, return -1.

from collections import deque
n = 2
start_x = 1
start_y = 1
end_x = 1
end_y = 1

start_x -= 1
start_y -= 1
end_x -= 1
end_y -= 1

directions = ((1, -2), (-1, -2), (1, 2), (-1, 2), (2, -1), (2, 1), (-2, -1), (-2, 1))

def is_safe(x, y, n, visited):
    if x >=0 and y >=0 and x < n and y < n and not visited[x][y]:
        return True
    return False

def min_moves():
    if start_x == end_x and start_y == end_y:
        return 0
    visited = [[0 for _ in range(n)] for __ in range(n)]
    q = deque([[start_x, start_y]])
    visited[start_x][start_y] = 1
    count = 0
    while q:
        count +=1
        q_length = len(q)
        for _ in range(q_length):
            x, y = q.popleft()
            for i, j in directions:
                if x+i == end_x and y+j == end_y:
                    return count
                else:
                    if is_safe(x+i, y+j, n, visited):
                        q.append([x+i, y+j])
                        visited[x+i][y+j] = 1

    return -1

print(min_moves())