import networkx as nx
import matplotlib.pyplot as plt


def print_degrees(data):
    i = 1
    for city, degree in data.items():
        end = "" if i == len(data) else ", "
        print(f"{city}: {degree:.2f}", end=end)
        i += 1
    print()

def print_nodes_degree(data):
    i = 1
    for city, degree in data:
        end = "" if i == len(data) else ", "
        print(f"{city}: {degree}", end=end)
        i += 1
    print()


def draw_graph(graph: dict):
    # Створення графа
    G = nx.Graph()

    # Додавання міст і доріг
    for city, neighbors in graph.items():
        for neighbor_city, weight in neighbors.items():
            G.add_edge(city, neighbor_city, weight=weight)

    # Візуалізація графа
    pos = nx.spring_layout(G, seed=42)
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=800,
        node_color="skyblue",
        font_size=12,
        width=1,
    )
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    is_connected = nx.is_connected(G)

    print("\nОсновні характеристики:")
    print("-" * 28)
    print(f"Кількість вузлів: {num_nodes}")
    print(f"Кількість ребер: {num_edges}")
    print("Ступінь вершин:")
    print_nodes_degree(G.degree)
    print(f"Граф {"є сполученим" if is_connected else "не є сполученим"}")

    print("\nМетрик центральності вузлів:")
    print("-" * 28)

    degree_centrality = nx.degree_centrality(G)
    closeness_centrality = nx.closeness_centrality(G)
    betweenness_centrality = nx.betweenness_centrality(G)

    print("Ступінь центральності:")
    print_degrees(degree_centrality)
    print("Ступінь близькості:")
    print_degrees(closeness_centrality)
    print("Ступінь посередництва:")
    print_degrees(betweenness_centrality)

    plt.title("Граф ранспортної мережі між містами України")
    plt.show()


graph = {
    "Kyiv": {"Zhytomyr": 140, "Uman'": 215},
    "Zhytomyr": {"Vinnytsia": 155, "Lutks": 265},
    "Vinnytsia": {"Ternopil": 235, "Uman'": 160},
    "Lviv": {"Lutks": 155, "Ternopil": 127},
}

draw_graph(graph)
