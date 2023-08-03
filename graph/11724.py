import sys

N, M = map(int, sys.stdin.readline().split())
graph = dict()
for i in range(N):
    graph[i+1] = []

for _ in range(M):
    node1, node2 = map(int, sys.stdin.readline().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

visited = []
count = 0

def dfs(graph, root_node, visited):
    stack = [root_node]

    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            visited.append(current_node)
        # < time out >
        # if current_node in graph:
        #     for i in graph[current_node]:
        #         if i not in visited:
        #             stack.append(i)
            for i in graph[current_node]:
                stack.append(i)

for i in range(1, N+1):
    if i not in visited:
        count += 1
        dfs(graph, i, visited)

print(count)


