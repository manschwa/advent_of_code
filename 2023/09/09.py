print()
print(" *************************************** ")
print(" **  AoC 2023_09: Mirage Maintenance  ** ")
print(" *************************************** ")
print()

filename = "09.input"
with open(filename) as file:
    lines = file.read().splitlines()


def part_one():
    next_values = []
    for line in lines:
        last_values = []
        sequence = list(map(int, line.split()))
        while sequence.count(0) != len(sequence):
            last_values.append(sequence[-1])
            sub_sequence = []

            for i in range(0, len(sequence) - 1):
                diff = sequence[i + 1] - sequence[i]
                sub_sequence.append(diff)
            sequence = sub_sequence
        next_values.append(sum(last_values))

    return sum(next_values)

def part_two():
    prev_values = []
    for line in lines:
        first_values = []
        sequence = list(map(int, line.split()))
        while sequence.count(0) != len(sequence):
            first_values.append(sequence[0])
            sub_sequence = []

            for i in range(0, len(sequence) - 1):
                diff = sequence[i + 1] - sequence[i]
                sub_sequence.append(diff)
            sequence = sub_sequence
        for i in range(len(first_values) - 1, 0, -1):
            first_values[i - 1] -= first_values[i]
        prev_values.append(first_values[0])

    return sum(prev_values)


print("Part 1: ", part_one())
print("Part 2: ", part_two())