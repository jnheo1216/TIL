## 5356 의석아 화이팅
import sys
sys.stdin = open('input.txt', 'r')


def seat(length, words):
    result = ''
    for j in range(length):
        for i in range(5):
            if j >= len(words[i]):
                pass
            else:
                result += words[i][j]
    return result


testcase = int(input())

for i in range(testcase):
    word_list = []
    max_leng = 0
    for j in range(5):
        word = list(str(input()))
        if max_leng < len(word):
            max_leng = len(word)
        word_list.append(word)
    print('#{} {}'.format(i+1, seat(max_leng, word_list)))