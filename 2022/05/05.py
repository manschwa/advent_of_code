print()
print(" ******************************** ")
print(" **  AoC 2022_05: Supply Stack ** ")
print(" ******************************** ")
print()

filename = "05.input"
with open(filename) as file:
    lines = file.read().splitlines()

def stacks_amount():
    stacks = []
    for line in lines:
        if line[1] == '1':
            for i in range(0, int(len(line) / 4) + 1):
                stack = []
                stacks.append(stack)
            break
    return stacks

def build_stack():
    stacks = stacks_amount()
    for line in lines:
        for i in range(0, int(len(line) / 4) + 1):
            crate = line[i * 4 + 1]
            if crate != ' ':
                stacks[i].insert(0, crate)
        if line[1] == '1':
            break
    return stacks

def parse_moves():
    moves = []
    for line in lines:
        if line == '' or line[0] != 'm':
            continue
        else:
            move = line[4:].split('from')
            move[1] = move[1].split('to')
            moves.append(move)
    return moves

def part_one():
    stacks = build_stack()
    moves = parse_moves()
    for move in moves:
        for i in range(0, int(move[0])):
            crate = stacks[int(move[1][0]) - 1].pop()
            stacks[int(move[1][1]) - 1].append(crate)

    top_crates = ''
    for stack in stacks:
        top_crates += stack.pop()
    return top_crates

def part_two():
    stacks = build_stack()
    moves = parse_moves()
    for move in moves:
        for i in range(0, int(move[0])):
            crate = stacks[int(move[1][0]) - 1].pop()
            if i == 0:
                stacks[int(move[1][1]) - 1].append(crate)
            else:
                stacks[int(move[1][1]) - 1].insert(-i, crate)
    top_crates = ''
    for stack in stacks:
        top_crates += stack.pop()
    return top_crates

print("Part 1: ", part_one())
print("Part 2: ", part_two())
