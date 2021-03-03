"""
3. bfs - 인접 딕셔너리 구현
(필요하다면 기존에 작성한 내용을 복-붙 하셔도 됩니다!)
"""

def bfs(v):
    queue = [v]
    while queue:
        tmp = queue.pop(0)
        if not tmp in visited:
            visited.append(tmp)
        if tmp in graph:
            for i in graph[tmp]:
                if i not in visited:
                    queue.append(i)


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)
V, E = map(int, input().split())

# 간선 정보 초기화
numlist = list(map(int, input().split()))
print(numlist)

# Graph 초기화
graph = {}
for i in range(E):
    if numlist[i * 2] in graph:
        graph[numlist[i * 2]].append(numlist[i * 2 + 1])
    else:
        graph[numlist[i * 2]] = [numlist[i * 2 + 1]]
print(graph)
# 방문 표시 초기화
visited = []

# bfs 탐색 시작
bfs(1)
print(visited)