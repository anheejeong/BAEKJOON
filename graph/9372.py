import sys
from collections import deque

# 모든 나라가 연결되어있으므로 N+1 바로 출력해도 됨
# bfs 연습 코드

TestCase = int(sys.stdin.readline())

direction = dict()

# Time Fail
# def bfs(graph, root):
#     queue = deque([root])
#     visited = []
#     count = 0
#
#     while queue:
#         node = queue.popleft()
#         if node not in visited:
#             visited.append(node)
#             count += 1
#         for i in graph[node]:
#             if i not in visited:
#                 queue.append(i)
#
#     return count-1

def bfs(graph, root, visited):
    queue = deque([root])
    visited[root] = 1
    count = 0

    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = 1
                count += 1
                queue.append(i)

    return count

for _ in range(TestCase):
    National, Flight = map(int, sys.stdin.readline().split())
    for i in range(National):
        direction[i+1] = []
    for _ in range(Flight):
        n1, n2 = map(int, sys.stdin.readline().split())
        direction[n1].append(n2)
        direction[n2].append(n1)
    visited = [0 for _ in range(National + 1)]
    print(bfs(direction, 1, visited))
    direction.clear()
