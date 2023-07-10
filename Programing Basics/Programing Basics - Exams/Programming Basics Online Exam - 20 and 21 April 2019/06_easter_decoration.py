custumer_count = int(input())

purchase_count = 0
price = 0
total_price = 0
avg_price = 0

for i in range(1, custumer_count + 1):
    decoration_type = input()

    while decoration_type != "Finish":
        purchase_count += 1
        if decoration_type == "basket":
            price = 1.50
            total_price += price
        elif decoration_type == "wreath":
            price = 3.80
            total_price += price
        elif decoration_type == "chocolate bunny":
            price = 7
            total_price += price

        decoration_type = input()
    if purchase_count % 2 == 0:
        total_price = total_price * 0.80

    print(f"You purchased {purchase_count} items for {total_price:.2f} leva.")
    avg_price += total_price
    total_price = 0
    purchase_count = 0
avg_price = avg_price / custumer_count
print(f"Average bill per client is: {avg_price:.2f} leva.")