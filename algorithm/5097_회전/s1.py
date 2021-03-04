## 5097 회전
import sys
sys.stdin = open('input.txt', 'r')


def do_spiral(n, m, num_list):
    for i in range(m % n):
        tmp = num_list.pop(0)
        num_list.append(tmp)

    return num_list[0]


testcase = int(input())

for i in range(testcase):
    N, M = map(int, input().split())
    numlist = list(map(int, input().split()))
    print('#{} {}'.format(i + 1, do_spiral(N, M, numlist)))