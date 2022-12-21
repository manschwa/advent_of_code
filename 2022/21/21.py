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
    monkey, number = line.split(': ')
    monkeys[monkey] = number

def yell(monkey):
    number = monkeys[monkey]
    if len(number.split()) == 1:
        return int(number)
    else:
        monkey1, operation, monkey2 = number.split()
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
