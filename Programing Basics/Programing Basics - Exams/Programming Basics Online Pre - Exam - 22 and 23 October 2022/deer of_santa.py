import math

day_without_santa = int(input())
total_left_food = int(input())
first_deer_food = float(input())
second_deer_food = float(input())
third_deer_food = float(input())

total_deer_food = (first_deer_food + second_deer_food + third_deer_food) * day_without_santa
diff = abs( total_left_food - total_deer_food)
if total_deer_food < total_left_food:
    diff = math.floor(diff)
    print(f"{diff} kilos of food left.")
elif total_deer_food > total_left_food:
    diff = math.ceil(diff)
    print(f"{diff} more kilos of food are needed.")