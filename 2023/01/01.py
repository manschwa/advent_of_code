import re

print()
print(" ******************************** ")
print(" **  AoC 2023_01: Trebuchet?!  ** ")
print(" ******************************** ")
print()

filename = "01.input"
with open(filename) as file:
    lines = file.read().splitlines()

str2digit = {"one" :   "o1e",
             "two" :   "t2o",
             "three" : "t3e",
             "four" :  "f4r",
             "five" :  "f5e",
             "six" :   "s6x",
             "seven" : "s7n",
             "eight" : "e8t",
             "nine" :  "n9e"}

def find_sum():
    sum = 0
    for line in lines:
        numbers = re.findall(r'\d', line)
        number = int(numbers[0] + numbers[-1])
        sum += number
    return sum

def part_one():
    return find_sum()

def part_two():
    for num in str2digit:
        for i in range(0, len(lines)):
            lines[i] = lines[i].replace(num, str2digit[num])
    return find_sum()

print("Part 1: ", part_one())
print("Part 2: ", part_two())
