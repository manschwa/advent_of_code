import numpy as np

print()
print(" *********************************** ")
print(" ** AoC 2022_18: Boiling Boulders ** ")
print(" *********************************** ")
print()

filename = "18.input"
with open(filename) as file:
    lines = file.read().splitlines()

scan = []
dimension = 0

for line in lines:
    cube = list(map(int, line.split(',')))
    scan.append(cube)
    if max(cube) > dimension:
        dimension = max(cube)

world = np.zeros((dimension + 1, dimension + 1, dimension + 1))

for cube in scan:
    world[cube[0]][cube[1]][cube[2]] = 1


def count_neighbors(arr, x, y, z):
    neighbors = 0
    if x > 0 and arr[x-1][y][z] == 1:
        neighbors += 1
    if x < len(arr)-1 and arr[x+1][y][z] == 1:
        neighbors += 1
    if y > 0 and arr[x][y-1][z] == 1:
        neighbors += 1
    if y < len(arr[x])-1 and arr[x][y+1][z] == 1:
        neighbors += 1
    if z > 0 and arr[x][y][z-1] == 1:
        neighbors += 1
    if z < len(arr[x][y])-1 and arr[x][y][z+1] == 1:
        neighbors += 1
    return neighbors


def part_one():
    neighbors = 0
    for cube in scan:
        neighbors += count_neighbors(world, cube[0], cube[1], cube[2])
    return (len(scan) * 6 - neighbors)

def part_two():
    return True

print("Part 1:", part_one())
print("Part 2:", part_two())
