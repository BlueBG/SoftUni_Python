movie_budget = float(input())
people_count = int(input())
one_cloth_price = float(input())


deckor_coast = movie_budget * 0.10
clothes_coast = people_count * one_cloth_price
if people_count > 150:
    clothes_coast = clothes_coast - (clothes_coast * 0.10)

movie_coast = deckor_coast + clothes_coast
diff = abs(movie_budget - movie_coast)

if movie_budget >= movie_coast:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
elif movie_budget < movie_coast:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
