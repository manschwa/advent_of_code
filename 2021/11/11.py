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
print("     ,   ** Day 11: Dumbo Octopus **   ,     ")
print("     | ******************************* |     ")
print("     ***********************************     ")
print("                     ░░░                     ")
print("                     ░░░                     ")
print("                                             ")

filename = "11.input"
with open(filename) as file:
    raw = file.read().splitlines()

matrix = []
for line in raw:
    row = []
    for num in line:
        row.append(int(num))
    matrix.append(row)

matrix = np.array(matrix)


def increase_energy(matrix):
    for i, row in enumerate(matrix):
        for j, num in enumerate(row):
            matrix[i][j] += 1
            if matrix[i][j] == 10:
                flashes(matrix, i, j)

def flashes(matrix, row, col):
    row_range = [-1, 1]
    col_range = [-1, 1]

    if row == 0:
        row_range = [0, 1]
    if row == (len(matrix) - 1):
        row_range = [-1, 0]
    if col == 0:
        col_range = [0, 1]
    if col == (len(matrix[0]) - 1):
        col_range = [-1, 0]

    for i in range(row_range[0], row_range[1] + 1):
        for j in range(col_range[0], col_range[1] + 1):
            matrix[row + i][col + j] += 1
            if matrix[row + i][col + j] == 10:
                flashes(matrix, row + i, col + j)

def count_flashes(matrix):
    flashes = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > 9:
                flashes += 1
                matrix[i][j] = 0
    return flashes

def part_one(matrix):
    blinks = 0
    for i in range(100):
        increase_energy(matrix)
        blinks += count_flashes(matrix)
    return blinks

def part_two(matrix):
    steps = 0
    while count_flashes(matrix) != matrix.size:
        increase_energy(matrix)
        steps += 1
    return steps

print("Part 1: ", part_one(matrix.copy()))
print("Part 2: ", part_two(matrix.copy()))
