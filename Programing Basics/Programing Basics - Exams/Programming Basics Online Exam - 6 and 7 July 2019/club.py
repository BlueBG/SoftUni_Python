club_needed_money = float(input())

drink_price = 0
total_drink_price = 0
all_sum_amaunt = 0
flag = False
cocktail_name = input()
while cocktail_name != "Party!":
    cocktail_count = int(input())
    drink_price = len(cocktail_name)
    total_drink_price = drink_price * cocktail_count

    if total_drink_price % 2 != 0:
        total_drink_price = total_drink_price * 0.75
    all_sum_amaunt += total_drink_price

    if all_sum_amaunt >= club_needed_money:
        flag = True
        break

    cocktail_name = input()

if flag:
    print("Target acquired.")
    print(f"Club income - {all_sum_amaunt:.2f} leva.")
else:
    diff = abs(all_sum_amaunt - club_needed_money)
    print(f"We need {diff:.2f} leva more.")
    print(f"Club income - {all_sum_amaunt:.2f} leva.")
