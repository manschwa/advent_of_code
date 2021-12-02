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
REQ_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
valid_passports = 0
passport_fields = {'cid'}
passport_cnt = 0

with open(filename) as file:
    for line in file:
        if(line.strip()):
            pairs = line.split()
            for pair in pairs:
                passport_fields.add(pair.split(':')[0])
        else:
            passport_cnt += 1
            if(REQ_FIELDS == passport_fields):
                valid_passports += 1
            passport_fields = {'cid'}
# extra check for the last passport
passport_cnt += 1
if(REQ_FIELDS == passport_fields):
    valid_passports += 1

print("Number of passports:", passport_cnt)
print("Number of valid passports:", valid_passports)

