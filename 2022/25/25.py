print()
print(" *********************************** ")
print(" **  AoC 2022_25: Full of Hot Air ** ")
print(" *********************************** ")
print()

filename = "25_sample.input"
with open(filename) as file:
    lines = file.read().splitlines()

s_to_d = {
    '=': -2,
    '-': -1,
    '0': 0,
    '1': 1,
    '2': 2
}

d_to_s = {
    0: '0',
    1: '1',
    2: '2',
    3: '=',
    4: '-'
}

def snafu_to_decimal(snafu):
    decimal = 0
    length = len(snafu) - 1
    for char in snafu:
        decimal += s_to_d[char] * (5 ** length)
        length -= 1
    return decimal


def decimal_to_snafu(decimal):
    snafu = ''
    while decimal > 0:
        decimal, rem = divmod(decimal, 5)
        snafu += d_to_s[rem]
        if rem > 2:
            decimal += 1
    return snafu[::-1] if snafu else '0'


snafu_sum = 0
for snafu in lines:
    snafu_sum += snafu_to_decimal(snafu)

print(decimal_to_snafu(snafu_sum))
