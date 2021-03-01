import sys
sys.stdin = open('input.txt', 'r')

vertex, edge = map(int, input().split())
num_list = list(map(int, input().split()))

print(vertex, edge)
print(num_list)

graph = [[0] * (vertex + 1) for _ in range(vertex + 1)]

for i in range(edge):
    graph[num_list[i * 2]][num_list[i * 2 + 1]] = 1
    graph[num_list[i * 2 + 1]][num_list[i * 2]] = 1

for i in graph:
    print(i)
## graph 생성 완료
print()


stack = []
visited = [0] * (vertex + 1)

stack.append(1)  # 시작지점

while stack:
    nod = stack.pop()  # 스택에서 꺼내옴
    visited[nod] = 1

    print('현재 위치 : {}'.format(nod))  # 이것이 현재 위치

    for i in range(1, vertex + 1):
        if graph[nod][i] == 1 and visited[i] == 0:
            stack.append(i)
            print('{}로 이동 가능'.format(i))  # 안가본곳 중 이동가능한 곳들

    record = []
    for idx, val in enumerate(visited):  # 방문한 곳들의 번호를 기록
        if val == 1:
            record.append(idx)

    print('지나온길 : {}'.format(record))
    print()