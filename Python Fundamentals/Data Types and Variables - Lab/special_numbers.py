range_numbers = int(input())

for num in range(1, range_numbers + 1):

    num_as_string = str(num)
    sum_of_digits = 0

    for char in num_as_string:
        sum_of_digits += int(char)

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
