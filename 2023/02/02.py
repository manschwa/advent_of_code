print()
print(" *********************************** ")
print(" **  AoC 2023_02: Cube Conundrum  ** ")
print(" *********************************** ")
print()

filename = "02.input"
with open(filename) as file:
    lines = file.read().splitlines()

max_cubes = {'red': 12, 'green': 13, 'blue': 14}

def day_02():
    sum = prod_sum = 0
    for line in range(0, len(lines)):
        valid = True
        cubes = {'red': 0, 'green': 0, 'blue': 0}
        sets = lines[line].split(': ')[1].split('; ')
        for set in sets:
            game = set.split(', ')
            for pull in game:
                num, color = pull.split(' ')
                # Part One
                if int(num) > max_cubes[color]:
                    valid = False
                # Part Two
                if int(num) > cubes[color]:
                    cubes[color] = int(num)
        if valid:
            sum += (line + 1)
        prod_sum += cubes['red'] * cubes['green'] * cubes['blue']
    return sum, prod_sum

print("Part 1: ", day_02()[0])
print("Part 2: ", day_02()[1])