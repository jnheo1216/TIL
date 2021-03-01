import sys
sys.stdin = open('input.txt', 'r')

## 1.
N = int(input())

if N % 2 == 1:
    result = 1
else:
    result = 0

print(result)

## 2.
nums = map(int, input().split())

result = 0
for num in nums:
    result += num

print(result)

## 3.
N = int(input())

result_list = []
for i in range(N):
    lists = list(map(int, input().split()))
    result_list.append(lists)

print(result_list[1][1])