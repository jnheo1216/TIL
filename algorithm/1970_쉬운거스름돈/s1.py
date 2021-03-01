## 1970 거스름돈
import sys
sys.stdin = open('input.txt', 'r')


def exchange(input_money):
    ex_money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = ''

    for i in ex_money:  # 큰돈부터
        result += str(input_money // i) + ' '  # 뺄수 있는 만큼
        input_money -= (input_money // i) * i  # 남은돈은 빼줘서 구함

    return result


test_case = int(input())

for i in range(test_case):
    number = int(input())
    print('#{}'.format(i+1))
    print(exchange(number))