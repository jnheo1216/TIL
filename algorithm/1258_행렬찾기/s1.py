## 1258 행렬찾기
import sys
sys.stdin = open('input.txt', 'r')


def find_range(n, x, y, input_list):  # 어디까지 사각형일지 알아보는 함수
    countx = 0
    county = 0
    tmpx = x

    for _ in range(n - x):  # x축으로 길이 세기
        if x < n and input_list[x][y] > 0:
            countx += 1
        else:
            break
        x += 1

    x = tmpx
    for _ in range(n - y):  # y축으로 길이 세기
        if y < n and input_list[x][y] > 0:
            county += 1
        else:
            break
        y += 1

    return [countx, county]  # 사각형 크기 반환


def find_arr(n, chemi_list):
    result = []
    count = 0

    for i in range(n):
        for j in range(n):  # 완전탐색
            if chemi_list[i][j] > 0:  # 0보다 크면
                count += 1  # 찾았으니 갯수 더해주고
                tmplist = find_range(n, i, j, chemi_list)  # 사각형의 크기 알아옴
                result.append(tmplist)
                for a in range(tmplist[0]):  # 알아낸 사각형은 그 크기만큼 전부 0으로 바꿔줌
                    for b in range(tmplist[1]):
                        chemi_list[i+a][j+b] = 0

    sorted_result = sorted(result, key=lambda x: x[0])  # 일단 행으로 정렬하고
    sorted_result = sorted(sorted_result, key=lambda x: x[0]*x[1])  # 행열의 곱으로 정렬
    return count, sorted_result


testcase = int(input())

for i in range(testcase):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(N)]
    # for q in num_list:
    #     print(q)
    number, result_lists = find_arr(N, num_list)
    print('#{} {}'.format(i + 1, number), end=' ')
    for q in result_lists:
        print(*q, end=' ')
    print()