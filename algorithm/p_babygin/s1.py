import sys
sys.stdin = open('input.txt', 'r')


def babygin(cards):
    num_count = [0]*10
    for i in cards:
        num_count[int(i)] += 1

    count = 0
    for j in range(10):
        if num_count[j] >= 3:
            count += 1
            num_count[j] -= 3
    for j in range(10):
        if num_count[j] >= 3:
            count += 1
            num_count[j] -= 3

    relay = 0
    for k in range(10):
        if num_count[k] > 0:
            relay += 1
            num_count[k] -= 1
        else:
            relay = 0
        if relay > 2:
            count += 1
            break
    for k in range(10):
        if num_count[k] > 0:
            relay += 1
            num_count[k] -= 1
        else:
            relay = 0
        if relay > 2:
            count += 1
            break

    if count == 2:
        return 1
    else:
        return 0


N = int(input())

for i in range(N):
    card_list = input()
    print('#{} {}'.format(i+1, babygin(card_list)))