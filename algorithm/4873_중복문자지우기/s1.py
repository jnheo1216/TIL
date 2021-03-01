## 4873 중복문자지우기
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

    return len(stack)  # 리스트의 길이 반환


testcase = int(input())

for i in range(testcase):
    words = list(str(input()))
    print('#{} {}'.format(i + 1, del_word(words)))