## 1225 암호생성기
import sys
sys.stdin = open('input.txt', 'r')


def make_password(numlist):
    pass_button = False
    while True:
        for i in range(1, 6):
            tmp = numlist.pop(0)
            tmp -= i
            numlist.append(tmp)
            if tmp <= 0:
                pass_button = True
                numlist[-1] = 0
                break
        if pass_button:
            break
    return numlist


test_case = 10

for _ in range(test_case):
    N = int(input())
    num_list = list(map(int, input().split()))
    print('#{}'.format(N), *make_password(num_list))