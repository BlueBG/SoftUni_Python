budget_money = float(input())
video_card_count = int(input())
cpu_count = int(input())
ram_count = int(input())

video_card_price = video_card_count * 250
cpu_price = (video_card_price * 0.35) * cpu_count
ram_price = (video_card_price * 0.10) * ram_count
total_price = video_card_price + cpu_price + ram_price

if video_card_count > cpu_count:
    total_price = total_price * 0.85

diff = abs(budget_money - total_price)

if budget_money >= total_price:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")
