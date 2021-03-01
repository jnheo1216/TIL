## 1979 어디에 단어
import sys
sys.stdin = open('input.txt', 'r')


def is_k_in_list(k, list1line):  # 그 줄에 일치하는 공간 있나 없나
    count = 0
    result = []
    for i in list1line:  # 들어온 리스트에서
        if i == 1:  # 연속된 빈공간을
            count += 1  # 벽이나올때까지 다해주다가
        else:  # 벽이 나오면
            result.append(count)  # result에 넣어줌
            count = 0  # 이건 다시 0으로
    result.append(count)  # 마지막까지 더해줌

    count_k = 0
    for i in result:  # 빈공간들이 k와 일치하는지 확인
        if i == k:  # 일치하는 경우에는
            count_k += 1  # count_k에 합해서 반환

    return count_k


def where_word(n, k, input_list):
    result = 0
    # row에서 검색
    for i in input_list:
        result += is_k_in_list(k, i)
    # 검색 편하게 전치행렬로 바꾸기
    for i in range(n):
        for j in range(n):
            if i < j :
                input_list[i][j], input_list[j][i] = input_list[j][i], input_list[i][j]
    # col에서 검색
    for i in input_list:
        result += is_k_in_list(k, i)

    return result


testcase = int(input())

for i in range(testcase):
    N, K = (map(int, input().split()))
    nbyn_list = []
    for _ in range(N):
        nbyn_list.append(list(map(int, input().split())))
    print('#{} {}'.format(i+1, where_word(N, K, nbyn_list)))
