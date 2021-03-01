## 1289 원재야
import sys
sys.stdin = open('input.txt', 'r')


def memory_recovery(memory_list):
    zero_list = ['0'] * len(memory_list)
    count = 0

    for i in range(len(memory_list)):
        if zero_list[i] != memory_list[i]:
            for j in range(i, len(memory_list)):
                zero_list[j] = memory_list[i]
            count += 1

    return count


testcase = int(input())

for i in range(testcase):
    memory = list(str(input()))
    print('#{} {}'.format(i + 1, memory_recovery(memory)))