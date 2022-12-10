print()
print(" ************************************ ")
print(" **  AoC 2022_10: Cathode-Ray Tube ** ")
print(" ************************************ ")
print()

filename = "10.input"
with open(filename) as file:
    lines = file.read().splitlines()

def check_cycle(cycle):
    if cycle in [20, 60, 100, 140, 180, 220]:
        return True

def draw_row(row, cycle):
    if cycle in [40, 80, 120, 160, 200, 240]:
        print(row)
        return True

def part_one():
    signal = 1
    signals = []
    cycle = 0
    for line in lines:
        line = line.split()
        if line[0] == 'noop':
            cycle += 1
            if check_cycle(cycle):
                signals.append(cycle * signal)
        if line[0] == 'addx':
            for i in range(0, 2):
                cycle += 1
                if check_cycle(cycle):
                    signals.append(cycle * signal)
            signal += int(line[1])

    return sum(signals)


def check_pixel(position, cycle):
    if cycle in range(position - 1, position + 2):
        return True

def part_two():
    row = ''
    signal = 1
    cycle = 0
    for line in lines:
        line = line.split()
        if line[0] == 'noop':
            cycle += 1
            if check_pixel(signal, (cycle - 1) % 40):
                row += '#'
            else:
                row += '.'
            if draw_row(row, cycle):
                row = ''
        if line[0] == 'addx':
            for i in range(0, 2):
                cycle += 1
                if check_pixel(signal, (cycle - 1) % 40):
                    row += '#'
                else:
                    row += '.'
                if draw_row(row, cycle):
                    row = ''
            signal += int(line[1])

print("Part 1: ", part_one())
print("Part 2: ", part_two())
