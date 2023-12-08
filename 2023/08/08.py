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

directions = lines[0].replace('L', '0').replace('R', '1')
dict = {}
for i in range(2, len(lines)):
    key, value = lines[i].split(' = ')
    dict[key] = (value[1:4], value[6:9])

starting_keys = []
pattern = re.compile(r'.*A$')
for key in dict.keys():
    if pattern.match(key):
        starting_keys.append(key)


def part_one():
    current = 'AAA'
    i = 0
    counter = 0
    while current != 'ZZZ':
        current = dict[current][int(directions[i])]
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
            current = dict[current][int(directions[i])]
            i = (i + 1) % len(directions)
            counter += 1
        counters.append(counter)
    return np.lcm.reduce(counters)


print("Part 1: ", part_one())
print("Part 2: ", part_two())