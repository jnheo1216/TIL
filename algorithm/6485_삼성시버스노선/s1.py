## 6485 샘숭 버스노선
import sys
sys.stdin = open('input.txt', 'r')

#
# def get_nosun(buslines, busstops):
#     result = ''
#     bus_stop_5000 = [0] * 5001
#
#     for busline in buslines:
#         for j in range(busline[0], busline[1]+1):
#             bus_stop_5000[j] += 1
#
#     for busstop in busstops:
#         result += str(bus_stop_5000[busstop]) + ' '
#
#     return result
#
#
# test_case = int(input())
#
# busline_list = []
# busstop_list = []
#
# for i in range(test_case):
#     N = int(input())
#     for j in range(N):
#         busline_list.append(list(map(int, input().split())))
#     P = int(input())
#     for k in range(P):
#         busstop_list.append(int(input()))
#     print('#{} {}'.format(i+1, get_nosun(busline_list, busstop_list)))
#

test_case = int(input())

for i in range(test_case):
    bus_stop_5000 = [0] * 5001  # 5천개의 노선
    result = '#{} '.format(i+1)
    N = int(input())
    for j in range(N):
        start, end = map(int, input().split())  # 노선의 시작점과 끝점
        for k in range(start, end + 1):
            bus_stop_5000[k] += 1  # 노선이 지나는 정류장 표시
    P = int(input())  # 들어올 정류장 개수
    for j in range(P):
        busstop = int(input())
        result += str(bus_stop_5000[busstop])  # 해당 정류장에 몇개 노선이 지나는지
        result += ' '
    print(result)

#
# def get_nosun(buslines, busstops):
#     result = [0] * len(busstops)
#     for idx, busstop in enumerate(busstops):
#         for busline in buslines:
#             lines = [i for i in range(busline[0], busline[-1] + 1)]
#             if busstop in lines:
#                 result[idx] += 1
#
#     return_value = ''
#     for i in result:
#         return_value += str(i) + ' '
#
#     return return_value
#
#
# test_case = int(input())
#
# busline_list = []
# busstop_list = []
#
# for i in range(test_case):
#     N = int(input())
#     for j in range(N):
#         busline_list.append(list(map(int, input().split())))
#     P = int(input())
#     for k in range(P):
#         busstop_list.append(int(input()))
#     print('#{} {}'.format(i + 1, get_nosun(busline_list, busstop_list)))