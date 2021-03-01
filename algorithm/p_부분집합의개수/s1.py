nums = [7, 1, 5, 4]

n = len(nums)

cnt = 0

for i in range(1 << n):  # 모든 부분집합의 개수만큼!
    cnt += 1
    for j in range(n):  # 리스트 안에거 개수 만큼
        if i & (1 << j):
            print(nums[j], end=' ')
    print()
print(cnt)
