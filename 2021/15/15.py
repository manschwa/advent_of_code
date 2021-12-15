from collections import Counter
import networkx as nx
import numpy as np

print("                                             ")
print("                      △                      ")
print("                    ◁ ☆ ▷                    ")
print("                  ,   *   ,                  ")
print("                  | ***** |                  ")
print("             ,    *********    ,             ")
print("             |  *************  |             ")
print("         ,   Advent of Code 2021   ,         ")
print("         | *********************** |         ")
print("     ,   ****** Day 15: Chiton *****   ,     ")
print("     | ******************************* |     ")
print("     ***********************************     ")
print("                     ░░░                     ")
print("                     ░░░                     ")
print("                                             ")

filename = "15.sample"
with open(filename) as file:
    raw = file.read().splitlines()

SCAN = []
for line in raw:
    SCAN.append([int(i) for i in line])

SCAN = np.array(SCAN)
print(SCAN)

def add_edges(graph, row, col):
    row_range = [-1, 1]
    col_range = [-1, 1]

    if row == 0:
        row_range = [0, 1]
    if row == (len(SCAN) - 1):
        row_range = [-1, 0]
    if col == 0:
        col_range = [0, 1]
    if col == (len(SCAN[0]) - 1):
        col_range = [-1, 0]

    for i in range(row_range[0], row_range[1] + 1):
        for j in range(col_range[0], col_range[1] + 1):
            if abs(i) != abs(j):
                print("Node: ", row, col)
                print("neighbor: ", row + i, col + j)
                print("weight: ", SCAN[row + i][col + j])
                graph.add_edge((row, col), (row + i, col + j), weight = SCAN[row + i][col + j])

GRAPH = nx.Graph()
for i in range(len(SCAN)):
    for j in range(len(SCAN[0])):
        GRAPH.add_node((i, j))
        add_edges(GRAPH, i, j)
print(GRAPH.get_edge_data((2,3),(1,3)))
print(GRAPH.get_edge_data((1,3),(1,4)))
print(GRAPH.get_edge_data((1,4),(2,4)))
print()
print(GRAPH.get_edge_data((2,4),(2,4)))

def part_one():
    return nx.single_source_dijkstra(GRAPH, (0, 0), (9, 9))

def part_two():
    return 'part 2'

print("Part 1:", part_one())
print("Part 2:", part_two())
