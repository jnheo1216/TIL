## 1860 진기야
import sys
sys.stdin = open('input.txt', 'r')


def bung_a_bbang(m, k, sonnim):
    sonnim.sort()  # 오름차순으로 정렬해준다
    if sonnim[0] < m:  # 처음 붕어빵 나오는 시간보다 첫손님이 빠르면 소용없음
        return 'Impossible'
    bbang = 0
    for i in range(1, sonnim[-1] + 1):  # 마지막 손님이 오는 시간까지만 반복문
        if not i % m:  # 빵이 m초에 k개만큼 나오므로
            bbang += k  # 더해줌
        for j in range(len(sonnim)):  # 해당 초에 방문하는 손님이 있는지 (손님이 한꺼번에 오는 경우도 있기 때문에 반복문으로 다 봐야함)
            if sonnim[j] == i:
                bbang -= 1
            elif sonnim[j] > i:  # 방문시간이 더 커지면 볼 필요 없으니 바로 탈출
                break

        if bbang < 0:  # 빵이 다 써서 없다면
            return 'Impossible'

    return 'Possible'


test_case = int(input())

for i in range(test_case):
    N, M, K = map(int, input().split())
    customer = list(map(int, input().split()))
    print('#{} {}'.format(i + 1, bung_a_bbang(M, K, customer)))