orders_num = int(input())

total_price = 0

for _ in range(orders_num):
    price_per_capsule = float(input())
    days = int(input())
    capsuls_per_day = int(input())

    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    if days < 1 or days > 31:
        continue
    if capsuls_per_day < 1 or capsuls_per_day > 2000:
        continue

    price_per_order = price_per_capsule * days * capsuls_per_day
    total_price += price_per_order

    print(f"The price for the coffee is: ${price_per_order:.2f}")

print(f"Total: ${total_price:.2f}")
