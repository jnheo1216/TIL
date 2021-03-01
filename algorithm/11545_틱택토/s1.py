## 11545 택택토
import pandas as pd
import sys
sys.stdin = open('input.txt', 'r')


def who_win(tictic):
    x_win = False
    o_win = False
    game_end = 0

    for i in range(4):  # 가로
        count_x = 0
        count_o = 0
        for j in range(4):
            if tictic[i][j] == 'T':
                count_o += 1
                count_x += 1
            elif tictic[i][j] == 'X':
                count_o = 0
                count_x += 1
            elif tictic[i][j] == 'O':
                count_o += 1
                count_x = 0
            else:
                count_o = 0
                count_x = 0
                game_end += 1
        if count_o >= 4:
            o_win = True
        if count_x >= 4:
            x_win = True

    for j in range(4):  # 세로
        count_x = 0
        count_o = 0
        for i in range(4):
            if tictic[i][j] == 'T':
                count_o += 1
                count_x += 1
            elif tictic[i][j] == 'X':
                count_o = 0
                count_x += 1
            elif tictic[i][j] == 'O':
                count_o += 1
                count_x = 0
            else:
                count_o = 0
                count_x = 0
        if count_o >= 4:
            o_win = True
        if count_x >= 4:
            x_win = True

    count_o = 0
    count_x = 0
    for i in range(4):  # 대각선
        if tictic[i][i] == 'T':
            count_o += 1
            count_x += 1
        elif tictic[i][i] == 'X':
            count_o = 0
            count_x += 1
        elif tictic[i][i] == 'O':
            count_o += 1
            count_x = 0
        else:
            count_o = 0
            count_x = 0
    if count_o >= 4:
        o_win = True
    if count_x >= 4:
        x_win = True

    count_o = 0
    count_x = 0
    a = 0
    b = 3
    for _ in range(4):  # 역대각선
        if tictic[a][b] == 'T':
            count_o += 1
            count_x += 1
        elif tictic[a][b] == 'X':
            count_o = 0
            count_x += 1
        elif tictic[a][b] == 'O':
            count_o += 1
            count_x = 0
        else:
            count_o = 0
            count_x = 0
        a += 1
        b -= 1
    if count_o >= 4:
        o_win = True
    if count_x >= 4:
        x_win = True

    # 판결
    if o_win and x_win:
        return 'Draw'
    elif o_win:
        return 'O won'
    elif x_win:
        return 'X won'
    elif game_end == 0:
        return 'Draw'
    else:
        return 'Game has not completed'


testcase = int(input())

for i in range(testcase):
    tictacto = [list(str(input())) for j in range(4)]
    try:
        tmp = str(input())
    except:
        pass
    # print(pd.DataFrame(tictacto))
    print('#{} {}'.format(i + 1, who_win(tictacto)))