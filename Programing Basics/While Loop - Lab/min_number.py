import sys

input_number = input()

min_number = sys.maxsize

while input_number != "Stop":
    input_number = int(input_number)
    if min_number > input_number:
        min_number = input_number

    if min_number == "Stop":
        break
    input_number = input()

print(min_number)