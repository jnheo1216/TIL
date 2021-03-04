## 5099 피자
import sys
sys.stdin = open('input.txt', 'r')


def pizzafire(n, m, pizzas):
    queue = []  # 피자 화덕
    done = []  # 다 된 피자 빼는 곳
    for i in range(n):  # 일단 첫판 들어감
        queue.append(pizzas.pop(0))

    while True:
        for i in range(n):
            tmp = queue.pop(0)  # 피자 꺼냄
            tmp[1] = tmp[1] // 2  # 논리적으론 이게 앞이긴 하지만 아무튼 피자 치즈 녹음!
            if tmp[1] <= 0:  # 치즈 다 녹았나 확인
                done.append(tmp)  # 다 녹았으니까 출하
                if pizzas:  # 아직 안 구운 피자 있다면
                    queue.append(pizzas.pop(0))  # 화덕에 추가
            else:
                queue.append(tmp)  # 안익었으면 화덕에 다시 넣기
            if len(done) == m - 1:  # 피자가 하나 빼고 다 출하 되었다면
                return queue[0][0]  # 화덕에 마지막 남은 피자의 인덱스가 리턴


testcase = int(input())

for i in range(testcase):
    N, M = map(int, input().split())
    pizza_list = list(map(int, input().split()))
    new_pizza_list = [[j + 1, pizza_list[j]] for j in range(M)]  # 각각 인덱스를 붙인 리스트 새로 만듬
    print('#{} {}'.format(i + 1, pizzafire(N, M, new_pizza_list)))