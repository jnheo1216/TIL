## 1979 어디에 단어
import sys
sys.stdin = open('input.txt', 'r')


def is_palindrome(leng, palins):
    reverse_palin = [palins[i] for i in range(leng - 1, -1, -1)]
    if reverse_palin == palins:
        return 1
    else:
        return 0


def palindrome(n, m, input_list):
    result = 0
    # row 검색
    for i in input_list:
        for j in range(n - m + 1):
            if is_palindrome(m, i[j:j+m]):  # 회문인가 아닌가
                return i[j:j+m]  # 맞다면 바로 리턴
    # 검색 편하게 전치행렬로 바꾸기
    for i in range(n):
        for j in range(n):
            if i < j :
                input_list[i][j], input_list[j][i] = input_list[j][i], input_list[i][j]
    # col 검색
    for i in input_list:
        for j in range(n - m + 1):
            if is_palindrome(m, i[j:j+m]):  # 회문인가 아닌가
                return i[j:j+m]  # 맞다면 바로 리턴


testcase = int(input())

for j in range(testcase):
    N, M = (map(int, input().split()))
    nbyn_list = [0] * N
    for i in range(N):
        nbyn_list[i] = list(input().strip())

    resultlist = palindrome(N, M, nbyn_list)
    result = ''
    for i in resultlist:
        result += i

    print('#{} {}'.format(j+1, result))


