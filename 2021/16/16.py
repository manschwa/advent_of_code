print("                                             ")
print("                      △                      ")
print("                    ◁ ☆ ▷                    ")
print("                  ,   *   ,                  ")
print("                  | ***** |                  ")
print("             ,    *********    ,             ")
print("             |  *************  |             ")
print("         ,   Advent of Code 2021   ,         ")
print("         | *********************** |         ")
print("     ,   ** Day 16: Packet Decoder *   ,     ")
print("     | ******************************* |     ")
print("     ***********************************     ")
print("                     ░░░                     ")
print("                     ░░░                     ")
print("                                             ")

filename = "16.sample"
with open(filename) as file:
    raw = file.read().splitlines()

code = raw[0]
version_sum = 0

def hex2bits(code):
    packet = ''
    for char in code:
        packet += bin(int(char, 16))[2:].zfill(4)
    return packet

def decode(packet):
    print("packet:", packet)
    version = int(packet[:3], 2)
    version_sum += version
    print("version:", version)
    type_id = int(packet[3:6], 2)
    print("type_id:", type_id)

    if type_id == 4:
        literal_value_code = packet[6:]
        literal_value_bin = ''
        for i in range(0, len(literal_value_code), 5):
            literal_value_bin += literal_value_code[i + 1 : i + 5]
            if literal_value_code[i] == '0':
                break

        print(literal_value_bin)
        literal_value = int(literal_value_bin, 2)
        print(literal_value)
    else:
        len_type_id = packet[6]
        if len_type_id == '0':  # next 15 bits
            total_length_bin = packet[7:22]
        else:                   # next 11 bits
            total_length_bin = packet[7:18]

def part_one(code):
    packet = hex2bits(code)
    decode(packet)
    return version_sum

def part_two():
    return 'part 2'

print("Part 1:", part_one(code))
print("Part 2:", part_two())
