quantity = int(input())
days_left = int(input())

total_coast = 0
total_spirit = 0
multyplay = 0

for day in range(1, days_left + 1):
    quantity += multyplay
    if day % 2 == 0:
        total_coast += (2 * quantity)
        total_spirit += (5 * quantity)
    if day % 3 == 0:
        total_coast += 5 * quantity + 3 * quantity
        total_spirit += 3 * quantity + 10 * quantity
    elif day % 5 == 0:
        total_coast += (15 * quantity)
        total_spirit += (17 * quantity)
    if day % 10 == 0:
        total_spirit -= 20
        total_coast += 23
    elif day % 11 == 0:
        multyplay += 2

#'''This is not the hole task!!!'''


print(f"Total cost: {total_coast}")
print(f"Total spirit: {total_spirit}")