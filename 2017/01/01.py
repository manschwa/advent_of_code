print()
print(" ************************************ ")
print(" **  AoC 2017_01: Inverse Captcha  ** ")
print(" ************************************ ")
print()

filename = "01.input"
with open(filename) as file:
    lines = file.read().splitlines()

def part_one(num):
    sum = 0
    for i in range(0, (len(num))):
        if num[i] == num[(i + 1) % len(num)]:
            sum += int(num[i])
    return sum

def part_two(num):
    sum = 0
    for i in range(0, (len(num))):
        if num[i] == num[(i + int(len(num) / 2)) % len(num)]:
            sum += int(num[i])
    return sum

print("Part 1: ", part_one(lines[0]))
print("Part 2: ", part_two(lines[0]))
