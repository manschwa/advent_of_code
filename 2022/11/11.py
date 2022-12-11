import math

print()
print(" **************************************** ")
print(" **  AoC 2022_11: Monkey in the Middle ** ")
print(" **************************************** ")
print()

filename = "11.input"
with open(filename) as file:
    lines = file.read().splitlines()

inspects = []
items = []
operations = []
divisors = []
if_true = []
if_false = []

for i in range(0, len(lines), 7):
    inspects.append(0)
    items.append(list(map(int, lines[i + 1].split(': ')[1].split(', '))))
    operations.append(lines[i + 2].split(': ')[1].split('= ')[1])
    divisors.append(int(lines[i + 3].split()[-1]))
    if_true.append(int(lines[i + 4].split()[-1]))
    if_false.append(int(lines[i + 5].split()[-1]))

divisor = math.prod(divisors)
items_copy = items.copy()
inspects_copy = inspects.copy()

def monkey(i, part):
    for item in items[i]:
        inspects[i] += 1
        old = item
        item = eval(operations[i])
        if part == 1:
            item = int(item / 3)
        else:
            item %= divisor
        if item % divisors[i] == 0:
            items[if_true[i]].append(item)
        else:
            items[if_false[i]].append(item)
    items[i] = items[i][len(items[i]):]

def part_one():
    for i in range(0, 20):
        for m in range(0, len(inspects)):
            monkey(m, 1)
    return math.prod(sorted(inspects, reverse = True)[0:2])

def part_two():
    for i in range(0, 10000):
        for m in range(0, len(inspects)):
            monkey(m, 2)
    return math.prod(sorted(inspects, reverse = True)[0:2])

print("Part 1: ", part_one())
print("Part 2: ", part_two())
