number_lines = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(1, number_lines + 1):
    cur_number = int(input())
    if cur_number < 200:
        p1 += 1
    elif 200 <= cur_number <= 399:
        p2 += 1
    elif 400 <= cur_number <= 599:
        p3 += 1
    elif 600 <= cur_number <= 799:
        p4 += 1
    else:
        p5 += 1
p1 = p1 / number_lines * 100
p2 = p2 / number_lines * 100
p3 = p3 / number_lines * 100
p4 = p4 / number_lines * 100
p5 = p5 / number_lines * 100
print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")
