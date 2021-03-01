## 1210 사다리타기
import sys
sys.stdin = open('input.txt', 'r')


def index_endpoint(last_row):  # 이건 도착지점 찾는 함수
    for i in range(len(last_row)):
        if last_row[i] == 2:  # 2인 부분을 찾아서
            return i  # 반환

    return None


def find_startpoint(laddermap):
    endpoint = [99, index_endpoint(laddermap[-1])]  # 시작은 밑에서부터 올라가는 방식
    x = endpoint[0]
    y = endpoint[1]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]  # 상하좌우

    my_state = [-1, 0]

    while True:
        # print(1, x, y, my_state)
        if my_state[0] == -1 and my_state[1] == 0:  # 1. 현재 상태는 전진중
            if y > 0 and laddermap[x + dx[2]][y + dy[2]] == 1:  # 1-1. 왼쪽 길이 있다? 왼쪽으로 (단 y축 왼쪽으로 벗어나지 말아야함)
                my_state = [0, -1]
            elif y < 99 and laddermap[x + dx[3]][y + dy[3]] == 1:  # 1-2. 오른쪽 길이 있다? 오른쪽으로 (단 y축 오른쪽으로 벗어나지 말아야함)
                my_state = [0, 1]
            else:  # 1-3. 둘다 없으면 그대로 위로
                pass
        elif my_state[0] == 0 and my_state[1] == 1:  # 2. 현재 상태는 오른쪽 진행중
            if y == 99 or laddermap[x + dx[3]][y + dy[3]] == 0:  # 2-1. 계속 오른쪽으로 못갈만큼 왔다? 직진
                my_state = [-1, 0]
            else:  # 2-2. 그렇지 않다? 하던대로 계속
                pass
        elif my_state[0] == 0 and my_state[1] == -1:  # 3. 현재 상태는 왼쪽 진행중
            if y == 0 or laddermap[x + dx[2]][y + dy[2]] == 0:  # 3-1. 계속 왼쪽으로 못갈만큼 왔다? 직진
                my_state = [-1, 0]
            else:  # 3-2. 그렇지 않다? 하던대로 계속
                pass
        else:
            pass

        # 나의 위치 이동
        x += my_state[0]
        y += my_state[1]
        # print(2, x, y, my_state)

        if x == 0:
            break

    return y


testcase = 10

for i in range(testcase):
    N = int(input())
    ladder_list = []
    for _ in range(100):
        ladder_list.append(list(map(int, input().split())))
    print('#{}'.format(N), end=' ')
    print(find_startpoint(ladder_list))


