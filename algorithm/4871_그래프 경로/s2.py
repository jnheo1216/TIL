## 4871 그래프경로
import sys
sys.stdin = open('input.txt', 'r')


def find_load(s, g, graph):

    visited = []
    stack = [s]
    while stack:  # dfs
        nod = stack.pop()
        if not graph[nod]:  # 해당 노드에서 더 이상 연결된 노드가 없다면
            visited.append(nod)  # 방문했다는 기록만 남기고
            continue  # 다음 루프로
        if nod not in visited:  # 방문한 적이 없는 곳이라면
            visited.append(nod)  # 추가해주고
            stack += graph[nod]  # 스택에 해당 노드와 연결된 다른 노드들을 추가

        if g in stack:  # 만약 도착지에 왔다면
            return 1  # 바로 1반환

    return 0  # 도착지에 도달 못했으면 0반환


testcase = int(input())

for i in range(testcase):
    V, E = map(int, input().split())

    graph = [[] for _ in range(51)]  #
    for j in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)
    print(graph)  # {1: [4, 3], 2: [3, 5], 4: [6]} # [[], [4, 3], [3, 5], [], [6], [], []] ??

    S, G = map(int, input().split())

    print('#{} {}'.format(i+1, find_load(S, G, graph)))