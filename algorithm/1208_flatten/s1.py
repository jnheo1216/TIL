import sys
sys.stdin = open('input.txt', 'r')


def maxmax(input_list):  # 최댓값 찾기
    result = -65535
    for i in input_list:
        if i > result:
            result = i
    return result


def minmin(input_list):  # 최솟값 찾기
    result = 65535
    for i in input_list:
        if i < result:
            result = i
    return result


def indexindex(find_value, input_list):  # 해당 밸류의 인덱스 찾기
    for idx, val in enumerate(input_list):
        if val == find_value:
            return idx
    return None


def flatten_no_nejang(n, box_list):  # 내장함수 없는 버전
    for i in range(n):
        box_list[indexindex(maxmax(box_list), box_list)] -= 1  # 최대값의 요소에 마이너스 1
        box_list[indexindex(minmin(box_list), box_list)] += 1  # 최솟값의 요소에 플러스 1

        if maxmax(box_list) - minmin(box_list) <= 1:  # 차이가 1 이하라면 바로 탈출
            break

    return maxmax(box_list) - minmin(box_list)


def flatten(n, box_list):  # 내장함수 있는 버전
    for i in range(n):
        box_list[box_list.index(max(box_list))] -= 1
        box_list[box_list.index(min(box_list))] += 1

        if max(box_list) - min(box_list) <= 1:
            break

    return max(box_list) - min(box_list)


test_case = 10

for i in range(test_case):
    N = int(input())
    num_list = list(map(int, input().split()))
    print('#{} {}'.format(i + 1, flatten(N, num_list)))