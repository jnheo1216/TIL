## 1219 길찾기
import sys
sys.stdin = open('input.txt', 'r')


def find_load(leng, place_list):

    graph = {}  # 딕셔너리 사용
    for i in range(0, leng * 2, 2):
        if place_list[i] in graph:
            graph[place_list[i]].append(place_list[i + 1])
        else:
            graph[place_list[i]] = [place_list[i + 1]]

    # print(graph)

    visited = []
    stack = [0]
    while stack:  # dfs
        nod = stack.pop()
        if nod not in graph:  # 해당 노드에서 더 이상 연결된 노드가 없다면
            visited.append(nod)  # 방문했다는 기록만 남기고
            continue  # 다음 루프로
        if nod not in visited:  # 방문한 적이 없는 곳이라면
            visited.append(nod)  # 추가해주고
            stack += graph[nod]  # 스택에 해당 노드와 연결된 다른 노드들을 추가

        if 99 in visited:  # 만약 도착지에 왔다면
            return 1  # 바로 1반환

    return 0  # 도착지에 도달 못했으면 0반환


testcase = 10

for i in range(testcase):
    testcase_num, length = map(int, input().split())
    num_list = list(map(int, input().split()))
    print('#{} {}'.format(i+1, find_load(length, num_list)))