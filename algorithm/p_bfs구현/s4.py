"""
4. bfs - 1번 노드에서 가장 멀리 떨어진 노드 찾기
거리에 대한 정보 담아 놓기
(필요하다면 기존에 작성한 내용을 복-붙 하셔도 됩니다!)
"""
### 이게 맞나?


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
                    if not checklist[i]:
                        far[i] += 1 + far[tmp]
                        checklist[i] = 1


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
far = [0] * (V + 1)
checklist = [0] * (V + 1)

# bfs 탐색 시작
bfs(1)
print(visited)
print(visited[-1])

print(far)