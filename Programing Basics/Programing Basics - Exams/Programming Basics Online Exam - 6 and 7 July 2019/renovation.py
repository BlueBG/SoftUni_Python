import math

height = int(input())
width = int(input())
no_paint_percent = int(input())

area = 0
total_area = 0
percent = (100 - no_paint_percent) / 100
liters = 0
flag = False
paint_ltr = input()

while paint_ltr != "Tired!":
    paint = int(paint_ltr)
    area = height * width * 4
    total_area = math.ceil(area * percent)
    # total_area -= paint_ltr
    liters += paint

    if liters == total_area:
        print("All walls are painted! Great job, Pesho!")
        break
    elif liters > total_area:
        flag = True
        break
    else:
        paint_ltr = input()

diff = abs(total_area - liters)
if liters > total_area or flag:
    print(f"All walls are painted and you have {diff} l paint left!")
elif liters < total_area:
    print(f"{diff} quadratic m left.")
