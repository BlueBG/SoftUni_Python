square_meters = float(input())

landscaping_price = square_meters * 7.61
discount = landscaping_price * 0.18
total_price = landscaping_price - discount

print(f"The final price is: {total_price} lv.")
print(f"The discount is: {discount} lv.")
