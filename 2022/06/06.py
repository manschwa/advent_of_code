print()
print(" ********************************** ")
print(" **  AoC 2022_06: Tuning Trouble ** ")
print(" ********************************** ")
print()

filename = "06.input"
with open(filename) as file:
    line = file.read().splitlines()[0]

def parser(seq_len):
    for i in range(0, len(line)):
        sequence = set()
        for j in range(0, seq_len):
            sequence.add(line[i + j])
        if len(sequence) == seq_len:
            return i + seq_len

def part_one():
    return parser(4)

def part_two():
    return parser(14)

print("Part 1: ", part_one())
print("Part 2: ", part_two())
