budged = float(input())
season = input()

car_type = ""
car_price = 0
type_class = ""

if budged <= 100:
    type_class = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        car_price = budged * 0.35
    elif season == "Winter":
        car_type = "Jeep"
        car_price = budged * 0.65
elif budged <= 500:
    type_class = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        car_price = budged * 0.45
    elif season == "Winter":
        car_type = "Jeep"
        car_price = budged * 0.80
else:
    type_class = "Luxury class"
    car_type = "Jeep"
    car_price = budged * 0.90

print(f"{type_class}")
print(f"{car_type} - {car_price:.2f}")