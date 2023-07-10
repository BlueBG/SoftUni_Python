trip_price = float(input())
puzle_count = int(input())
dolls_count = int(input())
tedys_count = int(input())
minions_count = int(input())
trucks_count = int(input())

toys_amaunt = (puzle_count * 2.60) + (dolls_count * 3) + (tedys_count * 4.10) + \
              (minions_count * 8.20) + (trucks_count * 2)
all_toys_count = puzle_count + dolls_count + tedys_count + minions_count + trucks_count

if all_toys_count >= 50:
    toys_amaunt = toys_amaunt - (toys_amaunt * 0.25)

total_money = toys_amaunt - (toys_amaunt * 0.10)
diff = abs(trip_price - total_money)

if total_money >= trip_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")
