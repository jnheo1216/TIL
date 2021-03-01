import sys
sys.stdin = open('input.txt', 'r')


def bubble_special_sort(numbers):
    for i in range(len(numbers)):
        if i % 2:  # 홀수번
            for j in range(i+1, len(numbers)):
                if numbers[i] > numbers[j]:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
        else:  # 짝수번
            for j in range(i+1, len(numbers)):
                if numbers[i] < numbers[j]:
                    numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers


def selection_spectial_sort(numbers):
    for i in range(len(numbers)):
        tmp = numbers[i]
        idx = i
        if i % 2:  # 홀수번
            for j in range(i+1, len(numbers)):
                if numbers[j] < tmp:
                    tmp = numbers[j]
                    idx = j
        else:  # 짝수번
            for j in range(i+1, len(numbers)):
                if numbers[j] > tmp:
                    tmp = numbers[j]
                    idx = j
        numbers[i], numbers[idx] = tmp, numbers[i]

    return numbers


test_case = int(input())

for i in range(test_case):
    N = int(input())
    num_list = list(map(int, input().split()))
    print('#{}'.format(i+1), *bubble_special_sort(num_list)[:10])
    # print('#{}'.format(i+1), *selection_spectial_sort(num_list)[:10])

a = '012345'
print(a[1:9])
