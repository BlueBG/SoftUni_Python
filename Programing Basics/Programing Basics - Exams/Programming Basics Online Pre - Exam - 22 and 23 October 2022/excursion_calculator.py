people_count = int(input())
season_type = input()

total_price = 0
price_per_night = 0
if season_type == "spring":
    if people_count <= 5:
        price_per_night = 50
    else:
        price_per_night = 48

elif season_type == "summer":
    if people_count <= 5:
        price_per_night = 48.50
    else:
        price_per_night = 45

elif season_type == "autumn":
    if people_count <= 5:
        price_per_night = 60
    else:
        price_per_night = 49.50

elif season_type == "winter":
    if people_count <= 5:
        price_per_night = 86
    else:
        price_per_night = 85
if season_type == "summer":
    total_price = (people_count * price_per_night) * 0.85
elif season_type == "winter":
    total_price = (people_count * price_per_night) * 1.08
else:
    total_price = people_count * price_per_night
print(f"{total_price:.2f} leva.")
