import sys
sys.stdin = open("input.txt", "r")


# DFS
def DFS(v, e, l):
    visited = [False] * (v + 1)
    course = []

    adjacency_matrix = [[0] * (v + 1) for _ in range(v + 1)]
    for idx in range(e):
        adjacency_matrix[l[idx * 2]][l[idx*2 + 1]] = 1
        adjacency_matrix[l[idx*2 + 1]][l[idx * 2]] = 1

    # chose smaller one
    # 인접행렬을 앞에서 부터 살펴보면 작은 것부터 역이면 큰 것부터이다.
    start = 1
    course.append(start)
    a = []
    b = []
    while course:
        # 현재 course의 top item을 보고 방문 처리하는 과정
        # pop append가 아니라 peek으로 작성이 바람직해 보임
        vertex = course.pop()
        if not visited[vertex]:
            a.append(vertex)
        visited[vertex] = True
        course.append(vertex)
        b.append(vertex)
        # 인접 행렬을 통해서 해당 vertex의 edge를 살펴보고 방문한적이 없다면 course에 push하고 break
        for i in range(len((adjacency_matrix[vertex]))):
            if adjacency_matrix[vertex][i] and (not visited[i]):
                course.append(i)
                break
        # break가 없다면 연결된 vertex를 모두 갔다는 의미로 해당 vertex를 pop한다.
        else:
            course.pop()
        print("course: {0} 순서: {1} 누적순서:{2}".format(course, a, b))

# input and output
T = 1
for tc in range(1, T + 1):
    Vertex, Edge = map(int, input().split())
    Status = list(map(int, input().split()))
    print("#{0} {1}".format(tc, DFS(Vertex, Edge, Status)))