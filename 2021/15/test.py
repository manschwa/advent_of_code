import networkx as nx

G = nx.Graph()
for i in range():
    for j in range(5):
        G.add_node((i, j))

G.add_edge((0, 0),(0, 1), weight = 9)


print(G.number_of_nodes())
print(G.number_of_edges())
print(G.get_edge_data((0,0),(0,1)))
