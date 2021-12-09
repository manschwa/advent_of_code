import math

print("                                             ")
print("                      △                      ")
print("                    ◁ ☆ ▷                    ")
print("                  ,   *   ,                  ")
print("                  | ***** |                  ")
print("             ,    *********    ,             ")
print("             |  *************  |             ")
print("         ,   Advent of Code 2021   ,         ")
print("         | *********************** |         ")
print("     ,   *** Day 9: Smoke Basin  ***   ,     ")
print("     | ******************************* |     ")
print("     ***********************************     ")
print("                     ░░░                     ")
print("                     ░░░                     ")
print("                                             ")

filename = "09.input"
with open(filename) as file:
    raw = file.read().splitlines()
matrix = raw.copy()

def check_sink(matrix, row, col):
    up    = int(matrix[row - 1][col]) if row > 0 else float('inf')
    left  = int(matrix[row][col - 1]) if col > 0 else float('inf')
    right  = int(matrix[row][col + 1]) if col < (len(matrix[0]) - 1) else float('inf')
    down = int(matrix[row + 1][col]) if row < (len(matrix) -1) else float('inf')
    neighbors = [up, down, left, right]
    return int(matrix[row][col]) < min(neighbors)

def basin_size(matrix, row, col):
    sum = 0
    if int(matrix[row][col]) == 9:
        return 0
    else:
        matrix[row] = matrix[row][:col] + '9' + matrix[row][col + 1:]
        if row > 0:
            sum += basin_size(matrix, row - 1, col)
        if col < (len(matrix[0]) - 1):
            sum += basin_size(matrix, row, col + 1)
        if row < (len(matrix) - 1):
            sum += basin_size(matrix, row + 1, col)
        if col > 0:
            sum += basin_size(matrix, row, col - 1)
    return sum + 1

def part_one(matrix):
    sinks = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if check_sink(matrix, i, j):
                sinks.append(int(matrix[i][j]))
    return sum(sinks) + len(sinks)

def part_two(matrix):
    sinks = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if check_sink(matrix, i, j):
                sinks.append(basin_size(matrix.copy(), i, j))
    sinks.sort()
    return math.prod(sinks[-3:])

print("Part 1: ", part_one(matrix))
print("Part 2: ", part_two(matrix.copy()))

