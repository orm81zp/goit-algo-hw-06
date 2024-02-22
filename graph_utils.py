import networkx as nx
import matplotlib.pyplot as plt

default_title = "Граф ранспортної мережі між містами України"

def print_degrees(data, use_round=True):
    i = 1
    for city, degree in data:
        end = "" if i == len(data) else ", "
        if use_round:
            print(f"{city}: {degree:.2f}", end=end)
        else:
            print(f"{city}: {degree}", end=end)
        i += 1
    print()

def print_stat(Graph):
    num_nodes = Graph.number_of_nodes()
    num_edges = Graph.number_of_edges()
    is_connected = nx.is_connected(Graph)

    print("\nОсновні характеристики:")
    print("-" * 28)
    print(f"Кількість вузлів: {num_nodes}")
    print(f"Кількість ребер: {num_edges}")
    print("Ступінь вершин:")
    print_degrees(Graph.degree, False)
    print(f"Граф {"є сполученим" if is_connected else "не є сполученим"}")

    print("\nМетрик центральності вузлів:")
    print("-" * 28)

    degree_centrality = nx.degree_centrality(Graph)
    closeness_centrality = nx.closeness_centrality(Graph)
    betweenness_centrality = nx.betweenness_centrality(Graph)

    print("Ступінь центральності:")
    print_degrees(degree_centrality.items())
    print("Ступінь близькості:")
    print_degrees(closeness_centrality.items())
    print("Ступінь посередництва:")
    print_degrees(betweenness_centrality.items())

def draw_weight_graph(graph, show_stat=True, title=default_title):
    # Створення графа
    Graph = nx.Graph()

    # Додавання міст і відстань між ними
    for city, neighbors in graph.items():
        for neighbor_city, weight in neighbors.items():
            Graph.add_edge(city, neighbor_city, weight=weight)

    # Візуалізація графа
    pos = nx.spring_layout(Graph, seed=42)
    nx.draw(
        Graph,
        pos,
        with_labels=True,
        node_size=800,
        node_color="skyblue",
        font_size=12,
        width=1,
    )

    labels = nx.get_edge_attributes(Graph, "weight")
    nx.draw_networkx_edge_labels(Graph, pos, edge_labels=labels)

    if show_stat:
        print_stat(Graph)

    plt.title(title)
    plt.show()

def draw_graph(graph, show_stat=True, title=default_title):
    # Створення графа
    Graph = nx.Graph()

    # Додавання міст і відстань між ними
    for city, neighbors in graph.items():
        for neighbor_city in neighbors:
            Graph.add_edge(city, neighbor_city)

    # Візуалізація графа
    pos = nx.spring_layout(Graph, seed=42)
    nx.draw(
        Graph,
        pos,
        with_labels=True,
        node_size=800,
        node_color="skyblue",
        font_size=12,
        width=1,
    )

    if show_stat:
        print_stat(Graph)

    plt.title(title)
    plt.show()
