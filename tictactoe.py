def x_won():
    print("X won!!")


def o_won():
    print("O won!!")


def play():
    board = ("| 1 | 2 | 3 |\n"
             "|-----------|\n"
             "| 4 | 5 | 6 |\n"
             "|-----------|\n"
             "| 7 | 8 | 9 |\n")

    print(board)
    c = 0
    game = True
    while game:
        d = board.rstrip()
        list_data = d.split('|')
        e = list_data[1]
        f = list_data[2]
        g = list_data[3]
        h = list_data[7]
        i = list_data[8]
        j = list_data[9]
        k = list_data[13]
        l = list_data[14]
        m = list_data[15]

        q = 0
        for z in [e, f, g]:
            if "X" in z:
                q += 1
        if q == 3:
            x_won()
            break

        r = 0
        for z in [h, i, j]:
            if "X" in z:
                r += 1
        if r == 3:
            x_won()
            break

        s = 0
        for z in [k, l, m]:
            if "X" in z:
                s += 1
        if s == 3:
            x_won()
            break

        t = 0
        for z in [e, h, k]:
            if "X" in z:
                t += 1
        if t == 3:
            x_won()
            break

        u = 0
        for z in [f, i, l]:
            if "X" in z:
                u += 1
        if u == 3:
            x_won()
            break

        v = 0
        for z in [g, j, m]:
            if "X" in z:
                v += 1
        if v == 3:
            x_won()
            break

        w = 0
        for z in [e, i, m]:
            if "X" in z:
                w += 1
        if w == 3:
            x_won()
            break

        x = 0
        for z in [g, i, k]:
            if "X" in z:
                x += 1
        if x == 3:
            x_won()
            break

        q = 0
        for z in [e, f, g]:
            if "O" in z:
                q += 1
        if q == 3:
            o_won()
            break

        r = 0
        for z in [h, i, j]:
            if "O" in z:
                r += 1
        if r == 3:
            o_won()
            break

        s = 0
        for z in [k, l, m]:
            if "O" in z:
                s += 1
        if s == 3:
            o_won()
            break

        t = 0
        for z in [e, h, k]:
            if "O" in z:
                t += 1
        if t == 3:
            o_won()
            break

        u = 0
        for z in [f, i, l]:
            if "O" in z:
                    u += 1
        if u == 3:
            o_won()
            break

        v = 0
        for z in [g, j, m]:
            if "O" in z:
                v += 1
        if v == 3:
            o_won()
            break

        w = 0
        for z in [e, i, m]:
            if "O" in z:
                w += 1
        if w == 3:
            o_won()
            break

        x = 0
        for z in [g, i, k]:
            if "O" in z:
                x += 1
        if x == 3:
            o_won()
            break

        x_count = board.count("X")
        o_count = board.count("O")

        if board.count("X") + board.count("O") == 9:
            break

        elif x_count == o_count:
            placement = input("Where do u want to place X? (1,9) ")
            if placement == "1":
                board = board.replace("1", "X")
            elif placement == "2":
                board = board.replace("2", "X")
            elif placement == "3":
                board = board.replace("3", "X")
            elif placement == "4":
                board = board.replace("4", "X")
            elif placement == "5":
                board = board.replace("5", "X")
            elif placement == "6":
                board = board.replace("6", "X")
            elif placement == "7":
                board = board.replace("7", "X")
            elif placement == "8":
                board = board.replace("8", "X")
            elif placement == "9":
                board = board.replace("9", "X")

            print(board)

        elif o_count == x_count - 1:
            placement = input("Where do u want to place O? (1,9) ")

            if placement == "1":
                board = board.replace("1", "O")
            elif placement == "2":
                board = board.replace("2", "O")
            elif placement == "3":
                board = board.replace("3", "O")
            elif placement == "4":
                board = board.replace("4", "O")
            elif placement == "5":
                board = board.replace("5", "O")
            elif placement == "6":
                board = board.replace("6", "O")
            elif placement == "7":
                board = board.replace("7", "O")
            elif placement == "8":
                board = board.replace("8", "O")
            elif placement == "9":
                board = board.replace("9", "O")

            print(board)
