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

print(player_1)
print(player_2)
print(counter)

def part_one():
    return counter * min(player_1[1], player_2[1])

def part_two():
    return 'part 2'

print("Part 1:", part_one())
print("Part 2:", part_two())
