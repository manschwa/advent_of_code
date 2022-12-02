print()
print(" ***************************************** ")
print(" **  AoC 2022_02: Rock, Paper, Scissors ** ")
print(" ***************************************** ")
print()

filename = "02.input"
with open(filename) as file:
    lines = file.read().splitlines()

translate = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "X" : 1,
    "Y" : 2,
    "Z" : 3
}

def play(round):
    points = 0
    wins = [-2, 1]
    result = round[1] - round[0]
    if result in wins:
        points += 6
    elif result == 0:
        points += 3
    return points + round[1]

def part_one():
    points = 0
    for line in lines:
        points += play([translate[line[0]], translate[line[-1]]])
    return points

def part_two():
    points = 0
    win_strat = [0, 2, 3, 1]
    loss_strat = [0, 3, 1, 2]
    for line in lines:
        opponent = translate[line[0]]
        match line[-1]:
            case 'X':
                points += play([opponent, loss_strat[opponent]])
            case 'Y':
                points += play([opponent, opponent])
            case 'Z':
                points += play([opponent, win_strat[opponent]])
    return points

print("Part 1: ", part_one())
print("Part 2: ", part_two())
