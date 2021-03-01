## 스택을 클래스로 만들기
class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not len(self.stack):
            return None
        else:
            returns = self.stack[len(self.stack) - 1]
            self.stack = self.stack[:len(self.stack) - 1]
            return returns

    def is_empty(self):
        if self.stack:
            return 0
        else:
            print("스택 비어있음")
            return 1


print('hello world')

stack1 = Stack()
print(stack1.stack)
stack1.push(13)
print(stack1.stack)

print('-----------------')

stack2 = Stack()
print(stack2.stack)
stack2.push(19)
print(stack2.stack)
stack2.pop()
print(stack2.stack)

print('----------------')

print(stack1.is_empty())
print(stack2.is_empty())

