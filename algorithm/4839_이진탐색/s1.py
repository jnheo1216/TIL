## 4839 이진탐색
import sys
sys.stdin = open('input.txt', 'r')


def fight_binary(p, a):

    start = 1
    end = p
    count = 0

    while start <= end:
        idx = (start + end) // 2
        if idx == a:
            break
        elif idx > a:
            end = idx
        else:
            start = idx
        count += 1

    return count


testcase = int(input())

for i in range(testcase):
    P, A, B = map(int, input().split())
    print('#{}'.format(i+1), end=' ')
    if fight_binary(P, A) > fight_binary(P, B):
        print('B')
    elif fight_binary(P, A) < fight_binary(P, B):
        print('A')
    else:
        print(0)