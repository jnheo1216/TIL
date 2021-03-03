## 6019
import sys
sys.stdin = open('input.txt', 'r')


def noiman(d, a, b, f):
    return d / (a + b) * f


test_case = int(input())

for i in range(test_case):
    D, A, B, F = map(int, input().split())
    print('#{} {}'.format(i + 1, noiman(D, A, B, F)))