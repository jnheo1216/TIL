## 2005 파스칼
import sys
sys.stdin = open('input.txt', 'r')


def pascal_triangle(n):
    if n == 1:
        return [[1]]
    result = [[1], [1, 1]]
    for i in range(2, n):
        tmp = [1]
        for j in range(1, i):
            tmp.append(result[i-1][j-1] + result[i-1][j])
        tmp.append(1)
        result.append(tmp)

    return result


testcase = int(input())

for i in range(testcase):
    N = int(input())
    tri = pascal_triangle(N)
    print('#{}'.format(i+1))
    for i in tri:
        print(*i)