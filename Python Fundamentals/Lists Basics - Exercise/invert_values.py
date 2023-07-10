list_of_numbers = input().split()

opposite_list_numbers = []

for el in list_of_numbers:
    el = int(el)
    opposite_list_numbers.append(-el)

print(opposite_list_numbers)