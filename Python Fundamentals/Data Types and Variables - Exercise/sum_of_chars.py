number_of_lines = int(input())
sum_chars = 0

for i in range(number_of_lines):
    char = input()
    ascii_num = ord(char)
    sum_chars += ascii_num

print(f"The sum equals: {sum_chars}")
