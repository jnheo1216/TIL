## 1226 미로1
import sys
sys.stdin = open('input.txt', 'r')


def get_startpoint(inputlist):  # 시작지점을 알아온다.
    for i in range(len(inputlist)):
        for j in range(len(inputlist[0])):
            if inputlist[i][j] == 2:
                return [i, j]


def find_maze_exit_bfs(miro):
    startpoint = get_startpoint(miro)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]  # 상하좌우
    queue_xy = [startpoint]

    while queue_xy:
        now_point = queue_xy.pop(0)
        miro[now_point[0]][now_point[1]] = 1  # 지나온 표시
        for i in range(4):
            if miro[now_point[0] + dx[i]][now_point[1] + dy[i]] == 0:  # 갈수있는 길이 있다면
                queue_xy.append([now_point[0] + dx[i], now_point[1] + dy[i]])  # 큐에 추가해주기
            elif miro[now_point[0] + dx[i]][now_point[1] + dy[i]] == 3:  # 도착지점시 바로 탈출
                return 1

    return 0


testcase = 10

for _ in range(testcase):
    N = int(input())
    mirro100 = [list(map(int, list(str(input())))) for _ in range(16)]

    print('#{} {}'.format(N, find_maze_exit_bfs(mirro100)))