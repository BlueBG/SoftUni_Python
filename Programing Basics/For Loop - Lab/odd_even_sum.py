nuber_count = int(input())

even_sum = 0
odd_sum = 0

for i in range(1, nuber_count + 1):
    curent_num = int(input())
    if i % 2 == 0:
        even_sum += curent_num
    else:
        odd_sum += curent_num
if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")
else:
    diff = abs(even_sum - odd_sum)
    print("No")
    print(f"Diff = {diff}")
