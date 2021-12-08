print("                                             ")
print("                      △                      ")
print("                    ◁ ☆ ▷                    ")
print("                  ,   *   ,                  ")
print("                  | ***** |                  ")
print("             ,    *********    ,             ")
print("             |  *************  |             ")
print("         ,   Advent of Code 2021   ,         ")
print("         | *********************** |         ")
print("     ,   ***************************   ,     ")
print("     | ******************************* |     ")
print("     * Day 07: The Treachery of Whales *     ")
print("                     ░░░                     ")
print("                     ░░░                     ")
print("                                             ")

filename = "07.input"
with open(filename) as file:
    raw = file.read().splitlines()
positions = list(map(int, raw[0].split(',')))


def calc_fuel(positions, simple = True):
    min_fuel = float('inf')
    fuel = [0] * len(positions)

    for i in range(max(positions)):
        for j in range(len(fuel)):
            if simple:
                fuel[j] = abs(positions[j] - i)
            else:
                n = abs(positions[j] - i)
                fuel[j] = int((n * (n + 1)) / 2)
        if sum(fuel) < min_fuel:
            min_fuel = sum(fuel)

    return min_fuel


print("Part 1: The amount of fuel needed is {}".format(calc_fuel(positions)))
print("Part 2: The amount of fuel needed is {}".format(calc_fuel(positions, False)))

