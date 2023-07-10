number_of_days = int(input())
number_of_hours = int(input())
total_costs = 0

for day in range(1, number_of_days + 1):
    current_costs = 0
    for hour in range(1, number_of_hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            current_costs += 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            current_costs += 1.25
        else:
            current_costs += 1

    print(f'Day: {day} - {current_costs:.2f} leva')
    total_costs += current_costs

print(f'Total: {total_costs:.2f} leva')