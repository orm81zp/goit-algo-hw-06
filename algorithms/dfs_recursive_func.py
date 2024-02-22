def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)

    print(f"=> {vertex}", end=" ")
    for neigbor in graph[vertex]:
        if neigbor not in visited:
            dfs_recursive(graph, neigbor, visited)

    return visited
