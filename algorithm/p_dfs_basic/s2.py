import sys

sys.stdin = open('input.txt')

def dfs1(start): # stack 을 만들고 (dfs_스택 -> 재귀는 코드적 스택)
    visited = [0] * vertex
    stack = [start]
    visited[start] = 1
    while stack: # 스택에 있을 때까지
        a = stack.pop(-1) # 위에 값을 가져오자
        print('path', a, end=' ')
        result1.append(a) # 경로를 기억하자
        for ele in range(vertex): # 그래프에서 연결된 곳을 찾고
            if data[a][ele] == 1 and visited[ele] == 0:
                stack.append(ele) # 스택에 입력을 하자
                visited[ele] = 1  # 방문한 곳을 표시하자


vertex, edge = map(int, input().split())
result1 = []
data = [[0] * vertex for _ in range(vertex)]  # 2차원 맵 그리기

temp = list(map(int, input().split()))

for i in range(0, len(temp), 2):  # 그래프에 입력하기
    a, b = temp[i], temp[i + 1]
    a -= 1
    b -= 1  # 0으로 맞추는 건 좋아함
    data[a][b] = 1
    data[b][a] = 1

for i in data:
    print(i)
print('============================')

for ele in range(vertex):  # 출발점을 변경해서 찾아보자
    dfs1(ele)
    print(result1)
    result1 = []
