## 11315 오목
import sys
sys.stdin = open('input.txt', 'r')


def ohmok_test(n, ohmoks):
    for i in range(n):  # 가로
        count = 0
        for j in range(n):
            if ohmoks[i][j] == 'o':
                count += 1
                if count >= 5:
                    return 'YES'
            else:
                count = 0

    for j in range(n):  # 세로
        count = 0
        for i in range(n):
            if ohmoks[i][j] == 'o':
                count += 1
                if count >= 5:
                    return 'YES'
            else:
                count = 0
        if count >= 5:
            return 'YES'

    for i in range(n - 4):  # 대각선
        for j in range(n - 4):
            count = 0
            b = j
            for a in range(i, i + 5):
                if ohmoks[a][b] == 'o':
                    count += 1
                else:
                    count = 0
                b += 1
            if count >= 5:
                return 'YES'

    omok_left_right = [list(reversed(i)) for i in ohmoks]
    for i in range(n - 4):  # 역대각선
        for j in range(n - 4):
            count = 0
            b = j
            for a in range(i, i + 5):
                if omok_left_right[a][b] == 'o':
                    count += 1
                else:
                    count = 0
                b += 1
            if count >= 5:
                return 'YES'

    return 'NO'


testcase = int(input())

for i in range(testcase):
    N = int(input())
    ohmokpan = [list(str(input())) for j in range(N)]
    print('#{} {}'.format(i + 1, ohmok_test(N, ohmokpan)))


