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
print("     ,   *** Day 25: Sea Cucumber **   ,     ")
print("     | ******************************* |     ")
print("     ***********************************     ")
print("                     ░░░                     ")
print("                     ░░░                     ")
print("                                             ")

filename = "25.input"
with open(filename) as file:
    raw = file.read().splitlines()

FLOOR = np.array(list(map(list, raw)))
EMPTY, EAST, SOUTH = ".>v"

def step():
    moving_east = (FLOOR == EAST) & np.roll(FLOOR == EMPTY, -1, 1)

    FLOOR[moving_east] = EMPTY
    FLOOR[np.roll(moving_east, 1, 1)] = EAST

    moving_south = (FLOOR == SOUTH) & np.roll(FLOOR == EMPTY, -1, 0)

    FLOOR[moving_south] = EMPTY
    FLOOR[np.roll(moving_south, 1, 0)] = SOUTH

    return (moving_east | moving_south).any()

def part_one():
    return sum(iter(step, False)) + 1


print("Part 1:", part_one())
