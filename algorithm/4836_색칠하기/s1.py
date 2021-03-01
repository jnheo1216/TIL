import sys
sys.stdin = open('input.txt', 'r')


def fill_square(squre_infos):
    dohwaji1 = [[0] * 10 for _ in range(10)]  # 빨강
    dohwaji2 = [[0] * 10 for _ in range(10)]  # 파랑

    for squre in squre_infos:
        if squre[4] == 1:  # 빨강일때
            for i in range(squre[0], squre[2] + 1):
                for j in range(squre[1], squre[3] + 1):
                    dohwaji1[i][j] = 1
        else:  # 파랑일때
            for i in range(squre[0], squre[2] + 1):
                for j in range(squre[1], squre[3] + 1):
                    dohwaji2[i][j] = 1
            pass

        count = 0
        for i in range(10):
            for j in range(10):
                if dohwaji1[i][j] == 1 and dohwaji2[i][j] == 1:  # 둘다 칠해져있으면
                    count += 1

    return count


testcase = int(input())

for i in range(testcase):
    N = int(input())
    color_squre_infos = []
    for j in range(N):
        color_squre_infos.append(list(map(int, input().split())))
    print('#{}'.format(i+1), fill_square(color_squre_infos))