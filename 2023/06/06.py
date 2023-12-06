print()
print(" ******************************** ")
print(" **  AoC 2023_06: Wait For It  ** ")
print(" ******************************** ")
print()

filename = "06_sample.input"
with open(filename) as file:
    lines = file.read().splitlines()

times = list(map(int, lines[0].split(':')[1].split()))
distances = list(map(int, lines[1].split(':')[1].split()))

print(times)
print(distances)

def prod_ways_to_beat(times, distances):
    prod = 1
    for i in range(0, len(times)):
        ways_to_beat = 0
        for j in range(0, times[i]):
            if j * (times[i] - j) > distances[i]:
                ways_to_beat += 1
        prod *= ways_to_beat
    return prod

def part_one():
    return prod_ways_to_beat(times, distances)

def part_two():
    time = [int(''.join(map(str, times)))]
    distance = [int(''.join(map(str, distances)))]
    return prod_ways_to_beat(time, distance)

print("Part 1: ", part_one())
print("Part 2: ", part_two())