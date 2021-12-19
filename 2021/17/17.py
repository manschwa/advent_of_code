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

def check_hit(x, y, x_range, y_range):
    return (x in x_range and y in y_range)

def throw(x, y, x_range, y_range):
    y_max = 0
    x_step = x
    y_step = y
    while x <= max(x_range) and y >= min(y_range):
        if y > y_max:
            y_max = y
        if check_hit(x, y, x_range, y_range):
            return y_max
        if x_step > 0:
            x_step -= 1
        y_step -= 1
        x += x_step
        y += y_step
    return False


def part_one(x_range, y_range):
    max_height = 0
    for x in range(0, max(x_range)):
        for y in range(min(y_range), max(x_range)):
            if height := throw(x, y, x_range, y_range):
                if height > max_height:
                    max_height = height
    return max_height

def part_two():
    return 'part 2'

print("Part 1:", part_one(range(135, 156), range(-102, -77)))
print("Part 2:", part_two())
