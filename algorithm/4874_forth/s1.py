## 4874 후위연산하기
import sys
sys.stdin = open('input.txt', 'r')


def calcul(numbers):
    stack = []  # 숫자넣을 스택
    while numbers:
        if numbers[0] == '.':  # 만약 끝나는 신호가 오면
            break

        if numbers[0].isdigit():  # 들어오는 것이 숫자라면 (원래 try except로 했는데 이게 더 나은거같기도)
            stack.append(int(numbers[0]))  # 숫자에 추가 
        else:  # 연산자일시
            if len(stack) >= 2:  # 스택에 쌓여있는 수가 2개 이상이여야 성립
                if numbers[0] == '+':
                    tmp = stack[-2] + stack[-1]
                elif numbers[0] == '*':
                    tmp = stack[-2] * stack[-1]
                elif numbers[0] == '/':
                    tmp = stack[-2] / stack[-1]
                elif numbers[0] == '-':
                    tmp = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()  # 2개 pop
                stack.append(int(tmp))  # 계산값 추가 (정수 아니면 틀린걸로 하더라)
            else:
                return 'error'

        numbers.pop(0)  # 다음 요소로 가기 위해 

    if len(stack) == 1:  # 길이가 1이 아니라면 계산 이상한 것임
        return stack[-1]
    else:
        return 'error'


test_case = int(input())

for i in range(test_case):
    num_list = list(map(str, input().split()))
    print('#{} {}'.format(i + 1, calcul(num_list)))