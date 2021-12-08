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
print("     | * Day 8: Seven Segment Search * |     ")
print("     ***********************************     ")
print("                     ░░░                     ")
print("                     ░░░                     ")
print("                                             ")

filename = "08.input"
with open(filename) as file:
    raw = file.read().splitlines()
lines = list(raw)

def count_distinct_values(list):
    return sum(len(code) in (2, 3, 4, 7) for code in list)

def decode(codes):
    numbers = [0] * 10
    fiver = []
    sixer = []
    for code in codes:
        match len(code):
            case 2:
                numbers[1] = code
            case 3:
                numbers[7] = code
            case 4:
                numbers[4] = code
            case 5:
                fiver.append(code)
            case 6:
                sixer.append(code)
            case 7:
                numbers[8] = code
    for i in fiver:
        if set(numbers[1]).issubset(set(i)):
            numbers[3] = i
            fiver.remove(i)
    for i in sixer:
        if set(numbers[3]).issubset(set(i)):
            numbers[9] = i
            sixer.remove(i)
    for i in sixer:
        if set(numbers[1]).issubset(set(i)):
            numbers[0] = i
            sixer.remove(i)
    numbers[6] = sixer.pop()
    if set(fiver[0]).issubset(set(numbers[6])):
        numbers[5], numbers[2] = fiver[0], fiver[1]
    else:
        numbers[5], numbers[2] = fiver[1], fiver[0]

    return numbers


def get_code(code, numbers):
    number = ''
    for c in code:
        for n in numbers:
            if set(c) == set(n):
                number += str(numbers.index(n))
    return int(number)


def part_one(data):
    return sum(count_distinct_values(line.split()[-4:]) for line in data)

def part_two(data):
    return sum(get_code(line.split()[-4:], decode(line.split()[:10])) for line in data)

print("Part 1: The digits 1, 4, 7 and 8 appear {} times.".format(part_one(lines)))
print("Part 2: The sum of all decoded codes is ", part_two(lines))

