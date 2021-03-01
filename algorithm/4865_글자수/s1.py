import sys
sys.stdin = open('input.txt', 'r')


def geuljasu(nword, mword):
    result = 0
    for i in nword:
        count = 0
        for j in mword:
            if i == j:
                count += 1
        if count > result:
            result = count
    return result


testcase = int(input())

for i in range(testcase):
    Nword = input()
    Mword = input()
    print('#{} {}'.format(i+1, geuljasu(Nword, Mword)))