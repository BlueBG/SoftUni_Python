price = 0
taxes = 0
is_special = False
is_true = False
while True:
    str_parts_price = input()
    if str_parts_price == "special":
        is_special = True
        break
    elif str_parts_price == "regular":
        break

    parts_price = float(str_parts_price)

    if parts_price < 0:
        print("Invalid price!")
        continue

    price += parts_price

taxes = price * 0.20
total_price = price + taxes
if is_special:
    total_price = total_price * 0.90

if total_price > 0:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")
else:
    print(f"Invalid order!")

