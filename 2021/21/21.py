from functools import cache

print("                                             ")
print("                      △                      ")
print("                    ◁ ☆ ▷                    ")
print("                  ,   *   ,                  ")
print("                  | ***** |                  ")
print("             ,    *********    ,             ")
print("             |  *************  |             ")
print("         ,   Advent of Code 2021   ,         ")
print("         | *********************** |         ")
print("     ,   *** Day 21: Dirac Dice ****   ,     ")
print("     | ******************************* |     ")
print("     ***********************************     ")
print("                     ░░░                     ")
print("                     ░░░                     ")
print("                                             ")

def play():
# player = [position, points]
    player_1 = [5, 0]
    player_2 = [9, 0]
    die = [i for i in range(1, 101)]

    counter = 0
    while True:
        steps_p1 = 0
        for i in range(0, 3):
            steps_p1 += die[(counter + i) % 100]
        counter += 3
        player_1[0] = (player_1[0] + steps_p1)
        if player_1[0] % 10 == 0:
            player_1[0] = 10
        else:
            player_1[0] %= 10
        player_1[1] += player_1[0]
        if player_1[1] >= 1000:
            break

        steps_p2 = 0
        for i in range(0, 3):
            steps_p2 += die[(counter + i) % 100]
        counter += 3
        player_2[0] = (player_2[0] + steps_p2)
        if player_2[0] % 10 == 0:
            player_2[0] = 10
        else:
            player_2[0] %= 10
        player_2[1] += player_2[0]
        if player_2[1] >= 1000:
            break
    return counter * min(player_1[1], player_2[1])

@cache
def roll(pos1, pos2, points_1, points_2):
    if points_1 >= 21:
        return [1, 0]
    if points_2 >= 21:
        return [0, 1]
    wins = [0, 0]
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                new_pos1 = (pos1 + i + j + k - 1) % 10 + 1
                new_points_1 = points_1 + new_pos1
                u = roll(pos2, new_pos1, points_2, new_points_1)
                wins = [wins[0] + u[1], wins[1] + u[0]]
    return wins

def part_one():
    return play()

def part_two():
    return max(roll(5, 9, 0, 0))

print("Part 1:", part_one())
print("Part 2:", part_two())
