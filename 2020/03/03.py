print("                                             ")
print("                      *                      ")
print("                     ***                     ")
print("                      *                      ")
print("                    *****                    ")
print("                  *********                  ")
print("                *************                ")
print("             Advent of Code 2020             ")
print("           ***********************           ")
print("         ***************************         ")
print("       * Day 03: Toboggan Trajectory *       ")
print("     ***********************************     ")
print("                     ***                     ")
print("                     ***                     ")
print("                                             ")

filename = "03.input"
trees = 0
LINE_LEN = 31
position = 0

with open(filename) as file:
    for line in file:
        if(line[position] == '#'):
            trees += 1
        position += 3
        position %= LINE_LEN

print("Number of trees in the way: ", trees)

LINE_LEN     = 31
SLOPES       = 5
trees        = [0, 0, 0, 0, 0]
position     = [0, 0, 0, 0, 0]
steps_right  = [1, 3, 5, 7, 1]
steps_down   = [1, 1, 1, 1, 2]
line_counter = 0

with open(filename) as file:
    for line in file:
        for i in range(SLOPES):
            if(line_counter % steps_down[i] == 0):
                if(line[position[i]] == '#'):
                    trees[i] += 1
                position[i] += steps_right[i]
                position[i] %= LINE_LEN
        line_counter += 1

tree_product = 1
for i in range(SLOPES):
    print("Number of trees in the way of slope {}: {}".format(i, trees[i]))
    tree_product *= trees[i]
print("---------------------------------------------------")
print("Product of all trees in the way: ", tree_product)

