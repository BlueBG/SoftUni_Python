numbers = input().split()

list_of_numbers = [int(x) for x in numbers]
average_value = sum(list_of_numbers) / len(list_of_numbers)
greather_numbers = []
a = []

for num in list_of_numbers:
    if num > average_value:
        a = greather_numbers.append(num)
print(greather_numbers)