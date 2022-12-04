print()
print(" ******************************** ")
print(" **  AoC 2022_04: Camp Cleanup ** ")
print(" ******************************** ")
print()

filename = "04.input"
with open(filename) as file:
    lines = file.read().splitlines()

subsets = 0
overlaps = 0
for line in lines:
    sections = line.split(',')
    sec = []
    for i in range(0, len(sections)):
        start, end = list(map(int, sections[i].split('-')))
        sec.append(set(range(start, end + 1)))
    if sec[0].issubset(sec[1]) or sec[1].issubset(sec[0]):
        subsets += 1
    if sec[0].intersection(sec[1]):
        overlaps += 1

print("Part 1: ", subsets)
print("Part 2: ", overlaps)
