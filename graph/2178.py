import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maze =[[0 for _ in range(M)] for _ in range (N)]

for i in range(N):
    read = sys.stdin.readline().strip()
    maze[i] = list(map(int, read))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def check(x, y):
    if 0<=x<N and 0<=y<M:
        return True
    return False

def bfs(a, b):
    if maze[a][b] == 1:
        queue = deque([[a, b]])
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if check(nx, ny):
                    if maze[nx][ny] == 1:
                        maze[nx][ny] += maze[x][y]
                        queue.append([nx, ny])


bfs(0, 0)
print(maze[N-1][M-1])