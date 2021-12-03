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
print("     | ** Day 2: 1202 Program Alarm ** |     ")
print("     ***********************************     ")
print("                     ░░░                     ")
print("                     ░░░                     ")
print("                                             ")

filename = "02.input"
with open(filename) as file:
    for line in file:
        values = line.split(",")

values = list(map(int, values))

def intcode(noun, verb, vals):
    vals[1], vals[2] = noun, verb
    i = 0
    while i < len(vals):
        match vals[i]:
            case 1:
                vals[vals[i + 3]] = vals[vals[i + 1]] + vals[vals[i + 2]]
            case 2:
                vals[vals[i + 3]] = vals[vals[i + 1]] * vals[vals[i + 2]]
            case 99:
                break;
        i += 4
    return vals[0]

print("Part 1: Value in position [0]: {}".format(intcode(12, 2, values)))

for i in range(100):
    for j in range(100):
        if (intcode(i, j, values) == 19690720):
            print("noun = {}, verb = {}, 100 * {} + {} = {}".format(i, j, i, j, 100 * i + j))
            break;
