import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maze =[[0 for _ in range(M)] for _ in range (N)]

for i in range(N):
    read = sys.stdin.readline().strip()
    maze[i] = list(map(int, read))

def bfs(graph, root_node):
    queue = deque([root_node])
    visited = []
    key = 0

    while queue:
        ary = []
        while queue:
            n = queue.popleft()
            if n not in visited:
                visited.append(n)
            if M > n[1]+1 and graph[n[0]][n[1]+1]==1:
                ary.append([n[0], n[1]+1])
            if N > n[0]+1 and graph[n[0]+1][n[1]]==1:
                ary.append([n[0]+1, n[1]])
            if n[1]-1 >= 0 and graph[n[0]][n[1]-1]==1:
                ary.append([n[0], n[1]-1])
            if n[0]-1 >= 0 and graph[n[0]-1][n[1]]==1:
                ary.append([n[0]-1, n[1]])

        # print(ary)

        key += 1
        for i in reversed(ary):
            if i[0] == N-1 and i[1] == M-1:
                return key
            elif i in visited:
                continue
            else:
                queue.append(i)
                ary.pop()
        # print(queue)

    return key
