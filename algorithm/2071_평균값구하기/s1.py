import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
for i in range(N):
    nums = list(map(int, input().split()))
    print('#{} {}'.format(i + 1, round(sum(nums) / len(nums))))


