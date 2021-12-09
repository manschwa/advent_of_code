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

filename = "09.sample"
with open(filename) as file:
    raw = file.read().splitlines()
matrix = raw.copy()

def check_sink(matrix, row, col):
    up    = int(matrix[row - 1][col]) if row > 0 else float('inf')
    down  = int(matrix[row][col - 1]) if col > 0 else float('inf')
    left  = int(matrix[row][col + 1]) if col < (len(matrix[0]) - 1) else float('inf')
    right = int(matrix[row + 1][col]) if row < (len(matrix) -1) else float('inf')
    neighbors = [up, down, left, right]
    return int(matrix[row][col]) < min(neighbors)

def part_one(matrix):
    sinks = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if check_sink(matrix, i, j):
                sinks.append(int(matrix[i][j]))
    return sum(sinks) + len(sinks)

def part_two(data):
    return 42

print("Part 1: ", part_one(matrix))
print("Part 2: ", part_two(matrix))

