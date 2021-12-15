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

filename = "15.input"
with open(filename) as file:
    raw = file.read().splitlines()

SCAN = []
for line in raw:
    SCAN.append([int(i) for i in line])

SCAN = np.array(SCAN)

def add_edges(row, col):
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
                GRAPH.add_edge((row, col), (row + i, col + j), weight = SCAN[row + i][col + j])


GRAPH = nx.DiGraph()

for i in range(len(SCAN)):
    for j in range(len(SCAN[0])):
        add_edges(i, j)

def part_one():
    return nx.dijkstra_path_length(GRAPH, (0, 0), (99, 99))

def part_two():
    return 'part 2'

print("Part 1:", part_one())
print("Part 2:", part_two())
