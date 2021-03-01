import sys
sys.stdin = open('input.txt', 'r')


def paper_count(n):  # 1 -> 1, 2 -> 3, 3 -> 5, 4 -> 11, 5 -> 21 # 재귀 각
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return paper_count(n - 2) * 2 + paper_count(n - 1)


testcase = int(input())

for i in range(testcase):
    N = int(input())
    N = N // 10
    # print(N)
    print('#{} {}'.format(i + 1, paper_count(N)))
    # 1 -> 1, 2 -> 3, 3 -> 5, 4 -> 11, 5 -> 21