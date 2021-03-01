## 1213 string
import sys
sys.stdin = open('input.txt', 'r', encoding='UTF8')


def search(key, strings):
    result = 0
    if strings.find(key) == -1:  # 없으면
        return 0
    else:  # 있으면
        while len(key) <= len(strings):
            if strings.find(key) == -1:
                break
            strings = strings[strings.find(key) + len(key):]
            result += 1
        return result


test_case = 10

for _ in range(test_case):
    N = int(input())
    search_word = input().strip()
    sentence = input().strip()
    print('#{} {}'.format(N, search(search_word, sentence)))