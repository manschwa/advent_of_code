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
print("     ,   ** Day 22: Reactor Reboot *   ,     ")
print("     | ******************************* |     ")
print("     ***********************************     ")
print("                     ░░░                     ")
print("                     ░░░                     ")
print("                                             ")

filename = "22.input"
with open(filename) as file:
    raw = file.read().splitlines()

INSTRUCTIONS = []
for line in raw:
    on_off, ranges = line.split()
    x_range, y_range, z_range = ranges.split(',')
    x_range = [int(i) for i in x_range[2:].split('..')]
    y_range = [int(i) for i in y_range[2:].split('..')]
    z_range = [int(i) for i in z_range[2:].split('..')]
    INSTRUCTIONS.append([on_off, x_range, y_range, z_range])

REACTOR = np.zeros((101, 101, 101))

def reboot():
    for instruction in INSTRUCTIONS:
        x_range = range(instruction[1][0] + 50, instruction[1][1] + 50 + 2)
        x_length = x_range[-1] - x_range[0]
        y_range = range(instruction[2][0] + 50, instruction[2][1] + 50 + 2)
        y_length = y_range[-1] - y_range[0]
        z_range = range(instruction[3][0] + 50, instruction[3][1] + 50 + 2)
        z_length = z_range[-1] - z_range[0]
        if instruction[0] == 'on':
            cuboid = np.ones((x_length, y_length, z_length))
        else:
            cuboid = np.zeros((x_length, y_length, z_length))
        REACTOR[x_range[0]:x_range[-1], y_range[0]:y_range[-1], z_range[0]:z_range[-1]] = cuboid
    return sum(sum(sum(REACTOR)))

def part_one():
    return reboot()

def part_two():
    return 'part 2'

print("Part 1:", part_one())
print("Part 2:", part_two())
