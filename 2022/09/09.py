import numpy as np

print()
print(" ******************************* ")
print(" **  AoC 2022_09: Rope Bridge ** ")
print(" ******************************* ")
print()

filename = "09_sample.input"
with open(filename) as file:
    lines = file.read().splitlines()

SIZE = 50
LENGTH = 10
rope = ((int(SIZE / 2), int(SIZE / 2)),) * LENGTH
rope = list(rope)
moves = []

for line in lines:
    direction, steps = line.split()
    moves.append([direction, int(steps)])

# start position, HEAD and TAIL overlap

def are_neighbors(arr, cell1, cell2):
    row1, col1 = cell1
    row2, col2 = cell2
    # Check if the cells are adjacent horizontally, vertically, or diagonally
    if abs(row1 - row2) <= 1 and abs(col1 - col2) <= 1:
        return True
    else:
        return False

tiles = np.full((SIZE + 1, SIZE + 1), False, dtype = bool)

# start position, the first tile is True
tiles[rope[LENGTH - 1]] = True

for move in moves:
    for i in range(1, move[1] + 1):
        index_head = 0
        index_tail = 1
        for j in range(0, LENGTH -1):
            if move[0] == 'R':
                if index_head > 0:
                    if not are_neighbors(tiles, rope[index_head - 1], rope[index_head]):
                        rope[index_head] = (rope[index_head][0], rope[index_head][1] + 1)
                else:
                    rope[index_head] = (rope[index_head][0], rope[index_head][1] + 1)

                if not are_neighbors(tiles, rope[index_head], rope[index_tail]):
                    rope[index_tail] = (rope[index_head][0], rope[index_head][1] - 1)
                if index_tail < LENGTH - 1:
                    index_head += 1
                    index_tail += 1

            if move[0] == 'L':
                if index_head > 0:
                    if not are_neighbors(tiles, rope[index_head - 1], rope[index_head]):
                        rope[index_head] = (rope[index_head][0], rope[index_head][1] - 1)
                else:
                    rope[index_head] = (rope[index_head][0], rope[index_head][1] - 1)

                if not are_neighbors(tiles, rope[index_head], rope[index_tail]):
                    rope[index_tail] = (rope[index_head][0], rope[index_head][1] + 1)
                if index_tail < LENGTH - 1:
                    index_head += 1
                    index_tail += 1

            if move[0] == 'U':
                if index_head > 0:
                    if not are_neighbors(tiles, rope[index_head - 1], rope[index_head]):
                        rope[index_head] = (rope[index_head][0] - 1, rope[index_head][1])
                else:
                    rope[index_head] = (rope[index_head][0] - 1, rope[index_head][1])

                if not are_neighbors(tiles, rope[index_head], rope[index_tail]):
                    rope[index_tail] = (rope[index_head][0] + 1, rope[index_head][1])
                if index_tail < LENGTH - 1:
                    index_head += 1
                    index_tail += 1

            if move[0] == 'D':
                if index_head > 0:
                    if not are_neighbors(tiles, rope[index_head - 1], rope[index_head]):
                        rope[index_head] = (rope[index_head][0] + 1, rope[index_head][1])
                else:
                    rope[index_head] = (rope[index_head][0] + 1, rope[index_head][1])

                if not are_neighbors(tiles, rope[index_head], rope[index_tail]):
                    rope[index_tail] = (rope[index_head][0] - 1, rope[index_head][1])
                if index_tail < LENGTH - 1:
                    index_head += 1
                    index_tail += 1

        if index_tail == LENGTH - 1:
            tiles[rope[index_tail]] = True
    print(rope)


def part_one():
    return np.count_nonzero(tiles)

def part_two():
    return True

print("Part 1: ", part_one())
print("Part 2: ", part_two())
