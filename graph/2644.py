import sys

N = int(sys.stdin.readline())
p1, p2 = map(int, sys.stdin.readline().split())
line = int(sys.stdin.readline())

graph = dict()
for i in range(N):
    graph[i+1] = []

for _ in range(line):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visited = [False] * (N+1)
check = 0

def dfs(root_num, count):
    global check
    count += 1
    visited[root_num] = True

    if root_num == p2:
        check = count
        return

    for i in graph[root_num]:
        if not visited[i]:
            dfs(i, count)

dfs(p1, 0)

if check == 0:
    print(-1)
else:
    print(check-1)