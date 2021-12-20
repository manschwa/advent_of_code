import numpy as np

print("                                             ")
print("                      △                      ")
print("                    ◁ ☆ ▷                    ")
print("                  ,   *   ,                  ")
print("                  | ***** |                  ")
print("             ,    *********    ,             ")
print("             |  *************  |             ")
print("         ,   Advent of Code 2021   ,         ")
print("         | *********************** |         ")
print("     ,   *** Day 20: Trench Map  ***   ,     ")
print("     | ******************************* |     ")
print("     ***********************************     ")
print("                     ░░░                     ")
print("                     ░░░                     ")
print("                                             ")

filename = "20.input"
with open(filename) as file:
    raw = file.read().splitlines()

ALGO = []
for char in raw[0]:
    if char == '#':
        ALGO.append(1)
    else:
        ALGO.append(0)

image = []
for i in range(2, len(raw)):
    line = []
    for char in raw[i]:
        if char == '#':
            line.append(1)
        else:
            line.append(0)
    image.append(line)

image = np.array(image)

def enlarge_image(image, iteration):
    if ALGO[0] == 1 and ALGO[-1] == 0 and iteration % 2 == 1:
        enlarged_image = np.ones((len(image) + 4, len(image[1]) + 4))
    else:
        enlarged_image = np.zeros((len(image) + 4, len(image[1]) + 4))
    enlarged_image[2:(len(image) + 2), 2:(len(image[0]) + 2)] = image
    return enlarged_image

def crop_image(image):
    return image[1:-1, 1:-1]

def convert_pixel(image, row, col):
    binary_number = ''
    row_range = range(-1, 2)
    col_range = range(-1, 2)
    for i in row_range:
        for j in col_range:
            binary_number += str(int(image[row + i][col + j]))
    index = int(binary_number, 2)
    return ALGO[index]

def convert_image(image, iteration):
    image = enlarge_image(image, iteration)
    converted_image = np.zeros(image.shape)
    for i in range(1, len(image) - 1):
        for j in range(1, len(image[0]) - 1):
            converted_image[i][j] = convert_pixel(image, i, j)
    return crop_image(converted_image)

def print_image(image):
    for row in image:
        for char in row:
            if char == 1:
                print("░", end = '')
            else:
                print(" ", end = '')
        print()

def part_one(image):
    for i in range(2):
        image = convert_image(image, i)
    return sum(sum(image))

def part_two(image):
    for i in range(50):
        image = convert_image(image, i)
    return sum(sum(image))

print("Part 1:", part_one(image.copy()))
print("Part 2:", part_two(image.copy()))
