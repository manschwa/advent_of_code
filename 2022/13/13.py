import functools

print()
print(" ********************************** ")
print(" ** AoC 2022_13: Distress Signal ** ")
print(" ********************************** ")
print()

filename = "13.input"
with open(filename) as file:
    lines = file.read().splitlines()

packets = []
for line in lines:
    if len(line) > 0:
        packets.append(eval(line))

def check_order(packet_1, packet_2):
    elements = zip(packet_1, packet_2)
    for a, b in elements:
        if isinstance(a, list) and isinstance(b, list):
            c = check_order(a, b)
            if c != 0:
                return c
        elif isinstance(a, list) and isinstance(b, int):
            c = check_order(a, [b])
            if c != 0:
                return c
        elif isinstance(a, int) and isinstance(b, list):
            c = check_order([a], b)
            if c != 0:
                return c
        else:
            c = basic_compare(a, b)
            if c != 0:
                return c

    if len(packet_1) < len(packet_2):
        return 1
    elif len(packet_1) > len(packet_2):
        return -1
    else:
        return 0

def basic_compare(a, b):
    if a < b:
        return 1
    elif a > b:
        return -1
    return 0

def part_one():
    index = 1
    res = 0
    while len(packets) > 0:
        packet_1 = packets.pop(0)
        packet_2 = packets.pop(0)

        if check_order(packet_1, packet_2) >= 0:
            res += index
        index += 1
    return res

def part_two():
    packets.append([[2]])
    packets.append([[6]])
    sorted_packets = sorted(packets, key=functools.cmp_to_key(check_order), reverse = True)
    index_1 = sorted_packets.index([[2]]) + 1
    index_2 = sorted_packets.index([[6]]) + 1
    return index_1 * index_2

print("Part 1:", part_one())
print("Part 2:", part_two())
