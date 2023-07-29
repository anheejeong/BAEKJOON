# BFS : Breadth first search => queue 사용
from collections import deque

# Dict()
graph_list = { # No-Direction Graph
    1: set([2, 5, 9]),
    2: set([1, 3]),
    3: set([2, 4]),
    4: set([3]),
    5: set([1, 6, 8]),
    6: set([5, 7]),
    7: set([6]),
    8: set([5]),
    9: set([1, 10]),
    10: set([9])
}

graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}
root_node = 1

def BFS_QUEUE(graph, root):
    queue = deque([root])
    visited = []

    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            visited.append(current_node)
            #queue += graph[current_node] - set(visited) #set일때
            for i in graph[current_node]:
                if i not in visited:
                    queue.append(i)
    return visited

print(BFS_QUEUE(graph, root_node))