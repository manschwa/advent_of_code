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
print("       * Day 02: Password Philosophy *       ")
print("     ***********************************     ")
print("                     ***                     ")
print("                     ***                     ")
print("                                             ")

filename = "02.input"
valid_passwords = 0

with open(filename) as file:
    for line in file:
        line_ary = line.split()
        count = line_ary[0]
        cnt_from = int(count.split('-')[0])
        cnt_to = int(count.split('-')[1])
        char = line_ary[1][0]
        sequence = line_ary[2]
        if(sequence.count(char) >= cnt_from and sequence.count(char) <= cnt_to):
            valid_passwords += 1

print("Part 1: Number of valid passwords after rule 1: ", valid_passwords)

valid_passwords = 0

with open(filename) as file:
    for line in file:
        line_ary = line.split()
        count = line_ary[0]
        cnt_from = int(count.split('-')[0])
        cnt_to = int(count.split('-')[1])
        char = line_ary[1][0]
        sequence = line_ary[2]
        if((sequence[cnt_from - 1] == char) ^ (sequence[cnt_to - 1] == char)):
            valid_passwords += 1

print("Part 2: Number of valid passwords after rule 2: ", valid_passwords)
