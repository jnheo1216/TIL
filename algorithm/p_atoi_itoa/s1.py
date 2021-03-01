# atoi (ASCII to Integer)
# 문자 -> 숫자 / Python의 int()


def atoi(my_str):
    result = 0
    for i in range(len(my_str)):
        result += (ord(my_str[i]) - 48) * 10 ** (len(my_str) - 1 - i)

    return result


my_str = '123'
print(my_str, type(my_str))

my_int1 = atoi(my_str)
print(my_int1, type(my_int1))

my_int2 = int(my_str)
print(my_int2, type(my_int2))
