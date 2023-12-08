import re

print()
print(" ******************************** ")
print(" **  AoC 2023_07: Camel Cards  ** ")
print(" ******************************** ")
print()

filename = "07.input"
with open(filename) as file:
    lines = file.read().splitlines()

hands = []
bets = []

def replace_labels(hand):
    hand = hand.replace('A', 'Z')
    hand = hand.replace('K', 'Y')
    hand = hand.replace('Q', 'X')
    hand = hand.replace('J', 'W')
    hand = hand.replace('T', 'V')
    return hand

for line in lines:
    l = line.split(' ')
    hands.append(l[0])
    bets.append(int(l[1]))

def all_chars_same(hand):
    pattern = re.compile(r'^(.)\1*$')
    return pattern.match(hand)

def has_char_four_times(hand):
    pattern = re.compile(r'(.).*\1.*\1.*\1')
    return pattern.search(hand)

def has_char_three_times(hand):
    pattern = re.compile(r'(.).*\1.*\1')
    return pattern.search(hand)

def has_char_two_times(hand):
    pattern = re.compile(r'(.).*\1')
    return pattern.search(hand)

def all_chars_unique(hand):
    pattern = re.compile(r'^(?!.*(.).*\1).*$')
    return pattern.match(hand)

def part_one():
    types = [[], [], [], [], [], [], []]
    ranks = len(hands)
    for i in range(0, ranks):
        hands[i] = replace_labels(hands[i])
        if all_chars_same(hands[i]):
            types[0].append((hands[i], bets[i]))
        elif has_char_four_times(hands[i]):
            types[1].append((hands[i], bets[i]))
        elif match := has_char_three_times(hands[i]):
            rest = hands[i].replace(hands[i][match.start()], '')
            if all_chars_same(rest):
                types[2].append((hands[i], bets[i]))
            else:
                types[3].append((hands[i], bets[i]))
        elif match := has_char_two_times(hands[i]):
            rest = hands[i].replace(hands[i][match.start()], '')
            if all_chars_unique(rest):
                types[5].append((hands[i], bets[i]))
            elif all_chars_same(rest):
                types[2].append((hands[i], bets[i]))
            else:
                types[4].append((hands[i], bets[i]))
        elif all_chars_unique(hands[i]):
            types[6].append((hands[i], bets[i]))
    
    one_list = []
    for list in types:
        one_list += sorted(list, reverse = True)
    sum = 0
    r = ranks
    for i in range(0, ranks):
        r -= 1
        sum += (i + 1) * one_list[r][1]
    return sum


def part_two():
    types = [[], [], [], [], [], [], []]
    ranks = len(hands)
    for i in range(0, ranks):
        hands[i] = hands[i].replace('W', '0')
        main_rest = hands[i].replace('0','')

        if hands[i].count('0') == 0:
            if all_chars_same(hands[i]):
                types[0].append((hands[i], bets[i]))
            elif has_char_four_times(hands[i]):
                types[1].append((hands[i], bets[i]))
            elif match := has_char_three_times(hands[i]):
                rest = hands[i].replace(hands[i][match.start()], '')
                if all_chars_same(rest):
                    types[2].append((hands[i], bets[i]))
                else:
                    types[3].append((hands[i], bets[i]))
            elif match := has_char_two_times(hands[i]):
                rest = hands[i].replace(hands[i][match.start()], '')
                if all_chars_unique(rest):
                    types[5].append((hands[i], bets[i]))
                elif all_chars_same(rest):
                    types[2].append((hands[i], bets[i]))
                else:
                    types[4].append((hands[i], bets[i]))
            elif all_chars_unique(hands[i]):
                types[6].append((hands[i], bets[i]))
        elif hands[i].count('0') in range(4, 5 + 1):
            types[0].append((hands[i], bets[i]))
        elif hands[i].count('0') == 3:
            if all_chars_same(main_rest):
                types[0].append((hands[i], bets[i]))
            elif all_chars_unique(main_rest):
                types[1].append((hands[i], bets[i]))
        elif hands[i].count('0') == 2:
            if all_chars_same(main_rest):
                types[0].append((hands[i], bets[i]))
            elif all_chars_unique(main_rest):
                types[3].append((hands[i], bets[i]))
            elif has_char_two_times(main_rest):
                types[1].append((hands[i], bets[i]))
        elif hands[i].count('0') == 1:
            if all_chars_same(main_rest):
                types[0].append((hands[i], bets[i]))
            elif has_char_three_times(main_rest):
                types[1].append((hands[i], bets[i]))
            elif all_chars_unique(main_rest):
                types[5].append((hands[i], bets[i]))
            elif match := has_char_two_times(main_rest):
                rest = main_rest.replace(main_rest[match.start()], '')
                if all_chars_same(rest):
                    types[2].append((hands[i], bets[i]))
                else:
                    types[3].append((hands[i], bets[i]))

    one_list = []
    for list in types:
        one_list += sorted(list, reverse = True)
    sum = 0
    r = ranks
    for i in range(0, ranks):
        r -= 1
        sum += (i + 1) * one_list[r][1]
    return sum


print("Part 1: ", part_one())
print("Part 2: ", part_two())