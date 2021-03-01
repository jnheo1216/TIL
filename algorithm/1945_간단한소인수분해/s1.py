## 1945 간단한 소인수분해
import sys
sys.stdin = open('input.txt', 'r')


def simple_factorization(input_number):
    insus = [2, 3, 5, 7, 11]
    result = [0, 0, 0, 0, 0]

    for idx, insu in enumerate(insus):
        while True:
            if not input_number % insu:  # 나머지가 나오지 않을 때 까지 나눠줌
                result[idx] += 1
                input_number = input_number // insu
            else:  # 나머지가 있다면 바로 탈출시킴
                break

    return_value = ''
    for i in result:
        return_value += str(i) + ' '

    return return_value


test_case = int(input())

for i in range(test_case):
    number = int(input())
    print('#{} {}'.format(i+1, simple_factorization(number)))