print()
print(" ******************************************* ")
print(" **  AoC 2022_03: Rucksack Reorganization ** ")
print(" ******************************************* ")
print()

filename = "03.input"
with open(filename) as file:
    lines = file.read().splitlines()

def part_one():
    total = 0
    for line in lines:
        first = line[0:int((len(line) / 2))]
        second = line[int((len(line) / 2)):]
        for char in first:
            if char in second:
                if char.islower():
                    total += ord(char) - 96
                else:
                    total += ord(char) - 38
                break
    return total

def part_two():
    total = 0
    for i in range(0, len(lines), 3):
        s = set(lines[i]).intersection(lines[i + 1]).intersection(lines[i + 2])
        char = s.pop()
        if char.islower():
            total += ord(char) - 96
        else:
            total += ord(char) - 38
    return total

print("Part 1: ", part_one())
print("Part 2: ", part_two())
