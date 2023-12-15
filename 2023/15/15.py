print()
print(" ******************************** ")
print(" **  AoC 2023_15: Lens Library ** ")
print(" ******************************** ")
print()

filename = "15.input"
with open(filename) as file:
    lines = file.read().splitlines()

sequence = lines[0].split(',')

def hash(str):
    val = 0
    for char in str:
        val = ((val + ord(char)) * 17) % 256
    return val

def part_one():
    sum = 0
    for seq in sequence:
        sum += hash(seq)
    return sum

def part_two():
    boxes = [{} for i in range(0, 256)]
    for seq in sequence:
        if seq.count('=') == 1:
            label, focal_length = seq.split('=')
            boxes[hash(label)][label] = focal_length
        else:
            label = seq[0:-1]
            boxes[hash(label)].pop(label, None)
    sum = 0
    for i in range(0, 256):
        slot = 0
        for key in boxes[i]:
            sum += (i + 1) * (slot + 1) * int(boxes[i][key])
            slot += 1
    return sum


print("Part 1: ", part_one())
print("Part 2: ", part_two())