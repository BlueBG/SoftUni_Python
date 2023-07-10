import math

fan_name = input()
budget = float(input())
beer_count = int(input())
chips_count = int(input())

total_beer_price = beer_count * 1.20
chips_pack_price = total_beer_price * 0.45
total_chips_price = math.ceil(chips_count * chips_pack_price)
all_coast = total_beer_price + total_chips_price
diff = abs(budget - all_coast)

if budget >= all_coast:
    print(f"{fan_name} bought a snack and has {diff:.2f} leva left.")
elif budget < all_coast:
    print(f"{fan_name} needs {diff:.2f} more leva!")