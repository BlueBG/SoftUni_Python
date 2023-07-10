import sys

number_lines = int(input())

sum_numbers = 0
sum_without_max_number = 0
max_nubmer = -sys.maxsize

for i in range(1, number_lines + 1):
    curent_number = int(input())
    sum_numbers += curent_number
    if curent_number > max_nubmer:
        max_nubmer = curent_number
sum_without_max_number = sum_numbers - max_nubmer

if sum_without_max_number == max_nubmer:
    print("Yes")
    print(f"Sum = {max_nubmer}")
else:
    diff = abs(sum_without_max_number - max_nubmer)
    print("No")
    print(f"Diff = {diff}")
