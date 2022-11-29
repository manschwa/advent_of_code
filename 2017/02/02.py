import math

print()
print(" ************************************* ")
print(" **  AoC 2017_02: Corrupt Checksum  ** ")
print(" ************************************* ")
print()

filename = "02.input"
with open(filename) as file:
    lines = file.read().splitlines()

def part_one():
    sum = 0
    for line in lines:
        int_list = list(map(int, line.split()))
        sum += (max(int_list) - min(int_list))
    return sum

def part_two():
    sum = 0
    for line in lines:
        l = list(map(int, line.split()))
        for i in range(0, len(l) - 1):
            for j in range(i + 1, len(l)):
                x, y = l[i], l[j]
                if x > y and x % y == 0:
                    sum += (x / y)
                elif y > x and y % x == 0:
                    sum += (y / x)
    return int(sum)

print("Part 1: ", part_one())
print("Part 2: ", part_two())
