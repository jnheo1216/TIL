import sys
sys.stdin = open('input.txt', 'r')


def charge_point(k, n, m, charger_location):
    bus_locate = 0  # 버스가 위치하는 지점
    charge_count = 0  # 충전한 횟수

    while True:
        bus_locate += k  # 버스가 이동할 수 있는 최대 거리
        if bus_locate >= n:  # 탈출 조건
            break
        for i in range(1, m):
            if bus_locate < charger_location[i] and bus_locate >= charger_location[i-1]:  # 버스가 움직이는 최대거리 바로 전에 있는 충전소 찾기
                bus_locate = charger_location[i-1]  # 충전한 충전소부터 출발해야함
            if charger_location[i] - charger_location[i-1] > k:  # 충전소 사이의 거리가 버스 최대 거리보다 크면 못가니까 바로 반환
                return 0

        charge_count += 1   # 충전횟수 추가해줌

    return charge_count


test_case = int(input())

for i in range(test_case):
    K, N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    print('#{} {}'.format(i + 1, charge_point(K, N, M, num_list)))