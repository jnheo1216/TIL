## 2001 파리퇴치
import sys
sys.stdin = open('input.txt', 'r')


def kill_flys(n, m, flylist):
    hit = n - m + 1
    result = 0

    for a in range(hit):
        for b in range(hit):  # 파리채이동
            kills = 0
            for i in range(a, a + m):
                for j in range(b, b + m):
                    kills += flylist[i][j]  # 파리잡기
            if kills > result:
                result = kills  # 최대값 비교

    return result


testcase = int(input())

for i in range(testcase):
    N , M = map(int, input().split())
    flys = []
    for _ in range(N):
        flys.append(list(map(int, input().split())))
    print('#{}'.format(i+1), kill_flys(N, M, flys))