import sys
sys.stdin = open('input.txt', 'r')


# def s_to_n(list_leng, slist):
#     result_n = [0] * list_leng
#     for i in range(list_leng):
#         if slist[i] == 'ZRO':
#             result_n[i] = 0
#         elif slist[i] == 'ONE':
#             result_n[i] = 1
#         elif slist[i] == 'TWO':
#             result_n[i] = 2
#         elif slist[i] == 'THR':
#             result_n[i] = 3
#         elif slist[i] == 'FOR':
#             result_n[i] = 4
#         elif slist[i] == 'FIV':
#             result_n[i] = 5
#         elif slist[i] == 'SIX':
#             result_n[i] = 6
#         elif slist[i] == 'SVN':
#             result_n[i] = 7
#         elif slist[i] == 'EGT':
#             result_n[i] = 8
#         else:
#             result_n[i] = 9
#     return result_n
#
#
# def n_to_s(list_leng, nlist):
#     result_s = [0] * list_leng
#     for i in range(list_leng):
#         if nlist[i] == 0:
#             result_s[i] = 'ZRO'
#         elif nlist[i] == 1:
#             result_s[i] = 'ONE'
#         elif nlist[i] == 2:
#             result_s[i] = 'TWO'
#         elif nlist[i] == 3:
#             result_s[i] = 'THR'
#         elif nlist[i] == 4:
#             result_s[i] = 'FOR'
#         elif nlist[i] == 5:
#             result_s[i] = 'FIV'
#         elif nlist[i] == 6:
#             result_s[i] = 'SIX'
#         elif nlist[i] == 7:
#             result_s[i] = 'SVN'
#         elif nlist[i] == 8:
#             result_s[i] = 'EGT'
#         else:
#             result_s[i] = 'NIN'
#     return result_s
#
#
# def bubble_sort(numbers):
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             if numbers[i] > numbers[j]:
#                 numbers[i], numbers[j] = numbers[j], numbers[i]
#     return numbers
#
#
# def GNS(list_leng, input_list):
#     input_list = s_to_n(list_leng, input_list)
#     input_list = bubble_sort(input_list)
#     input_list = n_to_s(list_leng, input_list)
#     return input_list
#
#
# test_case = int(input())
#
# for n in range(test_case):
#     num, length = map(str, input().split())
#     num_list = list(map(str, input().split()))
#     print(num)
#     print(*GNS(int(length), num_list))

test_case = int(input())

for n in range(test_case):
    num, length = map(str, input().split())
    num_list = list(map(str, input().split()))

    nums_dictionary = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9,
                       0: 'ZRO', 1: 'ONE', 2: 'TWO', 3: 'THR', 4: 'FOR', 5: 'FIV', 6: 'SIX', 7: 'SVN', 8: 'EGT', 9: 'NIN'}

    num_count = [0] * 10

    for i in num_list:
        num_count[nums_dictionary[i]] += 1

    print(num)
    for idx, val in enumerate(num_count):
        print((nums_dictionary[idx] + ' ') * val, end=' ')
    print()