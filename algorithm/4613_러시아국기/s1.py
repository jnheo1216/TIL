## 4613 러시아국기
import sys
sys.stdin = open('input.txt', 'r')


def minimum_paint(n, m, russia):  # 서윤님 코드 보고 감탄했습니다..
    count = []

    count_w = 0
    for white in range(n - 2):
        for y in range(m):
            if russia[white][y] != 'W':
                count_w += 1

        count_b = 0
        for blue in range(white + 1, n - 1):
            for y in range(m):
                if russia[blue][y] != 'B':
                    count_b += 1

            count_r = 0
            for red in range(blue + 1, n):
                for y in range(m):
                    if russia[red][y] != 'R':
                        count_r += 1

            count.append(count_w + count_b + count_r)

    return min(count)


color = {0: 'W', 1: 'B', 2: 'R'}
maxsum = 0
tmpsum = 0

def jaegui(color_index, n, m, russia):  # 이거 재귀로 되게 쉽게 할 수 있을거같은데 흙흙
    global maxsum, tmpsum

    if color_index == 2:
        if maxsum < tmpsum:
            maxsum = tmpsum

    count = 0
    for white in range(n - 2):
        for y in range(m):
            if russia[white][y] != 'W':
                count += 1
                jaegui(color_index + 1, n, m, russia)


testcase = int(input())

for i in range(testcase):
    N, M = map(int, input().split())
    nation = [list(str(input())) for _ in range(N)]  # WBR
    # for j in nation:
    #     print(j)

    print('#{} {}'.format(i + 1, minimum_paint(N, M, nation)))