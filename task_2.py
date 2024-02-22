from constants import graph
from algorithms import dfs_recursive, bfs_iterative

start_city = "Kyiv"

print(f"Початок руху з міста {start_city}")
print("Пошук у глибину (DFS):")
dfs_recursive(graph, start_city)
print()
print("\nПошук у ширину (BFS):")
bfs_iterative(graph, start_city)
print()
