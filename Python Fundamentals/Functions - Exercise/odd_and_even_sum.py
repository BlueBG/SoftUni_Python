def sum_of_even_and_odd_nums(number_as_string):
    odd_sum = 0
    even_sum = 0
    for digit_as_string in number_as_string:
        digit = int(digit_as_string)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number_as_str = input()

print(sum_of_even_and_odd_nums(number_as_str))