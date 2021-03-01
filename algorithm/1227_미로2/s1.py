## 1227 미로2
import sys
sys.stdin = open('input.txt', 'r')


def get_startpoint(inputlist):  # 시작지점을 알아온다. 근데 이거 시작지점 다 1,1 이더라. 난 몰랐지
    for i in range(len(inputlist)):
        for j in range(len(inputlist[0])):
            if inputlist[i][j] == 2:
                return [i, j]


def find_maze_exit(miro_map):  # 탈출이 가능할까 불가능할까 판단해주는 함수
    startpoint = get_startpoint(miro_map)  # 출발지점
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]  # 상하좌우

    cheakpoint = [startpoint, startpoint]  # 스택형태로 해서 체크포인트를 찍어줌. 막힌다면 가장 최근꺼로 돌아가야 하니까
    my_location_x = startpoint[0]
    my_location_y = startpoint[1]  # 현재 위치

    while cheakpoint:  # dfs
        miro_map[my_location_x][my_location_y] = 1  # 현재 위치에 1을 기록해서 다시 갈 일 없게 막아줌
        galae = 0
        next_dx = 0
        next_dy = 0
        is_arrive = False

        for i in range(4):  # 상하좌우 4방향을 본다
            if miro_map[my_location_x + dx[i]][my_location_y + dy[i]] == 0:  # 만약 뚫려있다면
                galae += 1  # 갈래가 하나 추가
                next_dx = dx[i]
                next_dy = dy[i]  # 다음 갈 위치를 정해 두기
            elif miro_map[my_location_x + dx[i]][my_location_y + dy[i]] == 3:  # 3은 도착지. 만약 있다면 바로 탈출할 필요가 있다.
                is_arrive = True  # 탈출용 변수에 True
                break

        if is_arrive:  # 목적지를 찾았다. 바로 나가자
            return 1

        if galae == 0:  # 1. 더 이상 갈 길이 없으면? 예전 체크포인트로 돌아가야함
            my_location_x = cheakpoint[-1][0]
            my_location_y = cheakpoint[-1][1]
            cheakpoint.pop()  # 스택에서 빼주고 현재 위치 업데이트
        elif galae > 1:  # 2. 갈 수 있는 곳이 여러곳이다? 체크포인트로 해서 스택에 넣어놔야함
            cheakpoint.append([my_location_x, my_location_y])
        else:  # 3. 갈 길이 하나라면 체크포인트 관련 해서는 할 것이 없음
            pass

        my_location_x = my_location_x + next_dx
        my_location_y = my_location_y + next_dy  # 1의 경우 dxdy가 0이므로 상관없음. # 2의 경우 어떤 길을 먼저가보든 상관 없음

        # print(my_location_x, my_location_y)

    return 0  # 전부 탐색했는데 출구를 못찾았으니까 0반환


testcase = 10

for _ in range(testcase):
    N = int(input())
    mirro100 = [list(map(int, list(str(input())))) for _ in range(100)]  # 100x100 미로를 입력받는다.

    print('#{} {}'.format(N, find_maze_exit(mirro100)))