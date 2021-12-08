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
print("     | * Day 8: Seven Segment Search * |     ")
print("     ***********************************     ")
print("                     ░░░                     ")
print("                     ░░░                     ")
print("                                             ")

filename = "08.input"
with open(filename) as file:
    raw = file.read().splitlines()
lines = list(raw)

def count_distinct_values(list):
    return sum(len(code) in (2, 3, 4, 7) for code in list)

def part_one(data):
    return sum(count_distinct_values(line.split()[-4:]) for line in data)

def part_two(data):
    return 42

print("Part 1: ", part_one(lines))
print("Part 2: ", part_two(lines))

