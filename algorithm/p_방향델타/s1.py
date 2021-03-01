## 방향델타

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

print(arr)

# print('방향으로 2차배열 탐색')
x = 1
y = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] #상하좌우
# for i in range(4):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     if 0 <= nx < N and 0 <= ny < N:
#         print(arr[nx][ny])

result = []
for i in range(N):
    for j in range(N):
        sumsum = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                sumsum += abs(arr[nx][ny] - arr[i][j])
        result.append(sumsum)

for i in arr:
    print(i)
print(sum(result))