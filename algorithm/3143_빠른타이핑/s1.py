import sys
sys.stdin = open('input.txt', 'r')


def use_brutal(a, b):
    i = 0
    j = 0
    len_a = len(a)
    len_b = len(b)

    while i < len_a and j < len_b:
        if a[i] != b[j]:
            i = i - j
            j = -1
        i += 1
        j += 1

    if j == len_b:
        return i - len_b
    else:
        return -1


def fast_typing(aword, bword):
    result = 0
    while True:
        if use_brutal(aword, bword) == -1:
            result += len(aword)
            break
        else:
            result += 1
            tmp = use_brutal(aword, bword)
            for i in range(len(bword)):
                aword.pop(tmp)

    return result


testcase = int(input())

for i in range(testcase):
    Aword, Bword = map(str, input().split())
    print('#{} {}'.format(i + 1, fast_typing(list(Aword), list(Bword))))