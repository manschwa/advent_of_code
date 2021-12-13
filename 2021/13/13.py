import re
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
print("     ,   ***************************   ,     ")
print("     | * Day 13: Transparent Origami * |     ")
print("     ***********************************     ")
print("                     ░░░                     ")
print("                     ░░░                     ")
print("                                             ")

filename = "13.input"
with open(filename) as file:
    raw = file.read().splitlines()
lines = raw.copy()

####### initial parsing of the input file + creation of initial matrix ########

DOTS = []
FOLDS = []

row_max = 0
col_max = 0
for line in lines:
    if re.match('^\d.*', line):
        col = int(line.split(',')[0])
        row = int(line.split(',')[1])
        DOTS.append([row, col])
    elif re.match('^fold.*', line):
        axis = line.split('=')[0][-1]
        coord = int(line.split('=')[1])
        FOLDS.append(axis)
        if axis == 'x' and (coord * 2 + 1) > col_max:
            col_max = (coord * 2 + 1)
        elif axis == 'y' and (coord * 2 + 1) > row_max:
            row_max = (coord * 2 + 1)

matrix = np.full((row_max, col_max), False, dtype=bool)

for dot in DOTS:
    matrix[dot[0]][dot[1]] = True

###############################################################################

def fold(matrix, dimension):
    if dimension == 'x':
        fold_line = int(matrix.shape[1] / 2)
        return matrix[:, : fold_line] | np.fliplr(matrix[:, fold_line + 1 :])
    if dimension == 'y':
        fold_line = int(matrix.shape[0] / 2)
        return matrix[: fold_line] | np.flipud(matrix[fold_line + 1 :])

def print_matrix(matrix):
    for row in matrix:
        for col in row:
            if col:
                print("░", end = '')
            else:
                print(".", end = '')
        print()

def part_one(matrix):
    for i, f in enumerate(FOLDS):
        if i == 0:
            matrix = fold(matrix, f)
    return sum(sum(matrix))

def part_two(matrix):
    for f in FOLDS:
            matrix = fold(matrix, f)
    return matrix

print("Part 1: ", part_one(matrix.copy()))
print("Part 2:")
print_matrix(part_two(matrix.copy()))

