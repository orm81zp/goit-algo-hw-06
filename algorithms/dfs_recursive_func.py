def dfs_recursive(graph, vertex, visited=None, show_visited=False):
    if visited is None:
        visited = set()
    visited.add(vertex)

    if show_visited:
        print(vertex, end=" ")
    for neigbor in graph[vertex]:
        if neigbor not in visited:
            dfs_recursive(graph, neigbor, visited, show_visited)

    return visited
