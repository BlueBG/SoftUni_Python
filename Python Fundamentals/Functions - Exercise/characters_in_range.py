def get_char_in_range(start, end):
    result = []
    for num in range(ord(start) + 1, ord(end)):
        result.append(chr(num))
    return result


first_character = input()
second_character = input()

print(' '.join(get_char_in_range(first_character, second_character)))

