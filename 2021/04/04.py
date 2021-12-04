print("                                             ")
print("                      △                      ")
print("                    ◁ ☆ ▷                    ")
print("                  ,   *   ,                  ")
print("                  | ***** |                  ")
print("             ,    *********    ,             ")
print("             |  *************  |             ")
print("         ,   Advent of Code 2021   ,         ")
print("         | *********************** |         ")
print("     ,   *** Day 04: Giant Squid ***   ,     ")
print("     | ******************************* |     ")
print("     ***********************************     ")
print("                     ░░░                     ")
print("                     ░░░                     ")
print("                                             ")

filename = "04.input"
with open(filename) as file:
    raw = file.read().splitlines()

numbers = list(map(int, raw[0].split(",")))

boards = []
for i in range(2, len(raw), 6):
    board = []
    for j in range(5):
        board.append((list(map(int, raw[i + j].split()))))
    boards.append(board)


def print_board(board):
    for row in board:
        for char in row:
            print(format(char, '>4'), end = '')
        print()

def mark_board(board, number):
    for row in board:
        for i, num in enumerate(row):
            if number == num:
                row[i] = 'X'

def check_row(row):
    bingo = True
    for char in row:
        if char != 'X':
            bingo = False
    return bingo

def check_board(board):
    cols = len(board)
    for i in range(cols):
        col = []
        for row in board:
            if bingo := check_row(row):
                return bingo
            col.append(row[i])
        if bingo := check_row(col):
            return bingo
    return False

def calculate_sum(board):
    s = 0
    for row in board:
        s += sum(x for x in row if x != 'X')
    return s


initial_boards = len(boards)
for number in numbers:
    i = 0
    while i < len(boards):
        board = boards[i]
        mark_board(board, number)
        if bingo := check_board(board):
            if len(boards) == initial_boards or len(boards) == 1:
                print_board(board)
                s = calculate_sum(board)
                score = s * number
                num = "Last" if len(boards) == 1 else "FIRST"
                print("{} BINGO!".format(num))
                print("Number = {}, Sum = {}, Score = {}".format(number, s, score))
                print()
            boards.remove(board)
        else:
            i += 1
