import sys

numbers_of_lines = int(input())

max_number = -sys.maxsize
min_number = sys.maxsize

for _ in range(numbers_of_lines):
    input_number = int(input())

    if max_number < input_number:
        max_number = input_number
    if min_number > input_number:
        min_number = input_number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")