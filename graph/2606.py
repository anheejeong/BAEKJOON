import sys
from collections import deque

comp = int(sys.stdin.readline())

# create dictionary graph
graph = dict()
for i in range(0, comp+1):
    graph[i] = []

edge = int(sys.stdin.readline())
for _ in range(edge):
    node1, node2 = map(int, sys.stdin.readline().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

def bfs(graph_list, root):
    queue = deque([root])
    visited = []

    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            visited.append(current_node)
        if current_node in graph_list:
            for i in graph_list[current_node]:
                if i not in visited:
                    queue.append(i)

    return len(set(visited) - set([1]))

print(bfs(graph, 1))