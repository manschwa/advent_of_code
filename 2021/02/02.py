print("                      *                      ")
print("                    *****                    ")
print("                  *********                  ")
print("                *************                ")
print("             Advent of Code 2021             ")
print("           ***********************           ")
print("         **     Day 02: Dive!     **         ")
print("       *******************************       ")
print("     ***********************************     ")
print("                     ***                     ")
print("                     ***                     ")

filename = "02.input"
position = 0
depth = 0

with open(filename) as file:
    for line in file:
        cmd, val = line.split()
        val = int(val)
        match cmd:
            case 'forward':
                position += val
            case 'down':
                depth += val
            case 'up':
                depth -= val

print()
print("Horizontal position: {}, depth: {}, product of the two: {}".format(position, depth, position * depth))
print()

aim = 0
depth = 0
position = 0

with open(filename) as file:
    for line in file:
        cmd, val = line.split()
        val = int(val)
        match cmd:
            case 'down':
                aim += val
            case 'up':
                aim -= val
            case 'forward':
                position += val
                depth += aim * val

print("Horizontal position: {}, depth: {}, product of the two: {}".format(position, depth, position * depth))
print()
