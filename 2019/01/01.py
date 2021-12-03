print("                                             ")
print("                      △                      ")
print("                    ◁ ☆ ▷                    ")
print("                  ,   *   ,                  ")
print("                  | ***** |                  ")
print("             ,    *********    ,             ")
print("             |  *************  |             ")
print("         ,   Advent of Code 2019   ,         ")
print("         | *********************** |         ")
print("     ,   ***************************   ,     ")
print("     | ******************************* |     ")
print("     ***********************************     ")
print("  Day 1: The Tyranny of the Rocket Equation  ")
print("                     ░░░                     ")
print("                     ░░░                     ")
print("                                             ")

filename = "01.input"
with open(filename) as file:
    lines = file.read().splitlines()

masses = list(map(int, lines))

def simple_fuel_consumption(masses):
    return sum((int(fuel/3) - 2) for fuel in masses)

print("Part 1: fuel requirement: {}".format(simple_fuel_consumption(masses)))

def fuel(mass):
    fuel = int(mass / 3) - 2
    if (fuel <= 0):
        return 0
    return fuel + fuel(fuel)

def fuel_consumption(masses):
    return sum(fuel(mass) for mass in masses)

print("Part 2: fuel requirement (with fuel for fuel): {}".format(fuel_consumption(masses)))
