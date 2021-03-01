## 1222 계산기1
import sys
sys.stdin = open('input.txt', 'r')


def calcul(s):
    result = 0
    p_ys = []
    ys = []
    for i in s:
        if 48 <= ord(i) < 58:
            p_ys.append(i)
        else:
            ys.append(i)

    n = len(p_ys)
    for _ in range(len(ys)):
        p_ys.append(ys.pop())

    result = int(p_ys.pop(0))
    for i in range(n-1):
        if p_ys[i + n - 1] == '+':
            result += int(p_ys[i])

    return result


testcase = 10

for i in range(testcase):
    N = int(input())
    S = str(input())
    print('#{} {}'.format(i + 1, calcul(S)))