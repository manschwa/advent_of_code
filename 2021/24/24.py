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
print("     *** Day 24: Arithmetic Logic Uni **     ")
print("                     ░░░                     ")
print("                     ░░░                     ")
print("                                             ")

filename = "24.input"
with open(filename) as file:
    raw = file.read().splitlines()
instructions = []
for instruction in raw:
    instructions.append(instruction.split())


def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    return int(a / b)

def mod(a ,b):
    return a % b

def eql(a, b):
    return a == b

for code in range(99999999999999, 1, -1):
    if code % 10 == 0:
        continue

    vars = set()
    for i in instructions:
        vars.add(i[1])
        exec(i[1] + '= 0')

    code = str(code)
    for i in instructions:
        if i[0] == 'inp':
            exec(i[1] + '=' + code[0])
            if len(code) > 1:
                code = code[1:]
        else:
            exec(i[1] + '=' + str(eval(i[0] + '(' + i[1] + ',' + i[2] + ')')))
    if z == 0:
        print("z == 0, code =", code)
        break

for var in vars:
    print(var, eval(var))

def part_one():
    return 'part 1'

def part_two():
    return 'part 2'

print("Part 1:", part_one())
print("Part 2:", part_two())
