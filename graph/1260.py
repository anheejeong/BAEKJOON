import sys
from collections import deque


node, edge, root_node = map(int, sys.stdin.readline().split())
graph = dict()

#양방향인점 고려
for i in range(edge):
    node1, node2 = map(int, sys.stdin.readline().split())
    if node1 in graph:
        graph[node1].insert(0, node2)
        if node2 in graph:
            graph[node2].insert(0, node1)
        else:
            graph[node2] = [node1]
    else:
        graph[node1] = [node2]
        if node2 in graph:
            graph[node2].insert(0, node1)
        else:
            graph[node2] = [node1]

def dfs(graph, root):
    stack = [root]
    visited = []

    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            visited.append(current_node)
        # 이 if문 안 쓰면 KeyError(dict에 key가 없다는 error)
        if current_node in graph:
            temp = list(set(graph[current_node]) - set(visited))
            temp.sort(reverse=True)
            stack += temp
    return visited

def bfs(graph, root):
    queue = deque([root])
    visited = []

    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            visited.append(current_node)
        if current_node in graph:
            temp = list(set(graph[current_node]) - set(visited))
            temp.sort()
            queue += temp
    return " ".join(str(i) for i in visited) # join => list를 문자열로 바꿈

print(*dfs(graph, root_node)) # '*' 붙여주면 list 괄호 없이 출력
print(bfs(graph, root_node))