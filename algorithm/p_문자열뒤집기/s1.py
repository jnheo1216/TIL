def reverse_str(word):
    result = ''
    for i in range(1, len(word) + 1):
        result += word[i * -1]
    return result


word = 'tomato'
print(reverse_str(word))


