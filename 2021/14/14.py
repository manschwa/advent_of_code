from collections import Counter

print("                                             ")
print("                      △                      ")
print("                    ◁ ☆ ▷                    ")
print("                  ,   *   ,                  ")
print("                  | ***** |                  ")
print("             ,    *********    ,             ")
print("             |  *************  |             ")
print("         ,   Advent of Code 2021   ,         ")
print("         | *********************** |         ")
print("     ,   ***************************   ,     ")
print("     | ******************************* |     ")
print("     * Day 14: Extended Polymerization *     ")
print("                     ░░░                     ")
print("                     ░░░                     ")
print("                                             ")

filename = "14.input"
with open(filename) as file:
    raw = file.read().splitlines()

template = raw[0]

chars = Counter(template)
pairs = Counter(template[i:i + 2] for i in range(len(template) - 1))

RULES = {}
for i in range(2, len(raw)):
    pair, insert = raw[i].split(' -> ')
    RULES[pair] = insert

def iterate(pairs, steps):
    for step in range(steps):
        new_pairs = Counter()
        for pair, counter in pairs.items():
            if pair in RULES:
                char = RULES[pair]
                new_pairs[pair[0] + char] += counter
                new_pairs[char + pair[1]] += counter
                chars[char] += counter
            else:
                new_pairs[pair] = counter
        pairs = new_pairs

    return max(chars.values()) - min(chars.values())

def part_one(pairs, steps):
    return iterate(pairs, steps)

def part_two(pairs, steps):
    return iterate(pairs, steps)

print("Part 1:", part_one(pairs, 10))
print("Part 2:", part_two(pairs, 40))
