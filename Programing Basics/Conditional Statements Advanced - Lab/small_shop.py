product_type = input()
city = input()
quantity = float(input())
total_price = 0

if city == "Sofia":
    if product_type == "coffee":
        total_price = quantity * 0.50
    elif product_type == "water":
        total_price = quantity * 0.80
    elif product_type == "beer":
        total_price = quantity * 1.20
    elif product_type == "sweets":
        total_price = quantity * 1.45
    elif product_type == "peanuts":
        total_price = quantity * 1.60
elif city == "Plovdiv":
    if product_type == "coffee":
        total_price = quantity * 0.40
    elif product_type == "water":
        total_price = quantity * 0.70
    elif product_type == "beer":
        total_price = quantity * 1.15
    elif product_type == "sweets":
        total_price = quantity * 1.30
    elif product_type == "peanuts":
        total_price = quantity * 1.50
elif city == "Varna":
    if product_type == "coffee":
        total_price = quantity * 0.45
    elif product_type == "water":
        total_price = quantity * 0.70
    elif product_type == "beer":
        total_price = quantity * 1.10
    elif product_type == "sweets":
        total_price = quantity * 1.35
    elif product_type == "peanuts":
        total_price = quantity * 1.55
print(total_price)