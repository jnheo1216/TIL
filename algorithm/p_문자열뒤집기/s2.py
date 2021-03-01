# reversed() 직접 구현


def reverse_str_recursion(word):
    if len(word) <= 1:
        return word
    else:
        return reverse_str_recursion(word[1:]) + word[0]
    return


word = 'tomato'
print(reverse_str_recursion(word))
