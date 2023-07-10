total_budget = int(input())
season = input()
people_count = int(input())

boat_price = 0

if season == "Spring":
    boat_price = 3000
elif season == "Summer" or season == "Autumn":
    boat_price = 4200
else:
    boat_price = 2600

if people_count <= 6:
    boat_price = boat_price * 0.90
elif 6 < people_count <= 11:
    boat_price = boat_price * 0.85
else:
    boat_price = boat_price * 0.75

if people_count % 2 == 0 and season != "Autumn":
    boat_price = boat_price * 0.95

diff = abs(total_budget - boat_price)
if total_budget >= boat_price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
