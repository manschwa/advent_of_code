print("                                             ")
print("                      △                      ")
print("                    ◁ ☆ ▷                    ")
print("                  ,   *   ,                  ")
print("                  | ***** |                  ")
print("             ,    *********    ,             ")
print("             |  *************  |             ")
print("         ,   Advent of Code 2021   ,         ")
print("         | *********************** |         ")
print("     ,   ** Day 10: Syntax Scoring *   ,     ")
print("     | ******************************* |     ")
print("     ***********************************     ")
print("                     ░░░                     ")
print("                     ░░░                     ")
print("                                             ")

filename = "10.input"
with open(filename) as file:
    raw = file.read().splitlines()
lines = raw.copy()

OPENINGS = ['(', '[', '{', '<']
CLOSINGS = [')', ']', '}', '>']

def incomplete(line):
    stack = []
    for char in line:
        if char in OPENINGS:
            stack.append(char)
        else:
            if stack[-1] == OPENINGS[CLOSINGS.index(char)]:
                stack.pop()
            else:
                return False
    return True


def incomplete_score(line):
    stack = []
    incomplete_score = 0
    scores = {')' : 1,
              ']' : 2,
              '}' : 3,
              '>' : 4}
    for char in line:
        if char in OPENINGS:
            stack.append(char)
        else:
            stack.pop()

    for i in range(len(stack)):
        incomplete_score = (incomplete_score * 5) + scores[CLOSINGS[OPENINGS.index(stack.pop())]]
    return incomplete_score

def corrupt_score(line):
    stack = []
    scores = {')' : 3,
              ']' : 57,
              '}' : 1197,
              '>' : 25137}
    for char in line:
        if char in OPENINGS:
            stack.append(char)
        else:
            if stack[-1] == OPENINGS[CLOSINGS.index(char)]:
                stack.pop()
            else:
                return scores[char]
    return 0

def part_one(data):
    score = 0
    for line in data:
        score += corrupt_score(line)
    return score

def part_two(data):
    scores = []
    for line in data:
        if incomplete(line):
            scores.append(incomplete_score(line))
    scores.sort()
    return scores[int(len(scores) / 2)]

print("Part 1: ", part_one(lines))
print("Part 2: ", part_two(lines))

