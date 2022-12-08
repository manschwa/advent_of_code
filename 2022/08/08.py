import numpy as np

print()
print(" ****************************** ")
print(" **  AoC 2022_08: Tree House ** ")
print(" ****************************** ")
print()

filename = "08.input"
with open(filename) as file:
    lines = file.read().splitlines()

forest = []
for line in lines:
    row = []
    for i in line:
        row.append(int(i))
    forest.append(row)

forest = np.array(forest)

def check_visibility(height, row, col):
    if     (height > max(forest[:row, col]) or
            height > max(forest[row, col + 1:]) or
            height > max(forest[row + 1:, col]) or
            height > max(forest[row, :col])):
        return True
    return False

def check_line_of_sight(tree, line):
    for step, i in enumerate(line):
        if i >= tree or step + 1 == len(line):
            return step + 1

def scenic_score(height, row, col):
    return (1 *
            check_line_of_sight(height, np.flip(forest[:row, col])) *
            check_line_of_sight(height, forest[row, col + 1:]) *
            check_line_of_sight(height, forest[row + 1:, col]) *
            check_line_of_sight(height, np.flip(forest[row, :col])))


visible_trees = (len(forest[0,:]) * 2) + (len(forest[:,0]) * 2) - 4
scenic_scores = []
inner_forest = forest[1:-1, 1:-1]
for i, row in enumerate(inner_forest):
    for j, tree in enumerate(row):
        if check_visibility(tree, i + 1, j + 1):
            visible_trees += 1
        scenic_scores.append(scenic_score(tree, i + 1, j + 1))

print("Part 1: ", visible_trees)
print("Part 2: ", max(scenic_scores))
