## 4881 배열최소합
import sys
sys.stdin = open('input.txt', 'r')


## 중복조합 방식으로 해보려했는데 런타임에러남. 쉽지 않음 흑흑
############################################################################
def perm(lst, n):
    ret = []
    if n > len(lst):
        return ret

    if n == 1:
        for i in lst:
            ret.append([i])
    elif n > 1:
        for i in range(len(lst)):
            temp = [i for i in lst]
            temp.remove(lst[i])
            for p in perm(temp, n-1):
                ret.append([lst[i]]+p)

    return ret


def get_minimun_val(n, numlist):
    cases = perm(list(range(1, n + 1)), n)
    result = 1000000

    for case in cases:
        count = 0
        for i in range(n):
            count += numlist[i][case[i] - 1]
        if count < result:
            result = count

    return result
##########################################################################
## 폐기  (작은 규모는 잘 되지만 큰 규모는 런타임이 매우 큰 것으로 보임) (perm 부분 대충 가져다 쓴 게 폐해같음)


def get_mini_val_stack(idx, n, numlist):
    # global 쓸땐 쓰자... 몇분을 날리니
    global min_sum, tmp_sum  # 계속 해당 함수를 콜하기 때문에 밖에서 값을 선언하고 global을 쓰는게 맞음
    if min_sum < tmp_sum:  # 이미 최소합보다 크다면 볼 것도 없음. 탈출
        return

    if idx == n:  # 인덱스가 N에 도달했을때 -> 한 루트 끝점까지 탐색
        if tmp_sum < min_sum:  # 최소값보다 작다면
            min_sum = tmp_sum  # 바꿈
        return

    for c in range(n):
        if not visited[c]:  # 해당 열을 했는지 안했는지
            visited[c] = 1  # 하지 않았으면 방문 표시 후
            tmp_sum += numlist[idx][c]  # 더해주고
            get_mini_val_stack(idx + 1, n, numlist)  # 다음 행으로 가서 계속 탐색
            visited[c] = 0  # 그 루트에서 돌아온다면 다음 열로 가기 전에 0으로
            tmp_sum -= numlist[idx][c]  # 넣었던 값을 다시 빼주고 다음 열로 반복


testcase = int(input())

for i in range(testcase):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 10000000  # 결과값
    tmp_sum = 0  # 합들의 저장
    visited = [0] * N  # 방문 표시
    # print('#{} {}'.format(i + 1, get_minimun_val(N, num_list)))  # 실패
    get_mini_val_stack(0, N, num_list)
    print('#{} {}'.format(i + 1, min_sum))