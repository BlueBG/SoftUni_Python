see_vacation_count = int(input())
mountain_vacation_count = int(input())

total_incom = 0
see_left = see_vacation_count
mountain_left = mountain_vacation_count
flag = False

while True:
    pack_type = input()

    if pack_type == "Stop":
        break
    if pack_type == "sea":
        if see_left > 0:
            see_left -= 1
            total_incom += 680
        else:
            see_left -= 0
            total_incom += 0
    elif pack_type == "mountain":
        if mountain_left > 0:
            mountain_left -= 1
            total_incom += 499
        else:
            mountain_left -= 0
            total_incom += 0
    if see_left == 0 and mountain_left == 0:
        flag = True
        break

if flag:
    print("Good job! Everything is sold.")
    print(f"Profit: {total_incom} leva.")
else:
    print(f"Profit: {total_incom} leva.")
