from constants import graph_with_weight
from graph_utils import draw_weight_graph, print_degrees
from algorithms import dijkstra

start_city = "Kyiv"

distances = dijkstra(graph_with_weight, start_city)
print(f"Початок руху з міста {start_city}")
print("Найкоротші шляхи між всіма вершинами графа:")
print_degrees(distances.items(), False)
draw_weight_graph(graph_with_weight, False)
