## 4047 영준아 뭔 그런걸 해
import sys
sys.stdin = open('input.txt', 'r')


def card_check(card_list):
    card_dict = {'S': [], 'D': [], 'H': [], 'C': [], }
    for i in range(len(card_list) // 3):
        if card_list[1 + i * 3:3 + i * 3] in card_dict[card_list[0 + i * 3]]:
            return 'ERROR'
        else:
            card_dict[card_list[0 + i * 3]].append(card_list[1 + i * 3:3 + i * 3])

    result = str(13 - len(card_dict['S'])) + ' ' + str(13 - len(card_dict['D'])) + ' ' +  str(13 - len(card_dict['H'])) + ' ' +  str(13 - len(card_dict['C']))

    return result


testcase = int(input())

for i in range(testcase):
    cards = str(input())
    print('#{}'.format(i + 1), card_check(cards))
