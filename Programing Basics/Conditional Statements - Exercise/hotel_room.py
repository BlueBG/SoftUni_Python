mount = input()
night_count = int(input())

studio = 0
apartment = 0
total_studio_coast = 0
total_apartment_coast = 0

if mount == "May" or mount == "October":
    studio = 50
    apartment = 65
elif mount == "June" or mount == "September":
    studio = 75.20
    apartment = 68.70
elif mount == "July" or mount == "August":
    studio = 76
    apartment = 77
if night_count > 14:
    apartment = apartment * 0.90

if (mount == "May" or mount == "October") and (7 < night_count < 14):
    studio = studio * 0.95
elif (mount == "May" or mount == "October") and night_count > 14:
    studio = studio * 0.70
elif (mount == "June" or mount == "September") and night_count > 14:
    studio = studio * 0.80

total_studio_coast = studio * night_count
total_apartment_coast = apartment * night_count
print(f"Apartment: {total_apartment_coast:.2f} lv.")
print(f"Studio: {total_studio_coast:.2f} lv.")
