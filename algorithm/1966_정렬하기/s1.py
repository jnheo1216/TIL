## 1966 정렬
import sys
sys.stdin = open('input.txt', 'r')


def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


def selection_sort(numbers):
    for i in range(len(numbers)):
        tmp = numbers[i]
        idx = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < tmp:
                tmp = numbers[j]
                idx = j
        numbers[i], numbers[idx] = tmp, numbers[i]

    return numbers


def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = numbers[0]
        left = []
        right = []
        for i in range(1, len(numbers)):
            if numbers[i] <= pivot:
                left.append(numbers[i])
            else:
                right.append(numbers[i])

        return [*quick_sort(left), pivot, *quick_sort(right)]


test_case = int(input())

for i in range(test_case):
    N = int(input())
    number_list = list(map(int, input().split()))
    # print('#{}'.format(i+1), *bubble_sort(number_list))
    print('#{}'.format(i + 1), *quick_sort(number_list))
