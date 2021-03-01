## 5789 상자바꾸기
import sys
sys.stdin = open('input.txt', 'r')


def change_box_hyunju(n, q, LR_list):
    result = [0] * n
    for i in range(q):  # 버스노선같은 느낌으로
        for j in range(LR_list[i][0], LR_list[i][-1]+1):
            result[j-1] = i+1

    return result


test_case = int(input())

for i in range(test_case):
    N, Q = map(int, input().split())
    iLR = []
    for _ in range(Q):
        iLR.append(list(map(int, input().split())))
    print('#{}'.format(i+1), *change_box_hyunju(N, Q, iLR))