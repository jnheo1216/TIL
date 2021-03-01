## 2805 농작물
import sys
sys.stdin = open('input.txt', 'r')


def get_havest(n, batt_list):
    result = ''
    middle = n // 2
    size = 1

    for i in range(middle):  # 밭을 위아래로 반반 자름 # 위에거
        for j in batt_list[i][middle - size + 1:middle + size]:  # 중간 기준으로 슬라이싱.
            result += j
        size += 1  # 중간으로 갈수록 하나씩 증가시켜
    for i in range(middle, n):  # 아래거
        for j in batt_list[i][middle - size + 1:middle + size]:  # 중간 기준으로 슬라이싱
            result += j
        size -= 1  # 끝으로 갈수록 하나씩 감소시켜

    count = 0
    for i in result:
        count += int(i)  # 나온 값 전부 더해줘서 반환

    return count


def hav_index(n, batt_list):  # 인덱스?
    result = ''
    middle = n // 2
    size = 1

    for i in range(middle):  # 밭을 위아래로 반반 자름 # 위에거
        for j in range(middle - size + 1, middle + size):
            result += batt_list[i][j]
        size += 1  # 중간으로 갈수록 하나씩 증가시켜
    for i in range(middle, n):  # 아래거
        for j in range(middle - size + 1, middle + size):  # 바꾼건 이부분 하나 # 이렇게 하는게 맞는가?
            result += batt_list[i][j]
        size -= 1  # 끝으로 갈수록 하나씩 감소시켜

    count = 0
    for i in result:
        count += int(i)  # 나온 값 전부 더해줘서 반환

    return count


testcase = int(input())

for i in range(testcase):
    N = int(input())
    havest = [list(str(input())) for _ in range(N)]

    print('#{} {}'.format(i + 1, get_havest(N, havest)))
    print('#{} {}'.format(i + 1, hav_index(N, havest)))