## 1954 달팽이
import sys
sys.stdin = open('input.txt', 'r')


def snail(n):
    result = [[0] * n for i in range(n)]  # n*n크기의 빈 행렬 생성
    x = 0
    y = -1  # 0,0 부터 시작해야하기때문에 -1로 초기값을 잡아줌
    move = 1  # 움직이는 정도
    idx = 1

    while True:
        for _ in range(1, n + 1):
            y += move  # y축으로 안채워진 끝까지 움직여줌
            result[x][y] = idx
            idx += 1

        n -= 1  # 상자 테두리가 채워졌으니 빼서 빈거 밖으로 안넘어가게 해줌
        if n <= 0:
            break  # 다 채울때까지 반복

        for _ in range(1, n + 1):  # 이번엔 세로축으로
            x += move
            result[x][y] = idx
            idx += 1

        move = move * -1  # 다 채웠으니 방향을 반대로 바꿔줘야함

    return result


testcase = int(input())

for i in range(testcase):
    N = int(input())
    print('#{}'.format(i+1))
    snail_array = snail(N)
    for j in snail_array:
        print(*j)