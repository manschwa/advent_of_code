print()
print(" ******************************************* ")
print(" **  AoC 2022_07: No Space Left On Device ** ")
print(" ******************************************* ")
print()

filename = "07_sample.input"
with open(filename) as file:
    lines = file.read().splitlines()

for line in lines:
    line = line.split()
    if line[0] == "dir" or line[1] == "ls":
        pass
    elif line[0] != '$':
        d[-1] += int(line[0])
    elif line[2] == '..':
        s += [d.pop()]
        d[-1] += s[-1]
    elif line[2]=='/':
        s, d = [], [0]
    elif line[0] == "$" and line[1] == "cd":
        d.append(0)

print('Part 1:', sum(i for i in s + d[-1:] if i <= 100000))
print("Part 2:", min(i for i in s + d[-1:] if i > (sum(d) - 40000000)))
