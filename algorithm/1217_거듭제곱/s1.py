## 1217 거듭제곱
import sys
sys.stdin = open('input.txt', 'r')


def powerpower(n, m):
    if m < 1:
        return 1
    else:
        return powerpower(n, m - 1) * n


testcase = 10

for _ in range(testcase):
    tc = int(input())
    N, M = map(int, input().split())
    print('#{} {}'.format(tc, powerpower(N, M)))