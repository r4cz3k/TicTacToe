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