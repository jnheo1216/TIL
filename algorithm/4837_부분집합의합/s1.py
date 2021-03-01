## 4837 부분집합의합
import sys
sys.stdin = open('input.txt', 'r')


def sumsum(inputlist):
    result = 0
    for i in inputlist:
        result += i
    return result


def get_bubun_sum(n, k):
    list12 = [i for i in range(1, 13)]
    arr_bubun = []
    count = 0

    for i in range(1 << len(list12)):
        tmp = []
        for j in range(len(list12)):
            if i & (1 << j):
                tmp.append(list12[j])
        if len(tmp) == n:  # 부분집합의 길이가 n인 것들만
            arr_bubun.append(tmp)  # 추가

    for i in arr_bubun:  # 부분집합들 중에
        if sumsum(i) == k:  # 합이 k인 것이 있으면
            count += 1  # 카운트 1올려줌

    return count


testcase = int(input())

for i in range(testcase):
    N, K = map(int, input().split())
    print('#{}'.format(i+1), get_bubun_sum(N, K))