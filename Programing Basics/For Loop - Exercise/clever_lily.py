birdhdays_count = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money_from_birdhday = 0
total_money = 0
toys_count = 0
money_take = birdhdays_count // 2

for i in range(1, birdhdays_count + 1):
    if i % 2 == 0:
        money_from_birdhday += 10
        total_money += money_from_birdhday
    else:
        toys_count += 1
total_money += (toys_count * toy_price) - (money_take * 1)
diff = abs(washing_machine_price - total_money)
if total_money >= washing_machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
