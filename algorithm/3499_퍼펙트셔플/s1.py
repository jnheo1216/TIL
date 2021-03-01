## 3499 퍼펙트셔플
import sys
sys.stdin = open('input.txt', 'r')


def shupple(n, deck):
    mid = n // 2
    if n % 2:
        mid += 1

    front_deck = deck[:mid]
    back_deck = deck[mid:]

    result = []
    for i in range(n):
        if i % 2:
            result.append(back_deck.pop(0))
        else:
            result.append(front_deck.pop(0))

    return result


testcase = int(input())

for i in range(testcase):
    N = int(input())
    cards = list(map(str, input().split()))
    print('#{}'.format(i + 1), *shupple(N, cards))