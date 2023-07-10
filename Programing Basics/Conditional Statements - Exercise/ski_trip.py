stay_days = int(input())
room_type = input()
evaluation = input()

nights = stay_days - 1
room_coast = 18
apartment_coast = 25
president_coast = 35
total_price = 0

if stay_days < 10 and room_type == "apartment":
    total_price = (nights * apartment_coast) * 0.70
    if room_type == "president apartment":
        total_price = (nights * president_coast) * 0.90
elif 10 <= stay_days <= 15 and room_type == "apartment":
    total_price = (nights * apartment_coast) * 0.65
    if room_type == "president apartment":
        total_price = (nights * president_coast) * 0.85
elif stay_days > 15 and room_type == "apartment":
    total_price = (nights * apartment_coast) * 0.50
elif room_type == "president apartment":
    total_price = (nights * president_coast) * 0.80
else:
    total_price = room_coast * nights

if evaluation == "positive":
    total_price = total_price * 1.25
else:
    total_price = total_price * 0.90

print(f"{total_price:.2f}")
