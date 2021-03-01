import sys
sys.stdin = open('input.txt', 'r')


def sum_colrow(input_list):
    N = len(input_list)

    result = 0
    for i in range(N):  # 가로 합
        sumsum = 0
        for j in range(N):
            sumsum += input_list[i][j]
        if sumsum > result:
            result = sumsum

    for j in range(N):  # 세로 합
        sumsum = 0
        for i in range(N):
            sumsum += input_list[i][j]
        if sumsum > result:
            result = sumsum

    sumsum = 0
    for i in range(N):  # 대각선 합
        sumsum += input_list[i][i]
    if sumsum > result:
        result = sumsum

    x = 0
    y = 9
    sumsum = 0
    for i in range(N):  # 역대각선 합
        sumsum += input_list[x][y]
        x += 1
        y -= 1
    if sumsum > result:
        result = sumsum

    return result


testcase = 10

for i in range(testcase):
    N = int(input())
    list100 = []
    for _ in range(100):
        list100.append(list(map(int, input().split())))

    print('#{} {}'.format(N, sum_colrow(list100)))