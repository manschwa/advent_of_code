print()
print(" ************************************* ")
print(" **  AoC 2022_01: Calorie Counting  ** ")
print(" ************************************* ")
print()

filename = "01.input"
with open(filename) as file:
    lines = file.read().splitlines()

elves = [0]

def part_one():
    elf = 0
    for line in lines:
        if line == '':
            elf += 1
            elves.append(0)
        else:
            elves[elf] += int(line)
    return max(elves)

def part_two():
    strongest_elves = sorted(elves)[-3:]
    return sum(strongest_elves)

print("Part 1: ", part_one())
print("Part 2: ", part_two())
