## 5102 노드의 거리
import sys
sys.stdin = open('input.txt', 'r')


def minimum_route(v, start, end, nodedict):
    visit = [start]
    queue = nodedict[start]
    distance = [0] * (v + 1)
    for i in queue:
        distance[i] = 1

    while queue:  # 큐가 있는 동안 반복
        tmp = queue.pop(0)
        if distance[end]:  # 만약 도착지점 까지 거리가 측정되었다면
            return distance[end]  # 바로 반환

        if not tmp in visit:  # 꺼낸 것이 방문기록에 없을 경우에
            visit.append(tmp)  # 추가해주고
            if tmp in nodedict:  # 연결된 다른 노드를
                for i in nodedict[tmp]:
                    queue.append(i)  # 큐에 추가
                    if not i in visit and distance[i] == 0:  # 추가하는 것들 중에 해당 노드에 아직 방문한적 없고 거리 측정도 안했다면
                        distance[i] = distance[tmp] + 1  # 이전 노드 + 1 만큼 거리

    return distance[end]


testcase = int(input())

for j in range(testcase):
    V, E = map(int, input().split())
    nodes = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    graph = {}
    for i in range(E):  # 딕셔너리로 만들기
        if nodes[i][0] in graph:
            graph[nodes[i][0]].append(nodes[i][1])
        else:
            graph[nodes[i][0]] = [nodes[i][1]]
        if nodes[i][1] in graph:
            graph[nodes[i][1]].append(nodes[i][0])
        else:
            graph[nodes[i][1]] = [nodes[i][0]]

    # print(graph)

    print('#{} {}'.format(j + 1, minimum_route(V, S, G, graph)))