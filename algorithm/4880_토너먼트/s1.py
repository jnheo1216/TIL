## 4880 토너먼트
import sys
sys.stdin = open('input.txt', 'r')


def fight(a, b):
    if a[1] > b[1]:
        a, b = b, a

    if a[1] == 1 and b[1] == 2:  # 가위 바위
        return b
    elif a[1] == 2 and b[1] == 3:  # 바위 보
        return b
    elif a[1] == 1 and b[1] == 3:  # 가위 보
        return a
    else:
        return a


def rock_si_pa(cards):
    if len(cards) == 1:
        return cards[0]
    elif len(cards) == 2:
        return fight(cards[0], cards[1])
    else:
        if len(cards) % 2:
            return fight(rock_si_pa(cards[:len(cards) // 2 + 1]), rock_si_pa(cards[len(cards) // 2 + 1:]))
        else:
            return fight(rock_si_pa(cards[:len(cards) // 2]), rock_si_pa(cards[len(cards) // 2:]))


testcase = int(input())

for i in range(testcase):
    N = int(input())
    cards_list = list(map(int, input().split()))
    new_cards = [(i + 1, cards_list[i]) for i in range(N)]  # 각각 인덱스를 붙인 리스트 새로 만듬
    print('#{} {}'.format(i + 1, rock_si_pa(new_cards)[0]))

myarr = [1, 2, 4]
print(len(myarr))
print(myarr[:len(myarr) // 2 + 1])
print(myarr[len(myarr) // 2 + 1:])