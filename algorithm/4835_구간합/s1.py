import sys
sys.stdin = open('input.txt', 'r')


def maxmax(input_list):
    result = -655350
    for i in input_list:
        if i > result:
            result = i
    return result


def minmin(input_list):
    result = 655350
    for i in input_list:
        if i < result:
            result = i
    return result


def sumsum(input_list):
    result = 0
    for i in input_list:
        result += i
    return result


def gugan_sum(n, m, list_num):
    sum_list_size = n - m + 1
    result = []

    for i in range(sum_list_size):
        result.append(sumsum(list_num[i:i + m]))

    return maxmax(result) - minmin(result)


test_case = int(input())

for i in range(test_case):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    print('#{} {}'.format(i + 1, gugan_sum(N, M, num_list)))