## 4408 돌아가
import sys
sys.stdin = open('input.txt', 'r')


def find_load(n, student_route):
    room = [0] * 401
    for i in range(n):
        start = student_route[i][0]
        end = student_route[i][1]  # 시작점이 끝점보다 큰 경우에는 바꿔줘야 계산에 용이함
        if start > end:
            start, end = end, start
        if start % 2 == 1 and end % 2 == 1:  # 홀수방에서 홀수방
            for j in range(start, end + 2):
                room[j] += 1
        elif start % 2 == 0 and end % 2 == 0:  # 짝수방에서 짝수방
            for j in range(start - 1, end + 1):
                room[j] += 1
        elif start % 2 == 1 and end % 2 == 0:  # 훌수방에서 짝수방
            for j in range(start, end + 1):
                room[j] += 1
        elif start % 2 == 0 and end % 2 == 1:  # 짝수방에서 홀수방
            for j in range(start - 1, end + 2):
                room[j] += 1

    return max(room)


testcase = int(input())

for i in range(testcase):
    N = int(input())
    students = [list(map(int, input().split())) for _ in range(N)]
    print('#{} {}'.format(i + 1, find_load(N, students)))