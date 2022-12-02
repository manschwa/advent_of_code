print()
print(" ***************************************** ")
print(" **  AoC 2022_02: Rock, Paper, Scissors ** ")
print(" ***************************************** ")
print()

filename = "02.input"
with open(filename) as file:
    lines = file.read().splitlines()

def play(round):
    points = 0
    win = [-2, 1]
    result = round[1] - round[0]
    if result in win:
        points += 6
    elif result == 0:
        points += 3
    return points + round[1]

def part_one():
    points = 0
    for line in lines:
        l = line.replace('A', '1').replace('X', '1').replace('B', '2').replace('Y', '2').replace('C', '3').replace('Z', '3')
        rnd = list(map(int, l.split()))
        points += play(rnd)
    return points

def part_two():
    points = 0
    for line in lines:
        l = line.replace('A', '1').replace('B', '2').replace('C', '3')
        rnd = l.split()
        if rnd[1] == 'X':
            if rnd[0] == '1':
                rnd[1] = '3'
            if rnd[0] == '2':
                rnd[1] = '1'
            if rnd[0] == '3':
                rnd[1] = '2'
        if rnd[1] == 'Y':
            rnd[1] = rnd[0]
        if rnd[1] == 'Z':
            if rnd[0] == '1':
                rnd[1] = '2'
            if rnd[0] == '2':
                rnd[1] = '3'
            if rnd[0] == '3':
                rnd[1] = '1'
        rnd = list(map(int, rnd))
        points += play(rnd)
    return points

print("Part 1: ", part_one())
print("Part 2: ", part_two())
