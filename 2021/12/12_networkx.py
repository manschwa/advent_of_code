import networkx as nx

filename = "12.sample"
with open(filename) as file:
    lines = file.read().splitlines()

WAYS = nx.MultiGraph()
for line in lines:
    key, value = line.split('-')
    WAYS.add_edge(key, value)

print(WAYS)
for path in nx.all_simple_paths(WAYS, ('start'), ('end')):
    print(path)
