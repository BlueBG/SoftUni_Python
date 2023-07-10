drink_type = input()
sugar_type = input()
drinks_count = int(input())

price = 0

if sugar_type == "Without" and drink_type == "Espresso":
    price = (drinks_count * 0.90) * 0.65
    if drinks_count > 5:
        price = price * 0.75
elif sugar_type == "Without" and drink_type == "Cappuccino":
    price = drinks_count * 0.65
elif sugar_type == "Without" and drink_type == "Tea":
    price = (drinks_count * 0.50) * 0.65

if sugar_type == "Normal" and drink_type == "Espresso":
    price = drinks_count * 1
    if drinks_count > 5:
        price = price * 0.75
elif sugar_type == "Normal" and drink_type == "Cappuccino":
    price = drinks_count * 1.20
elif sugar_type == "Normal" and drink_type == "Tea":
    price = drinks_count * 0.60

if sugar_type == "Extra" and drink_type == "Espresso":
    price = drinks_count * 1.20
    if drinks_count > 5:
        price = price * 0.75
elif sugar_type == "Extra" and drink_type == "Cappuccino":
    price = drinks_count * 1.60
elif sugar_type == "Extra" and drink_type == "Tea":
    price = drinks_count * 0.70

if price > 15:
    price = price * 0.80

print(f"You bought {drinks_count} cups of {drink_type} for {price:.2f} lv.")
