print("                                             ")
print("                      △                      ")
print("                    ◁ ☆ ▷                    ")
print("                  ,   *   ,                  ")
print("                  | ***** |                  ")
print("             ,    *********    ,             ")
print("             |  *************  |             ")
print("         ,   Advent of Code 2021   ,         ")
print("         | *********************** |         ")
print("     ,   *** Day 07:  ***   ,     ")
print("     | ******************************* |     ")
print("     ***********************************     ")
print("                     ░░░                     ")
print("                     ░░░                     ")
print("                                             ")

filename = "07.input"
with open(filename) as file:
    raw = file.read().splitlines()
line = list(map(int, raw[0].split(',')))

def part_one(data):
    return 23

def part_two(data):
    return 42

print("Part 1: ", part_one())
print("Part 2: ", part_two())

