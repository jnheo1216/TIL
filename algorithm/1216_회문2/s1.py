## 1215 회문1
import sys
sys.stdin = open('input.txt', 'r')


def my_find(M):
    for i in range(N):
        for j in range(N - M + 1):
            for k in range(M // 2):
                if words[i][j+k] != words[i][j+M-1-k]:
                    break
                elif k == M // 2 - 1:
                    return M
            for k in range(M // 2):
                if words[j+k][i] != words[j+M-1-k][i]:
                    break
                elif k == M // 2 - 1:
                    return M

    return 0


for tc in range(10):
    tc_num = int(input())
    N = 100
    words = [input() for i in range(N)]

    for i in range(N, 0, -1):
        ans = my_find(i)
        if ans != 0:
            break

    print("#{} {}".format(tc_num, ans))