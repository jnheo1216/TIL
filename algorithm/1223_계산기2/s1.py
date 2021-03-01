## 1223 계산기2
import sys
sys.stdin = open('input.txt', 'r')


def calcul(s):
    p_ys = []  # 피연산자
    ys = []  # 연산자

    for i in s:
        if 48 <= ord(i) < 58:  # 숫자일때
            p_ys.append(i)
        else:  # 연산자일때
            ys.append(i)

    for _ in range(len(ys)):  # 연산자들도 합체해서 후위표기식으로 만들어줌
        p_ys.append(ys.pop())

    stack = []
    result = 0
    for i in range(len(p_ys)):
        tmp = p_ys.pop(0)  # 앞에서 하나를 빼줌
        if 48 <= ord(tmp) < 58:  # 숫자면 스택을 채워준다.
            stack.append(int(tmp))
        elif tmp == '*':  # 연산자 *의 경우
            a = stack.pop()
            b = stack.pop()  # 끝의 두개를 곱해서 다시 push해줌
            stack.append(a * b)
        elif tmp == '+':  # 연산자 +의 경우
            result += stack.pop()  # 맨 끝에 있는 값을 꺼내서 결과에 합쳐준다.
        # print(stack)
        # print(p_ys)

    return result + stack[0]  # 마지막 남은 하나까지 더해줘서 반환


testcase = 10

for i in range(testcase):
    N = int(input())
    S = str(input())
    print('#{} {}'.format(i + 1, calcul(S)))