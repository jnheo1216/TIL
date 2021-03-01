stack = []


def push(item):
    stack.append(item)


def pop():
    global stack
    if not len(stack):
        return None
    else:
        returns = stack[len(stack) - 1]
        stack = stack[:len(stack) - 1]
        return returns


push(1)
push(2)
push(3)
print(stack)

print('------')

# 가장 뒤(위)부터 pop
print(pop())
print(pop())
print(pop())
