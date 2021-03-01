## 1234 비밀번호
import sys
sys.stdin = open('input.txt', 'r')


def del_word(words_input):
    stack = []
    for i in words_input:
        if not stack:  # 아무것도 없을때는
            stack.append(i)  # 추가
        elif i == stack[-1]:  # 중복이라면
            stack.pop()  # 삭제
        else:  # 중복 아니면
            stack.append(i)  # 추가

    result = ''
    for i in stack:
        result += i

    return result  # 결과는 str로


testcase = 10

for i in range(testcase):
    length, words = map(str, input().split())
    words = list(words)
    print('#{} {}'.format(i + 1, del_word(words)))