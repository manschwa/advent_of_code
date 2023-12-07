import math

print()
print(" ******************************** ")
print(" **  AoC 2023_06: Wait For It  ** ")
print(" ******************************** ")
print()

filename = "06.input"
with open(filename) as file:
    lines = file.read().splitlines()

times = list(map(int, lines[0].split(':')[1].split()))
distances = list(map(int, lines[1].split(':')[1].split()))

def get_wins(time, distance):
    x_1 = (time / 2) - math.sqrt((time / 2) ** 2 - distance)
    return (time + 1) - (math.floor(x_1) + 1) * 2

def part_one():
    prod_wins = 1
    for i in range(0, len(times)):
        prod_wins *= get_wins(times[i], distances[i])
    return prod_wins

def part_two():
    time = int(''.join(map(str, times)))
    distance = int(''.join(map(str, distances)))
    return get_wins(time, distance)


print("Part 1: ", part_one())
print("Part 2: ", part_two())