## 1223 계산기2
import sys
sys.stdin = open('input.txt', 'r')


def calcul(s):
    p_ys = []  # 피연산자
    ys = []  # 연산자

    for i in s:
        if 48 <= ord(i) < 58:  # 숫자일때
            p_ys.append(i)
        elif i == '(':
            ys.append(i)
        elif i == ')':
            while ys[-1] != '(':  # 여는 괄호가 나올때까지
                p_ys.append(ys.pop())
            ys.pop()
        elif i == '*':
            while ys and ys[-1] == '*':
                p_ys.append(ys.pop())
            ys.append(i)
        elif i == '+':  # +
            while ys and ys[-1] != '(':
                p_ys.append(ys.pop())
            ys.append(i)

    for _ in range(len(ys)):  # 연산자들도 합체해서 후위표기식으로 만들어줌
        p_ys.append(ys.pop())
    print(p_ys)

    stack = []
    result = 0
    for i in range(len(p_ys)):
        # print(p_ys)
        # print(stack)
        # print(result)
        tmp = p_ys.pop(0)  # 앞에서 하나를 빼줌
        if 48 <= ord(tmp) < 58:  # 숫자면 스택을 채워준다.
            stack.append(int(tmp))
        elif tmp == '*':  # 연산자 *의 경우
            a = stack.pop()
            b = stack.pop()  # 끝의 두개를 곱해서 다시 push해줌
            stack.append(a * b)
        elif tmp == '+':  # 연산자 +의 경우
            a = stack.pop()
            b = stack.pop()  # 끝의 두개를 곱해서 다시 push해줌
            stack.append(a + b)

    return result + stack[0]


testcase = 10

for i in range(testcase):
    N = int(input())
    S = str(input())
    print('#{} {}'.format(i + 1, calcul(S)))



