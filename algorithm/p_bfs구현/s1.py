"""
1. bfs - 인접 행렬 구현
(필요하다면 기존에 작성한 내용을 복-붙 하셔도 됩니다!)
"""


def bfs(v):
    queue = [v]
    while queue:
        print(queue)
        v = queue.pop(0)
        visited[v] = 1
        for i in range(1, V+1):
            if visited[i] == 0 and graph[v][i] == 1:
                queue.append(i)
                visited[i] = 1


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
numlist = list(map(int, input().split()))
print(numlist)

# Graph 초기화
graph = [[0] * (V + 1) for _ in range(V+1)]

for i in range(0, E * 2, 2):
    graph[numlist[i]][numlist[i+1]] = 1
    graph[numlist[i+1]][numlist[i]] = 1
for n in graph:
    print(n)

# 방문 표시 초기화
visited = [0 for _ in range(V+1)]

# bfs 탐색 시작
bfs(1)

print(visited)