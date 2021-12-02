print("                                             ")
print("                      *                      ")
print("                     ***                     ")
print("                      *                      ")
print("                    *****                    ")
print("                  *********                  ")
print("                *************                ")
print("             Advent of Code 2020             ")
print("           ***********************           ")
print("         ** Day 01: Report Repair **         ")
print("       *******************************       ")
print("     ***********************************     ")
print("                     ***                     ")
print("                     ***                     ")
print("                                             ")

filename = "01.input"
with open(filename) as file:
    lines = file.read().splitlines()

values = list(map(int, lines))
values.sort()

def prod_of_2_addends(values):
    for a in values:
        if (b := 2020 - a) in values:
            return [a, b, a * b]

print("{} + {} = 2020, their product is {}".format(*prod_of_2_addends(values)))

def prod_of_3_addends(values):
    for a in values:
        for b in values:
            if (c := 2020 - (a + b)) in values:
                return [a, b, c, a * b * c]

print("{} + {} + {} = 2020, their product is {}".format(*prod_of_3_addends(values)))
