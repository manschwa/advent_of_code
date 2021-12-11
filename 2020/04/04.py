import re

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
print("       * Day 04: Passport Processing *       ")
print("     ***********************************     ")
print("                     ***                     ")
print("                     ***                     ")
print("                                             ")

filename = "04.input"
with open(filename) as file:
    raw = file.read().splitlines()

REQ_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
PATTERNS = {'byr' : '^19[2-9][\d]$|^200[0-2]$',
            'iyr' : '^201[\d]$|^2020$',
            'eyr' : '^202[\d]$|^2030$',
            'hgt' : '^1([5-8][\d]|9[0-3])cm$|^(59|6[\d]|7[0-6])in$',
            'hcl' : '^#[\da-f]{6}$',
            'ecl' : '^amb$|^blu$|^brn$|^gr(y|n)$|^hzl$|^oth$',
            'pid' : '^\d{9}$'}

passports = []
passport = []
for line in raw:
    if not line:
        passports.append(passport)
        passport = []
    else:
        passport.extend(line.split())
passports.append(passport)


def has_fields(passport):
    passport_fields = {'cid'}
    for field in passport:
        passport_fields.add(field.split(':')[0])
    return passport_fields == REQ_FIELDS

def is_valid(passport):
    if has_fields(passport):
        for attribute in passport:
            match attribute.split(':')[0]:
                case 'byr': pattern = PATTERNS['byr']
                case 'iyr': pattern = PATTERNS['iyr']
                case 'eyr': pattern = PATTERNS['eyr']
                case 'hgt': pattern = PATTERNS['hgt']
                case 'hcl': pattern = PATTERNS['hcl']
                case 'ecl': pattern = PATTERNS['ecl']
                case 'pid': pattern = PATTERNS['pid']
                case _ : pattern = ''
            attr = attribute.split(':')[1]
            if not re.match(pattern, attr):
                return False
        return True
    return False

def part_one(passports):
    return sum(has_fields(passport) for passport in passports)

def part_two(passports):
    return sum(is_valid(passport) for passport in passports)

print("Part 1: Number of valid passports:", part_one(passports))
print("Part 2: Number of valid passports:", part_two(passports))
