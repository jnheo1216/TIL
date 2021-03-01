import sys
sys.stdin = open('input.txt', 'r')


def switch(n):
    if n == 0:
        return 1
    else:
        return 0


N = int(input())  # 스위치 길이를 받아와요
button_list = list(map(int, input().split()))  # 스위치 리스트를 받아요
# print(button_list)
student_number = int(input())  # 학생수를 받아요

for i in range(student_number):
    gender, get_num = map(int, input().split())  # 각 학생의 성별과 숫자를 받아와요

    if gender == 1:  # 남자일때
        tmp_getnum = get_num
        while get_num <= N:  # 전체 길이를 넘지 않는 선에서
            button_list[get_num - 1] = switch(button_list[get_num - 1])  # 스위치 on off를 바꿔줌
            get_num += tmp_getnum  # 숫자를 배수 해줌
    else:  # 여자일때
        start = get_num - 1
        end = get_num - 1  # 시작포인트는 받은 원점부터
        while True:
            if start == 0 or end == N - 1:  # 만약 스위치 끝에 도달했으면 탈출
                break
            if button_list[start-1] == button_list[end+1]:  # 양 옆의 스위치 상태가 같다? 확장해라
                start -= 1
                end += 1
            else:  # 다르다면 바로 나와라
                break
        for i in range(start, end+1):  # 위에서 구한 해당 범위 만큼 스위치 상태 바꿔주기
            button_list[i] = switch(button_list[i])

print(*button_list)
