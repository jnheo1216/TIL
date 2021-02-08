import sys
sys.stdin = open('input.txt', 'r')


def get_zomangkwan(N, buildings):
    result = 0
    for i in range(2, N - 2):
        n1 = buildings[i] - buildings[i - 1]
        n2 = buildings[i] - buildings[i - 2]
        n3 = buildings[i] - buildings[i + 1]
        n4 = buildings[i] - buildings[i + 2]
        if n1 > 0 and n2 > 0 and n3 > 0 and n4 > 0:
            result += min([n1, n2, n3, n4])
    return result


for i in range(10):
    N = int(input())
    buildings = list(map(int, input().split()))
    print('#{} {}'.format(i+1, get_zomangkwan(N, buildings)))