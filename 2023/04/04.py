print()
print(" ********************************* ")
print(" **  AoC 2023_04: Scratchcards  ** ")
print(" ********************************* ")
print()

filename = "04.input"
with open(filename) as file:
    lines = file.read().splitlines()

def get_matches_len(line):
    winners, mine = line.split(': ')[1].split(' | ')
    winners = set(winners.split())
    mine = set(mine.split())
    return len(winners.intersection(mine))

def part_one():
    sum = 0
    for line in lines:
        matches = get_matches_len(line)
        if matches > 0:
            sum += 2 ** (matches - 1)
    return int(sum)

def part_two():
    instances = [1] * len(lines)
    for i in range(0, len(lines)):
        matches = get_matches_len(lines[i])
        for j in range(1, matches + 1):
            if (i + j) <= len(lines):
                instances[i + j] += 1 * instances[i]
    return sum(instances)

print("Part 1: ", part_one())
print("Part 2: ", part_two())