number_of_line = int(input())
total_water = 0

for i in range(number_of_line):
    water_lt = int(input())
    total_water += water_lt

    if total_water > 255:
        total_water -= water_lt
        print("Insufficient capacity!")
        continue
print(total_water)
