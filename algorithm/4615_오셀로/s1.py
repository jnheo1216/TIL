## 4615 오셀로
import sys
sys.stdin = open('input.txt', 'r')


def othello(n, m, play):
    pan = [[0] * n for _ in range(n)]
    pan[n // 2][n // 2] = 2
    pan[n // 2 - 1][n // 2 - 1] = 2
    pan[n // 2 - 1][n // 2] = 1
    pan[n // 2][n // 2 - 1] = 1  # 바둑판 만들기

    dx = [-1, 1, 0, 0, 1, -1, -1, 1]
    dy = [0, 0, -1, 1, 1, -1, 1, -1]  # 상하좌우+우하 좌상 우상 좌하

    for i in range(m):
        pan[play[i][0] - 1][play[i][1] - 1] = play[i][2]  # 돌을 놓는다

        if play[i][2] == 2:  # 둔 돌이 백돌일때
            for k in range(8):  # 8방향을 보기
                x = play[i][0] - 1
                y = play[i][1] - 1  # 현재 둔 돌의 위치
                tmp = []
                while 0 <= x < n and 0 <= y < n:  # 바둑판을 나가지 않게
                    x = x + dx[k]
                    y = y + dy[k]  # 방향으로 계속 ㄱ
                    if 0 <= x < n and 0 <= y < n and pan[x][y] == 0:  # 0이면 볼것도 없다
                        break
                    elif 0 <= x < n and 0 <= y < n and pan[x][y] == 1:  # 그 방향에 있는 돌이 다른 색이면
                        tmp.append([x, y])  # 거기 좌표를 기억해둔다
                    elif 0 <= x < n and 0 <= y < n and pan[x][y] == 2 and tmp:  # 그방향의 돌이 같은 색이며 지금까지 저장한 다른 돌이 있다면
                        for j in tmp:
                            pan[j[0]][j[1]] = 2  # 그 돌들의 색을 바꿔주고
                        break  # 탈출
                    elif 0 <= x < n and 0 <= y < n and pan[x][y] == 2 and tmp == []:  # 바로 같은 색 나오면 볼것도 없음
                        break  # 탈출
        if play[i][2] == 1:  # 둔 돌이 흑돌일때
            for k in range(8):
                x = play[i][0] - 1
                y = play[i][1] - 1
                tmp = []
                while 0 <= x < n and 0 <= y < n:
                    x = x + dx[k]
                    y = y + dy[k]
                    if 0 <= x < n and 0 <= y < n and pan[x][y] == 0:
                        break
                    elif 0 <= x < n and 0 <= y < n and pan[x][y] == 2:
                        tmp.append([x, y])
                    elif 0 <= x < n and 0 <= y < n and pan[x][y] == 1 and tmp:
                        for j in tmp:
                            pan[j[0]][j[1]] = 1
                        break
                    elif 0 <= x < n and 0 <= y < n and pan[x][y] == 1 and tmp == []:
                        break

    # for val in pan:
    #     print(val)

    b = 0
    w = 0

    for i in range(n):
        for j in range(n):
            if pan[i][j] == 1:
                b += 1
            elif pan[i][j] == 2:
                w += 1

    return [b, w]


test_case = int(input())

for i in range(test_case):
    N, M = map(int, input().split())
    play_list = [list(map(int, input().split())) for _ in range(M)]
    print('#{}'.format(i + 1), *othello(N, M, play_list))

########################