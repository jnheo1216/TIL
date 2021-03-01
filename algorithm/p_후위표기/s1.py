"""
수식 문자열을 읽어서 피연산자는 바로 출력하고 연산자는 stack에 push하여
수식이 끝나면 스택의 남아있는 연산자를 모두 pop하여 출력하시오.
(연산자는 사칙연산만 활용)

예시 입력)
2+3*4/5

예시 출력)
2345/*+
"""

s = '2+3*4/5'

p_ys = []
ys = []
for i in s:
    if 48 <= ord(i) < 58:
        p_ys.append(i)
    else:
        ys.append(i)

for _ in range(len(ys)):
    p_ys.append(ys.pop())

print(p_ys)

# print(ord('9'))