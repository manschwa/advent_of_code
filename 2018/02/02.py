filename = "02.input"
with open(filename) as file:
    raw = file.read().splitlines()
box_ids = list(raw)

def times_in_str(string, times):
    for char in string:
        if string.count(char) == times:
            return True

def differ_by_one(str1, str2):
    pos = -1
    for i, (c1, c2) in enumerate(zip(str1, str2)):
        if c1 != c2:
            if pos != -1:
                return -1
            else:
                pos = i
    return pos

def part_one(ids):
    twice = thrice = 0
    for id in ids:
        if times_in_str(id, 2):
            twice += 1
        if times_in_str(id, 3):
            thrice += 1
    return twice * thrice

def part_two(ids):
    for id_1 in ids:
        for id_2 in ids:
            pos = differ_by_one(id_1, id_2)
            if pos != -1:
                return id_1[:pos] + id_1[pos + 1:]

print("Part 1: checksum = ", part_one(box_ids))
print("Part 2: leftover string = ", part_two(box_ids))
