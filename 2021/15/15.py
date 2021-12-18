import numpy as np
import networkx as nx

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

################### Scan and fill the initial cave/map #########################
SCAN = []
for line in raw:
    SCAN.append([int(i) for i in line])

dim = len(SCAN)
times = 5
SCAN = np.array(SCAN)
CAVE = np.zeros((dim * times, dim * times))
CAVE[0:dim, 0:dim] = SCAN

for i in range(times):
    for j in range(times):
        if not (i == 0 and j == 0):
            if j == 0:  # take from above
                CAVE[(dim * i):((dim * i) + dim), (dim * j):((dim * j) + dim)] = (CAVE[(dim * (i - 1)):((dim * (i - 1)) + dim), (dim * j):((dim * j) + dim)] % 9) + 1
            else:       # take from left
                CAVE[(dim * i):((dim * i) + dim), (dim * j):((dim * j) + dim)] = (CAVE[(dim * i):((dim * i) + dim), (dim * (j - 1)):((dim * (j - 1)) + dim)] % 9) + 1

###############################################################################

def add_edges(row, col):
    row_range = [-1, 1]
    col_range = [-1, 1]

    if row == 0:
        row_range = [0, 1]
    if row == (len(CAVE) - 1):
        row_range = [-1, 0]
    if col == 0:
        col_range = [0, 1]
    if col == (len(CAVE[0]) - 1):
        col_range = [-1, 0]

    for i in range(row_range[0], row_range[1] + 1):
        for j in range(col_range[0], col_range[1] + 1):
            if abs(i) != abs(j):
                GRAPH.add_edge((row, col), (row + i, col + j), weight = CAVE[row + i][col + j])


# create the graph from the cave map
GRAPH = nx.DiGraph()

for i in range(len(CAVE)):
    for j in range(len(CAVE)):
        add_edges(i, j)

def part_one():
    return nx.dijkstra_path_length(GRAPH, (0, 0), (99, 99))

def part_two():
    return nx.dijkstra_path_length(GRAPH, (0, 0), (499, 499))

print("Part 1:", part_one())
print("Part 2:", part_two())
