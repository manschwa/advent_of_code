print()
print(" ****************************** ")
print(" ** AoC 2022_21: Monkey Math ** ")
print(" ****************************** ")
print()

filename = "21.input"
with open(filename) as file:
    lines = file.read().splitlines()

monkeys = {}

for line in lines:
    var, val = line.split(': ')
    monkeys[var] = val

def yell(monkey):
    sentence = monkeys[monkey]
    if len(sentence.split()) == 1:
        return int(sentence)
    else:
        monkey1, operation, monkey2 = sentence.split()
        return eval("{} {} {}".format(yell(monkey1), operation, yell(monkey2)))


def part_one():
    return int(yell('root'))

def part_two():
    monkeys['humn'] = '0'
    monkey1, operation, monkey2 = monkeys['root'].split()
    m = yell(monkey2)
    while(yell(monkey1) != m):
        monkeys['humn'] = str(int(monkeys['humn']) + 1)
    return monkeys['humn']


print("Part 1:", part_one())
print("Part 2:", part_two())
