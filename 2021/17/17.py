print("                                             ")
print("                      △                      ")
print("                    ◁ ☆ ▷                    ")
print("                  ,   *   ,                  ")
print("                  | ***** |                  ")
print("             ,    *********    ,             ")
print("             |  *************  |             ")
print("         ,   Advent of Code 2021   ,         ")
print("         | *********************** |         ")
print("     ,   **** Day 17: Trick Shot ***   ,     ")
print("     | ******************************* |     ")
print("     ***********************************     ")
print("                     ░░░                     ")
print("                     ░░░                     ")
print("                                             ")

HEIGHTS = []
HITS = []

def check_hit(x, y, x_range, y_range):
    return (x in x_range and y in y_range)

def throw(x, y, x_range, y_range):
    initial_x = x
    initial_y = y
    y_max = 0
    x_step = x
    y_step = y
    while x <= max(x_range) and y >= min(y_range):
        if y > y_max:
            y_max = y
        if check_hit(x, y, x_range, y_range):
            if (initial_x, initial_y) not in HITS:
                HITS.append((initial_x, initial_y))
            HEIGHTS.append(y_max)
        if x_step > 0:
            x_step -= 1
        y_step -= 1
        x += x_step
        y += y_step

def part_one(x_range, y_range):
    for x in range(0, max(x_range) + 1):
        for y in range(min(y_range), max(x_range) + 1):
            throw(x, y, x_range, y_range)
    return max(HEIGHTS), len(HITS)

print("Part 1, 2:", part_one(range(135, 156), range(-102, -77)))
