print("                                             ")
print("                      △                      ")
print("                    ◁ ☆ ▷                    ")
print("                  ,   *   ,                  ")
print("                  | ***** |                  ")
print("             ,    *********    ,             ")
print("             |  *************  |             ")
print("         ,   Advent of Code 2021   ,         ")
print("         | *********************** |         ")
print("     ,   **  Day 01: Sonar Sweep  **   ,     ")
print("     | ******************************* |     ")
print("     ***********************************     ")
print("                     ░░░                     ")
print("                     ░░░                     ")
print("                                             ")

filename = "01.input"
with open(filename) as file:
    lines = file.read().splitlines()

values = list(map(int, lines))

increase_cnt = sum(x < y for x, y in zip(values, values[1:]))

print("Part1: times the depth of the seafloor increased with 1 step: {}". format(increase_cnt))

# because every triple shares 2 values with the triple before,
# we just need to compare every 3 values
increase_cnt = sum(x < y for x, y in zip(values, values[3:]))
print("Part 2: times the depth of the seafloor increased with 3 steps: {}". format(increase_cnt))
