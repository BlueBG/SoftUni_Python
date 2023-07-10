budget = float(input())
season = input()

trip_price = 0
trip_destination = ""
place = ""
if budget <= 100:
    trip_destination = "Bulgaria"
    if season == "summer":
        trip_price = budget * 0.30
        place = "Camp"
    else:
        trip_price = budget * 0.70
        place = "Hotel
elif budget <= 1000:
    trip_destination = "Balkans"
    if season == "summer":
        trip_price = budget * 0.40
        place = "Camp"
    else:
        trip_price = budget * 0.80
        place = "Hotel"
elif budget > 1000:
    trip_destination = "Europe"
    trip_price = budget * 0.90
    place = "Hotel"

print(f"Somewhere in {trip_destination}")
print(f"{place} - {trip_price:.2f}")
