import numpy as np

print()
print(" ********************************************* ")
print(" **  AoC 2023_14: Parabolic Reflector Dish  ** ")
print(" ********************************************* ")
print()

filename = "14.input"
with open(filename) as file:
    lines = file.read().splitlines()

reflector = np.array(list(map(list, lines)))

def tilt(reflector):
    for col in range(0, len(reflector[0])):
        base = 0
        for row in range(0, len(reflector)):
            if reflector[row, col] == 'O':
                if '.' in reflector[base:row, col]:
                    index = np.where(reflector[base:row, col] == '.')[0][0]
                    reflector[index + base][col] = 'O'
                    reflector[row][col] = '.'
            elif reflector[row, col] == '#':
                base = row
    return reflector

def get_load(reflector):
    sum = 0
    for i in range(0, len(reflector)):
        sum += np.sum(reflector[i] == 'O') * (len(reflector) - i)
    return sum

def cycle(reflector):
    for i in range(0, 4):
        reflector = np.rot90(tilt(reflector), 3)
    return reflector

def part_one():
    tilted_reflector = tilt(reflector)
    return get_load(tilted_reflector)

def part_two():
    cycles = 1000
    reflector_copy = reflector
    for i in range(0, cycles):
        reflector_copy = cycle(reflector_copy)
        
    return get_load(reflector_copy)


print("Part 1: ", part_one())
print("Part 2: ", part_two())