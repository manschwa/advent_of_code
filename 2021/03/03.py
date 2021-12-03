print("                                             ")
print("                      △                      ")
print("                    ◁ ☆ ▷                    ")
print("                  ,   *   ,                  ")
print("                  | ***** |                  ")
print("             ,    *********    ,             ")
print("             |  *************  |             ")
print("         ,   Advent of Code 2021   ,         ")
print("         | *********************** |         ")
print("     ,   ***************************   ,     ")
print("     | ** Day 03: Binary Diagnostic ** |     ")
print("     ***********************************     ")
print("                     ░░░                     ")
print("                     ░░░                     ")
print("                                             ")

filename = "03.input"
with open(filename) as file:
    raw = file.read().splitlines()

# note: returns 1 when cnt(1) == cnt(0)
def determine_bit(index,  list):
    ones = sum(seq[index] == '1' for seq in list)
    zeros = sum(seq[index] == '0' for seq in list)
    if ones >= zeros:
        return '1'
    else:
        return '0'

gamma_s = epsilon_s = ''
for i in range(len(raw[0])):
    gamma_s += determine_bit(i, raw)
    epsilon_s += '0' if gamma_s[i] == '1' else '1'

gamma_int = int(gamma_s, 2)
epsilon_int = int(epsilon_s, 2)

print("PART 1:")
print("===============================================")
print("gamma = {}, gamma as Int = {}".format(gamma_s, gamma_int))
print("epsilon = {}, epsilon as Int = {}".format(epsilon_s, epsilon_int))
print("gamma * epsilon = {}".format(gamma_int * epsilon_int))

def seq_filter(raw, majority = True):
    for i in range(len(raw[0])):
        if majority:
            bit = determine_bit(i, raw)
        else:
            bit = '1' if determine_bit(i, raw) == '0' else '0'
        j = 0
        while j < len(raw) and len(raw) > 1:
            seq = raw[j]
            if seq[i] != bit:
                raw.remove(seq)
            else:
                j += 1
    return raw[0]

oxygen_bin = seq_filter(raw.copy())
oxygen_int = int(oxygen_bin, 2)

co2_bin = seq_filter(raw.copy(), False)
co2_int = int(co2_bin, 2)

print()
print("PART 2:")
print("===============================================")
print("Oxygen binary: {}, oxygen Int: {}".format(oxygen_bin, oxygen_int))
print("CO2 binary: {}, CO2 Int: {}".format(co2_bin, co2_int))
print("Oxygen * CO2 = {}".format(oxygen_int * co2_int))
