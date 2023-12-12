import numpy as np

print()
print(" ************************************* ")
print(" **  AoC 2023_11: Cosmic Expansion  ** ")
print(" ************************************* ")
print()

filename = "11.input"
with open(filename) as file:
    lines = file.read().splitlines()

universe = np.array(list(map(list, lines)))

double_rows = []
for i in range(0, len(universe)):
    if np.all(universe[i] == '.'):
        double_rows.append(i)

double_cols = []
for i in range(0, len(universe[i])):
    if np.all(universe[:, i] == '.'):
        double_cols.append(i)

galaxies = list(zip(*np.where(universe == '#')))

def galaxy_distance(g1, g2, expansion):
    col_expansion = len([x for x in double_cols if x in range(min(g1[1], g2[1]), max(g1[1], g2[1]) + 1)]) * (expansion - 1)
    row_expansion = len([x for x in double_rows if x in range(min(g1[0], g2[0]), max(g1[0], g2[0]) + 1)]) * (expansion - 1)
    return ((abs(g2[0] - g1[0]) + row_expansion) + (abs(g2[1] - g1[1]) + col_expansion))

def sum_galaxy_distances(galaxies, expansion):
    sum = 0
    for g in range(0, len(galaxies)):
        for j in range(g + 1, len(galaxies)):
            sum += galaxy_distance(galaxies[g], galaxies[j], expansion)
    return sum
    
print("Part 1: ", sum_galaxy_distances(galaxies, 2))
print("Part 2: ", sum_galaxy_distances(galaxies, 1000000))