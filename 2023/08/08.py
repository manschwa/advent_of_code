import numpy as np
import re

print()
print(" ************************************** ")
print(" **  AoC 2023_08: Haunted Wasteland  ** ")
print(" ************************************** ")
print()

filename = "08.input"
with open(filename) as file:
    lines = file.read().splitlines()

directions = lines[0]
dict = {}
for i in range(2, len(lines)):
    key, value = lines[i].split(' = ')
    dict[key] = (value[1:4], value[6:9])

pattern = re.compile(r'.*A$')
starting_keys = []
for key in dict.keys():
    if pattern.match(key):
        starting_keys.append(key)


def part_one():
    current = 'AAA'
    i = 0
    counter = 0
    while current != 'ZZZ':
        if directions[i] == 'L':
            current = dict[current][0]
        else:
            current = dict[current][1]
        i = (i + 1) % len(directions)
        counter += 1
    return counter

def part_two():
    counters = []
    pattern = re.compile(r'.*Z$')
    for key in starting_keys:
        current = key
        i = 0
        counter = 0
        while not(pattern.match(current)):
            if directions[i] == 'L':
                current = dict[current][0]
            else:
                current = dict[current][1]
            i = (i + 1) % len(directions)
            counter += 1
        counters.append(counter)
    return np.lcm.reduce(counters)


print("Part 1: ", part_one())
print("Part 2: ", part_two())