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

filename = "11.sample"
with open(filename) as file:
    raw = file.read().splitlines()
lines = raw.copy()


def part_one(data):
    return 23

def part_two(data):
    return 42

print("Part 1: ", part_one(lines))
print("Part 2: ", part_two(lines))

