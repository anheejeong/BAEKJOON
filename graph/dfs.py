# DFS : depth first search => Stack 사용

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
root_node = 1

def DFS_STACK(graph, root):
    stack = [root]
    visited = []

    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            visited.append(current_node)
            stack += graph[current_node] - set(visited) #set은 순서 x
    return visited

def dfs_stack(adjacent_graph, start_node):
    stack = [start_node]
    visited = []
    while stack:
        current_node = stack.pop()
        visited.append(current_node)
        for adjacent_node in adjacent_graph[current_node]:
            if adjacent_node not in visited:
                stack.append(adjacent_node)
    return visited

print(DFS_STACK(graph_list, root_node))
print(dfs_stack(graph_list, root_node))
