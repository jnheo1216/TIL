import sys
sys.stdin = open('input.txt', 'r')


def most_card_choice(card_list):
    numbers = [0] * 10  # 숫자카드가 몇개 있는지 카운트하기 위해 빈 리스트

    for i in card_list:
        numbers[int(i)] += 1  # 각 숫자가 몇개씩 있나 리스트에 더하기

    max_value_locate = 0
    max_value = numbers[0]

    for j in range(10):  # 어떤 숫자가 가장 많나
        if max_value <= numbers[j]:
            max_value = numbers[j]  # 최대 개수
            max_value_locate = j  # 최대 카드의 숫자

    return max_value_locate, max_value


test_case = int(input())

for i in range(test_case):
    N = int(input())
    num_list = input()
    max_loc, max_val = most_card_choice(num_list)
    print('#{} {} {}'.format(i + 1, max_loc, max_val))