import sys
sys.stdin = open('input.txt', 'r')


def minmax(size, numlist):
    max_value = numlist[0]
    min_value = numlist[0]
    for i in range(1, size):
        if max_value < numlist[i]:  # 최대값 찾기
            max_value = numlist[i]
        if min_value > numlist[i]:  # 최솟값 찾기
            min_value = numlist[i]

    return max_value - min_value


N = int(input())

for i in range(N):
    size = int(input())
    num_list = list(map(int, input().split()))
    print('#{} {}'.format(i+1, minmax(size, num_list)))