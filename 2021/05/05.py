print("                                             ")
print("                      △                      ")
print("                    ◁ ☆ ▷                    ")
print("                  ,   *   ,                  ")
print("                  | ***** |                  ")
print("             ,    *********    ,             ")
print("             |  *************  |             ")
print("         ,   Advent of Code 2021   ,         ")
print("         | *********************** |         ")
print("     ,   * *************************   ,     ")
print("     | * Day 5: Hydrothermal Venture * |     ")
print("     ***********************************     ")
print("                     ░░░                     ")
print("                     ░░░                     ")
print("                                             ")

filename = "05.input"
with open(filename) as file:
    raw = file.read().splitlines()
lines = list(raw)

def get_Max(lines, coordinate):
    max = 0
    for line in lines:
        start, end = get_coordinates(line)
        if start[coordinate] > max:
            max = start[coordinate]
        if end[coordinate] > max:
            max = end[coordinate]
    return max

def get_dimensions(lines):
    return get_Max(lines, 0) + 1, get_Max(lines, 1) + 1

def count_intersections(floor):
    intersections = 0
    for row in floor:
        intersections += sum(i > 1 for i in row)
    return intersections

def get_coordinates(line):
    start = list(map(int, line.split()[0].split(',')))
    end = list(map(int, line.split()[-1].split(',')))
    return start, end

def is_valid_line(line):
    start, end = get_coordinates(line)
    if start[0] == end [0] or start[1] == end[1]:
        return True
    return False

def draw_line(floor, line):
    start, end = get_coordinates(line)
    steps_col = end[0] - start[0]
    steps_row = end[1] - start[1]
    steps = max(abs(steps_col), abs(steps_row))
    step_col = int(steps_col / abs(steps_col)) if steps_col != 0 else 0
    step_row = int(steps_row / abs(steps_row)) if steps_row != 0 else 0
    col = start[0]
    row = start[1]
    for step in range(0, steps + 1):
        floor[row + (step * step_row)][col + (step * step_col)] += 1

def draw_ocean_floor(floor):
    for row in floor:
        for col in row:
            col = '.' if col == 0 else col
            print(format(col, '>4'), end = '')
        print()

def part_one(lines):
    max_x, max_y = get_dimensions(lines)
    floor = [[0 for i in range(max_x)] for j in range(max_y)]
    for line in lines:
        if is_valid_line(line):
            draw_line(floor, line)
    # draw_ocean_floor(floor)
    return count_intersections(floor)

def part_two(lines):
    max_x, max_y = get_dimensions(lines)
    floor = [[0 for i in range(max_x)] for j in range(max_y)]
    for line in lines:
        draw_line(floor, line)
    # draw_ocean_floor(floor)
    return count_intersections(floor)

print("Part 1: Intersections on the ocean floor (w/o diagonals) = ", part_one(lines))
print("Part 2: Intersections on the ocean floor (w/ diagonals) = ", part_two(lines))
