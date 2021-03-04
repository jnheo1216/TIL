## 4875 미로
import sys
sys.stdin = open('input.txt', 'r')


# 물이 번져가는 느낌으로
def get_startpoint(inputlist):  # 시작지점을 알아온다.
    for i in range(len(inputlist)):
        for j in range(len(inputlist[0])):
            if inputlist[i][j] == 2:
                return [i, j]


def mirro_minimun_route(n, miro):
    startpoint = get_startpoint(miro)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]  # 상하좌우
    queue_xy = [startpoint]
    distance = [[0] * (n + 2) for _ in range(n + 2)]  # 해당위치까지 거리를 표시할 배열

    while queue_xy:
        now_point = queue_xy.pop(0)
        miro[now_point[0]][now_point[1]] = 1  # 지나온 표시
        for i in range(4):
            if miro[now_point[0] + dx[i]][now_point[1] + dy[i]] == 0:  # 갈수있는 길이 있다면
                queue_xy.append([now_point[0] + dx[i], now_point[1] + dy[i]])  # 큐에 추가해주기
                distance[now_point[0] + dx[i]][now_point[1] + dy[i]] += distance[now_point[0]][now_point[1]] + 1  # 거기까지 거리도 표시
            elif miro[now_point[0] + dx[i]][now_point[1] + dy[i]] == 3:  # 도착지점시 바로 탈출
                return distance[now_point[0]][now_point[1]]

    return 0


testcase = int(input())

for i in range(testcase):
    N = int(input())
    mirroN = [list(map(int, list(str(input())))) for _ in range(N)]  # NxN 미로를 입력받는다.

    mirroN.insert(0, [1] * N)  # 쿠션 작업 # 상하좌우 전부
    mirroN.append([1] * N)
    for j in range(N + 2):
        mirroN[j].insert(0, 1)
        mirroN[j].append(1)

    print('#{} {}'.format(i + 1, mirro_minimun_route(N, mirroN)))
