filename = "01.input"
with open(filename) as file:
    raw = file.read().splitlines()
frequencies = list(map(int, raw))

def part_one(data):
    return sum(data)

def part_two(data):
    frequencies = []
    frequency = 0
    double = False
    while(not double):
        for i in data:
            frequency += i
            if frequency in frequencies:
                double = True
                break
            else:
                frequencies.append(frequency)
    return frequency

print("Part 1: Sum of all frequencies: ", part_one(frequencies))
print("Part 2: First frequency that appears twice: ", part_two(frequencies))
