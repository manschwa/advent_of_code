print("                                             ")
print("                      △                      ")
print("                    ◁ ☆ ▷                    ")
print("                  ,   *   ,                  ")
print("                  | ***** |                  ")
print("             ,    *********    ,             ")
print("             |  *************  |             ")
print("         ,   Advent of Code 2021   ,         ")
print("         | *********************** |         ")
print("     ,   *** Day 06: Lanternfish ***   ,     ")
print("     | ******************************* |     ")
print("     ***********************************     ")
print("                     ░░░                     ")
print("                     ░░░                     ")
print("                                             ")

filename = "06.input"
with open(filename) as file:
    raw = file.read().splitlines()
fish = list(map(int, raw[0].split(',')))

SPAWN_RATE = 7
TIME_TO_MATURE = 2
MAX_AGE = (SPAWN_RATE + TIME_TO_MATURE)
fishes = [0] * MAX_AGE

def calc_generations(days, fishes):
    for i in range(days):
        fishes[(i + SPAWN_RATE) % MAX_AGE] += fishes[i % MAX_AGE]
    return sum(fishes)


for i in fish:
    fishes[i] += 1

days = 80
print("Part 1: Amount of fish after {} days = {}".format(days, calc_generations(days, fishes.copy())))
days = 256
print("Part 2: Amount of fish after {} days = {}".format(days, calc_generations(days, fishes.copy())))
