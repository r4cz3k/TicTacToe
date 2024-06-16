import random

lines = ["   |   |   \n", "---+---+---\n", "   |   |   \n", "---+---+---\n", "   |   |   \n"]

round = 1

def print_lines():
    for line in lines:
        print(line)


def check_win():
    for line in lines:
        if line.count("x") == 3:
            print_lines()
            print("User WON")
            exit(0)

        if line.count("o") == 3:
            print_lines()
            print("CPU WON")
            exit(0)

    for i in range(1, 10, 4):
        if lines[0][i] == lines[2][i] and lines[2][i] == lines[4][i] and lines[4][i] == "x":
            print_lines()
            print("User WON")
            exit(0)

        if lines[0][i] == lines[2][i] and lines[2][i] == lines[4][i] and lines[4][i] == "o":
            print_lines()
            print("CPU WON")
            exit(0)

    if lines[0][1] == lines[2][5] and lines[2][5] == lines[4][9] and lines[4][9] == "x":
        print_lines()
        print("User WON")
        exit(0)

    if lines[0][1] == lines[2][5] and lines[2][5] == lines[4][9] and lines[4][9] == "o":
        print_lines()
        print("CPU WON")
        exit(0)

    if lines[0][9] == lines[2][5] and lines[2][5] == lines[4][1] and lines[4][1] == "x":
        print_lines()
        print("User WON")
        exit(0)

    if lines[0][9] == lines[2][5] and lines[2][5] == lines[4][1] and lines[4][1] == "o":
        print_lines()
        print("CPU WON")
        exit(0)

def format_index(unformatted_index):
    match unformatted_index:
        case 1:
            return 1
        case 2:
            return 5
        case 3:
            return 9
        case _:
            return 1

def format_line(unformatted_line):
    match unformatted_line:
        case 1:
            return 0
        case 2:
            return 2
        case 3:
            return 4
        case _:
            return 0

def play_round(player, given_char):
    while True:
        if player == 'user':
            index = format_index(int(input("Which column to put x: ")))
            line = format_line(int(input("Which row to put x: ")))
        else:
            index = format_index(random.randint(0, 3))
            line = format_line(random.randint(0, 3))

        if lines[line][index] != 'x' and lines[line][index] != 'o':
            break

    lines[line] = lines[line][:index] + given_char + lines[line][index + 1:]

while True:
    print(f'Round {round//1:.0f}\n')

    print_lines()

    play_round('user', 'x')

    check_win()

    round += 0.5

    if round == 5.5:
        print("DRAW")
        exit(0)

    play_round('cpu', 'o')

    check_win()

    round += 0.5