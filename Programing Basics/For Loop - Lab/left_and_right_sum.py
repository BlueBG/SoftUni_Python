number_of_lines = int(input())

left_sum = 0
right_sum = 0

for i in range(0, number_of_lines):
    curent_number = int(input())
    left_sum += curent_number
for i in range(0, number_of_lines):
    second_cur_number = int(input())
    right_sum += second_cur_number
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")
