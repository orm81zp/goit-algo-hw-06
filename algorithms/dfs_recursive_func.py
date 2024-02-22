def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)

    print(vertex, end=" ")
    for neigbor in graph[vertex]:
        if neigbor not in visited:
            dfs_recursive(graph, neigbor, visited)


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

dfs_recursive(graph, "A")
