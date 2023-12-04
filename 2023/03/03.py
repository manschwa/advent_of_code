import re

print()
print(" ******************************** ")
print(" **  AoC 2023_03: Gear Ratios  ** ")
print(" ******************************** ")
print()

filename = "03.input"
with open(filename) as file:
    lines = file.read().splitlines()

symbols = r'[^a-zA-Z0-9.]'
numbers = r'[0-9]+'

def find_indices(pattern, string):
    pattern = re.compile(pattern)
    matches = pattern.finditer(string)
    indices = [match.span() for match in matches]
    return indices

indices_numbers = []
indices_symbols = []
for line in lines:
    indices_numbers.append(find_indices(numbers, line))
    indices_symbols.append(find_indices(symbols, line))

def is_part(symbol_index, number_tupel):
    return symbol_index in range(number_tupel[0] - 1, number_tupel[-1] + 1)

def get_number(line, number_tupel):
    number = ''
    for i in range(number_tupel[0], number_tupel[-1]):
        number += lines[line][i]
    return int(number)

def get_parts(line):
    line_sum = 0
    for number_tupel in indices_numbers[line]:
        adjecent = False
        # line above
        if line > 0:
            for symbol_tupel in indices_symbols[line - 1]:
                if is_part(symbol_tupel[0], number_tupel):
                    adjecent = True
        # same line
        for symbol_tupel in indices_symbols[line]:
            if is_part(symbol_tupel[0], number_tupel):
                adjecent = True
        # line below
        if line < len(lines) - 1:
            for symbol_tupel in indices_symbols[line + 1]:
                if is_part(symbol_tupel[0], number_tupel):
                    adjecent = True
        if adjecent:
            line_sum += get_number(line, number_tupel)
    return line_sum

def get_gear_ratio(line, symbol_index):
    parts = []
    # line above
    if line > 0:
        for number_tupel in indices_numbers[line - 1]:
            if is_part(symbol_index, number_tupel):
                parts.append(get_number(line - 1, number_tupel))
    # same line
    for number_tupel in indices_numbers[line]:
        if is_part(symbol_index, number_tupel):
            parts.append(get_number(line, number_tupel))
    # line below
    if line < len(lines) - 1:
        for number_tupel in indices_numbers[line + 1]:
            if is_part(symbol_index, number_tupel):
                parts.append(get_number(line + 1, number_tupel))
    if len(parts) == 2:
        return parts[0] * parts[1]
    else:
        return 0

def get_gear_ratios(line):
    gear_ratio_sum = 0
    for symbol_tupel in indices_symbols[line]:
        if lines[line][symbol_tupel[0]] == '*':
            gear_ratio_sum += get_gear_ratio(line, symbol_tupel[0])
    return gear_ratio_sum

def part_one():
    sum = 0
    for i in range(0, len(lines)):
        sum += get_parts(i)
    return sum

def part_two():
    sum = 0
    for i in range(0, len(lines)):
        sum += get_gear_ratios(i)
    return sum


print("Part 1: ", part_one())
print("Part 2: ", part_two())