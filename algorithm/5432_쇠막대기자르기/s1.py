## 5432 쇠막대기자르기
import sys
sys.stdin = open('input.txt', 'r')


def metal_cutting_stack(metal_bar):
    stack = []
    maked_metal = 0
    metal_bar_list = list(metal_bar)

    for i in range(len(metal_bar_list)):
        if metal_bar_list == []:
            break

        if metal_bar_list[0] == '(' and metal_bar_list[1] == ')':
            maked_metal += len(stack)  # 막대기가 쌓인 만큼 철 생성
            metal_bar_list.pop(0)
            metal_bar_list.pop(0)
        elif metal_bar_list[0] == '(':
            stack.append(metal_bar_list.pop(0))  # 막대기 증가
        else:  # ')'
            stack.pop()  # 막대기 감소
            metal_bar_list.pop(0)
            maked_metal += 1  # 막대기가 끝나면 나오는 짜투리도 더해줘야함

    return maked_metal


# find 대신 indexing
def metal_cutting_indexing(metal_bar):
    bar_count = 0
    maked_metal = 0
    metal_bar_list = list(metal_bar)
    pass_button = False

    for i in range(len(metal_bar_list)):
        if pass_button:
            pass_button = False
            continue

        if metal_bar_list[i] == '(' and metal_bar_list[i+1] == ')':
            maked_metal += bar_count  # 막대기가 쌓인 만큼 철 생성
            pass_button = True
        elif metal_bar_list[i] == '(':
            bar_count += 1  # 막대기 증가
        else:  # ')'
            bar_count -= 1  # 막대기 감소
            maked_metal += 1  # 막대기가 끝나면 나오는 짜투리도 더해줘야함

    return maked_metal

# 이건 find쓰고 한거
# def metal_cutting(metal_bar):
#     bar_count = 0
#     maked_metal = 0
#
#     while metal_bar:
#         if metal_bar.find('()') == 0:
#             maked_metal += bar_count  # 막대기가 쌓인 만큼 철 생성
#             metal_bar = metal_bar[2:]
#         elif metal_bar[0] == '(':
#             bar_count += 1  # 막대기 증가
#             metal_bar = metal_bar[1:]
#         else:
#             bar_count -= 1  # 막대기 감소
#             maked_metal += 1  # 막대기가 끝나면 나오는 짜투리도 더해줘야함
#             metal_bar = metal_bar[1:]
#
#     return maked_metal


### while에서 무한루프가 도는건지 자꾸 런타임에러가 남. 슬라이싱으로 철막대기의 상태를 업데이트 해주는 것은 좋지않은 것 같아보임


testcase = int(input())

for i in range(testcase):
    bar = str(input())
    # print('#{} {}'.format(i+1, metal_cutting(bar)))
    print('#{} {}'.format(i+1, metal_cutting_indexing(bar)))
    print('#{} {}'.format(i+1, metal_cutting_stack(bar)))
