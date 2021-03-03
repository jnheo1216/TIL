"""
문제2. 기본 Queue 구현 - 클래스 구현 (가변)
 - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
 - 큐에서 세 개의 데이터를 차례로 꺼내어 출력
  (1, 2, 3을 차례대로 출력해야 함)
"""


class Queue:
    # 생성자 함수
    def __init__(self):
        self.queue = []

    # isEmpty
    def is_empty(self):
        if not self.queue:
            return True
        else:
            return False

    # enQueue
    def enqueue(self, val):
        self.queue.append(val)

        # deQueue

    def dequeue(self):
        return self.queue.pop(0)

    # size
    def size(self):
        return len(self.queue)


# 1. queue 인스턴스 생성
my_queue = Queue()
print(my_queue)
# 2. queue가 비었는지 확인
print(my_queue.is_empty())

# 3. 1, 2, 3 원소를 queue에 삽입
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

# 4. 원소가 정상적으로 삽입되었는지 확인 / 사이즈 확인 / 비었는지 여부 확인
print(my_queue.is_empty())
print(my_queue.size())

# 5. queue에서 원소 삭제 후 반환 & 원소 확인 / 사이즈 확인
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.size())
