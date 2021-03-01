## 1959 두개의 숫자열
import sys
sys.stdin = open('input.txt', 'r')


def list_mul(list1, list2):
    result = 0
    for i in range(len(list1)):
        result += list1[i] * list2[i]

    return result


def two_num_list(len1, len2, list1, list2):
    if len1 > len2:  # 위의 리스트가 짧은지 아래 리스트가 짧은지 아니면 길이가 같은지
        replay = len1 - len2 + 1  # 반복횟수는 두 리스트 길이의 차에 1더하기
        stop, move = list1, list2  # 움직일 리스트와 아닌 리스트
    elif len2 > len1:
        replay = len2 - len1 + 1
        stop, move = list2, list1
    else:
        return list_mul(list1, list2)

    result = -1000

    for i in range(replay):
        multi_sum = 0
        for j in range(len(move)):
            multi_sum += move[j] * stop[j+i]  # 곱해서 더해줌
        if multi_sum > result:  # 큰지 작은지 비교
            result = multi_sum

    return result


test_case = int(input())

for i in range(test_case):
    list_len1, list_len2 = map(int, input().split())
    num_list1 = list(map(int, input().split()))
    num_list2 = list(map(int, input().split()))
    print('#{} {}'.format(i+1, two_num_list(list_len1, list_len2, num_list1, num_list2)))