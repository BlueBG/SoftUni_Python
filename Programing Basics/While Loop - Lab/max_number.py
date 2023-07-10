import sys

input_number = input()

max_number = -sys.maxsize

while input_number != "Stop":
    input_number = int(input_number)
    if max_number < input_number:
        max_number = input_number

    if max_number == "Stop":
        break
    input_number = input()

print(max_number)