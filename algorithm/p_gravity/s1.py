import sys
sys.stdin = open('input.txt', 'r')


def get_fall_height(size, boxes_list):
    result = []

    for i in range(size):  # 각 박스 줄마다
        count = 0
        for j in range(i+1, size):  # 그 다음 박스들로, 오른쪽으로 떨어지므로 왼쪽 고려 x
            if boxes_list[j] >= boxes_list[i]:  # 높이가 같거나 크면 낙차 늘리지 말고
                pass
            else:  # 다음 박스 줄이 나보다 작으면 낙차가 늘어난다
                count += 1
        result.append(count)  # 각 박스 줄마다 낙차를 리스트에 append

    return max(result)  # 낙차 중 최대값 반환


N = int(input())  # 테스트케이스가 몇개냐

for i in range(N):
    size = int(input())
    boxes_list = list(map(int, input().split()))
    print('#{} {}'.format(i+1, get_fall_height(size, boxes_list)))