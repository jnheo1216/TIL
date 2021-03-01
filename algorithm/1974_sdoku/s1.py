## 1974 sdokus
import sys
sys.stdin = open('input.txt', 'r')


def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


def sdoku_test(sdoku_list):
    mobum = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # 가로
    for i in range(9):
        test_list = []
        for j in range(9):
            test_list.append(sdoku_list[i][j])
        s_test = bubble_sort(test_list)
        if s_test != mobum:
            return 0
    # 세로
    for j in range(9):
        test_list = []
        for i in range(9):
            test_list.append(sdoku_list[i][j])
        s_test = bubble_sort(test_list)
        if s_test != mobum:
            return 0
    # 사각 0,0 0,3 0,6 3,0 3,3 3,6 6,0 6,3 6,6
    for n in range(3):
        for k in range(3):
            test_list = []
            for i in range(n * 3, n * 3 + 3):
                for j in range(k * 3, k * 3 + 3):
                    test_list.append(sdoku_list[i][j])
            s_test = bubble_sort(test_list)
            if s_test != mobum:
                return 0

    return 1


testcase = int(input())

for i in range(testcase):
    sdoku = [list(map(int, input().split())) for _ in range(9)]
    print('#{} {}'.format(i+1, sdoku_test(sdoku)))
