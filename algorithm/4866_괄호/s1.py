## 4866
import sys
sys.stdin = open('input.txt', 'r')


def gualho(sentense):
    stack = ['x']
    for i in range(len(sentense)):
        if sentense[i] == '(' or sentense[i] == '{' or sentense[i] == '[':
            stack.append(sentense[i])
        elif sentense[i] == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                return 0
        elif sentense[i] == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                return 0
        elif sentense[i] == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                return 0

    if len(stack) > 1:
        return 0
    elif len(stack) == 1:
        return 1


testcase = int(input())

for i in range(testcase):
    N = list(str(input()))

    print('#{} {}'.format(i + 1, gualho(N)))
