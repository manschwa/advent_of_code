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
print("     | *** Day 12: Passage Pathing *** |     ")
print("     ***********************************     ")
print("                     ░░░                     ")
print("                     ░░░                     ")
print("                                             ")

filename = "12.sample"
with open(filename) as file:
    raw = file.read().splitlines()
lines = raw.copy()

WAYS = {}
for line in lines:
    key, value = line.split('-')
    if key not in WAYS.keys():
        WAYS[key] = [value]
    else:
        WAYS[key].append(value)
    if value not in WAYS.keys():
        WAYS[value] = [key]
    else:
        WAYS[value].append(key)

walked_ways = [[]]
def walk1(current, visited):
    visited.append(current)
    if 'end' not in visited:
        for way in WAYS[current]:
            if (way.islower() and way not in visited):
                walk1(way, visited.copy())
            elif (way.isupper()):
                walk1(way, visited.copy())
    walked_ways.append(visited)

def walk2(current, visited, revisit):
    visited.append(current)
    if 'end' not in visited:
        for way in WAYS[current]:
            if (way.islower() and way not in visited):
                walk2(way, visited.copy(), True)
            elif (way != 'start' and way.islower() and visited.count(way) == 1 and revisit):
                walk2(way, visited.copy(), False)
            elif (way.isupper()):
                walk2(way, visited.copy(), True)
    walked_ways.append(visited)

def part_one(data):
    walk1('start', [])
    i = 0
    while i < len(walked_ways):
        if 'end' not in walked_ways[i]:
            walked_ways.pop(i)
        else:
            i += 1
    return len(walked_ways)

def part_two(data):
    walk2('start', [], False)
    i = 0
    while i < len(walked_ways):
        if 'end' not in walked_ways[i]:
            walked_ways.pop(i)
        else:
            i += 1

    double = 0
    i = 0
    while i < len(walked_ways):
        for cave in walked_ways[i]:
            if cave.islower() and walked_ways[i].count(cave) == 2:
                double += 1
        if double >= 4:
            walked_ways.pop(i)
        else:
            i += 1
        double = 0
    return 42

print("Part 1: ", part_one(lines))
#print("Part 2: ", part_two(lines))

