def str_comparision(str1, str2):
    if len(str1) == len(str2):
        for i in range(len(str1)):
            if not str1[i] == str2[i]:
                return False
    else:
        return False

    return True


str1 = 'abccd'
str2 = 'abcd'

print(str_comparision(str1, str2))
